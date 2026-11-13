from __future__ import annotations

import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import textwrap
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).parents[1] / "scripts" / "compass_lex.py"
SHIPMENT = {
    "concept": "shipment", "speech": ["Shipment", "SHP"],
    "code": ["consignment", "shp"], "chart": "logistics.dispatch",
}
RESERVATION = {
    "concept": "reservation", "speech": ["Reservation"], "code": ["booking"],
    "scope": ["src/bookings/"], "note": "delivery scheduling only",
}
FORECAST = {
    "concept": "forecast", "speech": ["Weather Forecast"], "code": [],
    "where": "weather provider API in a separate repository",
}
SHOP_ACCOUNT = {
    "concept": "account", "root": "shop", "speech": ["Account"],
    "code": ["account"], "chart": "shop.account",
}
COMMUNITY_ACCOUNT = {
    "concept": "account", "root": "community", "speech": ["Account"],
    "code": ["member-account"], "chart": "community.member-account",
}
BILLING_ACCOUNT = {
    "concept": "billing-account", "root": "logistics", "context": "billing",
    "speech": ["Account"], "code": ["ledger-account"], "chart": "logistics.billing",
}
IDENTITY_ACCOUNT = {
    "concept": "login-account", "root": "logistics", "context": "identity",
    "speech": ["Account"], "code": ["login-account"], "chart": "logistics.identity",
}


class CompassLexTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory(prefix="compass lexicon ")
        self.repo_root = Path(self.temporary_directory.name)
        self.chart_root = self.repo_root / ".compass"
        self.write(".compass/logistics/dispatch/README.md", """
            # Dispatch

            ## Implementation coordinates

            `src/dispatch/SHPService.ts` covers `src/dispatch/`

            `src/consignments/`
            """)
        self.write(".compass/logistics/GLOSSARY.md", """
            # Glossary — logistics

            ## **Shipment**

            ### Meaning

            Goods sent together to a destination.
            """)
        self.write(".compass/logistics/DOMAIN.md", "# Logistics\n\n## Billing\n\n## Identity\n")
        for address in ("shop/account", "community/member-account", "logistics/billing", "logistics/identity"):
            self.write(f".compass/{address}/README.md", "# Account\n")
        self.write("src/dispatch/SHPService.ts", "export class SHPService {}\nconst consignment = 1;\n")
        self.write("src/consignments/index.ts", "const consignment = 1;\n")
        self.write("src/bookings/Booking.ts", "export class Booking {}\n")
        self.write("src/accounts.ts", "const account = 1; const memberAccount = 2;\nconst ledgerAccount = 3; const loginAccount = 4;\n")

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def write(self, relative_path: str, value: str) -> None:
        path = self.repo_root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(value).lstrip(), encoding="utf-8")

    def run_lex(self, *arguments: str, stdin: str | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--chart-root", str(self.chart_root),
             "--repo-root", str(self.repo_root), *arguments],
            check=False, capture_output=True, text=True, input=stdin,
        )

    def admit(self, *rows: dict, dry_run: bool = False) -> subprocess.CompletedProcess[str]:
        return self.run_lex("add", "--stdin", *(["--dry-run"] if dry_run else []),
                            stdin="\n".join(json.dumps(r) for r in rows) + "\n")

    def lexicon(self) -> Path:
        return self.chart_root / "LEXICON.jsonl"

    def link_shipment(self) -> None:
        glossary = self.chart_root / "logistics/GLOSSARY.md"
        glossary.write_text(glossary.read_text() + "\n### Lexicon\n\n`shipment`\n")

    def result(self, *arguments: str) -> dict:
        result = self.run_lex(*arguments, "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_add_admits_atomic_batch_in_order_and_passes_full_check(self) -> None:
        self.link_shipment()
        result = self.admit(SHIPMENT, RESERVATION, FORECAST, SHOP_ACCOUNT, COMMUNITY_ACCOUNT)
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = [json.loads(line) for line in self.lexicon().read_text().splitlines()]
        self.assertEqual([r["concept"] for r in rows], ["forecast", "reservation", "shipment", "account", "account"])
        self.assertEqual(self.run_lex("check").returncode, 0)

    def test_add_rejects_redundant_gap_and_accepts_root_collision(self) -> None:
        alone = self.admit(SHOP_ACCOUNT)
        self.assertEqual(alone.returncode, 1)
        self.assertIn("share vocabulary", alone.stderr)
        self.assertFalse(self.lexicon().exists())
        both = self.admit(SHOP_ACCOUNT, COMMUNITY_ACCOUNT)
        self.assertEqual(both.returncode, 0, both.stderr)

    def test_add_rejects_invalid_batch_without_partial_write(self) -> None:
        result = self.admit(SHIPMENT, dict(RESERVATION, concept="Bad Slug"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("lowercase-hyphen slug", result.stderr)
        self.assertFalse(self.lexicon().exists())

    def test_add_rejects_symbols_unknown_fields_and_marker_literals(self) -> None:
        for row, message in (
            (dict(SHIPMENT, code=["ShipmentService"]), "never the symbol"),
            (dict(SHIPMENT, provider="carrier"), "unknown field"),
            (dict(SHIPMENT, note="see compass: logistics.dispatch"), "marker literal"),
        ):
            with self.subTest(message=message):
                result = self.admit(row)
                self.assertEqual(result.returncode, 1)
                self.assertIn(message, result.stderr)

    def test_add_rejects_dangling_address_missing_scope_and_outside_root(self) -> None:
        for row, message in (
            (dict(SHIPMENT, chart="logistics.nowhere"), "resolves to no document"),
            (dict(RESERVATION, scope=["src/nowhere/"]), "not on disk"),
            (dict(SHIPMENT, root="shop"), "not under root"),
        ):
            with self.subTest(message=message):
                result = self.admit(row)
                self.assertEqual(result.returncode, 1)
                self.assertIn(message, result.stderr)

    def test_stale_and_generated_only_stems_are_rejected(self) -> None:
        self.write("dist/bundle.js", "const legacyParcel = 1;\n")
        for stem in ("legacy-parcel", "vanished-name"):
            result = self.admit(dict(SHIPMENT, code=["consignment", stem]))
            self.assertEqual(result.returncode, 1)
            self.assertIn(f"'{stem}' occurs in no identifier", result.stderr)

    def test_dry_run_changes_nothing(self) -> None:
        result = self.admit(SHIPMENT, dry_run=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("would admit", result.stdout)
        self.assertFalse(self.lexicon().exists())

    def test_add_checks_glossary_links_and_canonical_forms_before_writing(self) -> None:
        self.link_shipment()
        wrong = self.admit(dict(SHIPMENT, speech=["SHP", "Shipment"]))
        self.assertEqual(wrong.returncode, 1)
        self.assertIn("first speech form", wrong.stderr)
        self.assertFalse(self.lexicon().exists())
        missing = self.admit(RESERVATION)
        self.assertEqual(missing.returncode, 1)
        self.assertIn("no such row", missing.stderr)
        self.assertFalse(self.lexicon().exists())

    def test_check_detects_handwritten_bad_canonical_link_and_old_alias_section(self) -> None:
        self.link_shipment()
        self.lexicon().write_text(json.dumps(dict(SHIPMENT, speech=["SHP", "Shipment"])) + "\n")
        result = self.run_lex("check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("first speech form", result.stdout)
        self.write(".compass/logistics/GLOSSARY.md", "# Glossary\n\n## **Shipment**\n\n### Implementation aliases\n\n`SHPService`\n")
        self.assertIn("carries ### Implementation aliases", self.run_lex("check").stdout)
        before = self.lexicon().read_bytes()
        self.assertEqual(self.admit(RESERVATION).returncode, 1)
        self.assertEqual(self.lexicon().read_bytes(), before)

    def test_external_pointer_needs_no_local_code_stem(self) -> None:
        self.assertEqual(self.admit(FORECAST).returncode, 0)
        self.assertEqual(self.run_lex("check").returncode, 0)
        result = self.result("resolve", "Weather Forecast timeout")
        self.assertEqual(result["candidates"][0]["external"], [FORECAST["where"]])
        self.assertEqual(result["candidates"][0]["scopes"], [])

    def test_order_and_stale_stems_remain_checked(self) -> None:
        self.admit(SHIPMENT, RESERVATION)
        lines = self.lexicon().read_text().splitlines()
        self.lexicon().write_text("\n".join(reversed(lines)) + "\n")
        self.assertIn("not in the tool's order", self.run_lex("check").stdout)
        self.assertEqual(self.run_lex("sort").returncode, 0)
        self.assertEqual(self.run_lex("check").returncode, 0)
        self.write("src/dispatch/SHPService.ts", "export class ShipmentService {}\n")
        failure = self.run_lex("check")
        self.assertEqual(failure.returncode, 1)
        self.assertIn("code stem 'shp'", failure.stdout)
        self.assertIn("implementation remapping", failure.stdout)

    def test_key_order_is_not_a_contract_and_duplicate_forms_are(self) -> None:
        self.admit(SHIPMENT)
        self.lexicon().write_text(json.dumps(dict(reversed(list(SHIPMENT.items())))) + "\n")
        self.assertEqual(self.run_lex("check").returncode, 0)
        other = dict(RESERVATION, speech=["SHP"])
        self.assertIn("belongs to both", self.admit(other).stderr)
        with self.lexicon().open("a") as stream:
            stream.write(json.dumps(other) + "\n")
        self.assertIn("belongs to both", self.run_lex("check").stdout)

    def test_resolve_exposes_original_strict_and_scopes_before_alternatives(self) -> None:
        self.admit(SHIPMENT, RESERVATION)
        result = self.run_lex("resolve", "SHP booking timeout after cancellation")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("original: SHP booking timeout after cancellation", result.stdout)
        self.assertLess(result.stdout.index("strict:"), result.stdout.index("alternative 1:"))
        self.assertIn("chart query: Shipment Reservation timeout after cancellation", result.stdout)
        self.assertIn("code query: consignment booking timeout after cancellation", result.stdout)
        self.assertIn("src/dispatch/SHPService.ts, src/dispatch/, src/consignments/", result.stdout)
        self.assertIn("unmatched: timeout after cancellation", result.stdout)

    def test_rewrite_preserves_punctuation_qualifiers_and_repeated_occurrences(self) -> None:
        self.admit(SHIPMENT)
        query = "consignment: timeout, after cancellation; consignment retries fail."
        result = self.result("rewrite", query)
        self.assertEqual(result["query"], query)
        self.assertEqual(result["candidates"][0]["chart_query"], "Shipment: timeout, after cancellation; Shipment retries fail.")
        self.assertIn("timeout", result["unmatched"])

    def test_recorded_compact_spaced_hyphen_and_identifier_forms_match(self) -> None:
        self.write("src/checks.ts", "class HealthCheckRunner {}\n")
        row = {"concept": "readiness", "speech": ["Readiness"], "code": ["healthcheck"], "scope": ["src/checks.ts"]}
        self.assertEqual(self.admit(row).returncode, 0)
        for query in ("healthcheck", "HealthCheck", "health-check", "health check", "HealthCheckRunner"):
            with self.subTest(query=query):
                result = self.result("rewrite", query)
                self.assertEqual(result["matches"][0]["concept"], "readiness")
        for query in ("healthchecker", "health to check", "unhealthy checker"):
            with self.subTest(query=query):
                self.assertEqual(self.run_lex("resolve", query).returncode, 1)
        self.assertIn("readiness", self.run_lex("reverse", "HealthCheckRunner").stdout)

    def test_unrecorded_shorthand_is_not_guessed_and_stop_words_are_not_shorthand(self) -> None:
        self.admit(SHIPMENT)
        result = self.run_lex("resolve", "SHP AND the ID")
        shorthand = next(line for line in result.stdout.splitlines() if line.startswith("looks like shorthand"))
        self.assertIn("ID", shorthand)
        self.assertNotIn("AND", shorthand)
        unknown = self.run_lex("resolve", "XYZController is slow")
        self.assertEqual(unknown.returncode, 1)
        self.assertIn("looks like shorthand with no row: XYZController", unknown.stdout)

    def test_missing_lexicon_has_honest_single_and_bulk_misses(self) -> None:
        single = self.run_lex("resolve", "SHP")
        self.assertEqual(single.returncode, 1)
        self.assertIn("strict query stands", single.stderr)
        bulk = self.run_lex("rewrite", "--stdin", stdin='{"id":"missing","query":"SHP timeout"}\n')
        self.assertEqual(bulk.returncode, 1)
        record = json.loads(bulk.stdout)
        self.assertEqual(record["status"], "miss")
        self.assertEqual(record["query"], "SHP timeout")
        self.assertEqual(record["candidates"], [])

    def test_root_collisions_remain_separate_and_filterable(self) -> None:
        self.admit(SHOP_ACCOUNT, COMMUNITY_ACCOUNT)
        result = self.result("rewrite", "Account locked")
        self.assertEqual(result["status"], "ambiguous")
        self.assertEqual(len(result["candidates"]), 2)
        self.assertEqual({c["concepts"][0]["root"] for c in result["candidates"]}, {"shop", "community"})
        narrowed = self.result("rewrite", "--root", "community", "Account locked")
        self.assertEqual(narrowed["status"], "hit")
        self.assertEqual(len(narrowed["candidates"]), 1)
        self.assertEqual(narrowed["candidates"][0]["code_queries"], ["member-account locked"])

    def test_context_senses_in_one_root_are_admitted_and_selectable(self) -> None:
        admitted = self.admit(BILLING_ACCOUNT, IDENTITY_ACCOUNT)
        self.assertEqual(admitted.returncode, 0, admitted.stderr)
        self.assertEqual(self.run_lex("check").returncode, 0)
        result = self.result("rewrite", "--root", "logistics", "Account closed after cancellation")
        self.assertEqual(result["status"], "ambiguous")
        self.assertEqual({c["concepts"][0]["context"] for c in result["candidates"]}, {"billing", "identity"})
        narrowed = self.result("rewrite", "--root", "logistics", "--context", "billing", "Account closed")
        self.assertEqual(narrowed["status"], "hit")
        self.assertEqual(narrowed["candidates"][0]["code_queries"], ["ledger-account closed"])
        duplicate = dict(BILLING_ACCOUNT, concept="another-billing-account")
        self.assertIn("belongs to both", self.admit(duplicate).stderr)
        self.assertIn("context=identity", self.run_lex("reverse", "--context", "identity", "LoginAccountService").stdout)
        self.assertNotIn("billing-account", self.run_lex("list", "--context", "identity").stdout)

    def test_context_requires_actual_domain_heading_and_root(self) -> None:
        result = self.admit(dict(RESERVATION, context="invented"))
        self.assertIn("context requires its owning root", result.stderr)
        result = self.admit(dict(BILLING_ACCOUNT, context="invented"))
        self.assertIn("not a bounded-context heading", result.stderr)
        self.assertFalse(self.lexicon().exists())
        self.write(".compass/logistics/DOMAIN.md", "# Domain\n\n```markdown\n## Invented\n```\n")
        self.assertIn("not a bounded-context heading", self.admit(dict(BILLING_ACCOUNT, context="invented")).stderr)

    def test_same_concept_slug_can_have_two_contextual_senses(self) -> None:
        billing = dict(BILLING_ACCOUNT, concept="account")
        identity = dict(IDENTITY_ACCOUNT, concept="account")
        self.write(".compass/logistics/GLOSSARY.md", "# Glossary\n\n## **Account**\n\n### Lexicon\n\n`account`\n")
        result = self.admit(billing, identity)
        self.assertEqual(result.returncode, 0, result.stderr)
        lookup = self.result("resolve", "Account")
        self.assertEqual(lookup["status"], "ambiguous")
        self.assertEqual({c["concepts"][0]["context"] for c in lookup["candidates"]}, {"billing", "identity"})

    def test_reverse_symbol_path_address_and_bare_root(self) -> None:
        self.admit(SHIPMENT, RESERVATION, SHOP_ACCOUNT, COMMUNITY_ACCOUNT)
        self.assertIn("shipment  (via code stem shp)", self.run_lex("reverse", "SHPService").stdout)
        self.assertIn("reservation  (via scope src/bookings/)", self.run_lex("reverse", "src/bookings/Booking.ts").stdout)
        self.assertIn("shipment  (via chart logistics.dispatch)", self.run_lex("reverse", "--as", "chart", "logistics.dispatch").stdout)
        self.assertIn("root=shop", self.run_lex("reverse", "--as", "chart", "shop").stdout)
        self.assertEqual(self.run_lex("reverse", "UnrecordedSymbol").returncode, 1)

    def test_bulk_preserves_order_ids_errors_misses_and_context_overrides(self) -> None:
        self.admit(SHIPMENT, BILLING_ACCOUNT, IDENTITY_ACCOUNT)
        before = {p: p.read_bytes() for p in self.repo_root.rglob("*") if p.is_file()}
        lines = [
            {"id":"s", "query":"consignment timeout"},
            {"id":"a", "query":"Account locked", "root":"logistics"},
            {"id":"b", "query":"Account locked", "root":"logistics", "context":"billing"},
            {"id":"m", "query":"unrecorded"},
            {"id":"bad", "query":123},
            {"id":"typo", "query":"Shipment", "contex":"billing"},
            {"id":"last", "query":"SHP retry"},
        ]
        result = self.run_lex("rewrite", "--stdin", stdin="\n".join(map(json.dumps, lines)) + "\n")
        self.assertEqual(result.returncode, 2)
        records = list(map(json.loads, result.stdout.splitlines()))
        self.assertEqual([r["id"] for r in records], [r["id"] for r in lines])
        self.assertEqual([r["status"] for r in records], ["hit","ambiguous","hit","miss","error","error","hit"])
        self.assertEqual([r["line"] for r in records], list(range(1,8)))
        self.assertEqual(before, {p:p.read_bytes() for p in self.repo_root.rglob("*") if p.is_file()})
        reverse = self.run_lex("reverse", "--stdin", stdin='{"id":1,"target":"SHPService"}\n{"id":2,"target":"Nothing"}\n')
        self.assertEqual(reverse.returncode, 0)
        self.assertEqual([r["status"] for r in map(json.loads, reverse.stdout.splitlines())], ["hit","miss"])

    def test_bulk_loads_rows_and_coordinates_once(self) -> None:
        self.admit(SHIPMENT)
        spec = importlib.util.spec_from_file_location("lexicon_batch_test", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with patch.object(module, "load_rows", wraps=module.load_rows) as load, \
             patch.object(module, "coordinates_of", wraps=module.coordinates_of) as coords, \
             patch("sys.stdin", io.StringIO('{"query":"Shipment"}\n{"query":"SHP"}\n')), redirect_stdout(io.StringIO()):
            code = module.main(["--chart-root", str(self.chart_root), "resolve", "--stdin"])
        self.assertEqual(code, 0)
        self.assertEqual(load.call_count, 1)
        self.assertEqual(module.coordinates_of.cache_info().misses, 1)

    def test_rewrite_caps_interpretations_and_source_variants_visibly(self) -> None:
        self.admit(SHIPMENT, BILLING_ACCOUNT, IDENTITY_ACCOUNT)
        ambiguous = self.result("rewrite", " ".join(["Account"] * 6))
        self.assertEqual(len(ambiguous["candidates"]), 32)
        self.assertEqual(ambiguous["candidates_omitted"], 32)
        variants = self.result("rewrite", " ".join(["SHP"] * 6))
        self.assertEqual(len(variants["candidates"][0]["code_queries"]), 32)
        self.assertEqual(variants["candidates"][0]["code_queries_omitted"], 32)

    def test_batch_empty_malformed_and_missing_inputs_are_explicit(self) -> None:
        for stdin in ("", "\n", "not-json\n", '[]\n', '{"query":""}\n'):
            with self.subTest(stdin=stdin):
                result = self.run_lex("resolve", "--stdin", stdin=stdin)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(json.loads(result.stdout)["status"], "error")
        self.assertEqual(self.run_lex("resolve").returncode, 2)
        self.assertEqual(self.run_lex("resolve", "input", "--stdin", stdin="").returncode, 2)
        self.assertEqual(self.run_lex("resolve", "--root", "Bad Root", "anything").returncode, 2)

    def test_add_and_check_reject_a_repo_outside_chart_and_invalid_chart(self) -> None:
        for command in ("add", "check"):
            result = subprocess.run([sys.executable,str(SCRIPT),"--chart-root",str(self.chart_root),
                                     "--repo-root",str(self.repo_root/"src"),command], capture_output=True,text=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn("not under repo root", result.stderr)
        result = subprocess.run([sys.executable,str(SCRIPT),"--chart-root",str(self.repo_root/"missing"),"list"],capture_output=True,text=True)
        self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
