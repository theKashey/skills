from __future__ import annotations

import html
import importlib.util
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "render.py"
SENTINEL = "zqxsentinel"

FLOW = """flowchart TB
  classDef ghost fill:#fff,stroke:#16a34a
  subgraph core["core"]
    B1["B1 store «Upgrade»"]:::ghost
    B2["B2 queue «Ghost»"]
  end
  B1 -->|"+ writes"| B2
"""

STATE = """stateDiagram-v2
  [*] --> pending
  pending --> approved: + approve
  approved --> [*]
"""

SEQUENCE = """sequenceDiagram
  participant A as Client
  participant B as Server
  A->>B: + request
  B-->>A: reply
"""

# Lines a valid diagram may hold, each carrying the sentinel somewhere the
# reader must see it, including the last word of the line.
INSERTS = {
    FLOW: [
        f"  B2 --> B3[{SENTINEL}]",
        f"  B1 -- {SENTINEL} --> B2",
        f"  note right of B1 : {SENTINEL}",
        f'  click B1 "{SENTINEL}"',
        f"  B1 & B2 --> {SENTINEL}X",
        f"  linkStyle 0 stroke:{SENTINEL}",
        f"  B1@{{ label: \"{SENTINEL}\" }}",
    ],
    STATE: [
        f"  note right of pending: owner {SENTINEL}",
        f"  note left of approved\n    first line\n    {SENTINEL}\n  end note",
        f"  pending: {SENTINEL}",
        f"  pending --> {SENTINEL}",
        f'  state "{SENTINEL} wait" as waiting',
        f"  state fork_x <<fork>>\n  pending --> fork_x: {SENTINEL}",
        f"  pending --> approved: {SENTINEL} and more",
    ],
    SEQUENCE: [
        f"  Note over A,B: {SENTINEL}",
        f"  A->>B: {SENTINEL}",
        f"  loop {SENTINEL}\n  A->>B: again\n  end",
        f"  alt ok {SENTINEL}\n  A->>B: yes\n  else no\n  A->>B: no\n  end",
        f"  rect rgb(1,2,3)\n  A->>B: {SENTINEL}\n  end",
        f"  A-)B: {SENTINEL}",
        f"  activate A\n  A->>B: x\n  deactivate A {SENTINEL}",
    ],
}


spec = importlib.util.spec_from_file_location("render", SCRIPT)
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


def render(diagrams: list[str]) -> str:
    md = "# Test\n\n" + "\n".join(f"```mermaid\n{d}```\n" for d in diagrams)
    with tempfile.TemporaryDirectory() as tmp:
        source = Path(tmp) / "t.md"
        source.write_text(md, encoding="utf-8")
        result = subprocess.run([sys.executable, str(SCRIPT), str(source)],
                                capture_output=True, text=True)
        assert result.returncode in (0, 1), result.stderr
        return source.with_suffix(".html").read_text(encoding="utf-8")


def visible(page: str) -> str:
    """Text a reader sees: drawn labels and source fallbacks, not hover titles."""
    page = re.sub(r"<style>.*?</style>|<title>.*?</title>", " ", page, flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", " ", page))


class RenderTest(unittest.TestCase):
    def test_note_is_drawn_with_its_text(self):
        page = render([STATE + "  note right of pending: owner only\n"])
        self.assertIn('<figure class="d">', page)
        self.assertNotIn("Left as Mermaid source", page)
        self.assertIn("Note on pending: owner only", visible(page))

    def test_unterminated_block_note_keeps_the_rest(self):
        page = render([STATE + "  note left of pending\n    one\n  pending --> lost_state\n"])
        self.assertIn("Left as Mermaid source", page)
        self.assertIn("lost_state", visible(page))

    def test_outer_group_name_survives_nesting(self):
        page = render([FLOW.replace('subgraph core["core"]', f'subgraph outer["{SENTINEL}"]\n  subgraph core["core"]')
                       .replace("  end\n", "  end\n  end\n")])
        self.assertIn('<figure class="d">', page)
        self.assertIn(f"{SENTINEL} › core", visible(page))

    def test_autonumber_keeps_numbers(self):
        page = render([SEQUENCE.replace("\n", "\n  autonumber\n", 1)])
        self.assertIn("1. + request", visible(page))

    def test_corpus_draws_without_fallback(self):
        page = render([FLOW, STATE, SEQUENCE])
        self.assertEqual(page.count('<figure class="d">'), 3)

    def test_no_inserted_line_disappears(self):
        for base, lines in INSERTS.items():
            for line in lines:
                with self.subTest(line=line):
                    page = render([base + line + "\n"])
                    self.assertIn(SENTINEL, visible(page))

    def test_a_line_the_drawing_drops_sends_the_view_to_source(self):
        # Stand in for any parser that accepts a line and then draws nothing
        # for it: draw the diagram without the inserted lines.
        graph, sequence = renderer.draw_graph, renderer.draw_sequence
        try:
            for base, lines in INSERTS.items():
                base_lines = base.splitlines()
                renderer.draw_graph = lambda code, hover: graph(base_lines, hover)
                renderer.draw_sequence = lambda body: sequence(base_lines[1:])
                for line in lines:
                    with self.subTest(line=line):
                        out = renderer.diagram((base + line).splitlines(), {})
                        self.assertIn(SENTINEL, visible(out))
                        self.assertIn("Left as Mermaid source", out)
        finally:
            renderer.draw_graph, renderer.draw_sequence = graph, sequence


if __name__ == "__main__":
    unittest.main()
