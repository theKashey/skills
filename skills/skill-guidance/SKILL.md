---
name: skill-guidance
description: Use when advising on, auditing, or evaluating an agent skill's activation, runtime decisions, references, or standalone packaging; not for creating or editing the target skill.
---

# Skill Guidance

Review a proposed or existing agent skill and return evidence-backed design
advice. Leave target-package creation and mutation to the host-provided skill
creator.

## Review the activation boundary

**Activation boundary — Separate activation from execution.** Check that every
skill-level activation condition is in the frontmatter description. It must be
one sentence and at most 240 characters, naming the concrete situation and
behavior that need the skill without listing hypothetical failures, adjacent
tools, or workflow phases. The body must start after activation and retain only
post-trigger decisions, actions, resources, boundaries, and completion checks.
Internal branch conditions remain execution logic.

## Apply the eight decision laws

Read and apply [The Laws of Agent Instruction](LAWS.md) before selecting a
route, admitting an obligation, or loading a branch procedure. `LAWS.md` is the
canonical owner of all eight identifiers, titles, and decision constraints.

## Name the active laws

While reviewing a proposed or existing skill, name every [Law](LAWS.md) that
materially constrains its design in a concise advisory record:

```text
Law: Law I — Point at the delta
Target choice: retain the repository-specific test command and its flag
Evidence: package scripts and representative task
```

Use the exact canonical identifier and title, the target-skill choice it
governs, and evidence. Cite
[`Law VII — Enforce or delete mechanical rules`](LAWS.md#law-vii--enforce-or-delete-mechanical-rules),
for example, when a duplicate prose rule must be removed. The named set is a
compact review checklist, not an exception list: every law still applies when
its condition arises. Keep this record in the advisory report or handoff, never
in the distributed package. Recommend naming a law in the target runtime only
when its title plus local consequence selects an action for that target skill's
agent; never recommend a bare framework label or a dependency on this package.

## Enforce package isolation

Treat the target skill directory as the entire runtime universe. Check that
every required instruction, reference, script, asset, and template is bundled
inside it, every local link stays within that boundary, and the package works
when copied alone, offline, without repository-root files or another skill.

Repository orchestration must stay outside distributed skills. A runtime
package may describe the outcome expected from another role or system, but
every conditional path must remain inside that package. When this fails,
recommend vendoring the required runtime material or narrowing the contract.

From this skill directory, run:

```bash
python3 scripts/validate_skill.py TARGET_SKILL_DIRECTORY
```

## Select one route

Choose one primary route before loading references. Load only the references in
that row; return here if the task materially changes.

| Request | Primary procedure | Required validation |
| --- | --- | --- |
| A host skill creator needs design advice before or during creation, revision, restructuring, pruning, or repair | [Advisory design assessment](references/build-or-revise.md) | Return the ownership and design recommendation; when a candidate runtime contract exists, [validate changed choices](references/validate-changes.md) |
| Audit or review without editing | [Audit a skill](references/audit-skill.md) | Use the audit completion contract; load [Validate changed choices](references/validate-changes.md) only when runtime outcome evidence is requested |
| Evaluate routing, runtime behavior, or context cost | [Validate changed choices](references/validate-changes.md) | Use its frozen evaluation contract |

Return recommendations and evidence to the host skill creator; do not create,
edit, rename, or delete target-package files. Do not turn a mechanical-only
check into an audit or outcome evaluation. This skill advises on admission,
ownership, isolation, locality, and behavioral-validation choices.

## Test each obligation

For every proposed or retained rule, reference, script, tool call, test, or
independent review, answer:

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

Recommend rejecting an item missing a concrete Choice, Default, Authority,
Gravity, Surface, or Completion. Always consider Gate; `none` is valid only
when deterministic enforcement cannot own the choice. Prefer a `No-op`,
amendment to the canonical owner, or structural repair over a new runtime
obligation.

## Review the reader contract

Check that the candidate uses the finished operational present for an agent
mid-task. Its governed capability, reader, scope, supported action, and boundary
must be inferable from the runtime artifact itself. Each fact needs one
canonical owner, with branch-specific detail exposed through a direct,
conditional pointer. Activation criteria belong in the description; durable,
subject-facing reasons belong in `README.md`; authoring history, validation
narration, review records, generic surface-selection rationale, and
non-operational framework provenance belong in the handoff.

A standalone package carries a maintainer `README.md` that owns those durable
reasons — recurring problem, affected reader, intended effect, boundaries,
rejected alternatives, and component ownership — and stays outside the runtime
dependency graph. A missing README is never a blocking finding; when the
user asks for one, generate it to exactly that contract. A README holding
handoff material (authoring narrative, validation records, pending work,
environment deixis) is repaired by relocating that content, never by deleting
the file.

Complete with an evidence-backed advisory report, audit verdict, or behavioral
evaluation. A clean-context comparison can expose routing or interpretation
regressions but does not establish behavior under accumulated-context stress.
When that stressed effect matters, require a representative target-harness
observation with the plausible wrong default and competing context present.
Report `UNVALIDATED` whenever required evidence cannot be obtained.
