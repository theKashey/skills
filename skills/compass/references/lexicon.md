# The Lexicon

Throughout, `{compass-skill}` is the directory this skill is installed in and
`{chart-root}` is the chart root the host declares. `{chart-root}/LEXICON.jsonl`
is a database, not a document: one JSON object per line, one row per concept,
written and read by [`scripts/compass_lex.py`](../scripts/compass_lex.py) and
by nothing else. It exists because three
languages that name the same thing share no vocabulary by default — what people
say (`WIV`, `QuickAction`, `AGG`), what identifiers say (`WIVService`,
`ActionDropdown`, nothing at all), and where the chart or repository keeps it
(`tracker.work-item-view`, `src/work-item/menu/`, a schema in another
repository). `compass_search.py` bridges the pairs that identifier splitting
already reaches: `work item` finds `WorkItemService` and `tracker.work-item`.
It cannot reach across an abbreviation or a rename, because those carry no
tokens to match. A lexicon row is exactly that missing hop, and nothing else:
a code name that differs from the product term but shares its tokens
(`MatterRecord` for **Matter**) is recorded nowhere, by design, because the
search already makes that hop.

`GLOSSARY.md` owns meaning; the lexicon owns forms. A row never says what a
concept is. A glossary term links to its row with `### Lexicon`, and the
glossary heading — the product or domain term — is the row's first `speech`
form. A glossary carries no `### Implementation aliases` section: `check`
fails one that does, because two owners of the same form diverge and the
divergent copy is the one an agent finds.

## Schema

```jsonl
{"concept":"work-item-view","speech":["Work Item","WIV","work item view"],"code":["wiv","work-item"],"chart":"tracker.work-item-view"}
{"concept":"quick-action","speech":["QuickAction","quick action"],"code":["action-dropdown"],"scope":["src/work-item/menu/"],"note":"a controller composing activities"}
{"concept":"atlassian-graphql-gateway","speech":["AGG","Atlassian GraphQL Gateway"],"code":["relay"],"where":"relay schema in the gateway repository; federation defined at repo-xyz"}
{"concept":"sense","root":"variance-authority","speech":["sense"],"code":["sense"],"chart":"variance-authority.sense"}
{"concept":"sense","root":"shadow","speech":["sense"],"code":["shadow-sense"],"chart":"shadow.shadow-sense"}
```

| Field | Required | Holds |
|---|---|---|
| `concept` | yes | lowercase-hyphen slug; unique per root |
| `root` | no | the root the row speaks for; absent means chart-wide. A `chart` address must start with this root. Same word, different roots: one row per root, admitted in the same batch, and `resolve` lists them all as a collision until `--root` picks one |
| `speech` | yes | every form a person says, first form canonical — the glossary heading when the row is linked. Within one root a form belongs to one concept |
| `code` | yes; may be empty on a `where` row | split stems as they occur inside identifiers — `wiv`, `action-dropdown` — never the symbol. Every stem must occur in some identifier under the row's scopes, or anywhere in the repository when the row has none; `check` fails a stem that no longer does. Within one root a stem belongs to one concept |
| locator: exactly one of `chart` / `scope` / `where` | yes | `chart`: an address; scopes come from that document's `## Implementation coordinates`. `scope`: repository-relative paths. `where`: a pointer outside the repository — the row's only search gain, and never searched itself |
| `note` | no | at most 25 words; disambiguation only, never meaning |

Any other field is rejected, which is how the schema stays fixed. No field may
contain a `compass:` or `compass-abstraction:` literal: the chart check counts
markers in every file, and a row is not a marker.

Rows sort by `(root, concept)` and the file is rewritten whole on every `add`.
Edit the file by hand only to delete a row; if the order breaks, `check` says
so and `sort` repairs it.

## Admission

Admission is Create work and runs as its own task — never as a side effect of
the task that noticed the gap, and never during Consume. When `resolve`
reports `looks like shorthand with no row`, record the word as a candidate in
the task's own record, ask what it means if someone can answer, and carry on
searching with the strict tokens; the candidate is the admission task's input.
L0 completes with candidates recorded, not with rows admitted.

Run from the repository root, or pass `--repo-root`; `add` and `check` refuse
a repository root that does not contain the chart root:

```bash
python3 "{compass-skill}/scripts/compass_lex.py" --chart-root "{chart-root}" \
  add --stdin --dry-run < candidates.jsonl
```

`--dry-run` reports what would be admitted and writes nothing; rerun without
it to write. A batch is gated as one unit against the whole file, with the same rules
`check` applies: one rejected row and nothing is written, and a written file
always passes `check`. The gate admits a row only when at least one of its
forms shares no token with one of the other two languages — `WIV` against
`tracker.work-item-view`, `QuickAction` against `src/work-item/menu/` — because
that hop is the only recall lexical search does not already have. A row whose
every form reaches every language restates the baseline and is refused with
the token sets that overlap. The one exception is a form another root claims:
the collision itself is the gain, and the rows are admitted together, in one
batch, since either alone is a restatement.

Before admitting, the row's address must resolve to a chart document under
its root, every scope must exist on disk, and every code stem must occur in
some identifier under the row's scopes. The rejection names which.

When a candidate has a glossary meaning, the admission task also gives the
term a `### Lexicon` section naming the slug, replacing any
`### Implementation aliases` it carried, so `check` can prove the link and
the canonical form.

## The installed check

Install the check before the first row is admitted; a lexicon without it is
unproven from the next rename onward. Installing or changing it in the host's
test suite is ask-first, like the chart check (`create.md` §Boundaries), but
unlike the chart check it is not copied: the host test invokes the script by
the same `{compass-skill}` path the usage hook uses, so there is no installed
copy to compare with a fence.

```bash
python3 "{compass-skill}/scripts/compass_lex.py" \
  --chart-root "{chart-root}" --repo-root "{repo-root}" check
```

It decides everything a script can decide about the file — order, duplicate
concepts and forms, dangling addresses, addresses outside their root, missing
scopes, stale stems, the gap gate, every `### Lexicon` link and its canonical
form, and the absence of `### Implementation aliases` — reports every failing
row, and exits 1 if any did. A stale stem is a finding to classify as
implementation remapping (`growth-and-drift.md` §Classifying disagreement)
before the row is edited.

## Reading it

```bash
python3 "{compass-skill}/scripts/compass_lex.py" --chart-root "{chart-root}" \
  resolve "There is a problem in WIV QuickAction around AGG"
python3 "{compass-skill}/scripts/compass_lex.py" --chart-root "{chart-root}" \
  reverse WIVService
```

`resolve` prints the strict tokens first, then each matched concept with its
forms and scopes, then a `collision:` line when one form matched rows of
several roots, then the unmatched words, then the disclosed expansion and the
`search in:` list. Search with the strict tokens; add the expansion only when
the strict search misses, and say the expansion was used. `reverse` takes a
symbol, a repository path, or an address and returns the concept and what
people call it; a bare root name needs `--as chart` and returns every row of that root. `list` renders the file
as a table; `--root` narrows `resolve` and `list`. Exit status is 0 for a hit,
1 for no hit or no lexicon, and 2 for an invalid argument, chart root, or a
row the file cannot load. A row only `check` catches — a stale stem, a
dangling address — does not stop translation; the installed check owns it.
None of the three commands writes.
