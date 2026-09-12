#!/usr/bin/env python3
"""Enforce repository-wide skill isolation with the bundled package validator.

Also compares text a package deliberately shares with another package, and
inline phrases a package deliberately repeats across its own files. Each
skill installs alone, so shared runtime text cannot be factored out, and a
SKILL.md that must execute without loading its references has to carry some
definitions verbatim; only a comparison can catch one copy drifting into a
paraphrase of the other.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPOSITORY_ROOT / "skills"
VALIDATOR = SKILLS_ROOT / "skill-guidance" / "scripts" / "validate_skill.py"
ROOT_LICENSE = REPOSITORY_ROOT / "LICENSE"

# Fenced blocks that two packages must carry with identical text. Paths are
# relative to skills/; `canonical` names the owning package's copy. Copies are
# compared after dedenting, because a surrounding list indents the block
# without changing what it says.
SHARED_BLOCKS = (
    {
        "label": "isolated-reader question",
        "marker": "From the candidate alone, infer:",
        "canonical": "read-the-terrain/SKILL.md",
        "copies": ("retrospective/SKILL.md",),
    },
)

# Inline prose that one package deliberately carries word-for-word in several
# of its own files. Whitespace is normalized before matching because Markdown
# reflows lines. Each file listed must contain the phrase exactly once, and no
# other file in the package may contain it, so a copy cannot appear or vanish
# unnoticed. Only prose that is genuinely duplicated belongs here: where a file
# links to the owning reference instead of restating it, there is no second
# copy to compare and no entry to declare.
SHARED_PHRASES = (
    {
        "label": "context-docs assumed priors",
        "phrase": "stable general knowledge, named concepts, and ordinary tool "
        "or platform competence",
        "files": (
            "context-docs/references/casting.md",
            "context-docs/references/content-architecture.md",
        ),
    },
    {
        "label": "context-docs JSDoc overlay",
        "phrase": "JSDoc on an established public-contract symbol remains a "
        "public-contract surface",
        "files": (
            "context-docs/SKILL.md",
            "context-docs/references/quality-maintenance.md",
            "context-docs/references/review-documentation-at-wrap-up.md",
        ),
    },
)


def run(
    command: list[str], cwd: Path = REPOSITORY_ROOT, quiet: bool = False
) -> bool:
    """Run a validator command; `quiet` drops its stdout (errors stay on
    stderr) so a repeated run does not print the same report twice."""
    stdout = subprocess.DEVNULL if quiet else None
    completed = subprocess.run(command, cwd=cwd, check=False, stdout=stdout)
    return completed.returncode == 0


def fenced_blocks(text: str) -> list[list[str]]:
    """Return the raw lines of every fenced code block, fences excluded."""
    blocks: list[list[str]] = []
    fence: str | None = None
    current: list[str] = []
    for line in text.splitlines():
        marker = line.lstrip()[:3]
        if fence is None:
            if marker in {"```", "~~~"}:
                fence, current = marker, []
        elif line.lstrip().startswith(fence):
            blocks.append(current)
            fence = None
        else:
            current.append(line)
    return blocks


def shared_block(text: str, marker: str) -> str | None:
    """Return the fenced block opening with `marker`, dedented so surrounding
    list indentation cannot hide a paraphrase."""
    for block in fenced_blocks(text):
        if block and block[0].strip() == marker:
            body = "\n".join(line.rstrip() for line in block)
            return textwrap.dedent(body).strip("\n")
    return None


def shared_block_errors(packages: list[Path]) -> list[str]:
    errors: list[str] = []
    for spec in SHARED_BLOCKS:
        label, marker = spec["label"], spec["marker"]
        declared = {spec["canonical"], *spec["copies"]}
        found: dict[str, str] = {}
        for package in packages:
            for path in sorted(package.rglob("*.md")):
                relative = path.relative_to(SKILLS_ROOT).as_posix()
                try:
                    text = path.read_text(encoding="utf-8")
                except (OSError, UnicodeDecodeError):
                    continue
                block = shared_block(text, marker)
                if block is not None:
                    found[relative] = block
                elif any(line.strip() == marker for line in text.splitlines()):
                    errors.append(
                        f"shared block {label!r}: copy outside a fenced block "
                        f"in {relative}"
                    )
        for missing in sorted(declared - set(found)):
            errors.append(f"shared block {label!r}: missing from {missing}")
        for extra in sorted(set(found) - declared):
            errors.append(f"shared block {label!r}: undeclared copy in {extra}")
        canonical = found.get(spec["canonical"])
        if canonical is None:
            continue
        for copy in sorted((set(found) & declared) - {spec["canonical"]}):
            if found[copy] != canonical:
                errors.append(
                    f"shared block {label!r}: {copy} diverges from "
                    f"canonical {spec['canonical']}"
                )
    return errors


def shared_phrase_errors(packages: list[Path]) -> list[str]:
    errors: list[str] = []
    for spec in SHARED_PHRASES:
        label, phrase = spec["label"], " ".join(spec["phrase"].split())
        package_name = spec["files"][0].split("/", 1)[0]
        declared = set(spec["files"])
        counts: dict[str, int] = {}
        for package in packages:
            if package.name != package_name:
                continue
            for path in sorted(package.rglob("*.md")):
                relative = path.relative_to(SKILLS_ROOT).as_posix()
                try:
                    text = " ".join(path.read_text(encoding="utf-8").split())
                except (OSError, UnicodeDecodeError):
                    continue
                counts[relative] = text.count(phrase)
        for relative in sorted(declared):
            found = counts.get(relative, 0)
            if found != 1:
                errors.append(
                    f"shared phrase {label!r}: expected exactly one copy in "
                    f"{relative}, found {found}"
                )
        for relative, found in sorted(counts.items()):
            if found and relative not in declared:
                errors.append(
                    f"shared phrase {label!r}: undeclared copy in {relative}"
                )
    return errors


def main() -> int:
    packages = [
        path
        for path in sorted(SKILLS_ROOT.iterdir())
        if path.is_dir() and not path.name.startswith(".")
    ]
    if not packages:
        print("ERROR no skill packages found", file=sys.stderr)
        return 1
    if not VALIDATOR.is_file():
        print(f"ERROR missing isolation validator: {VALIDATOR}", file=sys.stderr)
        return 1
    if not ROOT_LICENSE.is_file():
        print(f"ERROR missing repository license: {ROOT_LICENSE}", file=sys.stderr)
        return 1

    expected_license = ROOT_LICENSE.read_bytes()
    if not run([sys.executable, str(VALIDATOR), "--self-test"]):
        return 1

    print("phase: in-place validation", flush=True)
    for package in packages:
        package_license = package / "LICENSE"
        if not package_license.is_file():
            print(
                f"ERROR {package.name}: missing standalone LICENSE",
                file=sys.stderr,
            )
            return 1
        if package_license.read_bytes() != expected_license:
            print(
                f"ERROR {package.name}: LICENSE differs from repository LICENSE",
                file=sys.stderr,
            )
            return 1
        if not run(
            [
                sys.executable,
                str(VALIDATOR),
                str(package),
            ]
        ):
            return 1

    print("phase: shared-block identity", flush=True)
    block_errors = shared_block_errors(packages) + shared_phrase_errors(packages)
    if block_errors:
        for error in block_errors:
            print(f"ERROR {error}", file=sys.stderr)
        return 1

    print("phase: standalone-copy validation", flush=True)
    for package in packages:
        with tempfile.TemporaryDirectory(prefix=f"{package.name}-standalone-") as temp:
            copied_root = Path(temp)
            copied = copied_root / package.name
            shutil.copytree(package, copied)
            if not run(
                [sys.executable, str(VALIDATOR), str(copied)],
                cwd=copied_root,
                quiet=True,
            ):
                return 1

            if package.name == "skill-guidance":
                copied_validator = copied / "scripts" / "validate_skill.py"
                if not run(
                    [
                        sys.executable,
                        str(copied_validator),
                        "--self-test",
                        str(copied),
                    ],
                    cwd=copied,
                    quiet=True,
                ):
                    return 1

    blocks = f"{len(SHARED_BLOCKS)} shared block"
    if len(SHARED_BLOCKS) != 1:
        blocks += "s"
    phrases = f"{len(SHARED_PHRASES)} shared phrase"
    if len(SHARED_PHRASES) != 1:
        phrases += "s"
    print(
        f"PASS {len(packages)} licensed, structurally isolated skill packages, "
        f"{blocks} compared across packages, {phrases} compared within a "
        "package, and one-package copy checks"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
