# Skill Guidance

Skill Guidance creates, revises, audits, and validates independently installable
agent skills, so an agent loads the right instruction, makes the intended
post-trigger choice, and stops on observable evidence.

## Why it exists

Agent skills fail when relevant advice is mistaken for a decision-changing
instruction. Activation text accumulates explanations, runtime bodies repeat
why the skill loaded, maintainer rationale leaks into every invocation, and a
structurally valid package is mistaken for changed agent behavior.

Skill Guidance exists to keep those surfaces separate and make every retained
instruction earn its recurring context cost. Its intended effect is a
standalone package that loads for the right problem, changes one consequential
post-trigger choice, and stops on observable evidence rather than on prose,
tool use, or structural validity alone.

Documentory supplies the reader-locality and progressive-disclosure discipline
used to decide what a maintainer needs to understand about that package. Skill
Guidance supplies the agent-instruction discipline used to package and maintain
Documentory as a skill. They are used to build each other, but neither runtime
package invokes or depends on the other.

## When to use this skill

Use Skill Guidance while creating, revising, restructuring, pruning, repairing,
or auditing an agent skill. It also owns decisions about:

- whether guidance belongs in a skill at all;
- whether content belongs in activation metadata, runtime instructions,
  maintainer documentation, or a deterministic gate;
- routing and progressive disclosure inside a skill package;
- standalone package isolation;
- behavioral evaluation and completion criteria.

Do not use it as a substitute for the domain workflow the target skill teaches,
for a narrow mechanical check already owned by repository tooling, or for
general documentation work that does not change an agent skill. Pair it with
the repository's documentation guidance when README prose, examples,
references, or reader paths change.

## Runtime architecture

| File | Owns |
| --- | --- |
| [SKILL.md](SKILL.md) | Universal decision laws, package isolation, route selection, obligation admission, and completion |
| [Build or revise](references/build-or-revise.md) | Capability ownership, activation/runtime separation, authoring, pruning, and structural validation |
| [Audit a skill](references/audit-skill.md) | Evidence-backed review without mutation |
| [Validate changed choices](references/validate-changes.md) | Frozen behavioral evaluation and verdicts |
| [Validator](scripts/validate_skill.py) | Standalone structural and isolation checks |

Keep each rule with one canonical owner. The runtime router may point to a
reference, but it must not point here.

## Law alignment

While forming a skill, name the exact Skill Guidance law identifier and title
that materially constrains its design—for example, `Law VII — Enforce or delete
mechanical rules`. Each citation carries the target-skill choice it governs and
evidence for that choice. This creates a short, reviewable design checklist
without copying the full law set into every package, and lets an audit point to
one broken law rather than a vague principle.

The alignment record stays in the handoff by default. A target runtime may name
a law only when the law and its local consequence tell its agent what to do;
a bare law or framework label is not an instruction. Naming selected laws does
not exempt the skill from any other law whose conditions arise, and it never
creates a runtime dependency on Skill Guidance.

## Changing the contract

Start with an observed wrong activation, execution choice, premature stop, or
maintenance failure. Identify the surface that owned the missing decision
before adding prose.

For any changed sentence, ask:

1. Is it a trigger, an execution instruction, a behavior-improving causal
   rationale, maintainer support, or a deterministic rule?
2. Would deleting it change activation, a post-trigger choice, or completion?
3. Is another surface already the canonical owner?
4. Can a gate enforce it more reliably than prose?

Move the sentence to its owner or delete it when those answers do not justify
runtime context. Git history records superseded wording; the README records
current design, not the edit narrative.
