#!/usr/bin/env python3
"""Resolve, reverse, admit, and check the chart's lexicon: `{chart-root}/LEXICON.jsonl`.

The lexicon is a database, one JSON object per line, one row per concept. Each row
carries the concept's forms in three languages that share no vocabulary by default —
what people say (`speech`), what identifiers say (`code`, as split stems), and where
the chart or repository keeps it (`chart` address, `scope` paths, or `where` outside
the repository) — so a lookup can start in any language and end in the other two.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent))
from compass_search import STOP_WORDS, TOKEN_RE, singular  # noqa: E402

# The search splits `workItem`; the lexicon also splits `WIVService` into `wiv service`,
# because an all-caps prefix is exactly the kind of form a row exists to carry.
CAMEL_BOUNDARY_RE = re.compile(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")


def tokenize(text: str) -> list[str]:
    expanded = CAMEL_BOUNDARY_RE.sub(" ", text).replace("_", "-")
    return [
        token.casefold()
        for token in TOKEN_RE.findall(expanded)
        if len(token) > 1 and token.casefold() not in STOP_WORDS
    ]

LEXICON_NAME = "LEXICON.jsonl"
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
# `root`, `root.block`, `root.block.component` — coordinate-system.md §Addresses.
ADDRESS_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*(?:\.[a-z0-9]+(?:-[a-z0-9]+)*){0,2}$")
LOCATORS = ("chart", "scope", "where")
KNOWN_FIELDS = {"concept", "root", "speech", "code", "note", *LOCATORS}
NOTE_BUDGET = 25
# Path segments too common to bridge anything: their overlap with a form is not evidence.
PATH_NOISE = {"src", "app", "lib", "packages", "apps", "index", "main", "internal", "pkg"}
# A word with two capitals or a camel hump: `WIV`, `PTSController`, `quickAction`. Nothing to
# split it on says what it stands for; only a lexicon row can.
SHORTHAND_RE = re.compile(r"^(?:(?=(?:.*[A-Z]){2})[A-Za-z0-9]+|[a-z0-9]+[A-Z][A-Za-z0-9]*)$")
MARKER_RE = re.compile(r"compass(?:-abstraction)?:")


class LexiconError(Exception):
    pass


# --- rows ---------------------------------------------------------------------------


def stems(text: str) -> tuple[str, ...]:
    """Identifier-split, lower-cased, stop-word-free tokens of any form or symbol."""

    return tuple(tokenize(text))


def row_key(row: dict) -> tuple[str, str]:
    return (row.get("root") or "", row["concept"])


def locator_of(row: dict) -> str | None:
    present = [name for name in LOCATORS if name in row]
    return present[0] if len(present) == 1 else None


def locator_tokens(row: dict) -> set[str]:
    kind = locator_of(row)
    if kind == "chart":
        return gate_tokens(row["chart"].replace(".", " "))
    if kind == "scope":
        tokens: set[str] = set()
        for path in row["scope"]:
            for part in Path(path).parts:
                if part.casefold() not in PATH_NOISE:
                    tokens.update(gate_tokens(part))
        return tokens
    return set()


def gate_tokens(text: str) -> set[str]:
    return {singular(token) for token in stems(text)}


def speech_tokens(row: dict) -> set[str]:
    return {token for form in row["speech"] for token in gate_tokens(form)}


def code_tokens(row: dict) -> set[str]:
    return {token for stem in row["code"] for token in gate_tokens(stem)}


def bridges_a_gap(row: dict) -> bool:
    """The admission gate: some single form cannot reach some other language lexically.

    Identifier-split lexical search already carries `work item` to `WorkItemService`
    and to `tracker.work-item`. A row earns its place only when at least one of its
    forms shares no token with one of the other two languages — `WIV` against the
    chart address, `action-dropdown` against every speech form — because that is the
    hop nothing else makes. A row whose every form reaches every language restates
    the baseline and is rejected, so the lexicon measures incremental recall.
    """

    if locator_of(row) == "where":
        return True  # nothing in the repository to search; the pointer is the whole gain
    languages = {"speech": speech_tokens(row), "code": code_tokens(row), "location": locator_tokens(row)}
    for language, forms in (("speech", row["speech"]), ("code", row["code"])):
        for form in forms:
            tokens = gate_tokens(form)
            for other, other_tokens in languages.items():
                if other != language and not (tokens & other_tokens):
                    return True
    return False


def collides_across_roots(row: dict, rows: Sequence[dict]) -> bool:
    """A form that means something else in another root is admitted for that reason."""

    if not row.get("root"):
        return False
    forms = {form.casefold() for form in row["speech"]}
    return any(
        other.get("root") and other.get("root") != row["root"]
        and forms & {form.casefold() for form in other["speech"]}
        for other in rows
    )


def validate_row(row: object, line_number: int | None = None) -> list[str]:
    where = f"line {line_number}: " if line_number else ""
    if not isinstance(row, dict):
        return [f"{where}not a JSON object"]
    fail: list[str] = []
    label = row.get("concept") if isinstance(row.get("concept"), str) else "<row>"
    for name in sorted(set(row) - KNOWN_FIELDS):
        fail.append(f"{where}{label}: unknown field '{name}'")
    concept = row.get("concept")
    if not isinstance(concept, str) or not SLUG_RE.match(concept):
        fail.append(f"{where}{label}: concept must be a lowercase-hyphen slug")
    root = row.get("root")
    if root is not None and (not isinstance(root, str) or not SLUG_RE.match(root)):
        fail.append(f"{where}{label}: root must be a lowercase-hyphen slug")
    for field in ("speech", "code"):
        values = row.get(field)
        may_be_empty = field == "code" and "where" in row
        if not isinstance(values, list) or (not values and not may_be_empty) or not all(
            isinstance(v, str) and v.strip() for v in values
        ):
            fail.append(f"{where}{label}: {field} must be a list of strings" + ("" if may_be_empty else ", not empty"))
            continue
        if field == "code":
            for stem in values:
                if not SLUG_RE.match(stem):
                    fail.append(
                        f"{where}{label}: code stem '{stem}' is not lowercase-hyphen — "
                        "write the split stem (`wiv`, `action-dropdown`), never the symbol"
                    )
    kind = locator_of(row)
    if kind is None:
        fail.append(f"{where}{label}: exactly one of chart, scope, where")
    elif kind == "chart":
        if not isinstance(row["chart"], str) or not ADDRESS_RE.match(row["chart"]):
            fail.append(f"{where}{label}: chart must be an address root[.block[.component]]")
    elif kind == "scope":
        paths = row["scope"]
        if not isinstance(paths, list) or not paths or not all(isinstance(p, str) and p for p in paths):
            fail.append(f"{where}{label}: scope must be a non-empty list of repository-relative paths")
        else:
            for path in paths:
                if Path(path).is_absolute() or ".." in Path(path).parts:
                    fail.append(f"{where}{label}: scope '{path}' must be repository-relative")
    elif not isinstance(row["where"], str) or not row["where"].strip():
        fail.append(f"{where}{label}: where must be a non-empty string")
    for name, value in row.items():
        text = " ".join(value) if isinstance(value, list) else str(value)
        if MARKER_RE.search(text):
            fail.append(
                f"{where}{label}: field '{name}' carries a `compass:` marker literal — "
                "chart_check counts markers in every file; write the address in `chart` instead"
            )
    note = row.get("note")
    if note is not None:
        if not isinstance(note, str):
            fail.append(f"{where}{label}: note must be a string")
        elif len(note.split()) > NOTE_BUDGET:
            fail.append(
                f"{where}{label}: note is {len(note.split())} words, budget is {NOTE_BUDGET} — "
                "a row is a pointer; meaning belongs to the glossary"
            )
    return fail


def load_rows(path: Path) -> tuple[list[dict], list[str]]:
    rows: list[dict] = []
    fail: list[str] = []
    if not path.is_file():
        return rows, fail
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            fail.append(f"line {number}: blank line")
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as error:
            fail.append(f"line {number}: invalid JSON ({error.msg})")
            continue
        problems = validate_row(row, number)
        fail.extend(problems)
        if not problems:
            rows.append(row)
    return rows, fail


def dump_rows(rows: Sequence[dict]) -> str:
    ordered = sorted(rows, key=row_key)
    return "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in ordered)


# --- chart resolution ---------------------------------------------------------------


def address_document(chart_root: Path, address: str) -> Path:
    return chart_root.joinpath(*address.split(".")) / "README.md"


def coordinates_of(chart_root: Path, address: str) -> list[str]:
    """Repository paths the addressed document names under `## Implementation coordinates`."""

    document = address_document(chart_root, address)
    if not document.is_file():
        return []
    body = document.read_text(encoding="utf-8", errors="ignore")
    section = re.search(r"^## Implementation coordinates\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    if not section:
        return []
    paths = []
    for coordinate in re.findall(r"`([^`]+)`", section.group(1)):
        if "/" in coordinate and not any(c in coordinate for c in "<>{}*"):
            if coordinate not in paths:
                paths.append(coordinate)
    return paths


def row_scopes(chart_root: Path, row: dict) -> list[str]:
    kind = locator_of(row)
    if kind == "scope":
        return list(row["scope"])
    if kind == "chart":
        return coordinates_of(chart_root, row["chart"])
    return []


SRC_SUFFIXES = {".py", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".go", ".rs", ".java", ".rb",
                ".swift", ".sql", ".kt", ".cs", ".php", ".scala", ".vue", ".svelte"}
IDENTIFIER_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]+")
# Never evidence that a stem is live: generated, vendored, or dependency trees.
SCAN_EXCLUDED = {".git", "node_modules", ".venv", "dist", "build", "vendor", "target", "out", "coverage"}
_SCAN_CACHE: dict[tuple[Path, tuple[str, ...]], set[tuple[str, ...]]] = {}


def source_identifier_tokens(repo_root: Path, scopes: Sequence[str]) -> set[tuple[str, ...]]:
    """Every identifier under the given scopes (or the whole repository), as split-token tuples."""

    key = (repo_root, tuple(sorted(scopes)))
    if key in _SCAN_CACHE:
        return _SCAN_CACHE[key]
    roots = [repo_root / scope for scope in scopes] or [repo_root]
    seen: set[tuple[str, ...]] = set()
    for start in roots:
        if start.is_file():
            files: Iterable[Path] = [start]
        elif start.is_dir():
            files = (p for p in start.rglob("*") if p.is_file() and p.suffix in SRC_SUFFIXES
                     and not any(part in SCAN_EXCLUDED for part in p.parts))
        else:
            continue
        for file in files:
            text = file.read_text(encoding="utf-8", errors="ignore")
            for identifier in set(IDENTIFIER_RE.findall(text)):
                seen.add(tuple(singular(t) for t in stems(identifier)))
    _SCAN_CACHE[key] = seen
    return seen


def stem_in_source(stem: str, identifiers: set[tuple[str, ...]]) -> bool:
    needle = [singular(t) for t in stems(stem)]
    return any(contiguous(needle, identifier) is not None for identifier in identifiers)


def stale_stems(repo_root: Path, row: dict, scopes: Sequence[str]) -> list[str]:
    """Code stems no identifier under the row's scopes (or, with no scopes, anywhere in
    the repository) still contains — the alias rotted."""

    if not row["code"]:
        return []
    identifiers = source_identifier_tokens(repo_root, scopes)
    return [stem for stem in row["code"] if not stem_in_source(stem, identifiers)]


# --- resolve ------------------------------------------------------------------------


def contiguous(needle: Sequence[str], haystack: Sequence[str]) -> int | None:
    if not needle or len(needle) > len(haystack):
        return None
    for start in range(len(haystack) - len(needle) + 1):
        if tuple(haystack[start : start + len(needle)]) == tuple(needle):
            return start
    return None


def form_matches(row: dict, query_tokens: Sequence[str]) -> list[tuple[str, str, int, int]]:
    """(language, form, start, length) for every speech form or code stem inside the query."""

    found: list[tuple[str, str, int, int]] = []
    folded = [singular(token) for token in query_tokens]
    for language, forms in (("speech", row["speech"]), ("code", row["code"])):
        for form in forms:
            needle = [singular(token) for token in stems(form)]
            start = contiguous(needle, folded)
            if start is not None:
                found.append((language, form, start, len(needle)))
    return found


def resolve(rows: Sequence[dict], chart_root: Path, sentence: str, root: str | None) -> tuple[list[dict], list[str], list[str]]:
    raw_tokens = [t for t in re.findall(r"[^\s,;:()\[\]{}\"']+", sentence)]
    query_tokens = stems(sentence)
    hits: list[dict] = []
    covered: set[int] = set()
    for row in rows:
        if root and row.get("root") not in (None, root):
            continue
        matches = form_matches(row, query_tokens)
        if not matches:
            continue
        for _, _, start, length in matches:
            covered.update(range(start, start + length))
        hits.append({"row": row, "matches": matches, "scopes": row_scopes(chart_root, row)})
    unmatched = [
        token for index, token in enumerate(query_tokens)
        if index not in covered and token not in STOP_WORDS
    ]
    shorthand = [
        token for token in dict.fromkeys(raw_tokens)
        if SHORTHAND_RE.match(token) and stems(token) and all(t in unmatched for t in stems(token))
    ]
    return hits, unmatched, shorthand


def render_resolve(hits: Sequence[dict], unmatched: Sequence[str], shorthand: Sequence[str], sentence: str) -> str:
    out = [f"strict: {' '.join(stems(sentence))}"]
    if hits:
        out.append("matched:")
    for hit in hits:
        row = hit["row"]
        by = ", ".join(f"{form} [{language}]" for language, form, _, _ in hit["matches"])
        root = f" root={row['root']}" if row.get("root") else ""
        out.append(f"  {by} → {row['concept']}{root}")
        out.append(f"    speech: {', '.join(row['speech'])}")
        out.append(f"    code: {', '.join(row['code'])}")
        kind = locator_of(row)
        if kind == "chart":
            out.append(f"    chart: {row['chart']}")
        elif kind == "scope":
            out.append(f"    scope: {', '.join(row['scope'])}")
        else:
            out.append(f"    where: outside this repository — {row['where']}")
        if kind == "chart":
            out.append(
                "    scope: " + (", ".join(hit["scopes"]) if hit["scopes"] else
                "no implementation coordinates under that address (unsealed or stale — a finding, not a miss)")
            )
        if row.get("note"):
            out.append(f"    note: {row['note']}")
    roots_by_form: dict[str, set[str]] = {}
    for hit in hits:
        for _, form, _, _ in hit["matches"]:
            roots_by_form.setdefault(form.casefold(), set()).add(hit["row"].get("root") or "")
    collisions = sorted(form for form, roots in roots_by_form.items() if len(roots) > 1)
    if collisions:
        out.append("collision: " + ", ".join(collisions) + " — one form, several roots; pass --root to pick one")
    if unmatched:
        out.append("unmatched: " + " ".join(dict.fromkeys(unmatched)) + "  (no lexicon row; not expanded)")
    if shorthand:
        out.append("looks like shorthand with no row: " + ", ".join(shorthand) + " — ask, or capture for admission")
    if hits:
        expansion = list(dict.fromkeys(
            stem for hit in hits for stem in (hit["row"]["code"] + [f.casefold() for f in hit["row"]["speech"]])
        ))
        scopes = list(dict.fromkeys(scope for hit in hits for scope in hit["scopes"]))
        out.append("expanded: " + " ".join(expansion) + "  (disclosed; strict tokens above came first)")
        if scopes:
            out.append("search in: " + " ".join(scopes))
    return "\n".join(out)


# --- reverse ------------------------------------------------------------------------


def reverse(rows: Sequence[dict], chart_root: Path, target: str, as_kind: str) -> list[tuple[dict, str]]:
    found: list[tuple[dict, str]] = []
    if as_kind == "auto":
        as_kind = "path" if "/" in target else "chart" if "." in target and ADDRESS_RE.match(target) else "code"
    if as_kind == "code":
        tokens = [singular(t) for t in stems(target)]
        for row in rows:
            for stem in row["code"]:
                if contiguous([singular(t) for t in stems(stem)], tokens) is not None:
                    found.append((row, f"code stem {stem}"))
                    break
    elif as_kind == "chart":
        for row in rows:
            if locator_of(row) == "chart" and (row["chart"] == target or target.startswith(row["chart"] + ".")):
                found.append((row, f"chart {row['chart']}"))
            elif "." not in target and row.get("root") == target:
                found.append((row, f"root {target}"))
    else:
        for row in rows:
            for scope in row_scopes(chart_root, row):
                if target == scope or target.startswith(scope.rstrip("/") + "/"):
                    found.append((row, f"scope {scope}"))
                    break
    return found


def render_reverse(found: Sequence[tuple[dict, str]]) -> str:
    out = []
    for row, via in found:
        root = f" root={row['root']}" if row.get("root") else ""
        out.append(f"{row['concept']}{root}  (via {via})")
        out.append(f"  say: {', '.join(row['speech'])}")
        out.append(f"  code: {', '.join(row['code'])}")
        kind = locator_of(row)
        out.append(f"  {kind}: {row[kind] if kind != 'scope' else ', '.join(row['scope'])}")
    return "\n".join(out)


# --- check --------------------------------------------------------------------------


def glossary_links(chart_root: Path) -> list[tuple[Path, str, str]]:
    """(glossary, term, slug) for every `### Lexicon` field in every root glossary."""

    links = []
    for glossary in sorted(chart_root.glob("*/GLOSSARY.md")):
        body = glossary.read_text(encoding="utf-8", errors="ignore")
        for term, section in re.findall(r"^## (.+?)\s*\n(.*?)(?=^## |\Z)", body, re.S | re.M):
            field = re.search(r"^### Lexicon[ \t]*\n(.*?)(?=^### |\Z)", section, re.S | re.M)
            if field:
                for slug in re.findall(r"`([^`\n]+)`", field.group(1)):
                    links.append((glossary, term, slug))
    return links


def row_failures(rows: Sequence[dict], chart_root: Path, repo_root: Path) -> list[str]:
    """Every rule `add` and `check` share, over one set of rows, so a gated batch can never
    leave the file failing its own check."""

    fail: list[str] = []
    keys = [row_key(r) for r in rows]
    for key in sorted({k for k in keys if keys.count(k) > 1}):
        fail.append(f"duplicate concept {key[1]!r}" + (f" in root {key[0]}" if key[0] else ""))
    forms: dict[tuple[str, str, str], str] = {}
    for row in rows:
        for language, values in (("speech", row["speech"]), ("code", row["code"])):
            for value in values:
                key = (row.get("root") or "", language, " ".join(stems(value)))
                if key in forms and forms[key] != row["concept"]:
                    fail.append(
                        f"{language} form {value!r} belongs to both {forms[key]!r} and {row['concept']!r}"
                        + (f" in root {key[0]}" if key[0] else "") + " — give each row a root, or merge them"
                    )
                forms.setdefault(key, row["concept"])
    for row in rows:
        kind = locator_of(row)
        if kind == "chart":
            if not address_document(chart_root, row["chart"]).is_file():
                fail.append(f"{row['concept']}: chart {row['chart']} resolves to no document")
            elif row.get("root") and row["chart"].split(".")[0] != row["root"]:
                fail.append(f"{row['concept']}: chart {row['chart']} is not under root {row['root']}")
        elif kind == "scope":
            for scope in row["scope"]:
                if not (repo_root / scope).exists():
                    fail.append(f"{row['concept']}: scope {scope} is not on disk")
        if not bridges_a_gap(row) and not collides_across_roots(row, rows):
            fail.append(
                f"{row['concept']}: rejected — speech {sorted(speech_tokens(row))}, code {sorted(code_tokens(row))}, "
                f"and location {sorted(locator_tokens(row))} share vocabulary; lexical search already finds this"
            )
        for stem in stale_stems(repo_root, row, row_scopes(chart_root, row)):
            fail.append(
                f"{row['concept']}: code stem {stem!r} occurs in no identifier under its scope — "
                "the alias rotted; classify as implementation remapping before editing"
            )
    return fail


def check(chart_root: Path, repo_root: Path) -> tuple[list[str], dict[str, int]]:
    path = chart_root / LEXICON_NAME
    rows, fail = load_rows(path)
    seen = {"rows": len(rows), "chart": 0, "scope": 0, "where": 0, "glossary_links": 0}
    if rows and [row_key(r) for r in rows] != sorted(row_key(r) for r in rows):
        fail.append(f"{LEXICON_NAME}: rows are not in the tool's order (root, concept) — run `sort`")
    fail.extend(f"{LEXICON_NAME}: {problem}" for problem in row_failures(rows, chart_root, repo_root))
    for row in rows:
        seen[locator_of(row)] += 1
    for glossary, term, slug in glossary_links(chart_root):
        seen["glossary_links"] += 1
        root = glossary.parent.name
        linked = [r for r in rows if r["concept"] == slug and r.get("root") in (None, root)]
        if not linked:
            fail.append(f"{glossary.relative_to(chart_root)}: {term}: ### Lexicon names {slug!r}, no such row")
            continue
        if " ".join(stems(term)) != " ".join(stems(linked[0]["speech"][0])):
            fail.append(
                f"{glossary.relative_to(chart_root)}: {term}: the glossary term is not row {slug}'s first speech "
                f"form ({linked[0]['speech'][0]!r}) — the product term is canonical and comes first"
            )
    for glossary in sorted(chart_root.glob("*/GLOSSARY.md")):
        if re.search(r"^### Implementation aliases", glossary.read_text(encoding="utf-8", errors="ignore"), re.M):
            fail.append(
                f"{glossary.relative_to(chart_root)}: carries ### Implementation aliases; the lexicon owns every form — "
                "admit the alias as a row and replace the section with ### Lexicon"
            )
    return fail, seen


# --- add ----------------------------------------------------------------------------


def add(chart_root: Path, repo_root: Path, new_rows: Sequence[dict], dry_run: bool) -> tuple[list[str], list[dict]]:
    path = chart_root / LEXICON_NAME
    existing, fail = load_rows(path)
    if fail:
        return [f"{LEXICON_NAME} is not clean; run check first"] + fail, []
    for row in new_rows:
        fail.extend(validate_row(row))
    if fail:
        return fail, []
    merged = list(existing) + list(new_rows)
    fail = row_failures(merged, chart_root, repo_root)
    if fail:
        return fail, []
    if not dry_run:
        path.write_text(dump_rows(merged), encoding="utf-8")
    return [], list(new_rows)


# --- list ---------------------------------------------------------------------------


def render_list(rows: Sequence[dict], root: str | None) -> str:
    out = ["| root | concept | speech | code | locator |", "| --- | --- | --- | --- | --- |"]
    for row in sorted(rows, key=row_key):
        if root and row.get("root") not in (None, root):
            continue
        kind = locator_of(row)
        locator = f"{kind}: " + (", ".join(row["scope"]) if kind == "scope" else row[kind])
        out.append(
            f"| {row.get('root') or ''} | {row['concept']} | {', '.join(row['speech'])} | "
            f"{', '.join(row['code'])} | {locator} |"
        )
    return "\n".join(out)


# --- cli ----------------------------------------------------------------------------


def read_rows_argument(args: argparse.Namespace) -> list[dict]:
    texts: list[str] = []
    if args.row:
        texts.extend(args.row)
    if args.stdin:
        texts.extend(line for line in sys.stdin.read().splitlines() if line.strip())
    rows = []
    for text in texts:
        try:
            rows.append(json.loads(text))
        except json.JSONDecodeError as error:
            raise LexiconError(f"invalid JSON row: {error.msg}: {text[:80]}")
    if not rows:
        raise LexiconError("nothing to add: pass --row '<json>' or --stdin")
    return rows


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--chart-root", required=True, type=Path, help="host-declared Compass chart root")
    parser.add_argument("--repo-root", type=Path, default=Path("."), help="repository root that scope paths are relative to (default: cwd)")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("resolve", help="sentence in any language → concepts, expansions, scopes, honest misses")
    p.add_argument("--root", help="answer for one root only; collisions are otherwise all listed")
    p.add_argument("sentence", nargs="+")

    p = sub.add_parser("reverse", help="code symbol, repository path, or chart address → concept and speech forms")
    p.add_argument("--as", dest="as_kind", choices=("auto", "code", "path", "chart"), default="auto")
    p.add_argument("target")

    p = sub.add_parser("add", help="admit rows: validate, run the gap gate, insert in tool order")
    p.add_argument("--row", action="append", help="one JSON row; repeatable")
    p.add_argument("--stdin", action="store_true", help="read JSONL rows from stdin (a batch is gated together)")
    p.add_argument("--dry-run", action="store_true")

    sub.add_parser("check", help="every invariant a script can decide; install this in the host's test suite")
    sub.add_parser("sort", help="rewrite a hand-edited lexicon in the tool's order (root, concept)")

    p = sub.add_parser("list", help="render the lexicon as a table")
    p.add_argument("--root")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    chart_root = args.chart_root.expanduser()
    if not chart_root.is_dir():
        print(f"error: chart root is not a directory: {chart_root}", file=sys.stderr)
        return 2
    chart_root = chart_root.resolve()
    repo_root = args.repo_root.expanduser().resolve()
    if args.command in ("check", "add") and not chart_root.is_relative_to(repo_root):
        print(f"error: chart root {chart_root} is not under repo root {repo_root}; pass --repo-root", file=sys.stderr)
        return 2
    lexicon = chart_root / LEXICON_NAME

    if args.command == "check":
        fail, seen = check(chart_root, repo_root)
        counts = ", ".join(f"{v} {k}" for k, v in seen.items())
        print("\n".join(fail) or f"lexicon: clean — {counts}")
        return 1 if fail else 0

    if args.command == "add":
        try:
            new_rows = read_rows_argument(args)
        except LexiconError as error:
            print(f"error: {error}", file=sys.stderr)
            return 2
        fail, admitted = add(chart_root, repo_root, new_rows, args.dry_run)
        if fail:
            print("\n".join(fail), file=sys.stderr)
            return 1
        verb = "would admit" if args.dry_run else "admitted"
        print(f"{verb} {len(admitted)} row(s): " + ", ".join(r["concept"] for r in admitted))
        return 0

    rows, fail = load_rows(lexicon)
    if args.command == "sort":
        if fail:
            print("\n".join(fail), file=sys.stderr)
            return 1
        lexicon.write_text(dump_rows(rows), encoding="utf-8")
        print(f"sorted {len(rows)} row(s)")
        return 0
    if fail:
        print(f"error: {LEXICON_NAME} is not clean; run check", file=sys.stderr)
        print("\n".join(fail), file=sys.stderr)
        return 2
    if not rows:
        print(f"No lexicon at {lexicon.relative_to(chart_root.parent) if lexicon.is_relative_to(chart_root.parent) else lexicon}: nothing to translate; the strict query stands.", file=sys.stderr)
        return 1

    if args.command == "list":
        print(render_list(rows, args.root))
        return 0
    if args.command == "reverse":
        found = reverse(rows, chart_root, args.target, args.as_kind)
        if not found:
            print(f"No lexicon row names {args.target}", file=sys.stderr)
            return 1
        print(render_reverse(found))
        return 0
    sentence = " ".join(args.sentence)
    hits, unmatched, shorthand = resolve(rows, chart_root, sentence, args.root)
    print(render_resolve(hits, unmatched, shorthand, sentence))
    return 0 if hits else 1


if __name__ == "__main__":
    raise SystemExit(main())
