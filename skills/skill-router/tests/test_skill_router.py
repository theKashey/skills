from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "skill_router.py"

spec = importlib.util.spec_from_file_location("skill_router", SCRIPT)
router = importlib.util.module_from_spec(spec)
spec.loader.exec_module(router)

USE = "a CI test passes on rerun without code changes"
DONT = ["for a test that fails deterministically", "for quarantining tests in bulk"]
TRIAGE = "Rerun the failing test alone with the same seed."

HEADINGS = f"""
### Use when
- {USE}

### Do not use
- {DONT[0]}
- {DONT[1]}

## Triage
{TRIAGE}
"""

LABELS = f"""
## Boundary

Use when:
- {USE}

Do not use:
- {DONT[0]}
- {DONT[1]}

## Triage
{TRIAGE}
"""


def sections(body: str) -> dict[str, list[str]]:
    use_when, dont_use, headings, prose = router.body_sections(body)
    return {"use": use_when, "dont": dont_use, "headings": headings, "prose": prose}


class BoundaryListsTest(unittest.TestCase):
    def assert_boundary(self, body: str) -> dict[str, list[str]]:
        got = sections(body)
        self.assertEqual(got["use"], [USE])
        self.assertEqual(got["dont"], DONT)
        for line in DONT:
            self.assertNotIn(line, got["prose"])
        self.assertIn(TRIAGE, got["prose"])
        return got

    def test_headings_open_use_and_dont_lists(self):
        got = self.assert_boundary(HEADINGS)
        self.assertEqual(got["headings"], ["Use when", "Do not use", "Triage"])

    def test_label_lines_parse_like_headings(self):
        got = self.assert_boundary(LABELS)
        self.assertNotIn("Do not use:", got["dont"])
        self.assertEqual(got["headings"], ["Boundary", "Triage"])

    def test_bold_labels(self):
        for use, dont in (("**Use when:**", "**Do not use:**"), ("**Use when**:", "**Do not use**:"), ("*Use when:*", "_Don't use:_")):
            with self.subTest(use=use, dont=dont):
                self.assert_boundary(LABELS.replace("Use when:", use).replace("Do not use:", dont))

    def test_next_heading_ends_label_list(self):
        got = sections(LABELS + "- Retry with logging turned up to debug.\n")
        self.assertEqual(got["dont"], DONT)
        self.assertNotIn("Retry with logging turned up to debug.", " ".join(got["use"]))
        self.assertIn("Retry with logging turned up to debug.", got["prose"])

    def test_label_covers_only_its_list(self):
        step = "Then rerun the suite with the cache cleared and compare."
        got = sections(f"## Triage\n\nDo not use:\n\n- {DONT[0]}\n  across every platform\n- {DONT[1]}\n{step}\n")
        self.assertEqual(got["dont"], [f"{DONT[0]} across every platform", DONT[1]])
        self.assertIn(step, got["prose"])

    def test_label_list_returns_to_heading_mode(self):
        got = sections(f"## When to use\n\nDo not use:\n- {DONT[0]}\n\n{USE}\n")
        self.assertEqual(got["dont"], [DONT[0]])
        self.assertEqual(got["use"], [USE])

    def test_label_inside_procedure_keeps_later_lists_out(self):
        later = "say the column is optional and describe what it holds"
        got = sections(f"## Rules\n\nNever use:\n- {DONT[0]}\n\nUse instead:\n- {later}\n")
        self.assertEqual(got["dont"], [DONT[0]])
        self.assertIn(later, got["prose"])

    def test_next_label_switches_list(self):
        got = sections(f"## Boundary\n\nDo not use:\n- {DONT[0]}\nUse when:\n- {USE}\n")
        self.assertEqual(got["dont"], [DONT[0]])
        self.assertEqual(got["use"], [USE])

    def test_fenced_label_switches_nothing(self):
        got = sections(f"## Triage\n\n```text\nDo not use:\n```\n- {DONT[0]}\n")
        self.assertEqual(got["dont"], [])
        self.assertIn(DONT[0], got["prose"])

    def test_line_needs_whole_label_and_colon(self):
        for line in ("  trigger.", "Use when the tests fail: rerun them alone.", "Avoid:", "Use when"):
            with self.subTest(line=line):
                got = sections(f"## Triage\n\n{line}\n- {DONT[0]}\n")
                self.assertEqual(got["use"], [])
                self.assertEqual(got["dont"], [])
                self.assertIn(DONT[0], got["prose"])


class DontLineTest(unittest.TestCase):
    def test_line_initial_exclusions_are_dont_lines(self):
        for line in (f"- Do not use {DONT[1]}", f"Do not use: {DONT[1]}"):
            with self.subTest(line=line):
                got = sections(f"## Triage\n\n{line}\n")
                self.assertEqual(len(got["dont"]), 1)
                self.assertEqual(got["prose"], [])

    def test_mid_line_exclusion_stays_prose(self):
        line = "Run it alone; do not use it for bulk quarantine."
        got = sections(f"## Triage\n\n{line}\n")
        self.assertEqual(got["dont"], [])
        self.assertEqual(got["prose"], [line])


class RouteTest(unittest.TestCase):
    def test_label_exclusions_count_against_the_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            for name, body in (("headings", HEADINGS), ("labels", LABELS)):
                folder = Path(tmp) / name
                folder.mkdir()
                (folder / "SKILL.md").write_text(
                    f"---\nname: {name}\ndescription: Triages a flaky test to a cause before retry.\n---\n{body}",
                    encoding="utf-8",
                )
            out = subprocess.run(
                [sys.executable, str(SCRIPT), "route", "--skills", tmp, "--json", "quarantine flaky tests in bulk"],
                capture_output=True, text=True, check=True,
            ).stdout
        result = json.loads(out)
        scores = {s["name"]: s["score"] for s in result["picks"] + result["set_aside"]}
        self.assertAlmostEqual(scores["labels"], scores["headings"], places=1)


if __name__ == "__main__":
    unittest.main()
