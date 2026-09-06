#!/usr/bin/env python3
"""Search a declared Compass chart without building a persistent index."""

from __future__ import annotations

import argparse
import math
import os
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
FENCE_RE = re.compile(r"^[ \t]*(`{3,}|~{3,})")
TOKEN_RE = re.compile(r"[^\W_]+", re.UNICODE)
CAMEL_BOUNDARY_RE = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")
INLINE_CODE_RE = re.compile(r"`([^`\n]+)`")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")
MARKDOWN_DECORATION_RE = re.compile(r"[*_~]")

KINDS = (
    "all",
    "abstraction",
    "blocks",
    "domain",
    "external",
    "glossary",
    "identity",
    "other",
    "registry",
    "viewport",
)

# These add noise to lexical discovery without helping distinguish chart concepts.
STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "how",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "this",
    "to",
    "was",
    "what",
    "when",
    "where",
    "which",
    "who",
    "with",
}

SIGNAL_ORDER = {"address": 0, "exact": 1, "heading": 2, "literal": 3, "related": 4}
# `root`, `root.block`, `root.block.component`: the address grammar coordinate-system.md §Addresses fixes.
ADDRESS_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*(?:\.[a-z0-9]+(?:-[a-z0-9]+)*)+$")
# A heading or slug the query names outright outranks an identifier mentioned in a body.
EXACT_STRENGTH = {"heading": 2, "identifier": 1}


@dataclass(frozen=True)
class Section:
    path: Path
    relative_path: str
    kind: str
    start_line: int
    end_line: int
    headings: tuple[str, ...]
    lines: tuple[str, ...]
    heading_text: str
    body_text: str
    inline_identifiers: frozenset[str]
    tokens: tuple[str, ...]
    entity_slug: str | None
    is_identity: bool


@dataclass(frozen=True)
class Match:
    section: Section
    signal: str
    score: float
    anchor_line: int
    phrase: str
    phrase_length: int
    strength: int


def clean_markdown(text: str) -> str:
    """Remove common inline Markdown while preserving the visible words."""

    text = MARKDOWN_LINK_RE.sub(r"\1", text)
    text = INLINE_CODE_RE.sub(r"\1", text)
    return MARKDOWN_DECORATION_RE.sub("", text).strip()


def normalized_text(text: str) -> str:
    return " ".join(clean_markdown(text).casefold().split())


def singular(text: str) -> str:
    """Fold a plain English plural so `customers` names the glossary's `Customer`."""

    words = []
    for word in text.split():
        if len(word) > 3 and word.endswith("ies"):
            word = word[:-3] + "y"
        elif len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
            word = word[:-1]
        words.append(word)
    return " ".join(words)


def tokenize(text: str) -> list[str]:
    expanded = CAMEL_BOUNDARY_RE.sub(" ", text).replace("_", "-")
    return [
        token.casefold()
        for token in TOKEN_RE.findall(expanded)
        if len(token) > 1 and token.casefold() not in STOP_WORDS
    ]


def chart_kind(relative_path: str) -> str:
    path = Path(relative_path)
    name = path.name.upper()
    if name == "ABSTRACTIONS.MD":
        return "abstraction"
    if name == "GLOSSARY.MD":
        return "glossary"
    if name == "DOMAIN.MD":
        return "domain"
    if name == "CONTAINERS.MD":
        return "blocks"
    if name == "VIEWPORTS.MD":
        return "viewport"
    if name == "COMPASS.MD":
        return "registry"
    if name == "README.MD":
        return "identity"
    if "externals" in {part.casefold() for part in path.parts}:
        return "external"
    return "other"


def markdown_headings(lines: Sequence[str]) -> list[tuple[int, int, str]]:
    headings: list[tuple[int, int, str]] = []
    fence: str | None = None
    for index, line in enumerate(lines):
        fence_match = FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)
            if fence is None:
                fence = marker[0]
            elif marker[0] == fence:
                fence = None
            continue
        if fence is not None:
            continue
        match = HEADING_RE.match(line)
        if match:
            headings.append((index, len(match.group(1)), clean_markdown(match.group(2))))
    return headings


def make_section(
    path: Path,
    relative_path: str,
    kind: str,
    lines: Sequence[str],
    start: int,
    end: int,
    h1: str | None,
    h2: str | None,
    entity_slug: str | None = None,
) -> Section:
    section_lines = tuple(lines[start:end])
    headings = tuple(value for value in (h1, h2) if value)
    if not headings:
        headings = (relative_path,)
    heading_text = " > ".join(headings)
    body_text = "\n".join(section_lines)
    identifiers = frozenset(
        singular(normalized_text(identifier))
        for identifier in INLINE_CODE_RE.findall(body_text)
        if normalized_text(identifier)
    )
    # Repeating headings makes them a stronger BM25 field without obscuring exact tiers.
    tokens = tuple(tokenize(body_text) + (tokenize(heading_text) * 2))
    return Section(
        path=path,
        relative_path=relative_path,
        kind=kind,
        start_line=start + 1,
        end_line=end,
        headings=headings,
        lines=section_lines,
        heading_text=heading_text,
        body_text=body_text,
        inline_identifiers=identifiers,
        tokens=tokens,
        entity_slug=entity_slug,
        is_identity=h2 is None and entity_slug is not None,
    )


def parse_markdown(path: Path, root: Path) -> list[Section]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []
    lines = text.splitlines()
    if not lines:
        return []

    relative_path = path.relative_to(root).as_posix()
    kind = chart_kind(relative_path)
    headings = markdown_headings(lines)
    h1 = next((title for _, level, title in headings if level == 1), None)
    h2s = [(index, title) for index, level, title in headings if level == 2]
    # A README below the chart root is an entity's identity document; its directory
    # name is the entity's address segment, whether or not the prose repeats it.
    entity_slug = None
    if kind == "identity" and path.parent != root:
        entity_slug = normalized_text(path.parent.name)

    if not h2s:
        return [
            make_section(
                path, relative_path, kind, lines, 0, len(lines), h1, None, entity_slug
            )
        ]

    sections: list[Section] = []
    first_h2 = h2s[0][0]
    if entity_slug is not None or (
        first_h2 and any(line.strip() for line in lines[:first_h2])
    ):
        sections.append(
            make_section(
                path, relative_path, kind, lines, 0, first_h2, h1, None, entity_slug
            )
        )
    for position, (start, title) in enumerate(h2s):
        end = h2s[position + 1][0] if position + 1 < len(h2s) else len(lines)
        sections.append(
            make_section(path, relative_path, kind, lines, start, end, h1, title)
        )
    return sections


def markdown_files(root: Path) -> Iterable[Path]:
    for current, directories, filenames in os.walk(root, followlinks=False):
        directories[:] = sorted(
            directory
            for directory in directories
            if directory not in {".git", "node_modules"}
            and not Path(current, directory).is_symlink()
        )
        for filename in sorted(filenames):
            path = Path(current, filename)
            if path.suffix.casefold() == ".md" and not path.is_symlink():
                yield path


def load_sections(root: Path, kinds: set[str]) -> list[Section]:
    sections: list[Section] = []
    for path in markdown_files(root):
        for section in parse_markdown(path, root):
            if "all" in kinds or section.kind in kinds:
                sections.append(section)
    return sections


def bm25_scores(sections: Sequence[Section], query_tokens: Sequence[str]) -> list[float]:
    if not sections or not query_tokens:
        return [0.0] * len(sections)

    unique_query = tuple(dict.fromkeys(query_tokens))
    document_frequencies = {
        term: sum(term in set(section.tokens) for section in sections)
        for term in unique_query
    }
    average_length = sum(len(section.tokens) for section in sections) / len(sections)
    average_length = average_length or 1.0
    scores: list[float] = []
    k1 = 1.2
    b = 0.75

    for section in sections:
        frequencies = Counter(section.tokens)
        length_factor = 1 - b + b * len(section.tokens) / average_length
        score = 0.0
        for term in unique_query:
            frequency = frequencies[term]
            if not frequency:
                continue
            document_frequency = document_frequencies[term]
            inverse_document_frequency = math.log(
                1 + (len(sections) - document_frequency + 0.5)
                / (document_frequency + 0.5)
            )
            score += inverse_document_frequency * (
                frequency * (k1 + 1) / (frequency + k1 * length_factor)
            )
        scores.append(score)
    return scores


def query_addresses(query: str) -> list[str]:
    """Return every token of the query written in the address grammar."""

    addresses = []
    for token in query.split():
        candidate = token.strip("`'\"(),;:").casefold()
        if ADDRESS_RE.match(candidate) and candidate not in addresses:
            addresses.append(candidate)
    return addresses


def address_document(address: str) -> str:
    return "/".join(address.split(".")) + "/README.md"


def query_phrases(query: str) -> list[tuple[str, int]]:
    """Every contiguous run of query words, longest first, that is not only stop words.

    Task language rarely repeats a chart heading whole, but it usually contains one:
    a glossary term, a block slug, a component name. Matching those runs keeps the
    deterministic tier reachable from the hook's task-phrase input.
    """

    raw_words = normalized_text(query).split()
    words = singular(normalized_text(query)).split()
    phrases: list[tuple[str, int]] = []
    for length in range(len(words), 0, -1):
        for start in range(0, len(words) - length + 1):
            run = raw_words[start : start + length]
            if all(word in STOP_WORDS or len(word) < 2 for word in run):
                continue
            phrase = " ".join(words[start : start + length])
            if all(phrase != known for known, _ in phrases):
                phrases.append((phrase, length))
    return phrases


@dataclass(frozen=True)
class Signal:
    name: str
    phrase: str
    phrase_length: int
    strength: int


def match_signal(
    section: Section,
    query: str,
    phrases: Sequence[tuple[str, int]],
    address_documents: Sequence[str],
    score: float,
) -> Signal | None:
    normalized_heading = normalized_text(section.headings[-1])
    folded_query = normalized_text(query)
    folded_body = normalized_text(section.body_text)
    named = {
        singular(normalized_heading),
        singular(normalized_text(re.sub(r"\s*\([^)]*\)\s*$", "", section.headings[-1]))),
    }
    if section.entity_slug:
        named.add(singular(section.entity_slug))

    if section.is_identity and section.relative_path in address_documents:
        return Signal("address", folded_query, len(folded_query.split()), 3)
    for phrase, length in phrases:
        if phrase in named:
            return Signal("exact", phrase, length, EXACT_STRENGTH["heading"])
    for phrase, length in phrases:
        if phrase in section.inline_identifiers:
            return Signal("exact", phrase, length, EXACT_STRENGTH["identifier"])
    # Only the section's own heading counts: matching the ancestry string would turn
    # every section of one document into a hit for its title.
    if folded_query and folded_query in normalized_heading:
        return Signal("heading", folded_query, len(folded_query.split()), 0)
    if folded_query and folded_query in folded_body:
        return Signal("literal", folded_query, len(folded_query.split()), 0)
    if score > 0:
        return Signal("related", folded_query, 0, 0)
    return None


def anchor_line(section: Section, query: str, query_tokens: Sequence[str], signal: str) -> int:
    folded_query = normalized_text(query)
    if signal != "related":
        for offset, line in enumerate(section.lines):
            if folded_query in normalized_text(line):
                return section.start_line + offset

    terms = set(query_tokens)
    best_offset = 0
    best_overlap = -1
    for offset, line in enumerate(section.lines):
        overlap = sum(Counter(tokenize(line))[term] for term in terms)
        if overlap > best_overlap:
            best_overlap = overlap
            best_offset = offset
    return section.start_line + best_offset


def search(
    sections: Sequence[Section], query: str, include_related: bool
) -> list[Match]:
    query_tokens = tokenize(query)
    phrases = query_phrases(query)
    address_documents = [address_document(address) for address in query_addresses(query)]
    scores = bm25_scores(sections, query_tokens)
    matches: list[Match] = []
    for section, score in zip(sections, scores):
        signal = match_signal(section, query, phrases, address_documents, score)
        if signal is None or (signal.name == "related" and not include_related):
            continue
        matches.append(
            Match(
                section=section,
                signal=signal.name,
                score=score,
                anchor_line=anchor_line(section, signal.phrase, query_tokens, signal.name),
                phrase=signal.phrase,
                phrase_length=signal.phrase_length,
                strength=signal.strength,
            )
        )
    return sorted(
        matches,
        key=lambda match: (
            SIGNAL_ORDER[match.signal],
            -match.phrase_length,
            -match.strength,
            -match.score,
            match.section.relative_path,
            match.section.start_line,
        ),
    )


def owned_terms(matches: Sequence[Match], query: str) -> tuple[list[str], list[str]]:
    """Split the query into the phrases some chart section names and the leftover words."""

    owned = list(dict.fromkeys(m.phrase for m in matches if m.signal in {"address", "exact"}))
    covered = {word for phrase in owned for word in phrase.split()}
    unowned = [
        singular(word)
        for word in dict.fromkeys(normalized_text(query).split())
        if singular(word) not in covered and word not in STOP_WORDS and len(word) >= 2
    ]
    return owned, unowned


def excerpt_bounds(section: Section, anchor: int, max_lines: int) -> tuple[int, int]:
    total = len(section.lines)
    if total <= max_lines:
        return 0, total
    anchor_offset = max(0, min(total - 1, anchor - section.start_line))
    start = max(0, anchor_offset - max_lines // 2)
    end = min(total, start + max_lines)
    start = max(0, end - max_lines)
    return start, end


def render_match(match: Match, index: int, max_lines: int, query: str) -> str:
    section = match.section
    start_offset, end_offset = excerpt_bounds(section, match.anchor_line, max_lines)
    shown_start = section.start_line + start_offset
    shown_end = section.start_line + end_offset - 1
    heading = " > ".join(section.headings)
    signal = match.signal
    if signal == "exact" and match.phrase != singular(normalized_text(query)):
        signal = f"{signal} term={match.phrase!r}"
    output = [
        f"[{index}] {section.relative_path}:{shown_start}-{shown_end}",
        f"    kind={section.kind} signal={signal} bm25={match.score:.4f}",
        f"    heading={heading}",
    ]
    if start_offset:
        output.append(f"    ... {start_offset} earlier section lines omitted ...")
    width = len(str(shown_end))
    for offset in range(start_offset, end_offset):
        line_number = section.start_line + offset
        output.append(f"    {line_number:>{width}} | {section.lines[offset]}")
    remaining = len(section.lines) - end_offset
    if remaining:
        output.append(f"    ... {remaining} later section lines omitted ...")
    return "\n".join(output)


def positive_integer(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return number


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Search one declared Compass chart. Address, exact, heading, and literal matches come first; "
            "BM25 ranks lexical relevance and may add related sections."
        )
    )
    parser.add_argument(
        "--chart-root",
        required=True,
        type=Path,
        help="host-declared Compass chart root",
    )
    parser.add_argument(
        "--kind",
        action="append",
        choices=KINDS,
        help="limit records by chart role; repeat to select more than one",
    )
    parser.add_argument("--limit", type=positive_integer, default=10, help="maximum sections printed (default 10)")
    parser.add_argument(
        "--max-lines",
        type=positive_integer,
        default=48,
        help="maximum Markdown lines shown for each matching section",
    )
    parser.add_argument(
        "--literal-only",
        action="store_true",
        help="exclude BM25-only related sections (direct matches remain BM25-ranked)",
    )
    parser.add_argument("query", nargs="+", help="words or exact identifier to find")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.chart_root.expanduser()
    if not root.is_dir():
        print(f"error: chart root is not a directory: {root}", file=sys.stderr)
        return 2

    root = root.resolve()
    kinds = set(args.kind or ["all"])
    query = " ".join(args.query).strip()
    if not query:
        print("error: query must not be empty", file=sys.stderr)
        return 2

    sections = load_sections(root, kinds)
    for address in query_addresses(query):
        if not (root / address_document(address)).is_file():
            print(
                f"note: address {address} resolves to no chart document "
                f"({address_document(address)}); a marker carrying it is a "
                "classification finding, not a typo to delete",
                file=sys.stderr,
            )
    matches = search(sections, query, include_related=not args.literal_only)
    if not matches:
        print(f"No chart sections matched: {query}", file=sys.stderr)
        _, unowned = owned_terms(matches, query)
        if unowned:
            print("Named nowhere in the chart: " + ", ".join(unowned) + ".", file=sys.stderr)
        return 1

    shown = matches[: args.limit]
    direct = sum(match.signal != "related" for match in matches)
    related = len(matches) - direct
    print(
        f"Found {len(matches)} section(s): {direct} direct, {related} BM25-related. "
        "BM25 is a lexical ranking signal, not confidence or semantic proof."
    )
    owned, unowned = owned_terms(matches, query)
    if unowned:
        print(
            "Named by a chart heading, slug, or identifier: "
            + (", ".join(owned) or "nothing in this query")
            + ". Named nowhere in the chart: "
            + ", ".join(unowned)
            + "."
        )
    for index, match in enumerate(shown, start=1):
        if index > 1:
            print()
        print(render_match(match, index, args.max_lines, query))
    omitted = len(matches) - len(shown)
    if omitted:
        print(f"\n... {omitted} additional matching section(s) omitted by --limit ...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
