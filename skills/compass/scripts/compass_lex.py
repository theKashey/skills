#!/usr/bin/env python3
"""Resolve, rewrite, reverse, admit, and check vocabulary in `{chart-root}/LEXICON.jsonl`.

The lexicon is a database, one JSON object per line, one row per concept. Each row
carries the concept's forms in three languages that share no vocabulary by default —
what people say (`speech`), what identifiers say (`code`, as split stems), and where
the chart or repository keeps it (`chart` address, `scope` paths, or `where` outside
the repository) — so a lookup can start in any language and end in the other two.
"""

from __future__ import annotations

import argparse
import functools
import itertools
import json
import math
import re
import sys
from pathlib import Path
from typing import Iterable, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent))
from compass_search import STOP_WORDS, TOKEN_RE, markdown_headings, singular  # noqa: E402
from compass_batch import run_batch  # noqa: E402

# Keep abbreviation prefixes separate from the next identifier word.
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
KNOWN_FIELDS = {"concept", "root", "context", "speech", "code", "note", *LOCATORS}
NOTE_BUDGET = 25
# Path segments too common to bridge anything: their overlap with a form is not evidence.
PATH_NOISE = {"src", "app", "lib", "packages", "apps", "index", "main", "internal", "pkg"}
# Capitalized abbreviations and compound identifiers can expose missing vocabulary.
SHORTHAND_RE = re.compile(r"^(?:(?=(?:.*[A-Z]){2})[A-Za-z0-9]+|[a-z0-9]+[A-Z][A-Za-z0-9]*)$")
MARKER_RE = re.compile(r"compass(?:-abstraction)?:")


class LexiconError(Exception):
    pass


# --- rows ---------------------------------------------------------------------------


def stems(text: str) -> tuple[str, ...]:
    """Identifier-split, lower-cased, stop-word-free tokens of any form or symbol."""

    return tuple(tokenize(text))


def row_key(row: dict) -> tuple[str, str, str]:
    return (row.get("root") or "", row.get("context") or "", row["concept"])


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

    Token separation identifies potential retrieval gain, never shared meaning.
    Semantic admission is reviewed separately from this mechanical predicate.
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
    """A shared form in distinct declared roots or contexts has disambiguation value."""

    if not row.get("root"):
        return False
    forms = {form.casefold() for form in row["speech"]}
    return any(
        other.get("root") and (other.get("root"), other.get("context")) != (row.get("root"), row.get("context"))
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
    context = row.get("context")
    if context is not None:
        if not isinstance(context, str) or not SLUG_RE.match(context):
            fail.append(f"{where}{label}: context must be a lowercase-hyphen slug")
        if not root:
            fail.append(f"{where}{label}: context requires its owning root")
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
                        "write the split stem (`consignment`, `purchase-order`), never the symbol"
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


@functools.lru_cache(maxsize=None)
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
                seen.add(tuple(singular(t) for t, _, _ in token_spans(identifier)))
    _SCAN_CACHE[key] = seen
    return seen


def stem_in_source(stem: str, identifiers: set[tuple[str, ...]]) -> bool:
    return any(matching_spans(stem, identifier, compact=True) for identifier in identifiers)


def stale_stems(repo_root: Path, row: dict, scopes: Sequence[str]) -> list[str]:
    """Code stems no identifier under the row's scopes (or, with no scopes, anywhere in
    the repository) still contains — the alias rotted."""

    if not row["code"]:
        return []
    identifiers = source_identifier_tokens(repo_root, scopes)
    return [stem for stem in row["code"] if not stem_in_source(stem, identifiers)]


# --- resolve ------------------------------------------------------------------------


def token_spans(text: str) -> list[tuple[str, int, int]]:
    """Keep original offsets and stop words so rewrites cannot swallow qualifiers."""

    result = []
    for word in TOKEN_RE.finditer(text):
        boundaries = [0, *(m.start() for m in CAMEL_BOUNDARY_RE.finditer(word.group())), len(word.group())]
        for start, end in zip(boundaries, boundaries[1:]):
            result.append((word.group()[start:end].casefold(), word.start() + start, word.start() + end))
    return result


def matching_spans(form: str, query_tokens: Sequence[str], compact: bool = False) -> list[tuple[int, int]]:
    needle = [singular(t) for t, _, _ in token_spans(form)]
    folded = [singular(t) for t in query_tokens]
    found = []
    for start in range(len(folded)):
        if needle and folded[start:start + len(needle)] == needle:
            found.append((start, len(needle)))
        elif compact and needle:
            # Only recorded code forms earn case/word-boundary normalization.
            target = "".join(needle)
            joined = ""
            for end in range(start, len(folded)):
                joined += folded[end]
                if joined == target:
                    found.append((start, end - start + 1))
                    break
                if len(joined) >= len(target):
                    break
    return found


def form_matches(row: dict, query_tokens: Sequence[str]) -> list[tuple[str, str, int, int]]:
    """(language, form, start, length) for every speech form or code stem inside the query."""

    found: list[tuple[str, str, int, int]] = []
    for language, forms in (("speech", row["speech"]), ("code", row["code"])):
        for form in forms:
            for start, length in matching_spans(form, query_tokens, compact=language == "code"):
                found.append((language, form, start, length))
    return found


def selected_rows(rows: Sequence[dict], root: str | None, context: str | None) -> list[dict]:
    return [row for row in rows
            if (not root or row.get("root") in (None, root))
            and (not context or row.get("context") in (None, context))]


def resolve(rows: Sequence[dict], chart_root: Path, sentence: str, root: str | None,
            context: str | None = None) -> tuple[list[dict], list[str], list[str]]:
    raw_tokens = [t for t in re.findall(r"[^\s,;:()\[\]{}\"']+", sentence)]
    query_tokens = [t for t, _, _ in token_spans(sentence)]
    hits: list[dict] = []
    covered: set[int] = set()
    for row in selected_rows(rows, root, context):
        matches = form_matches(row, query_tokens)
        if not matches:
            continue
        for _, _, start, length in matches:
            covered.update(range(start, start + length))
        hits.append({"row": row, "matches": matches, "scopes": row_scopes(chart_root, row)})
    unmatched = [
        token for index, token in enumerate(query_tokens)
        if index not in covered and token not in STOP_WORDS and len(token) > 1
    ]
    shorthand = [
        token for token in dict.fromkeys(raw_tokens)
        if SHORTHAND_RE.match(token) and stems(token) and all(t in unmatched for t in stems(token))
    ]
    return hits, unmatched, shorthand


MAX_REWRITES = 32


def rewrite_queries(hits: Sequence[dict], sentence: str) -> tuple[list[dict], list[dict], int]:
    """Separate contextual interpretations; substitute spans without editing other text."""

    tokens = token_spans(sentence)
    by_span: dict[tuple[int, int], dict[tuple[str, str, str], dict]] = {}
    for hit in hits:
        for _, _, start, length in hit["matches"]:
            span = (tokens[start][1], tokens[start + length - 1][2])
            by_span.setdefault(span, {})[row_key(hit["row"])] = hit
    # An explicitly named longer phrase takes precedence over its fragments.
    chosen: list[tuple[int, int]] = []
    for span in sorted(by_span, key=lambda s: (-(s[1] - s[0]), s[0])):
        if not any(span[0] < end and start < span[1] for start, end in chosen):
            chosen.append(span)
    chosen.sort()
    if not chosen:
        return [], [], 0

    def substitute(replacements: Sequence[str]) -> str:
        text = sentence
        for (start, end), replacement in reversed(list(zip(chosen, replacements))):
            text = text[:start] + replacement + text[end:]
        return text

    choices = [list(by_span[span].values()) for span in chosen]
    collisions = [{"text": sentence[start:end], "senses": [identity(hit["row"]) for hit in by_span[(start, end)].values()]}
                  for start, end in chosen if len(by_span[(start, end)]) > 1]
    candidates = []
    for selection in itertools.islice(itertools.product(*choices), MAX_REWRITES):
        code_choices = [hit["row"]["code"] or [sentence[start:end]]
                        for hit, (start, end) in zip(selection, chosen)]
        code_queries = list(dict.fromkeys(substitute(values) for values in
                                         itertools.islice(itertools.product(*code_choices), MAX_REWRITES)))
        candidates.append({
            "concepts": [identity(hit["row"]) for hit in selection],
            "chart_query": substitute([hit["row"]["speech"][0] for hit in selection]),
            "code_queries": code_queries,
            "code_queries_omitted": max(0, math.prod(map(len, code_choices)) - MAX_REWRITES),
            "scopes": list(dict.fromkeys(scope for hit in selection for scope in hit["scopes"])),
            "external": list(dict.fromkeys(hit["row"]["where"] for hit in selection if "where" in hit["row"])),
        })
    return candidates, collisions, max(0, math.prod(map(len, choices)) - MAX_REWRITES)


def identity(row: dict) -> dict:
    return {key: row[key] for key in ("concept", "root", "context") if key in row}


def query_result(rows: Sequence[dict], chart_root: Path, sentence: str,
                 root: str | None = None, context: str | None = None) -> dict:
    hits, unmatched, shorthand = resolve(rows, chart_root, sentence, root, context)
    candidates, collisions, omitted = rewrite_queries(hits, sentence)
    return {
        "status": "ambiguous" if collisions else "hit" if hits else "miss",
        "query": sentence, "strict": " ".join(stems(sentence)),
        "matches": [{**identity(hit["row"]), "speech": hit["row"]["speech"], "code": hit["row"]["code"],
                     locator_of(hit["row"]): hit["row"][locator_of(hit["row"])],
                     "scopes": hit["scopes"],
                     "matched": [{"language": lang, "form": form, "start_token": start, "length": length}
                                 for lang, form, start, length in hit["matches"]]} for hit in hits],
        "unmatched": list(dict.fromkeys(unmatched)), "shorthand": shorthand,
        "collisions": collisions, "candidates": candidates, "candidates_omitted": omitted,
    }


def render_resolve(hits: Sequence[dict], unmatched: Sequence[str], shorthand: Sequence[str], sentence: str) -> str:
    out = [f"original: {sentence}", f"strict: {' '.join(stems(sentence))}"]
    if hits:
        out.append("matched:")
    for hit in hits:
        row = hit["row"]
        by = ", ".join(dict.fromkeys(f"{form} [{language}]" for language, form, _, _ in hit["matches"]))
        root = f" root={row['root']}" if row.get("root") else ""
        context = f" context={row['context']}" if row.get("context") else ""
        out.append(f"  {by} → {row['concept']}{root}{context}")
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
    candidates, collisions, omitted = rewrite_queries(hits, sentence)
    if collisions:
        out.append("collision: " + ", ".join(c["text"] for c in collisions)
                   + " — several meanings; consult the glossary or pass --root and --context")
    if unmatched:
        out.append("unmatched: " + " ".join(dict.fromkeys(unmatched)) + "  (no lexicon row; not expanded)")
    if shorthand:
        out.append("looks like shorthand with no row: " + ", ".join(shorthand) + " — ask, or capture for admission")
    for index, candidate in enumerate(candidates, 1):
        out.append(f"alternative {index}: " + ", ".join("/".join(identity.values()) for identity in candidate["concepts"]))
        out.append("  chart query: " + candidate["chart_query"])
        out.extend("  code query: " + query for query in candidate["code_queries"])
        if candidate["scopes"]:
            out.append("  search in: " + " ".join(candidate["scopes"]))
        if candidate["code_queries_omitted"]:
            out.append(f"  {candidate['code_queries_omitted']} code query alternatives omitted; narrow the query")
    if omitted:
        out.append(f"{omitted} interpretations omitted; narrow with --root/--context or a shorter query")
    return "\n".join(out)


# --- reverse ------------------------------------------------------------------------


def reverse(rows: Sequence[dict], chart_root: Path, target: str, as_kind: str,
            root: str | None = None, context: str | None = None) -> list[tuple[dict, str]]:
    found: list[tuple[dict, str]] = []
    rows = selected_rows(rows, root, context)
    if as_kind == "auto":
        as_kind = "path" if "/" in target else "chart" if "." in target and ADDRESS_RE.match(target) else "code"
    if as_kind == "code":
        tokens = [t for t, _, _ in token_spans(target)]
        for row in rows:
            for stem in row["code"]:
                if matching_spans(stem, tokens, compact=True):
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
        context = f" context={row['context']}" if row.get("context") else ""
        out.append(f"{row['concept']}{root}{context}  (via {via})")
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
        fail.append(f"duplicate concept {key[2]!r} in root/context {key[:2]}")
    forms: dict[tuple[str, str, str, str], str] = {}
    for row in rows:
        for language, values in (("speech", row["speech"]), ("code", row["code"])):
            for value in values:
                tokens = [singular(token) for token, _, _ in token_spans(value)]
                form_key = "".join(tokens) if language == "code" else " ".join(tokens)
                key = (row.get("root") or "", row.get("context") or "", language, form_key)
                if key in forms and forms[key] != row["concept"]:
                    fail.append(
                        f"{language} form {value!r} belongs to both {forms[key]!r} and {row['concept']!r}"
                        + f" in root/context {key[:2]} — distinguish their actual bounded contexts or correct the forms"
                    )
                forms.setdefault(key, row["concept"])
    for row in rows:
        if row.get("context"):
            domain = chart_root / row["root"] / "DOMAIN.md"
            body = domain.read_text(encoding="utf-8") if domain.is_file() else ""
            headings = [title for _, level, title in markdown_headings(body.splitlines()) if level == 2]
            anchors = {re.sub(r"[^\w-]", "", heading.casefold().replace(" ", "-")) for heading in headings}
            if row["context"] not in anchors:
                fail.append(f"{row['concept']}: context {row['context']!r} is not a bounded-context heading in {row['root']}/DOMAIN.md")
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


def check_rows(rows: Sequence[dict], chart_root: Path, repo_root: Path) -> tuple[list[str], dict[str, int]]:
    fail: list[str] = []
    seen = {"rows": len(rows), "chart": 0, "scope": 0, "where": 0, "glossary_links": 0}
    if rows and [row_key(r) for r in rows] != sorted(row_key(r) for r in rows):
        fail.append(f"{LEXICON_NAME}: rows are not in the tool's order (root, context, concept) — run `sort`")
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
        for row in linked:
            if " ".join(stems(term)) != " ".join(stems(row["speech"][0])):
                fail.append(
                    f"{glossary.relative_to(chart_root)}: {term}: the glossary term is not row {slug}'s first speech "
                    f"form ({row['speech'][0]!r}) — the product term is canonical and comes first"
                )
    for glossary in sorted(chart_root.glob("*/GLOSSARY.md")):
        if re.search(r"^### Implementation aliases", glossary.read_text(encoding="utf-8", errors="ignore"), re.M):
            fail.append(
                f"{glossary.relative_to(chart_root)}: carries ### Implementation aliases; the lexicon owns every form — "
                "admit the alias as a row and replace the section with ### Lexicon"
            )
    return fail, seen


def check(chart_root: Path, repo_root: Path) -> tuple[list[str], dict[str, int]]:
    rows, errors = load_rows(chart_root / LEXICON_NAME)
    fail, seen = check_rows(rows, chart_root, repo_root)
    return errors + fail, seen


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
    merged = sorted([*existing, *new_rows], key=row_key)
    fail, _ = check_rows(merged, chart_root, repo_root)
    if fail:
        return fail, []
    if not dry_run:
        path.write_text(dump_rows(merged), encoding="utf-8")
    return [], list(new_rows)


# --- list ---------------------------------------------------------------------------


def render_list(rows: Sequence[dict], root: str | None, context: str | None = None) -> str:
    out = ["| root | context | concept | speech | code | locator |", "| --- | --- | --- | --- | --- | --- |"]
    for row in sorted(selected_rows(rows, root, context), key=row_key):
        kind = locator_of(row)
        locator = f"{kind}: " + (", ".join(row["scope"]) if kind == "scope" else row[kind])
        out.append(
            f"| {row.get('root') or ''} | {row.get('context') or ''} | {row['concept']} | {', '.join(row['speech'])} | "
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

    for command in ("resolve", "rewrite", "reverse"):
        p = sub.add_parser(command, help={
            "resolve": "recorded forms → contextual concepts, query alternatives, scopes, honest misses",
            "rewrite": "preserve query qualifiers while proposing separate chart/source alternatives",
            "reverse": "code symbol, path, or chart address → concepts and speech forms",
        }[command])
        p.add_argument("--root", help="select a known logical root")
        p.add_argument("--context", help="select a known bounded-context anchor")
        p.add_argument("--json", action="store_true", help="structured single result (bulk is always JSONL)")
        p.add_argument("--stdin", action="store_true", help="read JSONL requests, keeping one result per input")
        if command == "reverse":
            p.add_argument("--as", dest="as_kind", choices=("auto", "code", "path", "chart"), default="auto")
            p.add_argument("target", nargs="?")
        else:
            p.add_argument("sentence", nargs="*")

    p = sub.add_parser("add", help="admit rows: validate, run the gap gate, insert in tool order")
    p.add_argument("--row", action="append", help="one JSON row; repeatable")
    p.add_argument("--stdin", action="store_true", help="read JSONL rows from stdin (a batch is gated together)")
    p.add_argument("--dry-run", action="store_true")

    sub.add_parser("check", help="every invariant a script can decide; install this in the host's test suite")
    sub.add_parser("sort", help="rewrite rows in (root, context, concept) order")

    p = sub.add_parser("list", help="render the lexicon as a table")
    p.add_argument("--root")
    p.add_argument("--context")
    return parser.parse_args(argv)


def lookup_result(args: argparse.Namespace, rows: Sequence[dict], chart_root: Path, record: dict) -> dict:
    root = record.get("root", args.root)
    context = record.get("context", args.context)
    for name, value in (("root", root), ("context", context)):
        if value is not None and (not isinstance(value, str) or not SLUG_RE.fullmatch(value)):
            raise ValueError(f"{name} must be a lowercase-hyphen slug")
    if args.command != "reverse":
        return query_result(rows, chart_root, record["query"], root, context)
    found = reverse(rows, chart_root, record["target"], args.as_kind, root, context)
    return {"status": "ambiguous" if len(found) > 1 else "hit" if found else "miss",
            "target": record["target"],
            "matches": [{**row, "via": via, "scopes": row_scopes(chart_root, row)} for row, via in found]}


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
    if args.command == "list":
        print(render_list(rows, args.root, args.context))
        return 0 if rows else 1
    field = "target" if args.command == "reverse" else "query"
    value = args.target if field == "target" else " ".join(args.sentence)
    if args.stdin:
        if value:
            print("error: pass a positional input or --stdin, not both", file=sys.stderr)
            return 2
        return run_batch(sys.stdin, {field, "root", "context"}, field,
                         lambda record: lookup_result(args, rows, chart_root, record))
    if not value or not value.strip():
        print(f"error: pass a non-empty {field} or --stdin", file=sys.stderr)
        return 2
    try:
        result = lookup_result(args, rows, chart_root, {field: value})
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(result, ensure_ascii=False))
        return 1 if result["status"] == "miss" else 0
    if not rows:
        print(f"No lexicon at {lexicon.relative_to(chart_root.parent) if lexicon.is_relative_to(chart_root.parent) else lexicon}: nothing to translate; the strict query stands.", file=sys.stderr)
        return 1

    if args.command == "reverse":
        found = reverse(rows, chart_root, args.target, args.as_kind, args.root, args.context)
        if not found:
            print(f"No lexicon row names {args.target}", file=sys.stderr)
            return 1
        print(render_reverse(found))
        return 0
    sentence = value
    hits, unmatched, shorthand = resolve(rows, chart_root, sentence, args.root, args.context)
    print(render_resolve(hits, unmatched, shorthand, sentence))
    return 0 if hits else 1


if __name__ == "__main__":
    raise SystemExit(main())
