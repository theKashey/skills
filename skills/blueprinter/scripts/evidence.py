#!/usr/bin/env python3
"""Fingerprint the files a blueprint read, and report which changed since.

Usage:
  evidence.py record <path>...   print one `<fingerprint> <path>` line per file,
                                 or `absent <path>` for a file not yet created
  evidence.py check <blueprint>  compare the blueprint's ```evidence block

Paths are relative to the current directory, the host repository's root. A
fingerprint is the file's Git blob hash, the value `git hash-object` prints,
computed from the bytes on disk. It changes whenever the content changes,
including a second edit to a file that is already uncommitted, which leaves
both the commit and the list of uncommitted paths as they were.

check prints `changed <path>`, `missing <path>`, or `created <path>` for each
file whose content differs from its recorded line. Exit 0 when every file
matches, 1 when any differs, 2 when the blueprint cannot be read or has no
evidence block.
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

BLOCK = re.compile(r"^```evidence\s*\n(.*?)^```", re.M | re.S)


def fingerprint(path: Path) -> str | None:
    try:
        data = path.read_bytes()
    except OSError:
        return None
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def record(paths: list[str]) -> int:
    for p in paths:  # a block placed at a new path starts absent
        print(f"{fingerprint(Path(p)) or 'absent'} {p}")
    return 0


def check(blueprint: str) -> int:
    try:
        match = BLOCK.search(Path(blueprint).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError) as error:
        print(f"evidence.py: {error}", file=sys.stderr)
        return 2
    if not match:
        print(f"evidence.py: {blueprint} has no ```evidence block", file=sys.stderr)
        return 2
    stale = 0
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        fp, _, p = line.strip().partition(" ")
        now = fingerprint(Path(p)) or "absent"
        if now != fp:
            print(f"{'missing' if now == 'absent' else 'created' if fp == 'absent' else 'changed'} {p}")
            stale += 1
    return 1 if stale else 0


def main(argv: list[str]) -> int:
    if len(argv) >= 2 and argv[0] == "record":
        return record(argv[1:])
    if len(argv) == 2 and argv[0] == "check":
        return check(argv[1])
    print(__doc__.split("\n\n")[1], file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
