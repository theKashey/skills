from __future__ import annotations

import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "compass_search.py"
PACKAGE_ROOT = Path(__file__).parents[1]


class CompassSearchTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory(prefix="compass chart ")
        self.chart_root = Path(self.temporary_directory.name)
        self.write(
            "README.md",
            """
            # Example chart

            ## Scope

            Routes work to the shop root.
            """,
        )
        self.write(
            "COMPASS.md",
            """
            # Registry

            ## Roots

            The shop owns purchasing and account access.
            """,
        )
        self.write(
            "ABSTRACTIONS.md",
            """
            # Named implementation abstractions

            ## Persisted Store Controller (`persisted-store-controller`)

            ### Meaning

            Coordinates restoration of durable client state.

            ### Essential discriminator

            Restoration completes before dependent readers are released.

            ### Nearest non-example

            A cache that may warm after readers start.

            ### Meaning-changing scope

            Reader release order changes the abstraction's meaning.

            ## Request Mapper (`request-mapper`)

            ### Meaning

            Translates an inbound request into domain input.
            """,
        )
        self.write(
            "shop/GLOSSARY.md",
            """
            # Shop glossary

            ## **Workspace**

            ### Meaning

            A customer's isolated collaboration area.

            ### Bounded context

            Account access.

            ### Product appearance

            The workspace switcher.

            ### Implementation aliases

            `Tenant`

            ## **Status**

            ### Meaning

            In fulfillment, the current parcel progress.

            ### Bounded context

            Fulfillment.

            ### Meaning

            In billing, the current invoice settlement state.

            ### Bounded context

            Billing.
            """,
        )
        self.write(
            "shop/DOMAIN.md",
            """
            # Shop domain

            ## Fulfillment

            ### What it is

            Coordinates order preparation and parcel dispatch.

            ### Concepts

            Order, parcel, dispatch window.
            """,
        )
        self.write(
            "shop/CONTAINERS.md",
            """
            # Shop blocks

            ## Blocks

            The Checkout block accepts purchases. The Fulfillment block dispatches them.
            """,
        )
        self.write(
            "shop/checkout/README.md",
            """
            # Checkout

            ## Responsibility

            Accept purchases and hand paid orders to fulfillment.

            ### Implementation coordinates

            `shop.checkout.purchase-entry`
            """,
        )

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def write(self, relative_path: str, value: str) -> None:
        path = self.chart_root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(value).lstrip(), encoding="utf-8")

    def run_search(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--chart-root", str(self.chart_root), *arguments],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_glossary_alias_returns_complete_owning_term(self) -> None:
        result = self.run_search("--kind", "glossary", "--literal-only", "Tenant")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("signal=exact", result.stdout)
        self.assertIn("A customer's isolated collaboration area.", result.stdout)
        self.assertIn("`Tenant`", result.stdout)
        self.assertNotIn("current parcel progress", result.stdout)

    def test_context_specific_glossary_meanings_stay_together(self) -> None:
        result = self.run_search("--kind", "glossary", "--literal-only", "Status")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("In fulfillment, the current parcel progress.", result.stdout)
        self.assertIn("In billing, the current invoice settlement state.", result.stdout)

    def test_abstraction_slug_returns_complete_definition_only(self) -> None:
        result = self.run_search(
            "--kind", "abstraction", "--literal-only", "persisted-store-controller"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("signal=exact", result.stdout)
        self.assertIn("### Essential discriminator", result.stdout)
        self.assertIn("### Nearest non-example", result.stdout)
        self.assertIn("### Meaning-changing scope", result.stdout)
        self.assertNotIn("## Request Mapper", result.stdout)

    def test_abstraction_name_is_an_exact_match(self) -> None:
        result = self.run_search(
            "--kind", "abstraction", "--literal-only", "Persisted Store Controller"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("signal=exact", result.stdout)

    def test_generic_structured_file_is_searchable(self) -> None:
        result = self.run_search("--kind", "blocks", "--literal-only", "dispatches")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("shop/CONTAINERS.md", result.stdout)
        self.assertIn("heading=Shop blocks > Blocks", result.stdout)

    def test_exact_address_is_deterministic(self) -> None:
        result = self.run_search(
            "--kind",
            "identity",
            "--literal-only",
            "shop.checkout.purchase-entry",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("signal=exact", result.stdout)
        self.assertIn("shop/checkout/README.md", result.stdout)

    def test_bm25_adds_non_literal_related_candidate(self) -> None:
        hybrid = self.run_search("--kind", "abstraction", "durable restoration")
        literal = self.run_search(
            "--kind", "abstraction", "--literal-only", "durable restoration"
        )
        self.assertEqual(hybrid.returncode, 0, hybrid.stderr)
        self.assertIn("signal=related", hybrid.stdout)
        self.assertIn("Persisted Store Controller", hybrid.stdout)
        self.assertEqual(literal.returncode, 1)

    def test_bm25_reranks_results_within_a_literal_tier(self) -> None:
        self.write(
            "NOTES.md",
            """
            # Notes

            ## Short

            Shared phrase appears with restoration.

            ## Strong

            Shared phrase appears. Shared phrase is repeated. Shared phrase remains.
            """,
        )
        result = self.run_search("--kind", "other", "--literal-only", "shared phrase")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertLess(
            result.stdout.index("heading=Notes > Strong"),
            result.stdout.index("heading=Notes > Short"),
        )

    def test_exact_match_precedes_high_scoring_related_match(self) -> None:
        self.write(
            "NOTES.md",
            """
            # Notes

            ## Restore State

            A concise exact section.

            ## Repetition

            Restore restore restore state state state while recovery continues.
            """,
        )
        result = self.run_search("--kind", "other", "restore state")
        self.assertEqual(result.returncode, 0, result.stderr)
        first_heading = next(
            line for line in result.stdout.splitlines() if "heading=" in line
        )
        self.assertIn("heading=Notes > Restore State", first_heading)
        self.assertIn("signal=exact", result.stdout)

    def test_stable_ties_use_relative_path_order(self) -> None:
        self.write("zeta/NOTES.md", "# Zeta\n\n## Topic\n\nrareword\n")
        self.write("alpha/NOTES.md", "# Alpha\n\n## Topic\n\nrareword\n")
        first = self.run_search("--kind", "other", "--literal-only", "rareword")
        second = self.run_search("--kind", "other", "--literal-only", "rareword")
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertLess(
            first.stdout.index("alpha/NOTES.md"),
            first.stdout.index("zeta/NOTES.md"),
        )

    def test_long_excerpt_is_bounded_around_the_match(self) -> None:
        filler = "\n".join(f"ordinary line {number}" for number in range(1, 81))
        self.write(
            "DECISIONS.md",
            f"# Decisions\n\n## Recovery\n\n{filler}\n"
            "The checker and its fixtures travel together.\n",
        )
        result = self.run_search(
            "--kind",
            "other",
            "--literal-only",
            "--max-lines",
            "8",
            "the checker and its fixtures",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("The checker and its fixtures travel together.", result.stdout)
        self.assertIn("earlier section lines omitted", result.stdout)

    def test_limit_reports_omitted_matches(self) -> None:
        self.write("NOTES.md", "# Notes\n\n## One\n\nneedle\n\n## Two\n\nneedle\n")
        result = self.run_search(
            "--kind", "other", "--literal-only", "--limit", "1", "needle"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("1 additional matching section(s) omitted", result.stdout)

    def test_invalid_root_and_no_match_have_distinct_exit_codes(self) -> None:
        invalid = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--chart-root",
                str(self.chart_root / "missing"),
                "term",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        no_match = self.run_search("--literal-only", "word-that-is-not-present")
        self.assertEqual(invalid.returncode, 2)
        self.assertEqual(no_match.returncode, 1)


    def test_address_resolves_to_its_directory_without_a_literal(self) -> None:
        self.write(
            "shop/checkout/purchase-entry/README.md",
            """
            # Purchase entry

            ## Responsibility

            Accept a purchase request.
            """,
        )
        result = self.run_search("--literal-only", "shop.checkout.purchase-entry")
        self.assertEqual(result.returncode, 0, result.stderr)
        first = result.stdout.index("[1] ")
        self.assertIn("shop/checkout/purchase-entry/README.md", result.stdout[first:].split("\n")[0])
        self.assertIn("signal=address", result.stdout)

    def test_unresolved_address_is_routed_to_classification(self) -> None:
        result = self.run_search("--literal-only", "shop.nowhere.thing")
        self.assertIn("shop.nowhere.thing resolves to no chart document", result.stderr)
        self.assertIn("classification finding", result.stderr)

    def test_entity_owner_precedes_its_consumers(self) -> None:
        self.write(
            "shop/fulfillment/README.md",
            """
            # Fulfillment

            ## Communicates with

            - ← [`checkout`](../checkout/README.md) — paid orders arrive here
            """,
        )
        result = self.run_search("--literal-only", "checkout")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertLess(
            result.stdout.index("shop/checkout/README.md"),
            result.stdout.index("shop/fulfillment/README.md"),
        )
        first = next(line for line in result.stdout.splitlines() if "signal=" in line)
        self.assertIn("signal=exact", first)

    def test_heading_tier_reads_the_section_heading_not_its_ancestry(self) -> None:
        self.write(
            "NOTES.md",
            """
            # Order Core

            ## Billing

            Settles invoices.

            ## Order lifecycle

            From draft to fulfilled.
            """,
        )
        result = self.run_search("--kind", "other", "--literal-only", "Order")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("heading=Order Core > Order lifecycle", result.stdout)
        self.assertNotIn("heading=Order Core > Billing", result.stdout)

    def test_task_phrase_matches_the_glossary_term_inside_it(self) -> None:
        result = self.run_search("--literal-only", "move a workspace between accounts")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("signal=exact term='workspace'", result.stdout)
        self.assertIn("A customer's isolated collaboration area.", result.stdout)
        named_nowhere = result.stdout.split("Named nowhere in the chart:")[1].split("\n")[0]
        self.assertIn("move", named_nowhere)


class CompassPackageContractTest(unittest.TestCase):
    def test_agent_hook_is_a_four_line_search_contract(self) -> None:
        hook = PACKAGE_ROOT / "references" / "agent-hook.md"
        lines = [line for line in hook.read_text(encoding="utf-8").splitlines() if line]
        self.assertEqual(len(lines), 4)
        rendered = "\n".join(lines)
        self.assertIn("{compass-skill}/scripts/compass_search.py", rendered)
        self.assertIn('--chart-root "{chart-root}"', rendered)
        self.assertIn("building any capability", rendered)
        self.assertIn("BM25-related results are leads", rendered)
        self.assertNotIn("--kind", rendered)
        self.assertNotIn("semantic search", rendered.casefold())


if __name__ == "__main__":
    unittest.main()
