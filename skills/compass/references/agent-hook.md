## Compass chart

For non-local work—crossing a boundary, changing a rule or invariant, adding a party, asking whether something belongs, or building any capability—search first: `python3 "{compass-skill}/scripts/compass_search.py" --chart-root "{chart-root}" "{task terms}"`.
Before treating vocabulary as missing, use an existing lexicon: `python3 "{compass-skill}/scripts/compass_lex.py" --chart-root "{chart-root}" rewrite --json "{task sentence}"`; consult ambiguous meanings, preserve task qualifiers, and use a disclosed candidate only when strict search misses. Use `--stdin` for independent JSONL lookups as Compass's main Consume procedure specifies.
Consult matched owning sections, then follow Compass's main Consume procedure through every chart level present; BM25-related results are leads, not semantic proof.
For a local one-file fix, rename, or line-specific bug, read code directly; Consume and query rewriting never authorize chart edits.
