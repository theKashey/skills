# Skill Guidance

Skill Guidance advises a host-provided skill creator and audits or evaluates
independently installable agent skills. It reviews whether activation, runtime
choices, completion, and package isolation support the intended behavior; it
does not create or edit the target skill.

## Why it exists

Agent skills fail when relevant advice is mistaken for a decision-changing
instruction. Activation text accumulates explanations, runtime bodies repeat
why the skill loaded, maintainer rationale leaks into every invocation, and a
structurally valid package is mistaken for changed agent behavior.

Skill Guidance exists to keep those surfaces separate and make every retained
instruction earn its recurring context cost. Its advice aims at a standalone
package that loads for the right problem, changes one consequential
post-trigger choice, and stops on observable evidence rather than on prose,
tool use, or structural validity alone.

That cost belongs to the flow an activation actually loads, not to
`SKILL.md` size in isolation. Moving material behind a pointer discloses it
progressively only when some applicable flow avoids it. Nested conditional
references can improve clarity and signal-to-noise, but each serial discovery
adds latency; the main `SKILL.md` should expose materially long journeys so the
agent can plan the required reads.

A tidy single-turn exercise gives an instruction unusually little competition
and is weak evidence for that intended effect. Structural validation and clean
comparisons can expose packaging, routing, or interpretation regressions; they
do not establish behavior under long-context stress. That requires a
representative task with the plausible wrong default and competing context
still present.

A host skill creator may use Context Docs for reader-facing truth, locality, and
progressive disclosure, and Skill Guidance for advisory review of the
agent-facing contract. Neither runtime package invokes or depends on the other.

Capability overlap creates a separate failure mode: one label can collapse why
a skill exists, what it owns, how it operates, and how it is packaged into a
false taxonomy. Skill Guidance instead derives an evidence-backed shape from
independent dimensions: reason, governed capability and responsibility,
operating form, package form, and capability relations. A single skill can
therefore own documentation and execute it through a workflow, be broader on
one decision axis and specialist on another, or consume an outcome without
owning its production.

Those relations must remain real. A specialist can refine only a named
condition under an established broader default; an orthogonal concern keeps its
own selection logic; and a coordinator or consumer does not absorb a
contributor's internals. Bundling mechanics needed for standalone delivery does
not grant adjacent expertise or make another skill a runtime dependency.

## When to use this skill

Use Skill Guidance for design advice while a host skill creator is creating or
revising a skill, or to audit and evaluate an existing skill. It reviews:

- whether guidance belongs in a skill at all;
- whether content belongs in activation metadata, runtime instructions,
  maintainer documentation, or a deterministic gate;
- routing and progressive disclosure inside a skill package;
- standalone package isolation;
- behavioral evaluation and completion criteria.

Do not use it as a substitute for the domain workflow the target skill teaches,
for a narrow mechanical check already owned by repository tooling, or for
general documentation work that does not change an agent skill. Pair it with
a documentation skill such as Context Docs (installed separately) when README
prose, examples, references, or reader paths change.

## Runtime architecture

| File | Owns |
| --- | --- |
| [The Laws of Agent Instruction](LAWS.md) | Canonical Law identifiers, titles, and universal decision constraints |
| [SKILL.md](SKILL.md) | Activation boundary, package isolation, route selection, obligation tests, and completion |
| [Advisory design assessment](references/build-or-revise.md) | Capability shape and neighbourhood, ownership, activation/runtime separation, pruning recommendations, and required validation |
| [Audit a skill](references/audit-skill.md) | Evidence-backed shape, route, and obligation review without mutation |
| [Validate changed choices](references/validate-changes.md) | Frozen behavioral evaluation and verdicts |
| [Validator](scripts/validate_skill.py) | Standalone structural and isolation checks |

Keep each rule with one canonical owner. The runtime router may point to a
reference, but it must not point here.

## Law alignment

While reviewing a skill design, name the exact [Agent Instruction
Law](LAWS.md) identifier and title that materially constrains it—for example,
[`Law VII — Enforce or delete mechanical rules`](LAWS.md#law-vii--enforce-or-delete-mechanical-rules).
Each citation carries the target-skill choice it governs and evidence for that
choice. This gives the host creator a short, reviewable design checklist without
copying the full law set into every package, and lets an audit point to one
broken law rather than a vague principle.

The alignment record stays in the handoff by default. A target runtime may name
a law only when the law and its local consequence tell its agent what to do;
a bare law or framework label is not an instruction. Naming selected laws does
not exempt the skill from any other law whose conditions arise, and it never
creates a runtime dependency on Skill Guidance.

## Reviewing a contract change

Start with an observed wrong activation, execution choice, premature stop, or
maintenance failure. Identify the surface that owned the missing decision
before recommending prose or structure to the host skill creator.

For any changed sentence, ask:

1. Is it a trigger, an execution instruction, a behavior-improving causal
   rationale, maintainer support, or a deterministic rule?
2. Would deleting it change activation, a post-trigger choice, or completion?
3. Is another surface already the canonical owner?
4. Can a gate enforce it more reliably than prose?

Recommend moving the sentence to its owner or deleting it when those answers do
not justify runtime context. The host skill creator owns any resulting file
change. Git history records superseded wording; the README records current
design, not the edit narrative.
