# Repository governance

Each `skills/<name>/` directory is an independent distribution unit. Assume a
consumer may install exactly one directory and nothing else from this
repository.

## Govern skill changes

- Use `skills/skill-guidance/SKILL.md` for every skill creation, runtime-content
  revision, routing decision, or skill audit.
- Also use `skills/documentory/SKILL.md` whenever prose, examples, references,
  comments, or reader paths change. `skill-guidance` owns agent-choice behavior;
  `documentory` owns truth, locality, reader context, and publishable end state.
- Use `skills/verify-complex-artifacts/SKILL.md` after authoring a multi-file
  skill package or repository-wide governance change.

## Preserve absolute skill isolation

Treat the target skill directory as its entire runtime universe. Vendor required
material into that directory or narrow the skill's contract until it works when
installed alone. Keep repository orchestration at the repository root or in CI.

Isolation gate:

```bash
python3 scripts/validate_skills.py
```

There are no isolation exceptions.
