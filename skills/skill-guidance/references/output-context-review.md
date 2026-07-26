# Output-context review

Review a final changed skill artifact from the context available to its runtime
reader. This semantic gate supplements factual, structural, routing, and
behavioral checks; it does not replace them.

## Review protocol

Create a fresh independent reviewer with no inherited drafting context. Give it
exactly two artifacts:

1. the complete final artifact under review, or a diff with enough final-state
   context to assess its opening and changed content;
2. this review-rules artifact.

The reviewer must not consult other sources, edit the target, receive a task
summary, or see producer rationale, validation results, prior reviews, expected
verdict, or intended repair.

Before judging, infer and cite from the target:

- governed capability and semantic subject;
- artifact role and locality;
- intended agent reader and activating task;
- invocation and branch classification;
- whether process content describes a durable runtime process or authoring
  residue.

Return:

```text
Status: PASS | BLOCK | NEEDS-HUMAN-DECISION | UNVALIDATED
Inferred context: capability, subject, role, locality, reader, task, invocation, branches, with locations
Process determination: absent | qualifies | fails | indeterminate, with locations
Rule results: rules 1–5, with target locations
Blockers: location, broken rule, agent impact, minimal repair direction
Review boundary: external factual correctness, routing outcomes, and deterministic checks not assessed
```

## Pass rules

Return `PASS` only when every applicable rule passes:

1. **Subject before artifact.** The title and first substantive prose establish
   the governed capability's outcome, responsibility, or boundary before
   discussing the skill file or authoring task.
2. **Durable reader value.** Every changed prose unit advances a current
   decision, procedure, boundary, rationale, completion condition, or necessary
   navigation for the inferred reader.
3. **Finished-artifact focus.** Drafting, validation, tool, review, and creation
   history stay outside runtime prose unless the durable process itself is the
   governed capability.
4. **Inferable context and locality.** The target alone supports a coherent
   inference of subject, role, scope, reader, task, and why the content belongs
   at that layer.
5. **Decision delta.** Each normative statement selects a supported move over a
   plausible default, sharpens a completion boundary, or routes to a canonical
   owner. Relevant knowledge without a behavioral delta fails.

Apply two checks to the opening:

- **Deletion:** remove artifact labels, paths, and phrases such as “this skill.”
  Useful claims about the governed capability must remain.
- **Substitution:** replace the capability with a sibling capability. If the
  opening remains equally true, it is generic artifact prose.

Return `BLOCK` for a known violation, `NEEDS-HUMAN-DECISION` only for genuine
scope or policy ambiguity, and `UNVALIDATED` when independent review cannot
run. After a repair, use a new fresh reviewer with only the revised target and
this unchanged rules artifact. Keep the verdict in the handoff, not the runtime
artifact.
