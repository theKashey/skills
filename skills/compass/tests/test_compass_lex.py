from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "compass_lex.py"

WORK_ITEM_VIEW = {
    "concept": "work-item-view",
    "speech": ["Work Item", "WIV", "work item view"],
    "code": ["wiv", "work-item"],
    "chart": "tracker.work-item-view",
}
QUICK_ACTION = {
    "concept": "quick-action",
    "speech": ["QuickAction", "quick action"],
    "code": ["action-dropdown"],
    "scope": ["src/work-item/menu/"],
    "note": "a controller composing activities",
}
GATEWAY = {
    "concept": "atlassian-graphql-gateway",
    "speech": ["AGG", "Atlassian GraphQL Gateway"],
    "code": ["agg", "relay"],
    "where": "relay schema at https://example.test/schema; federation in repo-xyz",
}
SENSE_VARIANCE = {
    "concept": "sense",
    "root": "variance-authority",
    "speech": ["sense"],
    "code": ["sense"],
    "chart": "variance-authority.sense",
}
SENSE_SHADOW = {
    "concept": "sense",
    "root": "shadow",
    "speech": ["sense"],
    "code": ["shadow-sense"],
    "chart": "shadow.shadow-sense",
}


class CompassLexTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory(prefix="compass lexicon ")
        self.repo_root = Path(self.temporary_directory.name)
        self.chart_root = self.repo_root / ".compass"
        self.write(
            ".compass/tracker/work-item-view/README.md",
            """
            # Work Item View

            ## Implementation coordinates

            `src/wiv/WIVService.ts` covers `src/wiv/`

            `src/work-item/`
            """,
        )
        self.write(
            ".compass/tracker/GLOSSARY.md",
            """
            # Glossary — tracker

            ## **Work Item**

            ### Meaning

            A unit of tracked work.

            ### Lexicon

            `work-item-view`
            """,
        )
        self.write(".compass/variance-authority/sense/README.md", "# Sense\n")
        self.write(".compass/shadow/shadow-sense/README.md", "# Shadow sense\n")
        self.write("src/wiv/WIVService.ts", "export class WIVService {}\nconst workItem = 1;\n")
        self.write("src/work-item/menu/ActionDropdown.tsx", "export const ActionDropdown = () => null;\n")
        self.write("src/work-item/index.ts", "import { relay } from 'agg';\nconst aggClient = 1;\n")
        self.write("src/sense/senseModel.ts", "export const sense = 1;\n")
        self.write("src/shadow/ShadowSense.ts", "export class ShadowSense {}\n")

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def write(self, relative_path: str, value: str) -> None:
        path = self.repo_root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(value).lstrip(), encoding="utf-8")

    def run_lex(self, *arguments: str, stdin: str | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--chart-root",
                str(self.chart_root),
                "--repo-root",
                str(self.repo_root),
                *arguments,
            ],
            check=False,
            capture_output=True,
            text=True,
            input=stdin,
        )

    def admit(self, *rows: dict) -> subprocess.CompletedProcess[str]:
        return self.run_lex("add", "--stdin", stdin="\n".join(json.dumps(r) for r in rows) + "\n")

    def lexicon(self) -> str:
        return (self.chart_root / "LEXICON.jsonl").read_text(encoding="utf-8")

    # --- admission -------------------------------------------------------------------

    def test_add_admits_a_batch_and_writes_it_in_tool_order(self) -> None:
        result = self.admit(WORK_ITEM_VIEW, QUICK_ACTION, GATEWAY, SENSE_VARIANCE, SENSE_SHADOW)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("admitted 5 row(s)", result.stdout)
        concepts = [json.loads(line)["concept"] for line in self.lexicon().splitlines()]
        self.assertEqual(
            concepts, ["atlassian-graphql-gateway", "quick-action", "work-item-view", "sense", "sense"]
        )
        self.assertEqual(self.run_lex("check").returncode, 0)

    def test_add_rejects_a_row_lexical_search_already_bridges(self) -> None:
        row = {"concept": "work-item", "speech": ["work item"], "code": ["work-item"], "chart": "tracker.work-item-view"}
        result = self.admit(row)
        self.assertEqual(result.returncode, 1)
        self.assertIn("share vocabulary", result.stderr)
        self.assertFalse((self.chart_root / "LEXICON.jsonl").exists())

    def test_add_admits_a_shared_form_only_when_another_root_claims_it(self) -> None:
        alone = self.admit(SENSE_VARIANCE)
        self.assertEqual(alone.returncode, 1, alone.stdout)
        self.assertIn("share vocabulary", alone.stderr)
        both = self.admit(SENSE_VARIANCE, SENSE_SHADOW)
        self.assertEqual(both.returncode, 0, both.stderr)

    def test_add_rejects_a_batch_as_one_unit(self) -> None:
        bad = {"concept": "Bad Slug", "speech": ["x"], "code": ["x"], "chart": "tracker.work-item-view"}
        result = self.admit(WORK_ITEM_VIEW, bad)
        self.assertEqual(result.returncode, 1)
        self.assertIn("concept must be a lowercase-hyphen slug", result.stderr)
        self.assertFalse((self.chart_root / "LEXICON.jsonl").exists())

    def test_add_rejects_a_symbol_written_as_a_stem(self) -> None:
        row = dict(WORK_ITEM_VIEW, code=["WIVService"])
        result = self.admit(row)
        self.assertEqual(result.returncode, 1)
        self.assertIn("never the symbol", result.stderr)

    def test_add_rejects_a_dangling_chart_address_and_a_missing_scope(self) -> None:
        dangling = dict(WORK_ITEM_VIEW, chart="tracker.nowhere")
        result = self.admit(dangling)
        self.assertEqual(result.returncode, 1)
        self.assertIn("resolves to no document", result.stderr)
        missing = dict(QUICK_ACTION, scope=["src/nowhere/"])
        result = self.admit(missing)
        self.assertEqual(result.returncode, 1)
        self.assertIn("is not on disk", result.stderr)

    def test_add_rejects_a_stem_no_identifier_carries(self) -> None:
        row = dict(WORK_ITEM_VIEW, code=["wiv", "work-item", "legacy-panel"])
        result = self.admit(row)
        self.assertEqual(result.returncode, 1)
        self.assertIn("'legacy-panel' occurs in no identifier", result.stderr)

    def test_add_rejects_a_marker_literal_inside_a_row(self) -> None:
        row = dict(QUICK_ACTION, note="see compass: tracker.work-item-view")
        result = self.admit(row)
        self.assertEqual(result.returncode, 1)
        self.assertIn("marker literal", result.stderr)

    def test_add_dry_run_writes_nothing(self) -> None:
        result = self.run_lex("add", "--dry-run", "--row", json.dumps(WORK_ITEM_VIEW))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("would admit 1 row(s)", result.stdout)
        self.assertFalse((self.chart_root / "LEXICON.jsonl").exists())

    # --- check -----------------------------------------------------------------------

    def test_check_fails_a_glossary_link_to_no_row(self) -> None:
        self.admit(QUICK_ACTION, GATEWAY)
        result = self.run_lex("check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("### Lexicon names 'work-item-view', no such row", result.stdout)

    def test_check_fails_when_the_glossary_term_is_not_the_first_speech_form(self) -> None:
        self.admit(dict(WORK_ITEM_VIEW, speech=["WIV", "Work Item", "work item view"]))
        result = self.run_lex("check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("not row work-item-view's first speech form ('WIV')", result.stdout)

    def test_where_row_needs_no_code_stem_and_is_never_stem_checked(self) -> None:
        row = {"concept": "ledger", "speech": ["Ledger", "PL"], "code": [], "where": "ledger service repository"}
        result = self.admit(WORK_ITEM_VIEW, row)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.run_lex("check").returncode, 0)
        resolved = self.run_lex("resolve", "PL is down")
        self.assertEqual(resolved.stdout.count("ledger service repository"), 1)

    def test_add_rejects_a_stem_found_only_in_a_build_tree(self) -> None:
        self.write("dist/bundle.js", "var legacyPanel = 1;\n")
        row = dict(WORK_ITEM_VIEW, code=["wiv", "legacy-panel"])
        result = self.admit(row)
        self.assertEqual(result.returncode, 1)
        self.assertIn("'legacy-panel' occurs in no identifier", result.stderr)

    def test_resolve_never_flags_a_stop_word_as_shorthand(self) -> None:
        self.admit(WORK_ITEM_VIEW)
        result = self.run_lex("resolve", "WIV AND the ID")
        self.assertIn("looks like shorthand with no row: ID", result.stdout)
        self.assertNotIn("AND", result.stdout.split("looks like")[1])

    def test_check_fails_a_glossary_that_still_carries_implementation_aliases(self) -> None:
        self.write(
            ".compass/tracker/GLOSSARY.md",
            """
            # Glossary — tracker

            ## **Work Item**

            ### Implementation aliases

            `WIVService`
            """,
        )
        result = self.run_lex("check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("carries ### Implementation aliases", result.stdout)

    def test_check_fails_a_hand_edited_order_and_sort_repairs_it(self) -> None:
        self.admit(WORK_ITEM_VIEW, QUICK_ACTION)
        lines = self.lexicon().splitlines()
        (self.chart_root / "LEXICON.jsonl").write_text("\n".join(reversed(lines)) + "\n", encoding="utf-8")
        result = self.run_lex("check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("not in the tool's order", result.stdout)
        self.assertEqual(self.run_lex("sort").returncode, 0)
        self.assertEqual(self.run_lex("check").returncode, 0)

    def test_check_fails_a_stale_stem_after_source_renames(self) -> None:
        self.admit(WORK_ITEM_VIEW)
        self.write("src/wiv/WIVService.ts", "export class WorkItemViewService {}\n")
        result = self.run_lex("check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("code stem 'wiv' occurs in no identifier", result.stdout)
        self.assertIn("implementation remapping", result.stdout)

    def test_add_and_check_share_the_duplicate_form_rule(self) -> None:
        self.admit(WORK_ITEM_VIEW)
        second = {"concept": "board", "speech": ["WIV"], "code": ["work-item"], "chart": "tracker.work-item-view"}
        result = self.admit(second)
        self.assertEqual(result.returncode, 1)
        self.assertIn("belongs to both", result.stderr)
        lines = self.lexicon().splitlines()
        (self.chart_root / "LEXICON.jsonl").write_text("\n".join(lines + [json.dumps(second)]) + "\n", encoding="utf-8")
        result = self.run_lex("check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("belongs to both", result.stdout)

    def test_add_rejects_an_address_outside_the_row_root(self) -> None:
        result = self.admit(dict(SENSE_SHADOW, chart="tracker.work-item-view"), SENSE_VARIANCE)
        self.assertEqual(result.returncode, 1)
        self.assertIn("is not under root shadow", result.stderr)

    def test_check_accepts_hand_written_key_order_when_row_order_holds(self) -> None:
        self.admit(WORK_ITEM_VIEW, QUICK_ACTION)
        rows = [json.loads(line) for line in self.lexicon().splitlines()]
        text = "\n".join(json.dumps({k: row[k] for k in reversed(list(row))}) for row in rows) + "\n"
        (self.chart_root / "LEXICON.jsonl").write_text(text, encoding="utf-8")
        self.assertEqual(self.run_lex("check").returncode, 0)

    # --- resolve ---------------------------------------------------------------------

    def test_resolve_discloses_strict_tokens_before_the_expansion(self) -> None:
        self.admit(WORK_ITEM_VIEW, QUICK_ACTION, GATEWAY)
        result = self.run_lex("resolve", "There is a problem in WIV QuickAction around AGG")
        self.assertEqual(result.returncode, 0, result.stderr)
        lines = result.stdout.splitlines()
        self.assertTrue(lines[0].startswith("strict: "), lines[0])
        self.assertIn("WIV [speech], wiv [code] → work-item-view", result.stdout)
        self.assertIn("scope: src/wiv/WIVService.ts, src/wiv/, src/work-item/", result.stdout)
        self.assertIn("code: action-dropdown", result.stdout)
        self.assertIn("where: outside this repository — relay schema", result.stdout)
        self.assertIn("unmatched: there problem around", result.stdout)
        self.assertLess(result.stdout.index("strict:"), result.stdout.index("expanded:"))
        self.assertIn("search in: src/work-item/menu/ src/wiv/WIVService.ts", result.stdout)

    def test_resolve_lists_every_root_on_a_collision_and_narrows_with_root(self) -> None:
        self.admit(SENSE_VARIANCE, dict(SENSE_SHADOW, concept="shadow-sense"))
        result = self.run_lex("resolve", "sense is wrong")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("collision: sense — one form, several roots", result.stdout)
        self.assertIn("root=shadow", result.stdout)
        self.assertIn("root=variance-authority", result.stdout)
        narrowed = self.run_lex("resolve", "--root", "shadow", "sense is wrong")
        self.assertNotIn("collision:", narrowed.stdout)
        self.assertNotIn("variance-authority", narrowed.stdout)

    def test_resolve_names_unrowed_shorthand_and_exits_one(self) -> None:
        self.admit(WORK_ITEM_VIEW)
        result = self.run_lex("resolve", "PTSController is flaky")
        self.assertEqual(result.returncode, 1)
        self.assertIn("looks like shorthand with no row: PTSController", result.stdout)
        self.assertIn("unmatched: pts controller flaky", result.stdout)

    def test_resolve_without_a_lexicon_keeps_the_strict_query(self) -> None:
        result = self.run_lex("resolve", "WIV")
        self.assertEqual(result.returncode, 1)
        self.assertIn("nothing to translate; the strict query stands", result.stderr)

    # --- reverse ---------------------------------------------------------------------

    def test_reverse_from_symbol_path_and_address(self) -> None:
        self.admit(WORK_ITEM_VIEW, QUICK_ACTION)
        symbol = self.run_lex("reverse", "WIVService")
        self.assertEqual(symbol.returncode, 0, symbol.stderr)
        self.assertIn("work-item-view  (via code stem wiv)", symbol.stdout)
        self.assertIn("say: Work Item, WIV, work item view", symbol.stdout)
        path = self.run_lex("reverse", "src/work-item/menu/ActionDropdown.tsx")
        self.assertIn("quick-action  (via scope src/work-item/menu/)", path.stdout)
        self.assertIn("work-item-view  (via scope src/work-item/)", path.stdout)
        address = self.run_lex("reverse", "--as", "chart", "tracker.work-item-view")
        self.assertIn("work-item-view  (via chart tracker.work-item-view)", address.stdout)
        miss = self.run_lex("reverse", "NothingHere")
        self.assertEqual(miss.returncode, 1)

    def test_reverse_bare_root_returns_every_row_of_that_root(self) -> None:
        self.admit(WORK_ITEM_VIEW, SENSE_VARIANCE, SENSE_SHADOW)
        result = self.run_lex("reverse", "--as", "chart", "shadow")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("sense root=shadow  (via root shadow)", result.stdout)
        self.assertNotIn("variance-authority", result.stdout)

    def test_add_and_check_refuse_a_repo_root_outside_the_chart(self) -> None:
        self.admit(WORK_ITEM_VIEW)
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--chart-root", str(self.chart_root),
             "--repo-root", str(self.repo_root / "src"), "check"],
            check=False, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertIn("is not under repo root", result.stderr)

    # --- cli -------------------------------------------------------------------------

    def test_list_renders_a_table_and_root_narrows_it(self) -> None:
        self.admit(WORK_ITEM_VIEW, SENSE_VARIANCE, SENSE_SHADOW)
        result = self.run_lex("list", "--root", "shadow")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("| shadow | sense |", result.stdout)
        self.assertNotIn("variance-authority", result.stdout)

    def test_invalid_chart_root_exits_two(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--chart-root", str(self.repo_root / "missing"), "check"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
