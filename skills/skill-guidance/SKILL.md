---
name: skill-guidance
description: Create, revise, and audit self-contained agent skills as verified decision maps. Use when skill work has an unresolved choice about admission, canonical ownership, invocation or routing, instruction locality, package isolation, rationale, completion criteria, pruning, or behavioral evaluation.
---

# Skill Guidance

Turn unresolved agent choices into the smallest verified runtime decision map.
Treat the repository and its tooling as the territory; preserve only the
selection criteria, hidden boundaries, and completion conditions the territory
does not supply.

## Apply the decision laws

1. **Point at the delta.** Admit an instruction only when it changes a plausible
   choice. Record the generic or locally attractive default it must beat.
   Paths, signatures, discoverable mechanics, and enforced policy stay in the
   territory; retain only the reef and the exact command or flag an agent would
   otherwise guess incorrectly.
2. **Spend the instruction budget.** Make every sentence avert a named wrong
   turn or premature stop. Delete no-ops, sediment, duplicated meaning, and
   context that is merely relevant. Put the most frequently missed,
   highest-consequence choices first.
3. **Recruit shared priors.** Prefer a precise leading concept such as
   Chesterton's Fence, POLA, TOCTOU, or N+1 over restating its generic theory.
   Add the local consequence when the name alone does not select an action.
4. **Lead with the supported move.** State `+ preferred choice` before
   `- plausible wrong choice`. Keep a prohibition only when the wrong route
   remains live after the positive route is explicit.
5. **Keep the chart local.** Put a rule at the narrowest stable scope encountered
   by every affected reader. Keep pre-arrival invariants at the root, and verify
   how the target harness resolves nested instructions before relying on depth.
6. **Carry verified why for surprising fences.** Preserve the shortest
   evidence-backed rationale that protects an apparently wrong constraint or
   helps an unseen choice. Record unresolved rationale as an explicit decision
   gap; never manufacture it.
7. **Let gates own mechanical rules.** Prefer types, lint, formatting, hooks,
   tests, or CI for enforceable constraints. Point to the gate and its exact
   invocation instead of duplicating its policy in prose.
8. **Keep every claim falsifiable.** Verify paths, commands, fields, versions,
   examples, links, and current behavior. A stale instruction is a defect, not
   harmless context.

## Enforce package isolation

Treat the target skill directory as the entire runtime universe. Bundle every
required instruction, reference, script, asset, and template inside it. Keep
all local links within that boundary and make the package work when copied
alone, offline, without repository-root files or another skill.

Keep repository orchestration outside distributed skills. A runtime package may
describe the outcome expected from another role or system; every conditional
path still stays inside that package. Vendor required runtime material into the
package or narrow its contract until it stands alone.

From this skill directory, run:

```bash
python3 scripts/validate_skill.py TARGET_SKILL_DIRECTORY
```

## Select one route

Choose one primary route before loading references. Load only the references in
that row; return here if the task materially changes.

| Request | Primary procedure | Required validation |
| --- | --- | --- |
| Create a skill or decide skill versus reference | [Build or revise a skill](references/build-or-revise.md) | For a changed runtime contract, [validate changed choices](references/validate-changes.md) and [review the final artifact in output context](references/output-context-review.md); for `No-op`, report the admission decision |
| Revise, restructure, prune, or repair a skill | [Build or revise a skill](references/build-or-revise.md) | For changed invocation, normative prose, scope, routing, or completion, [validate changed choices](references/validate-changes.md) and [review the final artifact in output context](references/output-context-review.md); for mechanical-only work, stop after the bundled validator passes |
| Audit or review without editing | [Audit a skill](references/audit-skill.md) | Use the audit completion contract; load [Validate changed choices](references/validate-changes.md) only when runtime outcome evidence is requested |
| Evaluate routing, runtime behavior, or context cost | [Validate changed choices](references/validate-changes.md) | Use its frozen evaluation contract |

Use normal file operations when a create or revise route reaches package
mechanics, then run the bundled validator against the target directory. Do not
turn mechanical-only work into an audit or outcome evaluation. This skill owns
unresolved admission, ownership, isolation, locality, and
behavioral-validation choices.

## Admit each obligation

Before adding a rule, reference, script, tool call, test, or independent review,
answer:

- **Choice:** What will the agent choose or complete differently?
- **Default:** What plausible route would it otherwise take?
- **Authority:** Which user decision, repository evidence, executable tool, or
  representative observation establishes the preferred route?
- **Gravity:** What is the narrowest stable owner visible to every affected
  activation?
- **Gate:** Can structure or deterministic enforcement own the constraint?
- **Completion:** What observable state distinguishes done from incomplete?

Reject an item missing a concrete Choice, Default, Authority, Gravity, or
Completion. Always consider Gate; `none` is valid only when deterministic
enforcement cannot own the choice. Prefer `No-op`, an amendment to the
canonical owner, or a structural repair over a new runtime obligation.

## Preserve the reader contract

Write the finished operational present for an agent mid-task. Make the governed
capability, reader, scope, supported action, and boundary inferable from the
artifact itself. Give each fact one canonical owner and expose branch-specific
detail through a direct, conditional pointer. Keep authoring history,
validation narration, and review records in the handoff rather than runtime
instructions.

Complete a changed runtime contract only when current source evidence,
deterministic checks, representative behavior, and a fresh output-context
review agree, or report `BLOCK`, `NEEDS-HUMAN-DECISION`, or `UNVALIDATED`.
For mechanical-only changes, stop when the bundled structural and isolation
validator passes.
