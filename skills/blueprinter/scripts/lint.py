#!/usr/bin/env python3
"""Check a blueprint's structure against the host tree.

Usage:
  lint.py <blueprint>   run from the host repository's root

Reports one line per problem:
  cite <path:line> <why>   a citation outside the evidence block, or past the
                           end of its file
  id <ID>                  a block ID on more than one card
  mark <ID> <mark>         a mark that is not one of the seven
  location <ID> <path>     an Existing, Upgrade, or Deconstruct file that does
                           not exist
  ghost <ID>               a Ghost or Acquire that names no capability from
                           the discovery table
  candidate <ID> <C>       that capability's discovery found something to use,
                           extend, or change, and no Assumptions line names it
  verdict <ID> <verdict>   a Checks row whose verdict is not yes, no, or
                           misframed
  landed <ID>              a landed block whose Checks rows are missing or not
                           all yes

Exit 0 when nothing is reported, 1 when anything is, 2 when the blueprint
cannot be read or has no block cards.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

MARKS = {"existing", "upgrade", "extract", "ghost", "acquire",
         "deconstruct", "document"}
FENCE = re.compile(r"^```(\w*)\s*\n(.*?)^```", re.M | re.S)
CITE = re.compile(r"(?<![\w:/.-])([\w.-]*[\w-][/.][\w./-]*\w):(\d+)\b")
VERDICTS = {"yes", "no", "misframed"}
CAPABILITY = re.compile(r"\bC\d+\b")
FILE_LIKE = re.compile(r"^[\w./-]+/[\w.-]+\.\w+$|^[\w.-]+\.\w+$")


def tables(text: str) -> list[tuple[list[str], list[list[str]]]]:
    found, rows = [], []
    for line in text.splitlines() + [""]:
        if line.lstrip().startswith("|"):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
            continue
        if len(rows) >= 2:
            found.append(([c.lower() for c in rows[0]], rows[2:]))
        rows = []
    return found


def column(header: list[str], *names: str) -> int | None:
    for i, cell in enumerate(header):
        if any(cell == n or cell.startswith(n + " ") for n in names):
            return i
    return None


def section(text: str, title: str) -> str:
    match = re.search(rf"^\W*{title}\b.*?(?=^#|^\*\*[A-Z]|\Z)", text,
                      re.M | re.S | re.I)
    return match.group(0) if match else ""


def lint(text: str) -> tuple[list[str], bool]:
    problems = []
    evidence = {}
    prose = text
    for kind, body in FENCE.findall(text):
        if kind == "evidence":
            for line in body.splitlines():
                fp, _, p = line.strip().partition(" ")
                if p:
                    evidence[p] = fp
        prose = prose.replace(body, "")

    for path, line in sorted(set(CITE.findall(prose))):
        if path not in evidence:
            problems.append(f"cite {path}:{line} not in the evidence block")
            continue
        try:
            length = len(Path(path).read_bytes().splitlines())
        except OSError:
            problems.append(f"cite {path}:{line} file does not exist")
            continue
        if int(line) > length:
            problems.append(f"cite {path}:{line} past the end ({length})")

    found = {}
    checks: dict[str, list[str]] = {}
    cards = None
    for header, rows in tables(text):
        if column(header, "capability") is not None and \
                column(header, "result") is not None:
            ic, ir = column(header, "id"), column(header, "result")
            for row in rows:
                if ic is not None and ic < len(row) and ir < len(row):
                    found[row[ic].strip("` ")] = row[ir].strip("*` ").lower()
        elif column(header, "id") is not None and \
                column(header, "part") is not None and \
                column(header, "verdict") is not None:
            ic, iv = column(header, "id"), column(header, "verdict")
            for row in rows:
                if max(ic, iv) < len(row):
                    verdict = row[iv].strip("*` ").lower()
                    bid = row[ic].strip("` ")
                    if verdict not in VERDICTS:
                        problems.append(f"verdict {bid} {verdict or '(none)'}")
                    checks.setdefault(bid, []).append(verdict)
        elif column(header, "id") is not None and \
                column(header, "mark") is not None and cards is None:
            cards = (header, rows)
    if cards is None:
        return problems, False

    assumptions = section(text, "Assumptions")
    header, rows = cards
    ii, im, il = column(header, "id"), column(header, "mark"), \
        column(header, "location")
    ist = column(header, "status")
    seen = set()
    for row in rows:
        if ii >= len(row):
            continue
        bid = row[ii].strip("` ")
        mark = row[im].strip("*` «»?").lower() if im < len(row) else ""
        if bid in seen:
            problems.append(f"id {bid}")
        seen.add(bid)
        status = row[ist].lower() if ist is not None and ist < len(row) else ""
        if status.startswith("dropped"):
            continue  # a retired ID keeps its row and nothing else
        landed = status.strip("*` ").startswith("landed")
        if landed and (not checks.get(bid) or
                       any(v != "yes" for v in checks[bid])):
            problems.append(f"landed {bid}")
        gone = mark == "deconstruct" and landed
        if mark not in MARKS:
            problems.append(f"mark {bid} {mark or '(none)'}")
        if mark in {"existing", "upgrade", "deconstruct"} and not gone \
                and il is not None \
                and il < len(row) and "?" not in row[il]:
            for token in re.findall(r"`([^`]+)`", row[il]) or [row[il]]:
                path = re.sub(r":\d+(-\d+)?$", "", token.strip())
                if FILE_LIKE.match(path) and not Path(path).exists():
                    problems.append(f"location {bid} {path}")
        if mark in {"ghost", "acquire"}:
            named = [c for c in CAPABILITY.findall(" ".join(row)) if c in found]
            if not named:
                problems.append(f"ghost {bid}")
            for c in named:
                if not found[c].startswith("none") and \
                        not re.search(rf"\b{c}\b", assumptions):
                    problems.append(f"candidate {bid} {c}")
    return problems, True


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print(__doc__.split("\n\n")[1], file=sys.stderr)
        return 2
    try:
        text = Path(argv[0]).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        print(f"lint.py: {error}", file=sys.stderr)
        return 2
    problems, has_cards = lint(text)
    for p in problems:
        print(p)
    if not has_cards:
        print(f"lint.py: {argv[0]} has no block cards table", file=sys.stderr)
        return 2
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
