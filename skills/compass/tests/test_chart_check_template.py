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

`src/{name}/`

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

`src/checkout/`

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


def chart_check_template() -> str:
    text = VERIFICATION.read_text(encoding="utf-8")
    fence = re.search(r"^````python\n(.*?)^````$", text, re.M | re.S)
    assert fence, "verification.md carries no ````python chart_check fence"
    return fence.group(1)


class ChartCheckTemplateTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory(prefix="compass host ")
        self.host = Path(self.temporary_directory.name)
        (self.host / "chart_check.py").write_text(chart_check_template(), encoding="utf-8")
        for name in ("checkout", "fulfillment"):
            (self.host / "src" / name).mkdir(parents=True)
        (self.host / "src" / "checkout" / "app.py").write_text(
            "# compass: shop.checkout\n", encoding="utf-8"
        )
        self.write(".compass/README.md", "# Chart\n\n## Scope\n\nThe shop.\n")
        self.write(
            ".compass/shop/README.md",
            "# Shop\n\n## Scope\n\nSelling.\n\n## Diagram\n\n```mermaid\nflowchart LR\n  a --> b\n```\n",
        )
        self.write(
            ".compass/shop/CONTAINERS.md",
            "# Blocks — shop\n\n## Blocks\n\n- [Checkout](./checkout/README.md)\n"
            "- [Fulfillment](./fulfillment/README.md)\n\n## Diagram\n\n```mermaid\n"
            "flowchart LR\n  a --> b\n```\n",
        )
        self.write(
            ".compass/shop/checkout/README.md",
            BLOCK.format(
                name="checkout",
                wires="- → [`fulfillment`](../fulfillment/README.md) — hands over paid orders\n",
                uses="### [`fulfillment`](../fulfillment/README.md)\n\n#### Why\n\nSomeone must ship.\n",
            ),
        )
        self.write(
            ".compass/shop/fulfillment/README.md",
            BLOCK.format(
                name="fulfillment",
                wires="- ← [`checkout`](../checkout/README.md) — paid orders arrive\n",
                uses="",
            ),
        )
        self.write(".compass/shop/checkout/entry/README.md", COMPONENT)
        self.write(".compass/shop/VIEWPORTS.md", VIEWPORTS.format(kind="lifecycle"))

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def write(self, relative_path: str, value: str) -> None:
        path = self.host / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(value).lstrip("\n"), encoding="utf-8")

    def run_check(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "chart_check.py"],
            cwd=self.host,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_template_chart_is_clean(self) -> None:
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("chart: clean", result.stdout)
        self.assertIn("1 addresses", result.stdout)

    def test_missing_block_heading_fails_and_routes_to_classification(self) -> None:
        block = self.host / ".compass/shop/checkout/README.md"
        block.write_text(
            block.read_text(encoding="utf-8").replace("## Boundary\n\nDoes not do the other thing.\n", ""),
            encoding="utf-8",
        )
        result = self.run_check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("checkout/README.md: missing ## Boundary", result.stdout)
        self.assertIn("Classify each failure before repairing it", result.stdout)

    def test_outbound_wire_without_a_uses_entry_fails(self) -> None:
        block = self.host / ".compass/shop/checkout/README.md"
        block.write_text(
            block.read_text(encoding="utf-8").replace(
                "### [`fulfillment`](../fulfillment/README.md)\n\n#### Why\n\nSomeone must ship.\n", ""
            ),
            encoding="utf-8",
        )
        result = self.run_check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("→ fulfillment has no ### entry under ## Uses", result.stdout)

    def test_missing_component_table_fails(self) -> None:
        block = self.host / ".compass/shop/fulfillment/README.md"
        block.write_text(
            re.sub(r"^\|.*\|\n", "", block.read_text(encoding="utf-8"), flags=re.M),
            encoding="utf-8",
        )
        result = self.run_check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("fulfillment/README.md: no component table", result.stdout)

    def test_component_without_a_stereotype_heading_fails(self) -> None:
        component = self.host / ".compass/shop/checkout/entry/README.md"
        component.write_text(
            component.read_text(encoding="utf-8").replace("## Stereotype\n\n«handler»\n\n", "«handler»\n\n"),
            encoding="utf-8",
        )
        result = self.run_check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("entry/README.md: missing ## Stereotype", result.stdout)

    def test_viewport_type_as_a_prose_line_fails(self) -> None:
        viewports = self.host / ".compass/shop/VIEWPORTS.md"
        viewports.write_text(
            viewports.read_text(encoding="utf-8").replace("### Type\n\nlifecycle\n", "Type: lifecycle\n"),
            encoding="utf-8",
        )
        result = self.run_check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing ### Type", result.stdout)
        self.assertNotIn("missing ### Question", result.stdout)

    def test_viewport_with_an_unknown_type_fails(self) -> None:
        self.write(".compass/shop/VIEWPORTS.md", VIEWPORTS.format(kind="sequence"))
        result = self.run_check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("type 'sequence' is not runtime, domain, boundary, or lifecycle", result.stdout)

    def test_viewport_with_an_empty_type_fails(self) -> None:
        self.write(".compass/shop/VIEWPORTS.md", VIEWPORTS.format(kind=""))
        result = self.run_check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("type '' is not runtime, domain, boundary, or lifecycle", result.stdout)


if __name__ == "__main__":
    unittest.main()
