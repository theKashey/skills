# Repository governance

Each `skills/<name>/` directory is an independent distribution unit. Assume a
consumer may install exactly one directory and nothing else from this
repository.

## Govern skill changes

- Before changing any skill, read that skill's `README.md` in full. Use
  second-order thinking to recover why the skill exists, which agent choices it
  changes, what downstream behavior depends on it, and what would be lost or
  distorted by the proposed edit. Treat existing runtime content as a
  Chesterton's fence until that rationale is understood.
- Keep each skill's durable, subject-facing reasons in its `README.md`: the
  recurring problem, affected developer or agent, intended effect, boundaries,
  important tradeoffs, rejected shortcuts, and second-order consequences. Do
  not record generic artifact self-description, build history, review process,
  or a framework declaration that does not change a reader's decision. Retain a
  concrete component map, ownership boundary, or framework distinction when it
  establishes the governed subject's behavior or a reader's next choice. Keep
  runtime instructions focused on execution. If a skill has no README,
  establish and record this subject rationale before revising its runtime
  content.
- Design skills to empower developers through small, evidence-producing
  iteration loops: document work, automate bounded operations, verify recorded
  observations and results, and remove uncertainty from both code and planning.
  A skill may cover one of these moves without pretending to own the whole
  development lifecycle.
- Use the host-provided skill creator for every skill creation or
  runtime-content revision. Consult `skills/skill-guidance/SKILL.md` for
  advisory review of activation, runtime choices, routing, isolation, or
  behavioral evaluation; Skill Guidance does not own file creation or mutation.
- Also use `skills/context-docs/SKILL.md` whenever prose, examples, references,
  comments, or reader paths change. `skill-guidance` reviews agent-choice
  behavior; `context-docs` owns truth, locality, reader context, and
  publishable end state.
- Before changing repository-level or skill-facing prose, use the
  [content-persona cast](.context-docs/CONTENT-PERSONAS.md). Select the class by
  the decision the entrant controls, then add only a proven modifier and the
  task-local episode. Treat an assumed reader, goal, subject, or surface as
  revisable when evidence conflicts; follow the casting result instead of
  forcing the original document. Keep the reader goal separate from the
  document's authorial goal, and load only applicable conditional detail. This
  repository authoring context must not become a runtime dependency of an
  independently installed skill.
- Use `skills/verify-complex-artifacts/SKILL.md` after authoring a multi-file
  skill package or repository-wide governance change.

## Review judgment-heavy changes

Use a fresh non-producing subagent as a pre-edit scope challenger when a change
may introduce, expand, remove, replace, substantially reorganize, or reinterpret
existing purpose, offering, routing, ownership, boundaries, or multiple
reader-facing requirements; when broad or corrective feedback leaves what must
survive unclear; or when repairing a rejected candidate, overshoot, omission,
or reversal. Judge cumulative semantic scope: splitting a rewrite into small
patches does not avoid this review.

Give the challenger the exact user request or correction, the complete current
artifact, its governing rationale and repository rules, any rejected candidate
or diff. Do not prime it with the producer's proposed repair or ask it to
approve a conclusion. The challenger reviews scope; it does not edit or rewrite.
Require an evidence-cited result with:

- `preserve` — content, behavior, and invariants that must survive;
- `change` — the exact defect and authorized edit surface;
- `evidence` — words from the request, artifact, and governing sources that
  support both lists;
- `smallest safe patch` — the least expansive change that satisfies the
  request;
- `unresolved decisions` — any conflict or missing authority that requires the
  user.

Do not begin a qualifying edit until those boundaries are explicit. If
`preserve` conflicts with `change`, narrow the patch or ask the user; never
resolve the conflict by deleting more. After an overshoot, the producing agent
must not attempt another broad self-correction without this review.

After the edit, use a different fresh subagent to compare the candidate with the
request and preservation set. Require `PASS` or `BLOCK` with evidence for every
preserved invariant and authorized change; an unavailable or incomplete review
is non-passing. Do not declare the work complete, commit it, or push it while
that review identifies a material loss, scope expansion, or unresolved
contradiction. Keep this history-aware preservation review separate from any
isolated output-context review: the latter receives only the final target and
neutral review rules and cannot prove that earlier requirements survived.

Skip the pre-edit scope challenge only for changes that cannot alter meaning or
ownership: typographical or formatting fixes, deterministic generated-file
refreshes, read-only checks, or already-bounded mechanical corrections with an
explicit target, end state, and preservation boundary. Re-run it if the
semantic scope changes.

## Preserve absolute skill isolation

Treat the target skill directory as its entire runtime universe. Vendor required
material into that directory or narrow the skill's contract until it works when
installed alone. Keep repository orchestration at the repository root or in CI.

Isolation gate:

```bash
python3 scripts/validate_skills.py
```

There are no isolation exceptions.
