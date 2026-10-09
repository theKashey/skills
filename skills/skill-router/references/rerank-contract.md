# Rerank contract

The second stage is any local command. The router calls it only when the
lexical stage lacks one clear pick, unless `--rerank-when always` is set. If
the command fails, times out, prints invalid JSON, or names an unknown skill,
the router keeps the BM25 result and reports the failure in `stage`.

## Input on stdin

```json
{
  "task": "the brief",
  "candidates": [
    {
      "name": "skill-name",
      "description": "frontmatter description",
      "use_when": ["up to six lines"],
      "dont_use": ["up to six lines"],
      "bm25": 12.4
    }
  ]
}
```

Candidates arrive in BM25 order. `--pool N` sets how many are sent (default
8); `--pool 0` sends every skill in the library, including skills with a BM25
score of 0. Use `--pool 0` when the right skill may not share words with the
task, which is common for process skills.

## Output on stdout

Print one of:

- `{"pick": "skill-name"}`: this skill first.
- `{"pick": null}`: no skill fits; the verdict becomes `ABSTAIN`.
- `{"ranking": [{"name": "skill-name", "score": 0.91}, ...]}`: higher scores
  come first.

After a pick or ranking, a skill the reply did not name is listed only if the
lexical stage picked it too.

Any other reply counts as a failure and keeps the BM25 result.

A model's order replaces the lexical score, evidence, and margin gates. It does
not override a skill's boundary: a candidate whose don't-use evidence reaches
60% of its use evidence stays set aside.

## Shape the question

Ask about each candidate on its own, in random order and without its BM25
rank: does the task need this skill, need only part of it, or not need it? Then
rank by the "needs it" probability. A single "which one of these?" question is
the weaker design: a small model tends to settle on a label it has learned to
like instead of reading the candidates.

Pass `use_when` and `dont_use` to the model together. The don't-use lines are
what separates near-identical skills, and a short description cannot carry
them.

## Keep it fast

`--timeout` defaults to 2 seconds. A command that loads a model on every call
usually spends most of that time on start-up. For an interactive budget, keep
the model warm in a local process and make the command a thin client that sends
the JSON and prints the reply.
