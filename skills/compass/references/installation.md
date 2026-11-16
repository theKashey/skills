# Install Compass

Install the [usage hook](agent-hook.md) in the host file that declares its chart
root when Phase B closes ([growth-and-drift.md](growth-and-drift.md)). Ask for
host approval before writing it, substitute the installed skill and declared
chart-root paths, and preserve the local-work exclusion. A host without a
chart starts at Phase 0; installation never invents a chart location.

Install the chart check in the host's test suite (`verification.md` §First)
and, before admitting a lexicon, the lexicon check (`lexicon.md` §The installed
check), both ask-first. The host invokes the lexicon helper from its installed
skill path rather than copying it. Verify these paths from the host repository
root, or supply `--repo-root` to lexicon admission and checking.

## Teach query rewriting

The installed hook must reach the routine Consume procedure in `SKILL.md`.
That procedure searches the original task terms first and consults contextual
meaning before using a rewritten candidate. A lexical miss is not proof that
the chart lacks the concept.

For example, in a synthetic shipping project where **Shipment** and
`consignment` name the same thing:

```sh
python3 "{compass-skill}/scripts/compass_search.py" \
  --chart-root "{chart-root}" "consignment timeout after cancellation"
python3 "{compass-skill}/scripts/compass_lex.py" \
  --chart-root "{chart-root}" rewrite --root shipping --json \
  "consignment timeout after cancellation"
```

How a consumer reads the candidates, uses them only after a strict miss,
resolves a word such as **Account** with distinct billing and identity meanings,
and records unresolved shorthand is owned by `SKILL.md` §Consume and §Read
contextual meanings; the hook points there rather than restating it. Lookup and
rewriting grant no authority to edit chart or host files.

## Batch independent questions

`resolve`, `rewrite`, and `reverse` accept JSONL on `--stdin`, reusing one loaded
lexicon. Supply `query` for resolve/rewrite or `target` for reverse, with optional
`id`, `root`, and `context` on each record. For example, a query file can contain:

```jsonl
{"id":"shipment","query":"consignment timeout after cancellation","root":"shipping"}
{"id":"account","query":"account mismatch","root":"commerce"}
```

```sh
python3 "{compass-skill}/scripts/compass_lex.py" \
  --chart-root "{chart-root}" rewrite --stdin < queries.jsonl
```

Per-record statuses, exit codes, omitted-candidate notices, and batch glossary
search with `compass_search.py --kind glossary --stdin` follow `SKILL.md`
§Batch independent lookups and §Read contextual meanings.

## Verify the host routes

Add these review checks, ask-first, to the review file the host's root
instructions point to; if none is named, ask where they belong:

- **Updated when needed.** A change that alters what the chart describes
  updates it through Create work, or records a classified disagreement in the
  PR, issue, or task record (`growth-and-drift.md` §Classifying Disagreement).
- **Consulted when needed** (optional). Non-local work shows chart consultation
  through the installed hook.

Verify the hook and chart check through the `verification.md` §L2 rows and the
lexicon check through a passing host suite. Exercise a canonical term, a
recorded alias, a miss, and an ambiguous term when the host has one. Check that
a rewrite preserves task qualifiers and contextual alternatives and that a
batch retains each result's identity. A host without ambiguous terms need not
invent one for installation. Confirm that review guidance arrives through the
host's established review path.

Agree a vocabulary-review cadence with the host's maintainer and domain expert
using the existing periodic spot check (`verification.md` §Spot Check). Review
observed usage, changed meanings, and evidenced terminology deprecations under
the normal human checkpoints. Event-driven chart maintenance continues; this
does not install an automation or create a second glossary owner.
