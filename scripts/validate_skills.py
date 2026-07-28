#!/usr/bin/env python3
"""Enforce repository-wide skill isolation with the bundled package validator."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPOSITORY_ROOT / "skills"
VALIDATOR = SKILLS_ROOT / "skill-guidance" / "scripts" / "validate_skill.py"
ROOT_LICENSE = REPOSITORY_ROOT / "LICENSE"


def run(command: list[str], cwd: Path = REPOSITORY_ROOT) -> bool:
    return subprocess.run(command, cwd=cwd, check=False).returncode == 0


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

    for package in packages:
        with tempfile.TemporaryDirectory(prefix=f"{package.name}-standalone-") as temp:
            copied_root = Path(temp)
            copied = copied_root / package.name
            shutil.copytree(package, copied)
            if not run(
                [sys.executable, str(VALIDATOR), str(copied)],
                cwd=copied_root,
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
                ):
                    return 1

    print(
        f"PASS {len(packages)} licensed, structurally isolated skill packages "
        "and one-package copy checks"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
