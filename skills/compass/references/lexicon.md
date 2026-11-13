# Maintain the lexicon

`{compass-skill}` is this installed skill directory; `{chart-root}` is the
host-declared chart root. `{chart-root}/LEXICON.jsonl` contains one JSON object
per line, written and read through [`compass_lex.py`](../scripts/compass_lex.py).
It translates recorded names for the same concept between human vocabulary,
source identifiers, and chart or repository locations.

`GLOSSARY.md` owns contextual meaning; `DOMAIN.md` owns relationships. A tool,
provider, library, or mechanism used by a concept is not another name for it.
The lexicon never converts a dependency into an alias. Routine lookup, query
rewriting, and bulk consultation are in
[`SKILL.md`](../SKILL.md#consume-search-rewrite-then-consult).

## Schema

These synthetic examples illustrate the supported row shapes:

```jsonl
{"concept":"shipment","root":"shipping","speech":["Shipment","consignment"],"code":["consignment"],"chart":"shipping.dispatch"}
{"concept":"purchase-order","speech":["Purchase Order","PO"],"code":["po"],"scope":["src/purchasing/"]}
{"concept":"exchange-rate-feed","speech":["Exchange Rate Feed"],"code":[],"where":"the rate provider's repository"}
{"concept":"account","root":"commerce","context":"billing","speech":["Account"],"code":["ledger-account"],"chart":"commerce.billing"}
{"concept":"account","root":"commerce","context":"identity","speech":["Account"],"code":["login-account"],"chart":"commerce.identity"}
```

| Field | Required | Holds |
| --- | --- | --- |
| `concept` | yes | Lowercase-hyphen slug; unique within `(root, context)` |
| `root` | no | The chart root the row speaks for; absent means chart-wide. A `chart` address starts with this root when present. |
| `context` | no | Lowercase-hyphen anchor of a bounded-context heading in that root's `DOMAIN.md`; requires `root`. Use an established domain context, never a new root invented to avoid ambiguity. |
| `speech` | yes | Observed human forms; first is canonical and matches the glossary heading when linked. A form belongs to one concept within `(root, context)`. |
| `code` | yes; may be empty on a `where` row | Lowercase-hyphen split stems, such as `consignment` or `purchase-order`, rather than complete source symbols. Each occurs in source under the row's scopes, or repository-wide when no scopes are declared. A stem belongs to one concept within `(root, context)`. |
| Exactly one of `chart`, `scope`, `where` | yes | `chart`: an address whose document supplies implementation scopes; `scope`: repository-relative paths; `where`: a pointer outside the repository, never searched by the helper. |
| `note` | no | At most 25 words of disambiguation, without a definition or a copy of glossary meaning. |

Rows without `context` keep their existing interpretation. When forms collide
across roots or contexts, lookup returns the alternatives; `--root` and
`--context` narrow only what task evidence has already identified. A context
label is not proof that two uses share a meaning. Definitions stay with their
separate glossary contexts.

Other fields are rejected. No field contains a `compass:` or
`compass-abstraction:` literal: the chart check counts those markers, and a row
is not a source claim. Rows sort by `(root, context, concept)`; `add` rewrites
the complete file. Hand editing is only for deleting a row; `sort` repairs order.

Recorded source stems match compact, spaced, hyphenated, and CamelCase forms
at identifier boundaries. For example, `purchase-order` can match the stem in
`PurchaseOrderClient`. This normalization does not infer an abbreviation or
match arbitrary substrings inside a different identifier.

## Admission

Admission is its own Create task, never a side effect of Consume or the task
that noticed a missing form. Record candidates in the task's PR, issue, or task
record. Phase A completes with candidates recorded, not rows admitted.

Before admission, record observed usage, the proposed contextual meaning, and
why each form names that same concept. Compare human-facing language with the
source use. Present uncertain meanings and alias claims to the domain expert
at the applicable human checkpoint. A shared folder, a dependency, or a code
stem's existence does not establish synonymy. Keep that evidence in the task
record; the lexicon carries only validated forms and locators.

A term can need a glossary definition without needing a lexicon row. The
mechanical gap gate admits forms that lexical search cannot connect, or
collisions that must remain distinct. It cannot prove meaning or authentic
usage. A reachable form such as `ShipmentRecord` for **Shipment** needs no row.

Run from the repository root, or pass `--repo-root`; the chart root must be
inside it:

```sh
python3 "{compass-skill}/scripts/compass_lex.py" \
  --chart-root "{chart-root}" add --stdin --dry-run < candidates.jsonl
```

This validates the entire candidate batch without writing. Rerun without
`--dry-run` to admit it atomically: one rejected row leaves the file unchanged.
Addresses resolve under their declared roots, scope paths exist, source stems
are live, and the merged file passes the same glossary-link and canonical-form
checks as `check` before it is written. The gap gate requires at least one
form with no token overlap in another naming language; `PO` versus a
purchase-order location is a synthetic example. A row whose every form is
already connected is rejected with the overlapping token sets. A collision
across roots or contexts is also a gain; admit the alternatives together.

When a candidate has a glossary definition, give that term a `### Lexicon`
section naming its concept slug. The heading remains the first `speech` form.
Replace any `### Implementation aliases` section: storing the same forms in
the glossary and lexicon creates two owners. Context-specific senses keep their
separate labelled meanings and corresponding contextual rows.

## The installed check

Install the check before the first row is admitted. Adding or changing it in
the host test suite is ask-first under `create.md` §Boundaries. The host invokes
the script by the same installed skill path the usage hook uses; it does not
copy the script:

```sh
python3 "{compass-skill}/scripts/compass_lex.py" \
  --chart-root "{chart-root}" --repo-root "{repo-root}" check
```

The check validates order, scoped uniqueness, row shape, addresses, scopes,
live stems, lexical gaps or collisions, glossary links and canonical forms,
and the absence of `### Implementation aliases`. It exits 1 on any finding.
A stale stem is an implementation-remapping finding to classify before editing.
A green result proves these mechanical properties, not same-concept meaning;
the semantic admission review and periodic vocabulary spot check own that.

Use `list` to inspect rows and `reverse` to trace symbols or locations back to
forms. Lookup can report a row with a stale stem or dangling address; the host
check owns those failures. Consult the complete glossary meaning before using
a name in a different context. Renames and deprecations retain the applicable
human decision and disagreement-classification boundaries.
