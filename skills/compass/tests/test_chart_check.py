from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


VERIFICATION = Path(__file__).parents[1] / "references" / "verification.md"

BLOCK = """
# {name}

## Responsibility

{name} does one thing.

## Logical role

Holds the {name} phenomenon.

## Boundary

Does not do the other thing.

## Technology

Python.

## Implementation coordinates

{coordinates}

## Communicates with

{wires}
## Uses

{uses}
## Components

| Component | Responsibility |
|---|---|
| entry | accepts work |

## Diagram

```mermaid
flowchart LR
  a --> b
```
"""

COMPONENT = """
# entry

## Stereotype

«handler»

## Responsibility

Accepts work.

## Bounded context

Selling.

## Inputs and outputs

Orders in, receipts out.

## Depends on

- nothing yet

## Used by

- the block

## Boundary

Does not ship.

## Implementation coordinates

{coordinates}

## Diagram

```mermaid
flowchart LR
  a --> b
```
"""

VIEWPORTS = """
# Viewports — shop

## How does a paid order reach fulfillment?

### Type

{kind}

### Question

Where the handover happens.

### Participants

- [`entry`](./checkout/entry/README.md) — accepts the order

### Diagram

```mermaid
sequenceDiagram
  a->>b: order
```

### Seams

The order payload.
"""

DIAGRAM = "\n## Diagram\n\n```mermaid\nflowchart TD\n  a --> b\n```\n"

ABSTRACTIONS = """
# Abstractions

## Deferred Reader (`deferred-reader`)

### Meaning

Reads durable state after restoration.

### Essential discriminator

Blocks readers until restoration ends.

### Nearest non-example

A cache that warms after readers start.
"""


def chart_check_template() -> str:
    text = VERIFICATION.read_text(encoding="utf-8")
    fence = re.search(r"^````python\n(.*?)^````$", text, re.M | re.S)
    assert fence, "verification.md carries no ````python chart_check fence"
    template = fence.group(1)
    # the source-side minimum a host commits once Phase F has sealed anything
    committed = template.replace('"addresses": 0, "abstraction_markers": 0}',
                                 '"addresses": 1, "abstraction_markers": 0}')
    assert committed != template, "MINIMUM line in verification.md changed shape"
    return committed


class ChartCheckTest(unittest.TestCase):
    """Runs the chart check template from verification.md against a host built in a temp dir.

    The base host is a template-complete chart — root `shop`, blocks `checkout` and
    `fulfillment`, component `checkout/entry`, one lifecycle viewport — sealed by one
    coordinate in `src/checkout/app.py`. Each test breaks exactly one thing.
    """

    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory(prefix="compass host ")
        self.host = Path(self.temporary_directory.name)
        (self.host / "chart_check.py").write_text(chart_check_template(), encoding="utf-8")
        (self.host / "src" / "fulfillment").mkdir(parents=True)
        self.write("src/checkout/app.py", "# compass: shop.checkout\n")
        self.write(".compass/README.md", "# Chart\n\n## Scope\n\nThe shop.\n")
        self.write(".compass/COMPASS.md", "# Registry\n\n[Shop](shop/README.md)\n")
        self.write(".compass/shop/README.md", "# Shop\n\n## Scope\n\nSelling.\n" + DIAGRAM)
        self.write(
            ".compass/shop/CONTAINERS.md",
            "# Blocks — shop\n\n## Blocks\n\n- [Checkout](./checkout/README.md)\n"
            "- [Fulfillment](./fulfillment/README.md)\n" + DIAGRAM,
        )
        self.block(
            "checkout",
            wires="- → [`fulfillment`](../fulfillment/README.md) — hands over paid orders\n",
            uses="### [`fulfillment`](../fulfillment/README.md)\n\n#### Why\n\nSomeone must ship.\n",
        )
        self.block("fulfillment", wires="- ← [`checkout`](../checkout/README.md#uses) — paid orders arrive\n")
        self.component()
        self.write(".compass/shop/VIEWPORTS.md", VIEWPORTS.format(kind="lifecycle"))

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    # -- fixture builders -------------------------------------------------------------

    def write(self, relative_path: str, value: str) -> None:
        path = self.host / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(value).lstrip("\n"), encoding="utf-8")

    def block(self, name: str, *, coordinates: str | None = None, wires: str = "", uses: str = "",
              prefix: str = "") -> None:
        body = BLOCK.format(name=name, coordinates=coordinates or f"`src/{name}/`", wires=wires, uses=uses)
        self.write(f".compass/shop/{name}/README.md", prefix + body.lstrip("\n"))

    def component(self, *, coordinates: str = "`src/checkout/`") -> None:
        self.write(".compass/shop/checkout/entry/README.md", COMPONENT.format(coordinates=coordinates))

    def root(self, name: str, *, coordinates: str | None = None) -> None:
        body = f"# {name}\n\n## Scope\n\nAnother product.\n"
        if coordinates:
            body += f"\n## Implementation coordinates\n\n{coordinates}\n"
        self.write(f".compass/{name}/README.md", body + DIAGRAM)
        self.write(f".compass/{name}/CONTAINERS.md", f"# Blocks — {name}\n\n## Blocks\n" + DIAGRAM)

    def edit(self, relative_path: str, old: str, new: str) -> None:
        path = self.host / relative_path
        text = path.read_text(encoding="utf-8")
        assert old in text, f"{relative_path} does not contain {old!r}"
        path.write_text(text.replace(old, new), encoding="utf-8")

    # -- running ----------------------------------------------------------------------

    def run_check(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "chart_check.py"], cwd=self.host,
            check=False, capture_output=True, text=True,
        )

    def assert_pass(self) -> str:
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("chart: clean", result.stdout)
        return result.stdout

    def assert_failure(self, *messages: str) -> str:
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        for message in messages:
            self.assertIn(message, result.stdout)
        return result.stdout

    # -- the base chart and the scan minimum -------------------------------------------

    def test_template_chart_is_clean(self) -> None:
        self.assertIn("1 addresses", self.assert_pass())

    def test_scan_that_stopped_looking_fails_the_committed_minimum(self) -> None:
        self.write("src/checkout/app.py", "value = 1\n")
        self.assert_failure("addresses: 0 scanned, minimum is 1")

    def test_failure_routes_to_classification(self) -> None:
        # a chart-versus-code failure alone routes to classification and never to the template rewrite
        self.write("src/checkout/app.py", "# compass: shop.missing\n")
        out = self.assert_failure("shop.missing resolves to nothing", "Classify each other failure before repairing it")
        self.assertNotIn("template:", out)

    # -- coordinate markers: where the checker looks and what it accepts -------------------

    def test_hidden_source_directory_is_scanned(self) -> None:
        self.write(".storybook/preview.ts", "// compass: shop.checkout\n")
        self.assertIn("2 addresses", self.assert_pass())
        self.write(".storybook/preview.ts", "// compass: shop.missing\n")
        self.assert_failure("shop.missing resolves to nothing")

    def test_supported_comment_forms_and_a_second_root(self) -> None:
        self.root("ledger")
        self.write("src/query.sql", "-- compass: shop.checkout\n-- compass: ledger\n")
        self.write("src/worker.py", "# Header\nimport os\n# compass: shop.checkout\n")
        self.assertIn("4 addresses", self.assert_pass())

    def test_malformed_coordinate_literals_fail(self) -> None:
        for claim in (
            "// compass:shop.checkout\n", "// compass:\n// shop.checkout\n",
            "// compass: \n", "// compass: shop..checkout\n",
            "/* compass: shop.checkout */\n", "// compass: ../README\n",
        ):
            with self.subTest(claim=claim):
                self.write("src/invalid.ts", claim)
                self.assert_failure("src/invalid.ts")

    def test_unsupported_suffix_cannot_hide_either_marker(self) -> None:
        for marker in ("compass: shop.checkout", "compass-abstraction: deferred-reader"):
            with self.subTest(marker=marker):
                self.write("src/view.vue", "<!-- " + marker + " -->\n")
                self.assert_failure("marker outside SRC_SUFFIXES")

    def test_excluded_trees_and_documentation_create_no_claims(self) -> None:
        for directory in (".git", "node_modules", ".venv", "tests/fixtures/compass"):
            self.write(directory + "/bad.ts", "// compass: missing\n// compass-abstraction: missing\n")
        self.write("worktrees/other/.git", "gitdir: elsewhere\n")
        self.write("worktrees/other/bad.ts", "// compass: missing\n")
        self.write("docs/example.md", "```ts\n// compass: missing\n```\n")
        self.assertIn("1 addresses", self.assert_pass())

    # -- named abstractions -------------------------------------------------------------

    def test_hidden_abstraction_claim_resolves(self) -> None:
        self.write(".compass/ABSTRACTIONS.md", ABSTRACTIONS)
        self.write(".hidden/reader.ts", "// compass-abstraction: deferred-reader\n")
        self.assertIn("1 abstraction_markers", self.assert_pass())

    def test_claim_without_a_definition_fails(self) -> None:
        self.write("src/reader.ts", "// compass-abstraction: deferred-reader\n")
        self.assert_failure("does not resolve exactly once")

    def test_invalid_abstraction_forms_fail(self) -> None:
        self.write(".compass/ABSTRACTIONS.md", ABSTRACTIONS)
        for claim in (
            "// compass-abstraction: Bad_Name\n", "// compass-abstraction:deferred-reader\n",
            "// compass-abstraction:\n// deferred-reader\n",
            "/* compass-abstraction: deferred-reader */\n",
        ):
            with self.subTest(claim=claim):
                self.write("src/reader.ts", claim)
                self.assert_failure("src/reader.ts")

    def test_duplicate_definition_and_missing_field_fail(self) -> None:
        catalog = self.host / ".compass/ABSTRACTIONS.md"
        self.write(".compass/ABSTRACTIONS.md", ABSTRACTIONS)
        body = catalog.read_text(encoding="utf-8")
        catalog.write_text(body + body, encoding="utf-8")
        self.assert_failure("duplicate abstraction slug")
        catalog.write_text(body.split("### Nearest non-example")[0], encoding="utf-8")
        self.assert_failure("lacks ### Nearest non-example")

    # -- inherited coordinates: carrier covers subtree ----------------------------------

    def test_nested_scopes_file_exception_and_independent_root(self) -> None:
        self.block("checkout", coordinates="- `src/checkout/app.py` covers `src/checkout/`",
                   wires="- → [`fulfillment`](../fulfillment/README.md) — hands over\n",
                   uses="### [`fulfillment`](../fulfillment/README.md)\n\n#### Why\n\nSomeone must ship.\n")
        self.component(coordinates="- `src/checkout/pricing/rules.ts` covers `src/checkout/pricing/`")
        self.root("ledger", coordinates="- `src/checkout/app.py` covers `src/checkout/`")
        self.write("src/checkout/app.py", "# compass: shop.checkout\n# compass: ledger\n")
        self.write("src/checkout/pricing/rules.ts", "// compass: shop.checkout.entry\n")
        self.write("src/checkout/pricing/round.ts", "export const round = Math.round;\n")
        self.write("src/checkout/pricing/exception.ts", "// compass: shop.checkout\n")
        self.assert_pass()

    def test_scope_requires_the_carrier_to_hold_the_declaring_address(self) -> None:
        self.block("checkout", coordinates="- `src/helper.ts` covers `src/`")
        self.assert_failure("carrier src/helper.ts lacks compass: shop.checkout")
        self.write("src/helper.ts", "// compass: shop\n")
        self.assert_failure("carrier src/helper.ts lacks compass: shop.checkout")

    def test_scope_carrier_must_be_inside_the_subtree(self) -> None:
        self.write("other/file.ts", "export const x = 1;\n")
        self.block("checkout", coordinates="- `src/checkout/app.py` covers `other/`")
        self.assert_failure("is not inside subtree")

    def test_malformed_scope_declaration_fails(self) -> None:
        self.block("checkout", coordinates="- `src/checkout/app.py` covers src/checkout/")
        self.assert_failure("malformed carrier/subtree declaration")
        self.block("checkout", coordinates="- `src/checkout/app.py` covers `src/checkout`")
        self.assert_failure("scope needs an addressed README and repository-relative paths")

    def test_conflicting_same_root_carriers_fail(self) -> None:
        self.block("checkout", coordinates="- `src/checkout/app.py` covers `src/`")
        self.component(coordinates="- `src/pricing.ts` covers `src/`")
        self.write("src/pricing.ts", "// compass: shop.checkout.entry\n")
        self.assert_failure("conflicting carrier scopes for root shop")

    # -- links, paths, and the document templates --------------------------------------

    def test_dead_link_and_missing_coordinate_fail(self) -> None:
        self.block("checkout", coordinates="`src/missing.ts`", prefix="[Missing](./missing.md)\n\n")
        self.assert_failure("dead link", "coordinate src/missing.ts not on disk")

    def test_missing_block_heading_fails(self) -> None:
        self.edit(".compass/shop/checkout/README.md", "## Boundary\n\nDoes not do the other thing.\n", "")
        out = self.assert_failure("checkout/README.md: template: missing ## Boundary",
                                  "A `template:` failure is a document written to an earlier or incomplete")
        self.assertNotIn("Classify each other failure", out)

    def test_outbound_wire_without_a_uses_entry_fails(self) -> None:
        self.edit(".compass/shop/checkout/README.md",
                  "### [`fulfillment`](../fulfillment/README.md)\n\n#### Why\n\nSomeone must ship.\n", "")
        self.assert_failure("template: → fulfillment has no ### entry under ## Uses")

    def test_missing_component_table_fails(self) -> None:
        block = self.host / ".compass/shop/fulfillment/README.md"
        block.write_text(re.sub(r"^\|.*\|\n", "", block.read_text(encoding="utf-8"), flags=re.M), encoding="utf-8")
        self.assert_failure("fulfillment/README.md: template: no component table")

    def test_component_without_a_stereotype_heading_fails(self) -> None:
        self.edit(".compass/shop/checkout/entry/README.md", "## Stereotype\n\n«handler»\n\n", "")
        self.assert_failure("entry/README.md: template: missing ## Stereotype")

    def test_component_with_a_prose_stereotype_is_named_as_the_older_template(self) -> None:
        self.edit(".compass/shop/checkout/entry/README.md", "## Stereotype\n\n«handler»\n\n", "«handler»\n\n")
        out = self.assert_failure("entry/README.md: template: written to an earlier Compass template",
                                  "stereotype is a prose line, now ## Stereotype")
        self.assertNotIn("missing ## Stereotype", out)

    def test_both_failure_kinds_route_separately(self) -> None:
        self.edit(".compass/shop/checkout/entry/README.md", "## Stereotype\n\n«handler»\n\n", "")
        self.write("src/checkout/stray.ts", "// compass: shop.missing\n")
        self.assert_failure("A `template:` failure is a document written to an earlier or incomplete",
                            "Classify each other failure before repairing it")

    def test_viewport_type_as_a_prose_line_fails(self) -> None:
        self.edit(".compass/shop/VIEWPORTS.md", "### Type\n\nlifecycle\n", "Type: lifecycle\n")
        out = self.assert_failure("template: viewport", "written to an earlier Compass template",
                                  "type is a prose line, now ### Type")
        self.assertNotIn("missing ### Type", out)
        self.assertNotIn("missing ### Question", out)

    def test_viewport_without_any_type_is_missing_not_older(self) -> None:
        self.edit(".compass/shop/VIEWPORTS.md", "### Type\n\nlifecycle\n", "")
        self.assertNotIn("earlier Compass template", self.assert_failure("template: viewport", "missing ### Type"))

    def test_viewport_with_an_unknown_type_fails(self) -> None:
        self.write(".compass/shop/VIEWPORTS.md", VIEWPORTS.format(kind="sequence"))
        self.assert_failure("template: viewport", "type 'sequence' is not runtime, domain, boundary, or lifecycle")

    def test_viewport_with_an_empty_type_fails(self) -> None:
        self.write(".compass/shop/VIEWPORTS.md", VIEWPORTS.format(kind=""))
        self.assert_failure("type '' is not runtime, domain, boundary, or lifecycle")


if __name__ == "__main__":
    unittest.main()
