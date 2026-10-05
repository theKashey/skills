from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "lint.py"
EVIDENCE = Path(__file__).parents[1] / "scripts" / "evidence.py"


def run(cwd: Path, script: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(script), *args], cwd=cwd,
                          capture_output=True, text=True)


def blueprint(evidence: str, discovery: str, cards: str,
              assumptions: str = "") -> str:
    return f"""# change

```evidence
{evidence}```

**Discovery**

| ID | Capability | Result | Evidence |
| --- | --- | --- | --- |
{discovery}

**Block cards**

| ID | Mark | Status | Location | Amendment |
| --- | --- | --- | --- | --- |
{cards}

**Assumptions** — {assumptions}
"""


class LintTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        (self.repo / "src").mkdir()
        (self.repo / "src" / "a.py").write_text("one\ntwo\n")
        self.evidence = run(self.repo, EVIDENCE, "record", "src/a.py").stdout

    def tearDown(self):
        self.tmp.cleanup()

    def lint(self, text: str) -> subprocess.CompletedProcess:
        (self.repo / "bp.md").write_text(text)
        return run(self.repo, SCRIPT, "bp.md")

    def test_clean_blueprint_passes(self):
        result = self.lint(blueprint(
            self.evidence,
            "| C1 | send it | none | searched `src/` (`src/a.py:2`) |",
            "| B1 | Upgrade | planned | `src/a.py` | change it |\n"
            "| B2 | Ghost | planned | src/new.py | build for C1 |"))
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.returncode, 0)

    def test_ghost_without_capability_is_reported(self):
        result = self.lint(blueprint(
            self.evidence, "| C1 | send it | none | - |",
            "| B1 | Ghost | planned | src/new.py | build it |"))
        self.assertIn("ghost B1", result.stdout)
        self.assertEqual(result.returncode, 1)

    def test_ghost_over_found_candidate_needs_assumption(self):
        rows = ("| C1 | send it | extend | `src/a.py:1` |",
                "| B1 | Ghost | planned | src/new.py | build for C1 |")
        self.assertIn("candidate B1 C1", self.lint(blueprint(
            self.evidence, *rows)).stdout)
        self.assertEqual(self.lint(blueprint(
            self.evidence, *rows,
            assumptions="B1: C1's candidate lacks retries")).returncode, 0)

    def test_landed_needs_every_check_yes(self):
        cards = ("| C1 | send it | none | - |",
                 "| B1 | Upgrade | landed | `src/a.py` | change it |")
        checks = ("\n| ID | Part | Verdict | Evidence |"
                  "\n| --- | --- | --- | --- |"
                  "\n| B1 | test | {} | `make test` passed |\n")
        self.assertIn("landed B1", self.lint(blueprint(
            self.evidence, *cards)).stdout)
        self.assertEqual(self.lint(blueprint(
            self.evidence, *cards) + checks.format("yes")).stdout, "")
        result = self.lint(blueprint(self.evidence, *cards)
                           + checks.format("misframed"))
        self.assertIn("landed B1", result.stdout)
        result = self.lint(blueprint(self.evidence, *cards)
                           + checks.format("met"))
        self.assertIn("verdict B1 met", result.stdout)

    def test_question_verdicts_are_not_checks(self):
        result = self.lint(blueprint(
            self.evidence, "| C1 | send it | none | - |",
            "| B1 | Upgrade | planned | `src/a.py` | change it |")
            + "\n| ID | Question | Answer | Verdict |"
            "\n| --- | --- | --- | --- |"
            "\n| Q1 | who reads it | B1 | yes, but owner unknown |"
            "\n| B1 | does B1 fit | it does | no |\n")
        self.assertEqual(result.stdout, "")

    def test_formatted_none_is_none(self):
        result = self.lint(blueprint(
            self.evidence, "| C1 | send it | **none** | - |",
            "| B1 | Ghost | planned | src/new.py | build for C1 |"))
        self.assertEqual(result.stdout, "")

    def test_citation_checks(self):
        result = self.lint(blueprint(
            self.evidence, "| C1 | x | use | `src/a.py:9`, `lib/b.py:1` |",
            "| B1 | Existing | planned | `src/gone.py` | - |\n"
            "| B1 | Rebuild | planned | ? | - |"))
        for line in ("cite src/a.py:9 past the end (2)",
                     "cite lib/b.py:1 not in the evidence block",
                     "location B1 src/gone.py", "id B1", "mark B1 rebuild"):
            self.assertIn(line, result.stdout)

    def test_urls_and_guesses_are_not_checked(self):
        result = self.lint(blueprint(
            self.evidence,
            "| C1 | x | none | https://example.com:443/docs |",
            "| B1 | Upgrade | planned | ? src/maybe.py | - |\n"
            "| B2 | Acquire | planned | vendor package | for C1 |"))
        self.assertEqual(result.stdout, "")

    def test_retired_and_removed_blocks_are_not_located(self):
        result = self.lint(blueprint(
            self.evidence, "| C1 | x | none | - |",
            "| B1 | — | dropped | — | retired |\n"
            "| B2 | Deconstruct | landed `abc` | `src/old.py` | deleted |")
            + "\n| ID | Part | Verdict | Evidence |\n| --- | --- | --- | --- |"
            "\n| B2 | file | yes | `src/old.py` absent |\n")
        self.assertEqual(result.stdout, "")

    def test_missing_cards_exit_2(self):
        self.assertEqual(self.lint("# nothing\n").returncode, 2)


if __name__ == "__main__":
    unittest.main()
