---
name: skill-guidance
description: Use when creating an agent skill from scratch or revising, auditing, or validating a skill's trigger description, runtime instructions, references, or standalone packaging; not for the domain workflow the skill teaches.
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

Read and apply [The Laws of Agent Instruction](LAWS.md) before selecting a
route, admitting an obligation, or loading a branch procedure. `LAWS.md` is the
canonical owner of all eight identifiers, titles, and decision constraints.

## Name the active laws

While forming or revising a skill, name every [Law](LAWS.md) that materially
constrains its design in a concise authoring record:

```text
Law: Law I — Point at the delta
Target choice: retain the repository-specific test command and its flag
Evidence: package scripts and representative task
```

Use the exact canonical identifier and title, the target-skill choice it
governs, and evidence. Cite
[`Law VII — Enforce or delete mechanical rules`](LAWS.md#law-vii--enforce-or-delete-mechanical-rules),
for example, when a duplicate prose rule must be removed. The named set is a
compact design checklist, not an exception list: every law still applies when
its condition arises. Keep this record in the handoff: the wrap-up report
returned to the requesting user or process at the end of the task, never a
file in the distributed package. Name a law in the target
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
| Create a skill or decide skill versus reference | [Build or revise a skill](references/build-or-revise.md) | For a changed runtime contract, [validate changed choices](references/validate-changes.md); for a `No-op` outcome (no runtime change admitted), report the admission decision |
| Revise, restructure, prune, or repair a skill | [Build or revise a skill](references/build-or-revise.md) | For changed invocation, normative prose, scope, routing, or completion, [validate changed choices](references/validate-changes.md); for mechanical-only work, use the [isolation gate](#enforce-package-isolation) |
| Audit or review without editing | [Audit a skill](references/audit-skill.md) | Use the audit completion contract; load [Validate changed choices](references/validate-changes.md) only when runtime outcome evidence is requested |
| Evaluate routing, runtime behavior, or context cost | [Validate changed choices](references/validate-changes.md) | Use its frozen evaluation contract |

Use normal file operations when a create or revise route reaches package
mechanics. Do not turn mechanical-only work into an audit or outcome
evaluation. This skill owns unresolved admission, ownership, isolation, locality, and
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

Complete a changed runtime contract when current source evidence and the
applicable deterministic checks agree. Add a representative clean-context
comparison when the changed instruction must prove an interpretation-dependent
choice; otherwise record the bounded evidence used. Report `UNVALIDATED` only
when required evidence cannot be obtained, not merely because creation and
validation occurred in one session.
