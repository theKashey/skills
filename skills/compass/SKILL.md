---
name: compass
description: Use when creating or consuming a Compass semantic architecture chart for non-local work; not for reader-facing docs, local code-only work, or implementation instructions.
---

# Compass

## Shared contract

Compass describes the logical system, not the repository that currently
implements it. Use it for non-local work that crosses a boundary, changes a
rule, adds a party, or asks whether something belongs. Building a new
capability is non-local even when it lands in one file. For a one-file fix,
rename, or line-specific bug, read the code instead.

Read the chart root declared by the host project's agent instructions before
using either flow. If none is declared, ask the user to configure one; never
invent a chart location.

Repository structure and executable code are evidence, not sole authority over
semantic identity. A `compass: <address>` coordinate locates implementation in
the chart; it does not define the semantic boundary. When chart and code
disagree, classify the finding as semantic change, implementation remapping, or
implementation violation before deciding what should change.

For inherited coordinates, the addressed document's `## Implementation
coordinates` records `carrier-path` covers `subtree-path/`, using backticked
repository-relative paths. The carrier must be an existing source file inside
that subtree and contain the document's address; only that address gains the
declared scope. Without that declaration a marker covers
only its file; a filename such as `index.ts` implies no scope. Resolve each
root independently: a file's explicit addresses for that root override inherited
ones; otherwise use the deepest declared covering subtree. Multiple carriers
at that subtree must agree on the address set for that root. Missing carriers
or conflicting declarations are remapping findings, not permission to guess.

## Choose exactly one flow

Select one flow before loading any reference. Do not combine the flows in one
task.

- **Create** — the task establishes or changes Compass-owned state: chart files,
  semantic entities, coordinates, viewports, lexicon rows, the host usage
  hook or installed checks, or named-abstraction definitions and claims. Maintenance, remapping,
  retirement, and completion verification are Create work. Read
  [references/create.md](references/create.md). Do not run the Consume procedure.
  Installing Compass in a host, or verifying that installation, is Create
  work too; read [references/installation.md](references/installation.md) for
  that and nothing else.
- **Consume** — the task reads and applies an existing chart without changing
  Compass-owned or Compass-installed state. Follow the procedure below; do not
  load Create references.

If Consume reveals missing, stale, or disputed chart content, classify it and
record it where the task's own evidence lives — the PR, issue, or task record —
then stop the Compass flow. That record is the task's, not Compass-owned state,
so writing there is not a Create action. A finding that exists only in the
conversation has no owner and is lost with the turn. Changing it is a separate
Create task with its own authority and checks. If a task requests both
outcomes, separate them into distinct tasks; never drift from Consume into
Create.

## Consume: search, rewrite, then consult

`{chart-root}` is the host-declared chart root; `{compass-skill}` is this
installed skill directory. Search the original task terms before broad chart
reading, without narrowing the kind:

```sh
python3 "{compass-skill}/scripts/compass_search.py" \
  --chart-root "{chart-root}" "{task terms}"
```

Read address, exact, heading, and literal matches first. BM25-related matches
are leads, not semantic proof. `Named nowhere in the chart` lists task words
that no heading, slug, or identifier names; it does not prove content is absent.

When `{chart-root}/LEXICON.jsonl` exists, use its recorded forms before treating
that vocabulary gap as missing chart content:

```sh
python3 "{compass-skill}/scripts/compass_lex.py" \
  --chart-root "{chart-root}" rewrite --json "{task sentence}"
```

Keep the original query and strict tokens. Each result candidate separates a
`chart_query` using domain terms from `code_queries` using recorded source forms
and scopes, grouped by concept and context. Rewriting preserves unmatched task
terms. Search alternatives separately rather than concatenating synonyms into one
query. Use a rewritten candidate only when the strict search misses, and
disclose the rewrite. A hit translates a recorded form; it does not establish
that the task has the same meaning.

If the result is ambiguous, consult the glossary meanings and task evidence;
use `--root` and `--context` only when that evidence identifies the scope.
Never combine alternative meanings or invent a root to disambiguate. Unknown
shorthand is a candidate for the task record, not an expansion to guess.
`resolve` reports contextual forms, locators, and query alternatives. To translate
a source symbol, repository path, or chart address back to human terminology,
use `reverse "{target}"`; a bare root needs `reverse --as chart "{root}"`.
These lookups are read-only. Exit 0 means a hit or ambiguity, 1 a miss or no
lexicon, and 2 an invalid input or chart root.

Rewriting returns at most 32 contextual interpretations and 32 source-query
variants per interpretation. When `candidates_omitted` or a candidate's
`code_queries_omitted` is nonzero, narrow the query or its evidenced root/context
rather than treating the bounded output as complete.

Without a lexicon, search task words with `--kind glossary`, then search again
with the terms those exact or BM25-related results name. If neither lookup
matches, use the bold terms and headings in the `DOMAIN.md` of each root that
`COMPASS.md` lists. A task word still named nowhere is a vocabulary finding
for the task record.

### Batch independent lookups

Use one process for independent queries. Lexicon `resolve`, `rewrite`, and
`reverse` accept `--stdin`; each input line is a JSON object with an optional
`id`, optional `root` and `context`, and `query` (resolve/rewrite) or `target`
(reverse):

```sh
python3 "{compass-skill}/scripts/compass_lex.py" \
  --chart-root "{chart-root}" rewrite --stdin < queries.jsonl
```

Output is one JSON result per input in order, with its ID and `hit`, `miss`,
`ambiguous`, or `error` status. An invalid record makes the batch exit 2;
otherwise any hit or ambiguity exits 0, and all misses exit 1. An empty batch
is invalid. Inspect each result; an aggregate success does not make every
query a hit. No batch lookup changes chart or source files.

### Interpret and bound search output

Search reads live Markdown without an index or cache. Each result gives its
chart-relative file, heading ancestry, match signal, and line-numbered excerpt.
A dotted address resolves to the addressed identity document first; exact
heading, entity-slug, or identifier matches come next (`term=` names the matched
phrase), then matches in the section's own heading, then literal text. BM25
reranks within direct-match tiers and may add lexical leads; its score is not
confidence, typo recovery, semantic similarity, or completeness. An unresolved
address is a finding to classify.

Use `--kind` when the chart role is known; it may be repeated. `--literal-only`
omits related candidates. Defaults are 10 sections and 48 Markdown lines per
section; `--limit` and `--max-lines` change those bounds. Search exits 0 for
results, 1 for no results, and 2 for invalid input or chart root. Use `--help`
for the option list.

Consult the matched owning sections, then traverse the implicated branch
through every chart level present:

```text
{chart-root}/README.md → COMPASS.md → {root}/README.md
  → DOMAIN.md → CONTAINERS.md
  → {block}/README.md → {component}/README.md
  → VIEWPORTS.md, when it exists
```

Do not skip a present level. Search narrows the branch; it does not replace
semantic context. When a section outside `GLOSSARY.md` reports omitted lines,
open that owning section before deciding.

### Read contextual meanings

`GLOSSARY.md` is not a zoom level. Read complete term sections, including their
bounded contexts, product appearances, and lexicon links, for each bold term in
a consulted section and each task word the chart names:

```sh
python3 "{compass-skill}/scripts/compass_search.py" \
  --chart-root "{chart-root}" --kind glossary "{term}"
```

For several terms, pass JSONL records with `query` and optional `id` to the
same command with `--stdin` instead of a positional query. It parses the chart
once and returns one JSON result per input; the result text retains omitted
section and line notices. Shared search flags apply to every input. Batch
exit codes follow the same any-result/all-miss/invalid-input rule above.

For an omitted glossary section tail, search its heading term with
`--kind glossary` and a larger `--max-lines`; when `--limit` omits sections,
raise it. This applies to glossary results from any search. Do not open the
whole glossary to finish either. Read the owning `DOMAIN.md` for relationships
and invariants. Use the canonical term for the relevant context in chart prose,
commit messages, and discussions of intent; preserve the separate source form
when discussing an identifier.

For a new capability, also search `ABSTRACTIONS.md` with capability terms when
the file exists. On a match, read the named-abstraction path below before
writing. You are oriented when you can state the task semantically, name every
affected component and crossed boundary, identify behavior or abstractions the
change could duplicate, and classify every chart/code disagreement.

### Load only the applicable detail

- For code rationale, a component, or cross-block debugging, read
  [Investigate through a Compass chart](references/consume-investigation.md).
- For estimation, review, refactoring, overreach, or architectural pull, read
  [Assess a change through a Compass chart](references/consume-change.md).
- When a named-abstraction marker or definition affects the task, read
  [Consume named abstractions](references/consume-named-abstractions.md).
- For overreach or level-contamination warning signs, read
  [Structural signals](references/structural-signals.md); these are leads.

### Classify and stop

Record a mismatch as **semantic change**, **implementation remapping**, or
**implementation violation**, with reproduction details and any implementation
plan in the task's PR, issue, or task record. Chart changes require separate
Create work under the flow boundary above.

### What the chart does not answer

The chart answers semantic responsibility, boundaries, relationships, and
intent. It does not own implementation mechanism, performance evidence, test
strategy, business requirements, or repository layout. Deployment topology
belongs only where a viewport question requires it; it never defines roots
or blocks.
