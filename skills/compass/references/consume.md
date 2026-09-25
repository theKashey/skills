# Consume a Compass chart

Use an existing chart for non-local work without changing Compass-owned or
installed state. `{chart-root}` is declared by the host project;
`{compass-skill}` is this installed skill directory.

The chart describes the logical system. Code is one realization. Treat a
mismatch as mapping evidence until it is classified.

## Search, then consult

Search before broad chart reading, using task terms without narrowing the kind:

```sh
python3 "{compass-skill}/scripts/compass_search.py" \
  --chart-root "{chart-root}" "{task terms}"
```

Read address, exact, heading, and literal matches first. Treat BM25-related
matches as leads, not semantic proof. The `Named nowhere in the chart` line
lists the task words no chart heading, slug, or identifier names. When
`{chart-root}/LEXICON.jsonl` exists, translate before reading the gap as
missing content:

```bash
python3 "{compass-skill}/scripts/compass_lex.py" \
  --chart-root "{chart-root}" resolve "{task sentence}"
```

Search again with the strict tokens it prints; use the disclosed expansion
only when strict misses, and say so. A `looks like shorthand with no row`
line is a finding for the task record, not a word to guess at. Without a
lexicon, search the task words with `--kind glossary`; the terms its exact and
BM25-related sections name are the glossary's own, and you search again with
those. When the glossary search on the task words, and any search on the
terms it named, matches nothing, take the bold terms and headings from
the `DOMAIN.md` of each root `COMPASS.md` lists, and search with them. A task
word still named nowhere is a vocabulary finding for the task record.

Consult the matched owning sections, then traverse the implicated
branch — the root, block, and component the matches name — through every
chart level present:

```text
{chart-root}/README.md → COMPASS.md → {root}/README.md
  → DOMAIN.md → CONTAINERS.md
  → {block}/README.md → {component}/README.md
  → VIEWPORTS.md, when it exists
```

Do not skip a present level. Search narrows the branch and candidate sections;
it does not replace semantic context. If output reports omitted lines in a
section outside `GLOSSARY.md`, open that owning section before deciding.

`GLOSSARY.md` is not a level you open. Read it one term at a time, through the
search, for each bold term in a section you consulted and each task word the
chart names:

```sh
python3 "{compass-skill}/scripts/compass_search.py" \
  --chart-root "{chart-root}" --kind glossary "{term}"
```

A term section comes back with its bounded context and lexicon link, up to
`--max-lines`. When any result from `GLOSSARY.md`, from any search, reports
omitted section lines, search that section's heading term with
`--kind glossary` and a larger `--max-lines`; when a `--kind glossary` search
reports sections omitted by `--limit`, raise `--limit`.
Do not open the file to finish either.

For a new capability, also search `ABSTRACTIONS.md` with capability terms when
the file exists. On a match, read
[Consume named abstractions](consume-named-abstractions.md) before writing.

You are oriented when you can state the task semantically, name every affected
component and crossed boundary, identify existing behavior or abstractions the
change could duplicate, and classify every chart/code disagreement.

## Load only the applicable detail

- For a narrower kind, different output bounds, or glossary interpretation, read
  [Search and interpret chart content](consume-search.md).
- To go from a symbol, path, or address back to what people call it, or to
  read what `resolve` prints, read [The Lexicon](lexicon.md) §Reading it.
- For code rationale, a component, or cross-block debugging, read
  [Investigate through a Compass chart](consume-investigation.md).
- For estimation, review, refactoring, overreach, or architectural pull, read
  [Assess a change through a Compass chart](consume-change.md).
- If a named-abstraction marker or definition affects the task, read
  [Consume named abstractions](consume-named-abstractions.md).

## Classify and stop

Classify a mismatch as **semantic change**, **implementation remapping**, or
**implementation violation**. Record the finding, reproduction details, and any
implementation plan in the task's PR, issue, or task record. Do not edit the
chart during Consume; chart changes are separate Create work.

## What the chart does not answer

The chart answers semantic responsibility, boundaries, relationships, and
intent. It does not own implementation mechanism, performance evidence, test
strategy, business requirements, or repository layout. Record deployment
topology only when a viewport question requires it; it never defines roots or
blocks.
