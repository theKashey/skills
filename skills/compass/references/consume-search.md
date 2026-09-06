# Search and interpret chart content

Use this route when a query needs a narrower kind, different output bounds, or
glossary interpretation. `{chart-root}` is the directory declared by the host
project, and `{compass-skill}` is the installed Compass skill directory.

## Targeted lookup

Narrow a query when the chart role is known:

```sh
python3 "{compass-skill}/scripts/compass_search.py" \
  --chart-root "{chart-root}" --kind glossary "term or task words"
```

The helper reads live Markdown and writes no index or cache. Results carry a
chart-relative file, heading ancestry, line-numbered bounded excerpt, and match
signal. A dotted address resolves to the identity section of the document its
segments name and precedes every other tier; then a chart heading, entity slug,
or identifier matched by the query or a phrase inside it (`term=` shows which
phrase); then a section whose own heading contains the query; then literal
text. When query words match no heading, slug, or identifier, a line before
the results lists them as named nowhere — a vocabulary lead, not a miss. An address that resolves to no
document is noted on stderr as a finding to classify. BM25 reranks inside each
direct-match tier and may add lexically related sections; its score is not
confidence, semantic similarity, proof of relevance, typo recovery, or a
completeness claim.

Use `--literal-only` when related candidates would be noise. The default bound
is 10 sections and 48 Markdown lines from each owning section; `--limit` and
`--max-lines` change those bounds, and `--kind` may be repeated. Exit status is
0 for results, 1 for no results, and 2 for an invalid argument or chart root.
Use `--help` for the full option list.

Lookup changes neither the chart nor `compass-abstraction:` source incidence.

## Understand a term

1. Search with `--kind glossary`, then read the complete returned term section,
   including its bounded context, product appearance, and implementation aliases.
2. Open that root's `DOMAIN.md` for the context, concepts, invariants, and
   relationships.

If code uses a glossary alias, use the canonical glossary term in chart
documents, commit messages, and discussions of intent.
