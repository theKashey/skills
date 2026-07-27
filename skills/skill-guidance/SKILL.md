---
name: skill-guidance
description: Use when creating, revising, or auditing an agent skill; or when deciding how a skill should activate, guide behavior, validate outcomes, or remain standalone.
---

# Skill Guidance

Turn unresolved agent choices into the smallest verified runtime decision map.

## Set the activation boundary

**Activation boundary — Separate activation from execution.** Put every
skill-level activation condition in the frontmatter description. Keep it to one
sentence and at most 240 characters. Name the concrete situation and behavior
that need the skill; do not list hypothetical failures, adjacent tools, or
workflow phases. Start the body after activation: retain only post-trigger
decisions, actions, resources, boundaries, and completion checks. Internal
branch conditions remain execution logic.

## Apply the eight decision laws

1. **Law I — Point at the delta.** Admit an instruction only when it changes a plausible
   choice. Record the generic or locally attractive default it must beat.
   Paths, signatures, discoverable mechanics, and enforced policy stay in the
   territory; retain only the reef and the exact command or flag an agent would
   otherwise guess incorrectly.
2. **Law II — Spend the instruction budget.** Make every sentence avert a named wrong
   turn or premature stop. Delete no-ops, sediment, duplicated meaning, and
   context that is merely relevant. Length and repetition both consume a
   bounded attention budget; put the most frequently missed,
   highest-consequence choices first.
3. **Law III — Recruit shared priors.** Prefer a precise leading concept such as
   Chesterton's Fence, POLA, TOCTOU, or N+1 over restating its generic theory.
   Add the local consequence when the name alone does not select an action.
4. **Law IV — Lead with the supported move.** State `+ preferred choice` before
   `- plausible wrong choice`. Keep a prohibition only when the wrong route
   remains live after the positive route is explicit; when a gate or structural
   change can remove that route, prefer it and delete the warning.
5. **Law V — Keep the chart local.** Put a rule at the narrowest stable scope encountered
   by every affected reader. Keep pre-arrival invariants at the root, and verify
   how the target harness resolves nested instructions before relying on depth:
   depth scopes a rule; it does not enforce it.
6. **Law VI — Carry verified why for surprising fences.** Preserve the shortest verified
   `X because Y` when it protects an apparently wrong constraint or transfers a
   choice to an unseen case. Keep other explanation, defense, apology,
   anticipated objections, authoring support, and design history out of runtime
   files. A README may explain durable reasons, concrete ownership, and a
   framework distinction that changes a reader's choice, but never becomes a
   runtime dependency. Keep construction and framework-provenance records in
   the handoff.
7. **Law VII — Enforce or delete mechanical rules.** Prefer types, lint, formatting, hooks,
   tests, or CI for enforceable constraints. Point to the gate and its exact
   invocation instead of duplicating its policy in prose.
8. **Law VIII — Keep every claim falsifiable.** Verify paths, commands, fields, versions,
   examples, links, and current behavior. A stale instruction is a defect, not
   harmless context: it is obeyed with the confidence of a live one.

## Name the active laws

While forming or revising a skill, name every law above that materially
constrains its design in a concise authoring record:

```text
Law: Law I — Point at the delta
Target choice: retain the repository-specific test command and its flag
Evidence: package scripts and representative task
```

Use the exact canonical identifier and title, the target-skill choice it
governs, and evidence. Cite `Law VII — Enforce or delete mechanical rules`,
for example, when a duplicate prose rule must be removed. The named set is a
compact design checklist, not an exception list: every law still applies when
its condition arises. Keep this record in the handoff. Name a law in the target
runtime only when its title plus local consequence selects an action for that
target skill's agent; never add a bare framework label or make the target depend
on this package.

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
| Create a skill or decide skill versus reference | [Build or revise a skill](references/build-or-revise.md) | For a changed runtime contract, [validate changed choices](references/validate-changes.md); for `No-op`, report the admission decision |
| Revise, restructure, prune, or repair a skill | [Build or revise a skill](references/build-or-revise.md) | For changed invocation, normative prose, scope, routing, or completion, [validate changed choices](references/validate-changes.md); for mechanical-only work, stop after the bundled validator passes |
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
- **Surface:** Is the content an activation trigger, runtime instruction,
  maintainer support or rationale, or deterministic rule?
- **Gate:** Can structure or deterministic enforcement own the constraint?
- **Completion:** What observable state distinguishes done from incomplete?

Reject an item missing a concrete Choice, Default, Authority, Gravity, Surface,
or Completion. Always consider Gate; `none` is valid only when deterministic
enforcement cannot own the choice. Prefer `No-op`, an amendment to the canonical
owner, or a structural repair over a new runtime obligation.

## Preserve the reader contract

Write the finished operational present for an agent mid-task. Make the governed
capability, reader, scope, supported action, and boundary inferable from the
runtime artifact itself. Give each fact one canonical owner and expose
branch-specific detail through a direct, conditional pointer. Keep activation
criteria in the description; keep durable, subject-facing reasons in `README.md`;
keep authoring history, validation narration, review records, generic
surface-selection rationale, and non-operational framework provenance in the
handoff.

Complete a changed runtime contract only when current source evidence,
deterministic checks, and representative behavior agree, or report `BLOCK`,
`NEEDS-HUMAN-DECISION`, or `UNVALIDATED`.
For mechanical-only changes, stop when the bundled structural and isolation
validator passes.
