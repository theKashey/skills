#!/usr/bin/env python3
"""Local skill router: extended skill table + BM25 ranking + optional local rerank.

Standard library only. No network. Three subcommands:

  table  Build the extended skill table (name, description, use_when,
         dont_use, headings) from one or more skill roots.
  route  Rank skills for a task brief; abstain when nothing fits.
  eval   Replay every skill's shipped evals/eval_queries.jsonl ({query,
         should_trigger}) and report routing accuracy.

A skill root is a skill folder or any directory with skill folders somewhere
below it. --from PATH adds every .<tool>/skills and .<tool>/available-skills
folder at PATH and each folder above it, up to the home folder, plus the home
folder's own, after any --skills roots; the first copy of a name wins, so the
nearest one does.

Routing reads only each SKILL.md. Shipped queries measure the router in eval;
they never steer a route.

Second stage: set --rerank CMD (or SKILL_ROUTER_RERANK) to any local command.
It receives {"task", "candidates": [...]} as JSON on stdin and prints
{"ranking": [{"name", "score"}]} or {"pick": name-or-null}. Any failure or
timeout falls back to the BM25 result and says so.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- tokenizing

STOPWORDS = frozenset(
    """a about above after again against all am an and any are as at be because
    been before being below between both but by can could did do does doing down
    during each few for from further had has have having he her here hers him his
    how i if in into is it its itself just let lets me more most my no nor not of
    off on once only or other our out over own same she should so some such than
    that the their them then there these they this those through to too under
    until up very was we were what when where which while who whom why will with
    would you your yours please want need like make sure also get got one two
    use using used user task help ok hey something thing way
    e g eg ie etc via per""".split()
)

# Words that appear in nearly every skill's routing text. On their own they are
# never evidence that a skill fits.
GENERIC = frozenset(
    """work change code review file files run new existing check make write update
    create add fix test tests issue project page system team""".split()
)

WORD_RE = re.compile(r"[A-Za-z0-9]+")
# Splits identifiers such as featureGate or TestRunner; the whole word is kept too.
CAMEL_RE = re.compile(r"[A-Z]+(?![a-z])|[A-Z]?[a-z0-9]+|\d+")


@functools.lru_cache(maxsize=None)
def stem(word: str) -> str:
    for suffix, repl in (("ies", "y"), ("ing", ""), ("ed", ""), ("es", ""), ("s", "")):
        if suffix == "s" and word.endswith(("ss", "us", "is")):
            continue
        if word.endswith(suffix) and len(word) - len(suffix) >= 3:
            return word[: -len(suffix)] + repl
    return word


@functools.lru_cache(maxsize=None)
def word_tokens(raw: str) -> tuple[str, ...]:
    words = [raw.lower()]
    parts = CAMEL_RE.findall(raw)
    if len(parts) > 1:
        words += [part.lower() for part in parts]
    return tuple(stem(w) for w in words if w not in STOPWORDS and len(w) > 1)


# Adjacent words also count as one pair token ("feature gate"), so two skills that
# share single words but not phrases stop looking alike. Pairs do not cross punctuation.
CLAUSE_RE = re.compile(r"[.;:!?,()\[\]\n]+")


def tokens(text: str) -> list[str]:
    out: list[str] = []
    for clause in CLAUSE_RE.split(text):
        heads = []
        for raw in WORD_RE.findall(clause):
            words = word_tokens(raw)
            out += words
            if words:
                heads.append(words[0])
        out += [a + " " + b for a, b in zip(heads, heads[1:])]
    return out


# ---------------------------------------------------------------- extraction

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
# Anchored: "Pipeline Trigger" or "post-trigger route" name a workflow step, not when to use the skill.
USE_HEADING_RE = re.compile(
    r"^\W*(?:use when|when to use|use (?:this|me) (?:when|for)|applies when|when this skill (?:applies|helps|activates)"
    r"|(?:skill )?triggers?(?: phrases| conditions)?\W*$)",
    re.I,
)
DONT_HEADING_RE = re.compile(
    r"\b(do not use|don'?t use|when not to use|not for|avoid|non-?goals?|out of scope|anti-?triggers?)\b", re.I
)
DONT_LINE_RE = re.compile(
    r"^\s*(?:[-*]\s*)?\**(?:do not use|don'?t use|(?:do not|don'?t) (?:load|invoke|trigger) (?:this|me)\b|not for|never use)\b", re.I
)
# Splits a description into its "use" part and its "not for" part.
DESC_NOT_RE = re.compile(r"[;.]\s*(?:but\s+)?(?:not (?:for|when|to)|do not use|don'?t use)\b", re.I)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    fields: dict[str, str] = {}
    key = None
    for line in match.group(1).splitlines():
        field = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if field:
            key = field.group(1)
            value = field.group(2).strip()
            fields[key] = "" if value in {">", "|", ">-", "|-"} else value.strip("\"'")
        elif key and line.startswith((" ", "\t")):
            fields[key] = (fields[key] + " " + line.strip()).strip()
    return fields, text[match.end():]


def split_description(desc: str) -> tuple[str, list[str]]:
    match = DESC_NOT_RE.search(desc)
    if not match:
        return desc, []
    return desc[: match.start()].strip(), [desc[match.start():].lstrip(";. ").strip()]


def body_sections(body: str) -> tuple[list[str], list[str], list[str]]:
    """Return (use_when lines, dont_use lines, headings) from a SKILL.md body."""
    use_when, dont_use, headings = [], [], []
    mode = None
    in_fence = False
    paragraph: list[str] = []

    def flush() -> None:
        if paragraph and mode:
            (use_when if mode == "use" else dont_use).append(" ".join(paragraph))
        paragraph.clear()

    for line in body.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        heading = re.match(r"^#{1,6}\s+(.*)$", line)
        if heading:
            flush()
            title = heading.group(1).strip()
            headings.append(title)
            mode = "dont" if DONT_HEADING_RE.search(title) else "use" if USE_HEADING_RE.match(title) else None
            continue
        stripped = line.strip()
        if DONT_LINE_RE.match(stripped):
            flush()
            dont_use.append(stripped.lstrip("-* ").strip("*"))
            continue
        if not stripped or stripped.startswith("|"):
            flush()
            continue
        if mode:
            if re.match(r"^[-*]\s+|^\d+\.\s+", stripped):
                flush()
                paragraph.append(re.sub(r"^[-*]\s+|^\d+\.\s+", "", stripped))
            else:
                paragraph.append(stripped)
    flush()
    return use_when, dont_use, headings


def load_queries(skill_md: str) -> tuple[list[str], list[str]]:
    """A skill's shipped eval queries; read only by eval, never by routing."""
    should, should_not = [], []
    jsonl = Path(skill_md).parent / "evals" / "eval_queries.jsonl"
    if jsonl.is_file():
        for line in jsonl.read_text(encoding="utf-8").splitlines():
            if line.strip():
                row = json.loads(line)
                (should if row.get("should_trigger") else should_not).append(row["query"])
    return should, should_not


def read_skill(skill_dir: Path) -> dict | None:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return None
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    fields, body = parse_frontmatter(text)
    description = fields.get("description", "")
    use_part, dont_desc = split_description(description)
    use_body, dont_body, headings = body_sections(body)
    return {
        "name": fields.get("name") or skill_dir.name,
        "path": str(skill_md),
        "description": description,
        "use_when": [use_part] + use_body if use_part else use_body,
        "dont_use": dont_desc + dont_body,
        "headings": headings,
        "source_hash": hashlib.sha256(text.encode()).hexdigest()[:12],
    }


LIBRARY_NAMES = ("skills", "available-skills")
SKIP_DIRS = frozenset({".git", "node_modules"})


def skill_dirs(root: Path, visited: set | None = None) -> list[Path]:
    """Every folder at or below `root` that holds a SKILL.md; a skill's own subfolders are not searched.

    `visited` holds (device, inode) pairs, so a folder reached twice through symlinks is read once.
    """
    visited = set() if visited is None else visited
    try:
        st = root.stat()
    except OSError:
        return []
    if (st.st_dev, st.st_ino) in visited:
        return []
    visited.add((st.st_dev, st.st_ino))
    if (root / "SKILL.md").is_file():
        return [root]
    found = []
    try:
        children = sorted(e.name for e in os.scandir(root) if e.name not in SKIP_DIRS and is_dir(e))
    except OSError:
        return []
    for name in children:
        found += skill_dirs(root / name, visited)
    return found


def is_dir(path) -> bool:
    try:
        return path.is_dir()
    except OSError:  # an unreadable entry such as a protected .env must not hide its neighbours
        return False


def libraries_from(start: Path) -> list[Path]:
    """Skill folders at the work location and each folder above it, nearest first, ending with the home folder."""
    start = start.expanduser().resolve()
    if not start.exists():  # a typo must not look like "no skill fits"
        sys.exit(f"skill_router: work location {start} does not exist")
    if not start.is_dir():
        start = start.parent
    home = Path.home().resolve()
    levels = [start, *start.parents]
    levels = levels[: levels.index(home) + 1] if home in levels else levels + [home]
    found = []
    for level in levels:
        try:
            tools = sorted(p for p in level.iterdir() if p.name.startswith("."))
        except OSError:
            continue
        found += [tool / name for tool in tools for name in LIBRARY_NAMES if is_dir(tool / name)]
    return found


def dirs_key(root: Path) -> set:
    try:
        st = root.stat()
    except OSError:
        return set()
    return {(st.st_dev, st.st_ino)}


def build_table(roots: list[Path], found: list[Path] = (), origin: Path | None = None) -> list[dict]:
    """Read every skill under the explicit `roots`, then the `found` libraries; the first copy of a name wins."""
    table, names, visited = [], set(), set()
    for root, explicit in [(r, True) for r in roots] + [(r, False) for r in found]:
        root = Path(os.path.abspath(root.expanduser()))  # printed load: paths work from any folder
        seen_before = bool(dirs_key(root) & visited) if explicit else False
        dirs = skill_dirs(root, visited)
        if explicit and not dirs and not seen_before:  # a typo must not look like "no skill fits"
            sys.exit(f"skill_router: no SKILL.md found under {root}")
        for skill_dir in dirs:
            entry = read_skill(skill_dir)
            if entry and entry["name"] not in names:
                names.add(entry["name"])
                table.append(entry)
    if not table:
        sys.exit(f"skill_router: no SKILL.md found from {origin}")
    return table


def load_table(args) -> list[dict]:
    """Explicit --skills roots first, in the order given, then the folders --from finds."""
    found = libraries_from(args.origin) if args.origin else []
    return build_table(args.roots or [], found, args.origin)


# ---------------------------------------------------------------- ranking

# The skill card (its own routing prose) is scored as one BM25F document.
CARD_FIELDS = {"name": 3.0, "use_when": 2.5, "description": 1.0, "headings": 0.5}
K1, B = 1.2, 0.75
MIN_IDF = 1.0
# A word on more than this share of skill cards is this library's boilerplate
# (the product's own name, "src", "package") and is not evidence.
GENERIC_SHARE = 0.35
DONT_WEIGHT = 0.8


def field_text(entry: dict, field: str) -> list[str]:
    value = entry.get(field, "")
    if field == "name":
        value = entry["name"].replace("-", " ").replace(":", " ")
    items = value if isinstance(value, list) else [value]
    return [item for item in items if item]


def counts(text: str) -> dict[str, int]:
    bag: dict[str, int] = {}
    for tok in tokens(text):
        bag[tok] = bag.get(tok, 0) + 1
    return bag


class Router:
    def __init__(self, table: list[dict]):
        self.table = table
        self.cards, self.dont = [], []
        for entry in table:
            card = {}
            for field, weight in CARD_FIELDS.items():
                for item in field_text(entry, field):
                    for tok in tokens(item):
                        card[tok] = card.get(tok, 0.0) + weight
            self.cards.append(card)
            self.dont.append(counts(" ".join(field_text(entry, "dont_use"))))
        units = self.cards + self.dont
        n = max(len(units), 1)
        df: dict[str, int] = {}
        for unit in units:
            for tok in unit:
                df[tok] = df.get(tok, 0) + 1
        self.idf = {t: math.log(1 + (n - d + 0.5) / (d + 0.5)) for t, d in df.items()}
        card_df: dict[str, int] = {}
        for card in self.cards:
            for tok in card:
                card_df[tok] = card_df.get(tok, 0) + 1
        self.boilerplate = {t for t, d in card_df.items() if d > max(GENERIC_SHARE * len(self.cards), 5)}
        self.avg_card = sum(sum(c.values()) for c in self.cards) / max(len(self.cards), 1) or 1.0
        self.avg_dont = sum(sum(d.values()) for d in self.dont) / max(len(self.dont), 1) or 1.0

    def bm25(self, query: set[str], bag: dict, avg: float) -> tuple[float, list[str]]:
        length = sum(bag.values())
        score, hits = 0.0, []
        for tok in query:
            tf = bag.get(tok)
            if tf:
                score += self.idf.get(tok, 0.0) * tf * (K1 + 1) / (tf + K1 * (1 - B + B * length / avg))
                hits.append(tok)
        return score, hits

    def rank(self, task: str, keep_all: bool = False) -> list[dict]:
        query = set(counts(task))
        results = []
        for i, entry in enumerate(self.table):
            use, hits = self.bm25(query, self.cards[i], self.avg_card)
            dont, dont_hits = self.bm25(query, self.dont[i], self.avg_dont) if self.dont[i] else (0.0, [])
            against = DONT_WEIGHT * dont
            if use <= 0 and not keep_all:
                continue
            evidence = sorted(
                t for t in hits
                if t not in GENERIC and t not in self.boilerplate and self.idf.get(t, 0) > MIN_IDF
            )
            # One distinctive shared word is chance in a large library: not enough to
            # route on, but kept so a CHOOSE list can show the skill after better cards.
            single = evidence if len(evidence) == 1 else []
            if single:
                evidence = []
            results.append({
                "name": entry["name"],
                "score": round(use - against, 3),
                "use_score": round(use, 3),
                "dont_score": round(against, 3),
                "evidence": evidence,
                "single": single,
                "dont_hits": sorted(dont_hits),
                "entry": entry,
            })
        results.sort(key=lambda r: r["score"], reverse=True)
        return results


def reasons(entry: dict, hits: list[str], field: str, limit: int = 2) -> list[str]:
    """The lines of `field` that share the most matched tokens with the task."""
    want = set(hits)
    scored = []
    for line in entry.get(field, []):
        overlap = len(want & set(tokens(line)))
        if overlap:
            scored.append((overlap, line))
    scored.sort(key=lambda x: -x[0])
    return [shorten(line) for _, line in scored[:limit]]


def shorten(text: str, width: int = 160) -> str:
    text = " ".join(text.split())
    return text if len(text) <= width else text[: width - 1].rstrip() + "…"


def decide(results: list[dict], min_score: float, margin: float, lexical: bool = True) -> tuple[list[dict], list[dict], str]:
    """Split ranked results into (picks, set-aside, verdict).

    Boundary checks always apply. The evidence, score, and margin gates are
    lexical and are skipped once a rerank command has ordered the results.
    """
    picks, aside = [], []
    for r in results:
        if r["dont_score"] > r["use_score"] * 0.6 and r["dont_hits"]:
            r["why_not"] = "task matches its don't-use boundary"
            aside.append(r)
        elif not lexical:
            picks.append(r)
        elif not r["evidence"]:
            r["why_not"] = "only generic words matched"
            aside.append(r)
        elif r["score"] < min_score:
            r["why_not"] = "score below threshold"
            aside.append(r)
        else:
            picks.append(r)
    if not picks:
        return [], aside, "ABSTAIN"
    if not lexical:
        return picks, aside, "ROUTE"
    top = picks[0]["score"]
    kept = [r for r in picks if r["score"] >= top * margin]
    for r in picks:
        if r not in kept:
            r["why_not"] = "well behind the top pick"
    aside = [r for r in picks if r not in kept] + aside
    return kept, aside, "ROUTE"


# ---------------------------------------------------------------- rerank hook


def rerank(command: str, task: str, results: list[dict], timeout: float) -> tuple[list[dict], str]:
    import shlex  # loaded only when a second stage is configured
    import subprocess

    candidates = [
        {
            "name": r["name"],
            "description": r["entry"]["description"],
            "use_when": r["entry"]["use_when"][:6],
            "dont_use": r["entry"]["dont_use"][:6],
            "bm25": r["score"],
        }
        for r in results
    ]
    try:
        proc = subprocess.run(
            shlex.split(command),
            input=json.dumps({"task": task, "candidates": candidates}),
            capture_output=True, text=True, timeout=timeout, check=True,
        )
        reply = json.loads(proc.stdout)
    except (subprocess.SubprocessError, OSError, ValueError) as exc:
        return results, f"rerank failed ({type(exc).__name__}); BM25 order kept"
    by_name = {r["name"]: r for r in results}
    try:
        return read_reply(reply, results, by_name)
    except (AttributeError, KeyError, TypeError, ValueError):
        return results, "rerank returned nothing usable; BM25 order kept"


def read_reply(reply, results: list[dict], by_name: dict) -> tuple[list[dict], str]:
    if not isinstance(reply, dict):
        raise TypeError("reply is not an object")
    if "pick" in reply:
        pick = reply["pick"]
        if pick is None:
            return [], "rerank abstained"
        if pick in by_name:
            by_name[pick]["named"] = True
            return [by_name[pick]] + [r for r in results if r["name"] != pick], "rerank picked"
        return results, "rerank picked an unknown skill; BM25 order kept"
    ranking = [x for x in reply.get("ranking", []) if x.get("name") in by_name]
    if not ranking:
        return results, "rerank returned nothing usable; BM25 order kept"
    order = [by_name[x["name"]] for x in sorted(ranking, key=lambda x: -float(x.get("score", 0)))]
    for r in order:
        r["named"] = True
    return order + [r for r in results if r not in order], "rerank ordered"


# ---------------------------------------------------------------- commands


def confident(picks: list[dict], results: list[dict]) -> bool:
    """One lexical pick that clearly leads, with no near-miss boundary hit."""
    if len(picks) != 1 or picks[0]["dont_hits"]:
        return False
    rest = [r["score"] for r in results if r is not picks[0]]
    return not rest or rest[0] < picks[0]["score"] * 0.5


def route(table: list[dict], task: str, args, router: "Router | None" = None) -> dict:
    """Route one task; eval passes one shared `router` for the whole library."""
    router = router or Router(table)
    results = router.rank(task)
    picks, aside, verdict = decide(results, args.min_score, args.margin)
    stage = "bm25"
    command = args.rerank or os.environ.get("SKILL_ROUTER_RERANK")
    pool = [] if not command else router.rank(task, keep_all=True) if args.pool <= 0 else results[: args.pool]
    if pool and (args.rerank_when == "always" or not confident(picks, results)):
        lexical_picks = {r["name"] for r in picks}
        head, stage = rerank(command, task, pool, args.timeout)
        if stage == "rerank abstained":
            return {"verdict": "ABSTAIN", "stage": stage, "picks": [], "set_aside": []}
        if stage.startswith("rerank ") and "kept" not in stage:
            # The model's order replaces the lexical score and margin, not the boundary checks.
            names = {r["name"] for r in head}
            reordered = head + [r for r in results if r["name"] not in names]
            for r in reordered:
                r.pop("why_not", None)
            picks, aside, verdict = decide(reordered, 0.0, 0.0, lexical=False)
            # The model vouches only for skills it named; the rest keep their lexical verdict.
            kept = [r for r in picks if r.get("named") or r["name"] in lexical_picks]
            for r in picks:
                if r not in kept:
                    r["why_not"] = "not named by the rerank stage"
            aside = [r for r in picks if r not in kept] + aside
            picks = kept
            if not picks:
                verdict = "ABSTAIN"
    limit = args.top
    lexical_only = stage == "bm25" or "kept" in stage  # no second stage ran, or it failed and BM25 stands
    if lexical_only and verdict == "ROUTE" and not confident(picks, results):
        # No clear pick: hand the caller a short list of cards to choose from. Skills
        # set aside by a boundary or by the score floor stay out. A skill resting on one
        # distinctive word may fill a card, after every better-supported one.
        behind = [r for r in aside if r["why_not"] == "well behind the top pick"]
        thin = [r for r in aside if r["why_not"] == "only generic words matched" and r["single"]]
        picks = picks + behind + thin
        # The less the scores separate, the more cards: keep every card within
        # --ratio of the top score, at least two, at most --shortlist.
        top = picks[0]["score"]
        picks = [r for i, r in enumerate(picks) if i < 2 or r["score"] >= top * args.ratio]
        aside = [r for r in aside if r not in behind and r not in thin]
        aside = [r for r in behind + thin if r not in picks] + aside
        verdict, limit = "CHOOSE", args.shortlist
    aside = aside + picks[limit:]
    seen = {name for names in args.seen or [] for name in names.split(",") if name}
    return {
        "verdict": verdict,
        "stage": stage,
        "picks": [card(r, verdict, r["name"] in seen) for r in picks[:limit]],
        "set_aside": [
            {"name": r["name"], "score": r["score"], "why_not": r.get("why_not", "beyond the list size"),
             "boundary": reasons(r["entry"], r["dont_hits"], "dont_use", 1)}
            for r in aside[:3]
        ],
    }


def card(r: dict, verdict: str, seen: bool) -> dict:
    """One skill as the caller sees it. A skill it has already seen keeps only the lines about this task."""
    entry = r["entry"]
    out = {
        "name": r["name"],
        "score": r["score"],
        "because": reasons(entry, r["evidence"], "use_when") or [shorten(entry["description"])],
        "mind": reasons(entry, r["evidence"] + r["dont_hits"], "dont_use", 1),
    }
    if seen:
        out["seen"] = True
        return out
    out["path"] = entry["path"]
    if verdict == "CHOOSE":
        # The caller decides here, so it gets the description and, failing a matched boundary,
        # the description's own "not for" part: the line that separates near neighbours.
        about = shorten(entry["description"], 240)
        if about not in out["because"]:
            out["description"] = about
        out["mind"] = out["mind"] or [shorten(x) for x in split_description(entry["description"])[1]]
    return out


def print_brief(task: str, result: dict) -> None:
    print(f"task: {shorten(task, 120)}")
    print(f"verdict: {result['verdict']}  (stage: {result['stage']})")
    if not result["picks"]:
        print("no skill fits; proceed without one")
    if result["verdict"] == "CHOOSE":
        print("no clear pick; choose one, several, or none of these")
    for i, pick in enumerate(result["picks"], 1):
        role = "candidate" if result["verdict"] == "CHOOSE" else "read first" if i == 1 else "also relevant"
        print(f"\n{i}. {pick['name']} — {role}  [{pick['score']}]" + ("  (seen)" if pick.get("seen") else ""))
        if "description" in pick:
            print(f"   about: {pick['description']}")
        if "path" in pick:
            print(f"   load: {pick['path']}")
        for line in pick["because"]:
            print(f"   because: {line}")
        for line in pick["mind"]:
            print(f"   mind the boundary: {line}")
    if result["set_aside"]:
        print("\nset aside:")
        for r in result["set_aside"]:
            extra = f" — {r['boundary'][0]}" if r["boundary"] else ""
            print(f"   {r['name']} [{r['score']}]: {r['why_not']}{extra}")


def cmd_table(args) -> int:
    table = load_table(args)
    if args.format == "json":
        json.dump(table, sys.stdout, indent=2, ensure_ascii=False)
        print()
        return 0
    print("| skill | use when | don't use |")
    print("| --- | --- | --- |")
    for e in table:
        use = "; ".join(shorten(x, 90) for x in e["use_when"][:3]).replace("|", "\\|")
        dont = "; ".join(shorten(x, 90) for x in e["dont_use"][:3]).replace("|", "\\|")
        print(f"| {e['name']} | {use} | {dont or '—'} |")
    return 0


def cmd_route(args) -> int:
    task = " ".join(args.task) if args.task else sys.stdin.read()
    result = route(load_table(args), task, args)
    if args.json:
        json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
        print()
    else:
        print_brief(task, result)
    return 0


def cmd_eval(args) -> int:
    table = load_table(args)
    router = Router(table)  # routing never sees the queries, so nothing needs leaving out
    top1 = listed = pos = rejected = neg = cards = 0
    misses, verdicts = [], {}
    for entry in table:
        should, should_not = load_queries(entry["path"])
        for query, expected in [(q, True) for q in should] + [(q, False) for q in should_not]:
            result = route(table, query, args, router=router)
            names = [p["name"] for p in result["picks"]]
            cards += len(names)
            verdicts[result["verdict"]] = verdicts.get(result["verdict"], 0) + 1
            if expected:
                pos += 1
                top1 += names[:1] == [entry["name"]]
                listed += entry["name"] in names
                ok = names[:1] == [entry["name"]]
            else:
                neg += 1
                ok = entry["name"] not in names
                rejected += ok
            if not ok:
                misses.append((entry["name"], expected, names, query))
    print(f"skills: {len(table)}   queries: {pos} should-trigger, {neg} should-not")
    if pos:
        print(f"should-trigger, owning skill read first:  {top1}/{pos} ({top1 / pos:.0%})")
        print(f"should-trigger, owning skill listed:      {listed}/{pos} ({listed / pos:.0%})")
    if neg:
        print(f"should-not, owning skill kept out:        {rejected}/{neg} ({rejected / neg:.0%})")
    print("verdicts: " + ", ".join(f"{v} {n}" for v, n in sorted(verdicts.items())))
    if pos + neg:
        print(f"skills returned per query: {cards / (pos + neg):.2f}")
    if args.verbose:
        lost: dict[tuple[str, str], int] = {}
        for name, expected, names, _ in misses:
            if expected and names:
                lost[(name, names[0])] = lost.get((name, names[0]), 0) + 1
        if lost:
            print("collisions (owner -> skill read first instead):")
            for (owner, winner), n in sorted(lost.items(), key=lambda x: -x[1])[:15]:
                print(f"  {n:3d}  {owner} -> {winner}")
        for name, expected, names, query in misses:
            want = "want first" if expected else "want absent"
            print(f"  MISS {name} ({want}) got {names or 'ABSTAIN'}: {shorten(query, 100)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)

    def roots(p):
        p.add_argument("--skills", dest="roots", type=Path, action="append",
                       help="skill root (a skill folder, or a directory with skill folders below it); repeatable")
        p.add_argument("--from", dest="origin", type=Path,
                       help="work location: find .<tool>/skills and .<tool>/available-skills here, above, and at home")

    def tuning(p):
        p.add_argument("--top", type=int, default=3, help="max skills to return when one clearly leads")
        p.add_argument("--shortlist", type=int, default=5, help="max cards to return when no skill clearly leads")
        p.add_argument("--ratio", type=float, default=0.6,
                       help="when no skill clearly leads, list cards scoring at least this share of the top (at least two)")
        p.add_argument("--seen", action="append",
                       help="comma-separated skills already in the caller's context; listed without their details")
        p.add_argument("--min-score", type=float, default=3.0, help="abstain below this BM25 score")
        p.add_argument("--margin", type=float, default=0.6, help="keep picks scoring at least this share of the top")
        p.add_argument("--rerank", help="local command for the second stage (default: $SKILL_ROUTER_RERANK)")
        p.add_argument("--pool", type=int, default=8, help="candidates sent to the rerank command; 0 sends every skill")
        p.add_argument("--rerank-when", choices=["uncertain", "always"], default="uncertain",
                       help="call the rerank command only when BM25 lacks one clear pick (default), or on every task")
        p.add_argument("--timeout", type=float, default=2.0, help="rerank timeout in seconds")

    p = sub.add_parser("table", help="print the extended skill table")
    roots(p)
    p.add_argument("--format", choices=["markdown", "json"], default="markdown")
    p.set_defaults(func=cmd_table)

    p = sub.add_parser("route", help="pick skills for a task brief (argument or stdin)")
    roots(p)
    tuning(p)
    p.add_argument("--json", action="store_true")
    p.add_argument("task", nargs="*")
    p.set_defaults(func=cmd_route)

    p = sub.add_parser("eval", help="replay shipped evals/eval_queries.jsonl against the router")
    roots(p)
    tuning(p)
    p.add_argument("-v", "--verbose", action="store_true")
    p.set_defaults(func=cmd_eval)

    args = parser.parse_args()
    if not args.roots and not args.origin:
        parser.error("pass --from <work location>, --skills <root>, or both")
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
