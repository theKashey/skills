#!/usr/bin/env python3
"""Per-scope comment budget check with a baseline that only shrinks.

    python3 comment_budget.py [options] PATH...      (--help lists options)

Counts the content lines of every file overview, docblock, and block comment
under PATH and fails when one exceeds its budget. Content lines are what the
reader reads: delimiter, blank, pragma, and bare machine-read tag lines are
not counted. The budget is a placement trigger, not a quality score: the
remedy for an over-budget comment is to move the overflow to the surface that
owns it, never to delete the cause or pad another comment.

Exit status: 0 within budget, 1 violations or a stale baseline, 2 usage.
Standard library only; Python 3.8+.
"""


from __future__ import annotations

import argparse
import fnmatch
import io
import json
import os
import re
import sys
import tokenize

HELP_EPILOG = """\
surface kinds:
  overview  the first comment before the file's first non-import code line
            that is not a pragma, a shebang, or a license header within the
            first five lines; or a `//!` / `/*!` inner doc comment
  jsdoc     a `/** */`, `///`, or Python docstring attached to a declaration
  block     any other comment spanning two or more lines; a single-line
            comment has no budget beyond its one line, and consecutive
            standalone line comments form one block

budget precedence: --limit, then "limits" in the baseline, then the defaults
(--defaults prints them).

supported syntaxes: JavaScript/TypeScript, Rust, Java, Kotlin, Go, C-family,
Swift, Dart, PHP, Scala (C-like lexer) and Python (tokenize). Source files
in Ruby, shell, Elixir, Perl, Lua, Haskell, or OCaml are reported as a count
of unsupported files; Markdown, data, and every other file type are skipped
silently, so a documentation tree always passes.
"""

DEFAULT_LIMITS = {"overview": 15, "jsdoc": 10, "block": 5}
BASELINE_NAME = "comment-budget.json"

C_LIKE = {
    ".ts": "js", ".tsx": "js", ".js": "js", ".jsx": "js", ".mjs": "js",
    ".cjs": "js", ".mts": "js", ".cts": "js",
    ".rs": "rs", ".java": "java", ".kt": "kt", ".kts": "kt", ".go": "c",
    ".c": "c", ".h": "c", ".cc": "c", ".cpp": "c", ".hpp": "c", ".cs": "c",
    ".swift": "c", ".dart": "c", ".php": "c", ".scala": "c",
}
PYTHON = {".py", ".pyi"}
# Source languages without a lexer here: counted so a host notices the gap.
UNSUPPORTED_SOURCE = {".rb", ".sh", ".bash", ".zsh", ".ex", ".exs", ".pl", ".lua", ".hs", ".ml"}

EXCLUDE_SEGMENTS = {
    "node_modules", ".git", "dist", "build", "out", "target", "coverage",
    "vendor", "vendored", "third_party", "generated", "__generated__",
    "fixtures", "__fixtures__", "fixture", "__snapshots__", ".venv", "venv",
}
GENERATED_RE = re.compile(r"@generated|DO NOT EDIT|auto-?generated", re.I)
LICENSE_RE = re.compile(
    r"\b(copyright|licen[sc]e[ds]?|SPDX-License-Identifier|all rights reserved)\b",
    re.I,
)
# Markers consumed by tools rather than read by people. A one-line comment
# that starts with one is skipped entirely, so it can never be taken as the
# file overview; a longer run is counted like any other comment unless every
# line of it is a pragma. TODO/FIXME
# are here only for that reason: a one-line TODO has no budget anyway.
PRAGMA_RE = re.compile(
    r"^\s*(//[/!]?|/\*\*?|#)\s*("
    r"@vitest-environment|@jest-environment|eslint-|biome-ignore|"
    r"prettier-ignore|@ts-(nocheck|ignore|expect-error)|istanbul ignore|"
    r"c8 ignore|v8 ignore|<reference\b|@refresh|noinspection|@jsx|"
    r"@jsxImportSource|#region|#endregion|type:\s*ignore|noqa|pylint:|"
    r"@formatter:|mypy:|ruff:|@flow|SAFETY:|TODO\b|FIXME\b)",
    re.I,
)
# A tag with at most one token after it (`@internal`, `@deprecated`,
# `owner: a/b`) and any `@see` / `{@link}` route line are machine-read, not
# content lines.
BARE_TAG_RE = re.compile(r"^(@\w+|\w+:)(\s+\S+)?$|^(@see\b|\{@link\b)")
TAG_RE = re.compile(r"^@\w+")

IMPORT_START = {
    "js": re.compile(
        r"^\s*(import\b|export\s+(\*|\{[^}]*\}?|type\s+\{)[^=]*?(from\b|$)|"
        r"(const|let|var)\s+[\w{}\s,]+=\s*require\(|['\"]use (strict|client|server)['\"])"
    ),
    "rs": re.compile(r"^\s*(pub(\([^)]*\))?\s+)?(use\b|extern\s+crate\b|mod\s+\w+\s*;|#!\[)"),
    "java": re.compile(r"^\s*(package\b|import\b)"),
    "kt": re.compile(r"^\s*(package\b|import\b|@file:)"),
    "c": re.compile(r"^\s*(package\b|import\b|#include\b|#pragma\b|using\b|namespace\b)"),
    "py": re.compile(r"^\s*(import\b|from\s+\S+\s+import\b|__future__)"),
}

REGEX_PREV_CHARS = set("(,=:[!&|?{};+-*%<>~^")
REGEX_PREV_WORDS = {
    "return", "typeof", "case", "do", "else", "in", "of", "new", "delete",
    "void", "throw", "yield", "await", "instanceof",
}


class Lexed:
    def __init__(self) -> None:
        self.comments: list[dict] = []  # style, start, end, col, text
        self.code_lines: set[int] = set()


def _rust_char(src: str, i: int) -> bool:
    """True if the ' at i starts a Rust char literal rather than a lifetime."""
    if i + 1 < len(src) and src[i + 1] == "\\":
        return True
    return i + 2 < len(src) and src[i + 2] == "'"


def lex_c_like(src: str, lang: str) -> Lexed:
    out = Lexed()
    n = len(src)
    i = 0
    line = 1
    stack: list[list] = [["code", 0]]  # ('code', brace_depth) or ('tmpl',)
    prev = ""  # previous significant token for regex-literal detection
    js = lang == "js"
    rust = lang == "rs"

    while i < n:
        mode = stack[-1]
        c = src[i]
        if mode[0] == "tmpl":
            if c == "\\":
                i += 2
                continue
            if c == "`":
                stack.pop()
                out.code_lines.add(line)
                i += 1
                prev = "x"
                continue
            if c == "$" and i + 1 < n and src[i + 1] == "{":
                stack.append(["code", 0])
                i += 2
                prev = "{"
                continue
            if c == "\n":
                line += 1
            else:
                out.code_lines.add(line)
            i += 1
            continue
        if c == "\n":
            line += 1
            i += 1
            continue
        if c in " \t\r\f\v":
            i += 1
            continue
        nxt = src[i + 1] if i + 1 < n else ""
        if c == "/" and nxt == "/":
            j = src.find("\n", i)
            j = n if j == -1 else j
            text = src[i:j]
            col = i - (src.rfind("\n", 0, i) + 1)
            style = "line"
            if text.startswith("///") and not text.startswith("////"):
                style = "doc_line"
            elif text.startswith("//!"):
                style = "inner_doc"
            out.comments.append(dict(style=style, start=line, end=line, col=col, text=text))
            i = j
            continue
        if c == "/" and nxt == "*":
            start = line
            col = i - (src.rfind("\n", 0, i) + 1)
            depth = 1
            j = i + 2
            while j < n and depth:
                if src.startswith("*/", j):
                    depth -= 1
                    j += 2
                    continue
                if rust and src.startswith("/*", j):
                    depth += 1
                    j += 2
                    continue
                if src[j] == "\n":
                    line += 1
                j += 1
            text = src[i:j]
            style = "doc_block" if text.startswith("/**") and not text.startswith("/**/") else "block"
            if text.startswith("/*!"):
                style = "inner_doc"
            out.comments.append(dict(style=style, start=start, end=line, col=col, text=text))
            i = j
            continue
        out.code_lines.add(line)
        prev_ident = i > 0 and (src[i - 1].isalnum() or src[i - 1] == "_")
        m = re.match(r'(br|r|b)(#*)"', src[i:i + 40]) if (rust and c in "rb" and not prev_ident) else None
        if m:
            hashes = m.group(2)
            j = i + m.end()
            if m.group(1) in ("r", "br"):
                end = '"' + hashes
                k = src.find(end, j)
                k = n if k == -1 else k + len(end)
            else:
                k = j
                while k < n and src[k] != '"':
                    if src[k] == "\\":
                        k += 1
                    k += 1
                k += 1
            seg = src[i:k]
            cnt = seg.count("\n")
            for d in range(cnt + 1):
                out.code_lines.add(line + d)
            line += cnt
            i += len(seg)
            prev = "x"
            continue
        if c == '"' or (c == "'" and not rust) or (c == "'" and rust and _rust_char(src, i)):
            if c == '"' and lang in ("java", "kt") and src.startswith('"""', i):
                k = src.find('"""', i + 3)
                k = n if k == -1 else k + 3
            else:
                k = i + 1
                while k < n and src[k] != c:
                    if src[k] == "\\":
                        k += 1
                    elif src[k] == "\n" and not rust:
                        break  # unterminated; stop at end of line
                    k += 1
                k += 1
            seg = src[i:k]
            cnt = seg.count("\n")
            for d in range(cnt + 1):
                out.code_lines.add(line + d)
            line += cnt
            i = k
            prev = "x"
            continue
        if js and c == "`":
            stack.append(["tmpl"])
            i += 1
            continue
        if js and c == "/" and (prev == "" or prev in REGEX_PREV_CHARS or prev in REGEX_PREV_WORDS):
            k = i + 1
            in_class = False
            ok = False
            while k < n and src[k] != "\n":
                ch = src[k]
                if ch == "\\":
                    k += 2
                    continue
                if ch == "[":
                    in_class = True
                elif ch == "]":
                    in_class = False
                elif ch == "/" and not in_class:
                    ok = True
                    break
                k += 1
            if ok:
                k += 1
                while k < n and src[k].isalpha():
                    k += 1
                i = k
                prev = "x"
                continue
        if c == "{":
            mode[1] += 1
        elif c == "}":
            if mode[1] == 0 and len(stack) > 1:
                stack.pop()  # back into the template literal
                i += 1
                continue
            mode[1] -= 1
        if c.isalnum() or c in "_$":
            m = re.match(r"[\w$]+", src[i:i + 64])
            prev = m.group(0)
            i += len(prev)
            continue
        prev = c
        i += 1
    return out


def lex_python(src: str) -> Lexed:
    out = Lexed()
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return out
    prev_sig = None
    for idx, t in enumerate(toks):
        tt, s, (sl, sc), (el, _ec), _ln = t
        if tt == tokenize.COMMENT:
            out.comments.append(dict(style="line", start=sl, end=sl, col=sc, text=s))
            continue
        if tt in (tokenize.NL, tokenize.NEWLINE, tokenize.INDENT, tokenize.DEDENT,
                  tokenize.ENDMARKER, tokenize.ENCODING):
            if tt == tokenize.NEWLINE:
                prev_sig = ("NEWLINE", "")
            continue
        if tt == tokenize.STRING and s.lstrip("rRbBuUfF").startswith(('"""', "'''")):
            nxt = next((x for x in toks[idx + 1:] if x[0] not in (tokenize.NL, tokenize.COMMENT)), None)
            if (prev_sig is None or prev_sig[0] == "NEWLINE" or prev_sig[1] == ":") and (
                nxt is None or nxt[0] in (tokenize.NEWLINE, tokenize.ENDMARKER)
            ):
                out.comments.append(dict(style="docstring", start=sl, end=el, col=sc, text=s))
                prev_sig = ("DOC", "")
                continue
        for ln_no in range(sl, el + 1):
            out.code_lines.add(ln_no)
        prev_sig = (tt, s)
    return out


def group_comments(lex: Lexed, lines: list[str]) -> list[dict]:
    """Merge consecutive standalone same-style line comments into runs."""
    groups: list[dict] = []
    for c in sorted(lex.comments, key=lambda c: (c["start"], c["col"])):
        trailing = c["start"] in lex.code_lines and lines[c["start"] - 1][: c["col"]].strip() != ""
        shebang = c["start"] == 1 and c["text"].startswith("#!")
        pragma = shebang or (bool(PRAGMA_RE.match(c["text"].split("\n")[0])) and c["end"] - c["start"] < 2)
        c = dict(c, trailing=trailing, pragma=pragma)
        if (
            groups
            and not trailing
            and c["style"] in ("line", "doc_line", "inner_doc")
            and c["style"] == groups[-1]["style"]
            and not groups[-1]["trailing"]
            and groups[-1]["end"] == c["start"] - 1
            and groups[-1]["text"].startswith(("//", "#"))
        ):
            g = groups[-1]
            g["end"] = c["start"]
            g["text"] += "\n" + c["text"]
            g["pragma"] = g["pragma"] and pragma
            continue
        groups.append(c)
    return groups


def content_lines(text: str) -> list[str]:
    """Strip delimiters and return the stripped content of each line."""
    if text.startswith("/*"):
        body = text[2:-2] if text.endswith("*/") else text[2:]
        body = body.lstrip("*!")
        out = []
        for raw in body.split("\n"):
            s = raw.strip()
            if s.startswith("*"):
                s = s[1:].strip()
            out.append(s)
    elif text.lstrip("rRbBuUfF").startswith(('"""', "'''")):
        body = text.lstrip("rRbBuUfF")[3:-3]
        out = [raw.strip() for raw in body.split("\n")]
    else:
        out = [re.sub(r"^(//[/!]?|#)", "", raw.strip()).strip() for raw in text.split("\n")]
    while out and out[0] == "":
        out.pop(0)
    while out and out[-1] == "":
        out.pop()
    return out


def count_content(content: list[str]) -> int:
    """Lines a reader reads: non-blank, not a bare machine-read tag. Fenced
    examples count, because the reader scrolls them."""
    total = 0
    for s in content:
        if not s or BARE_TAG_RE.match(s):
            continue
        total += 1
    return total


def import_region_end(lines: list[str], code_lines: set[int], lang: str) -> int:
    """1-based line of the first code line past the leading import region."""
    rx = IMPORT_START[lang]
    in_stmt = False
    for ln in range(1, len(lines) + 1):
        if ln not in code_lines:
            continue
        t = lines[ln - 1]
        if in_stmt:
            if re.search(r"\bfrom\s*['\"]|;\s*$|^\s*\}\s*$|\)\s*;?\s*$", t) or (lang == "rs" and t.rstrip().endswith(";")):
                in_stmt = False
            continue
        if t.startswith("#!") and ln == 1:
            continue
        if rx.match(t):
            stripped = t.rstrip()
            done = (
                stripped.endswith(";")
                or re.search(r"\bfrom\s*['\"][^'\"]*['\"]", t)
                or re.match(r"^\s*import\s+['\"]", t)
                or re.match(r"^\s*['\"]use ", t)
                or (lang in ("java", "kt", "py", "c") and not stripped.endswith(("(", "{", ",", "\\")))
                or (lang == "rs" and stripped.startswith("#![") and stripped.endswith("]"))
                or (lang == "js" and re.search(r"require\(.*\)\s*;?$", stripped))
            )
            in_stmt = not done
            continue
        return ln
    return len(lines) + 1


def lang_of(path: str) -> str | None:
    ext = os.path.splitext(path)[1].lower()
    if ext in PYTHON:
        return "py"
    return C_LIKE.get(ext)


def surfaces(path: str, src: str) -> list[dict]:
    """Classify each comment group of one file as overview, jsdoc, block, or
    line and count its content lines."""
    lang = lang_of(path)
    if lang is None or GENERATED_RE.search(src[:2000]):
        return []
    lex = lex_python(src) if lang == "py" else lex_c_like(src, lang)
    lines = src.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    groups = group_comments(lex, lines)
    comment_lines: set[int] = set()
    for g in groups:
        comment_lines.update(range(g["start"], g["end"] + 1))
    first_real = import_region_end(lines, lex.code_lines, lang)
    maxln = len(lines)
    found: list[dict] = []
    overview_taken = False
    for g in groups:
        if g["pragma"]:
            continue
        text = g["text"]
        span = g["end"] - g["start"] + 1
        content = content_lines(text)
        # next code line, skipping blank and comment lines
        nxt = g["end"] + 1
        while nxt <= maxln and nxt not in lex.code_lines:
            nxt += 1
        nxt = nxt if nxt <= maxln else None
        attached = nxt == g["end"] + 1 and not g["trailing"]
        before_code = g["start"] < first_real and not g["trailing"]
        if before_code and not overview_taken and g["start"] <= 5 and LICENSE_RE.search(text):
            continue  # a license header is not the overview
        if g["style"] == "inner_doc" or (before_code and not overview_taken):
            kind = "overview"
            overview_taken = True
            anchor = "<file>"
        elif g["style"] in ("doc_block", "doc_line", "docstring") and (attached or g["style"] == "docstring"):
            kind = "jsdoc"
            anchor = " ".join(lines[nxt - 1].split())[:80] if nxt else "<end>"
        elif span > 1:
            kind = "block"
            anchor = " ".join(lines[nxt - 1].split())[:80] if nxt else "<end>"
        else:
            continue  # a single line has no budget beyond itself
        found.append(dict(
            path=path, kind=kind, line=g["start"], end=g["end"], span=span,
            lines=count_content(content), anchor=anchor,
        ))
    return found


def iter_files(roots: list[str], excludes: list[str]):
    for root in roots:
        root = os.path.normpath(root)
        if os.path.isfile(root):
            yield root, os.path.basename(root)
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = sorted(d for d in dirnames if d not in EXCLUDE_SEGMENTS and not d.startswith("."))
            for name in sorted(filenames):
                full = os.path.join(dirpath, name)
                rel = os.path.relpath(full, root).replace(os.sep, "/")
                if any(fnmatch.fnmatch(rel, pat) or fnmatch.fnmatch(name, pat) for pat in excludes):
                    continue
                yield full, rel


def scan(roots: list[str], excludes: list[str]):
    """Return (surfaces keyed by stable id, unsupported file count)."""
    keyed: dict[str, dict] = {}
    unsupported = 0
    for full, rel in iter_files(roots, excludes):
        if lang_of(rel) is None:
            if os.path.splitext(rel)[1] in UNSUPPORTED_SOURCE:
                unsupported += 1
            continue
        try:
            with open(full, encoding="utf-8") as fh:
                src = fh.read()
        except (OSError, UnicodeDecodeError):
            continue
        seen: dict[str, int] = {}
        for s in surfaces(rel, src):
            base = f"{s['path']}::{s['kind']}::{s['anchor']}"
            seen[base] = seen.get(base, 0) + 1
            key = base if seen[base] == 1 else f"{base}#{seen[base]}"
            s["key"] = key
            keyed[key] = s
    return keyed, unsupported


def load_baseline(path: str) -> dict:
    if not os.path.exists(path):
        return {"limits": {}, "surfaces": {}}
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    data.setdefault("limits", {})
    data.setdefault("surfaces", {})
    return data


def resolve_limits(cli: list[str], baseline: dict) -> dict:
    limits = dict(DEFAULT_LIMITS)
    for kind, value in baseline.get("limits", {}).items():
        if kind in limits:
            limits[kind] = int(value)
    for item in cli:
        kind, _, value = item.partition("=")
        if kind not in limits or not value.isdigit():
            raise SystemExit(f"usage: --limit expects overview|jsdoc|block=N, got {item!r}")
        limits[kind] = int(value)
    return limits


def over_budget(keyed: dict, limits: dict) -> dict:
    return {k: s for k, s in keyed.items() if s["lines"] > limits[s["kind"]]}


def check(keyed: dict, limits: dict, baseline: dict, baseline_path: str) -> tuple[list[str], list[str]]:
    """Return (violations, stale) messages."""
    over = over_budget(keyed, limits)
    accepted = baseline["surfaces"]
    violations = []
    for key, s in sorted(over.items(), key=lambda kv: (-kv[1]["lines"], kv[0])):
        entry = accepted.get(key)
        if entry is not None and (entry.get("reason") or int(entry.get("lines", 0)) >= s["lines"]):
            continue
        state = "grew" if entry is not None else "new"
        violations.append(
            f"{s['path']}:{s['line']} {s['kind']} {s['lines']}/{limits[s['kind']]} content lines ({state}): "
            "move the overflow to the surface that owns it and keep a one-line route, "
            f"or record a reason in {baseline_path}"
        )
    stale = []
    for key, entry in sorted(accepted.items()):
        if entry.get("reason"):
            continue
        current = over.get(key)
        if current is None:
            stale.append(f"{key}: no longer over budget; rewrite the baseline with --write-baseline")
        elif current["lines"] < int(entry.get("lines", 0)):
            stale.append(
                f"{key}: shrank to {current['lines']} (baseline {entry['lines']}); "
                "rewrite the baseline with --write-baseline"
            )
    return violations, stale


def write_baseline(keyed: dict, limits: dict, baseline: dict, path: str, accept: bool) -> list[str]:
    over = over_budget(keyed, limits)
    old = baseline["surfaces"]
    new: dict[str, dict] = {}
    refused: list[str] = []
    for key, s in sorted(over.items()):
        entry = old.get(key)
        if entry is None:
            if not accept:
                refused.append(f"new: {key} ({s['lines']})")
                continue
            new[key] = {"lines": s["lines"]}
        elif entry.get("reason"):
            new[key] = {"lines": s["lines"], "reason": entry["reason"]}
        elif s["lines"] > int(entry.get("lines", 0)):
            if not accept:
                refused.append(f"grew: {key} ({entry['lines']} -> {s['lines']})")
                continue
            new[key] = {"lines": s["lines"]}
        else:
            new[key] = {"lines": s["lines"]}
    if refused:
        return refused
    data = {"limits": {k: v for k, v in limits.items() if v != DEFAULT_LIMITS[k]} or baseline.get("limits", {}),
            "surfaces": new}
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, sort_keys=True)
        fh.write("\n")
    return []


def report(keyed: dict, limits: dict) -> str:
    over = over_budget(keyed, limits)
    out = []
    for kind in ("overview", "jsdoc", "block"):
        total = sum(1 for s in keyed.values() if s["kind"] == kind)
        bad = sum(1 for s in over.values() if s["kind"] == kind)
        pct = f" ({bad * 100 // total}%)" if total else ""
        out.append(f"{kind:9} {bad}/{total} over {limits[kind]}{pct}")
    worst = sorted(over.values(), key=lambda s: -s["lines"])[:20]
    if worst:
        out.append("largest:")
        out.extend(f"  {s['path']}:{s['line']} {s['kind']} {s['lines']}" for s in worst)
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, epilog=HELP_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("paths", nargs="*", metavar="PATH", help="files or directories to scan")
    parser.add_argument("--baseline", metavar="FILE", help=(
        "JSON file of accepted over-budget surfaces (default: comment-budget.json in the "
        "first PATH). A surface in it passes while it does not grow; one with a \"reason\" "
        "passes at any size. A surface that shrank below its recorded size or left the file "
        "fails until the baseline is rewritten, so the ceiling only moves down."))
    parser.add_argument("--write-baseline", action="store_true", help=(
        "rewrite the baseline from the current tree. Existing entries keep the smaller of "
        "their recorded and current size; new surfaces and growth are refused unless "
        "--accept is given, and are then listed so a reviewer sees them"))
    parser.add_argument("--accept", action="store_true", help=(
        "with --write-baseline: admit new over-budget surfaces and growth (first adoption, "
        "or a reviewed exception that should then carry a \"reason\")"))
    parser.add_argument("--limit", action="append", default=[], metavar="KIND=N",
                        help="override a budget for overview, jsdoc, or block; repeatable")
    parser.add_argument("--exclude", action="append", default=[], metavar="GLOB", help=(
        "skip paths matching GLOB (fnmatch on the relative path); repeatable. Build, "
        "dependency, generated, fixture, and snapshot directories are always skipped"))
    parser.add_argument("--report", action="store_true", help=(
        "print counts of over-budget surfaces by kind and the largest ones, then exit 0"))
    parser.add_argument("--defaults", action="store_true", help="print the default budgets and exit")
    args = parser.parse_args(argv)
    if args.defaults:
        for kind, value in DEFAULT_LIMITS.items():
            print(f"{kind} {value}")
        return 0
    if not args.paths:
        parser.print_usage(sys.stderr)
        return 2
    first = args.paths[0]
    baseline_path = args.baseline or os.path.join(first if os.path.isdir(first) else os.path.dirname(first) or ".", BASELINE_NAME)
    baseline = load_baseline(baseline_path)
    limits = resolve_limits(args.limit, baseline)
    keyed, unsupported = scan(args.paths, args.exclude)
    if args.report:
        print(report(keyed, limits))
        if unsupported:
            print(f"unsupported files not counted: {unsupported}")
        return 0
    if args.write_baseline:
        refused = write_baseline(keyed, limits, baseline, baseline_path, args.accept)
        if refused:
            print("refusing to raise the baseline without --accept:", file=sys.stderr)
            for line in refused:
                print(f"  {line}", file=sys.stderr)
            return 1
        print(f"wrote {baseline_path}")
        return 0
    violations, stale = check(keyed, limits, baseline, baseline_path)
    for line in violations + stale:
        print(line)
    if unsupported:
        print(f"unsupported files not counted: {unsupported}", file=sys.stderr)
    if violations or stale:
        return 1
    print(f"comment budget ok ({len(keyed)} surfaces, limits {limits})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
