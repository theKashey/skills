from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "evidence.py"


def run(cwd: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=cwd,
                          capture_output=True, text=True)


def git(cwd: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True,
                          capture_output=True, text=True).stdout


class EvidenceTest(unittest.TestCase):
    def test_second_edit_to_a_dirty_file_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            git(repo, "init", "-q")
            (repo / "a.py").write_text("one\n")
            (repo / "b.py").write_text("steady\n")
            git(repo, "add", ".")
            git(repo, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "c")
            (repo / "a.py").write_text("two\n")  # dirty before the evidence is read

            recorded = run(repo, "record", "a.py", "b.py")
            self.assertEqual(recorded.returncode, 0)
            for line in recorded.stdout.splitlines():
                fp, _, p = line.partition(" ")
                self.assertEqual(fp, git(repo, "hash-object", p).strip())
            (repo / "bp.md").write_text(f"# x\n\n```evidence\n{recorded.stdout}```\n")
            self.assertEqual(run(repo, "check", "bp.md").returncode, 0)

            head, status = git(repo, "rev-parse", "HEAD"), git(repo, "status", "--porcelain", "a.py", "b.py")
            (repo / "a.py").write_text("three\n")  # edited again, still dirty
            self.assertEqual(git(repo, "rev-parse", "HEAD"), head)
            self.assertEqual(git(repo, "status", "--porcelain", "a.py", "b.py"), status)

            checked = run(repo, "check", "bp.md")
            self.assertEqual(checked.returncode, 1)
            self.assertEqual(checked.stdout.strip(), "changed a.py")

    def test_new_path_is_recorded_absent_until_created(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            recorded = run(repo, "record", "new.py")
            self.assertEqual((recorded.returncode, recorded.stdout), (0, "absent new.py\n"))
            (repo / "bp.md").write_text(f"```evidence\n{recorded.stdout}```\n")
            self.assertEqual(run(repo, "check", "bp.md").returncode, 0)
            (repo / "new.py").write_text("built\n")
            self.assertEqual(run(repo, "check", "bp.md").stdout.strip(), "created new.py")

    def test_missing_file_and_missing_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / "bp.md").write_text("```evidence\n0000 gone.py\n```\n")
            self.assertEqual(run(repo, "check", "bp.md").stdout.strip(), "missing gone.py")
            (repo / "bare.md").write_text("# no block\n")
            self.assertEqual(run(repo, "check", "bare.md").returncode, 2)


if __name__ == "__main__":
    unittest.main()
