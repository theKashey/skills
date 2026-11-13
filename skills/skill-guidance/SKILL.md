---
name: skill-guidance
description: Use when advising on, auditing, or evaluating an agent skill's activation, runtime decisions, references, context cost, or standalone packaging; not for creating or editing the target skill.
---

# Skill Guidance

Review a proposed or existing agent skill and return evidence-backed design
advice. Leave target-package creation and mutation to the host-provided skill
creator.

## Review the activation boundary

**Activation boundary — Separate activation from execution.** Check that every
skill-level activation condition is in the frontmatter description, without the
skill's own steps or procedure, an inventory of mechanisms, hypothetical
failures, or adjacent tools. State *what*: the response or outcome that
separates it from another skill with the same trigger; when no task evidence
selects between those outcomes, apply
[Law X](#law-x--restructure-overlap-do-not-reword-it) instead. State *when*:
the task or work situation that requires it, or the artifact its operation
changes, verifies, or must interpret—*adding or changing a migration*, not
*working with databases*—because a topic-wide trigger, or an artifact merely in
view, loads the skill for every nearby task. A timing condition may bound that
task, never replace it. Add a `not for` clause only for a neighboring task that
would otherwise activate it. Never demand selection—*always use*, *most
effective*, *whenever possible*, *even if they don't ask*—because demands from
every installed skill leave the router nothing to choose by; fix an undertrigger
with a sharper *what* or *when*, or Law X. Terse wording that leans on shared
priors is fine when the floor model—the least capable model the skill must
support—routes correctly on it. Aim for at most 240 characters, because every
installed description shares one listing budget; exceed that only when a needed
*what* or *when* clause cannot fit once the excluded content is gone, and never
beyond 500. The validator warns on any description over 240 or with demanding
wording and rejects one over 500. The body must start after activation and
retain only post-trigger decisions, actions, resources, boundaries, and
completion checks. Internal branch conditions remain execution logic.

**Boundary section — Only for a boundary the description cannot hold.** When
the cases and `not for` exclusions that separate the skill from neighboring
tasks do not fit within 240 characters beside its *what* and *when*, and Law X
does not apply, keep the description's *what* and *when*, plus the most
consequential `not for` that still fits. Move the rest into one section that
opens the body, with a `Use when` list and a `Do not use` list, each under its
own heading. It is the only skill-level activation content a body may hold.
List only cases inside the description's *what* and *when*, and exclusions for
a neighboring task that would otherwise load the skill. Name the task, never
another skill, and demand nothing. The headings let a router that reads skill
bodies count `Do not use` lines against the skill instead of as matching words,
and let an agent that loaded it for a listed exclusion stop at the top. A skill
whose boundary fits its description carries no such section, because the
section would repeat the description on every activation.

## The Laws of Agent Instruction

These laws govern every Skill Guidance route. Read and apply all of them;
naming the laws that materially constrain one decision does not exempt the
rest.

## Law I — Point at the delta

Admit an instruction only when it changes a plausible choice. Record the
generic or locally attractive default it must beat. Paths, signatures,
discoverable mechanics, and enforced policy stay in the territory; retain only
the non-obvious constraint and the exact command or flag an agent would otherwise guess
incorrectly.

## Law II — Spend the instruction budget

Length, repetition, and representation all draw on one bounded attention
budget, measured over the selected flow—`SKILL.md` plus every transitively
required reference—not an individual file. A saving counts only while the
agent still chooses reliably; compare representative choices when a proposed
saving could reduce reliability. Cite the clause that applies:

- **Admission:** make every sentence avert a named wrong turn or premature
  stop. Delete no-ops, sediment, unjustified duplication, and context that is
  merely relevant. Keep the complete rule with one canonical owner; a local
  cue or causal explanation elsewhere earns its cost only where it prevents a
  named error or repeated investigation.
- **Encoding:** choose the representation that preserves decision reliability
  at the lowest justified reading, retrieval, and execution cost. A diagram,
  table, or aligned block can earn its cost even when prose elsewhere
  expresses the same facts, by the same test.
- **Splitting:** moving always-read material behind a pointer is not
  progressive disclosure; it preserves the load and adds traversal. Split when
  a condition lets at least one relevant flow leave material unloaded. Nested
  conditional references may sharpen signal, but expose materially long read
  journeys in the main `SKILL.md` so the agent can plan them without serial
  discovery.
- **Order:** put the most frequently missed, highest-consequence choices
  first.

## Law III — Recruit shared priors

Prefer a precise leading concept such as Chesterton's Fence, POLA, TOCTOU, or
N+1 over restating its generic theory. Add the local consequence when the name
alone does not select an action.

## Law IV — Lead with the supported move

State `+ preferred choice` before `- plausible wrong choice`. Keep a
prohibition only when the wrong route remains live after the positive route is
explicit; when a gate or structural change can remove that route, prefer it and
delete the warning.

## Law V — Keep the chart local

Put a rule at the narrowest stable scope encountered by every affected reader.
Keep pre-arrival invariants at the root, and verify how the target harness
resolves nested instructions before relying on depth: depth scopes a rule; it
does not enforce it.

## Law VI — Carry verified why for surprising fences

Treat an apparently wrong constraint as Chesterton's Fence: delete it only
once its reason is known. Preserve the shortest verified `X because Y` when it
protects such a fence or transfers a choice to an unseen case. Keep other
explanation, defense, apology, anticipated objections, authoring support, and
design history out of runtime files. A README may explain durable reasons,
concrete ownership, and a framework distinction that changes a reader's choice,
but never becomes a runtime dependency. Keep construction and
framework-provenance records in the handoff.

## Law VII — Enforce or delete mechanical rules

Prefer types, lint, formatting, hooks, tests, or CI for enforceable constraints.
Before deleting an instruction in favor of a gate, verify the failure it covers,
that it runs on the affected path, and when it intervenes relative to the
consequential choice. Point to the gate and its exact invocation; remove policy
prose whose decision is already protected. Retain the smallest earlier decision
cue when the gate only detects a mistake after harm or costly rework. An
available gate without established coverage and timing is not a delegated
guarantee.

## Law VIII — Keep every claim falsifiable

Verify paths, commands, fields, versions, examples, links, and current behavior.
A stale instruction is a defect, not harmless context: it is obeyed with the
confidence of a live one.

## Law IX — Refine the paved road; do not reopen it

A specialist owns only a named conditional delta from an established broader
owner's default; a normal-case change belongs to that owner, and an orthogonal
concern keeps its own selection logic.

## Law X — Restructure overlap; do not reword it

When selectable units—skills, route rows, or conditional references—claim the
same trigger with different moves the task cannot choose between (a crowded
shelf), or one unit claims triggers that share no capability (a bloated book),
no wording lets the agent select correctly. Merge the competitors or demote
one, split the disjoint part, or establish a Law IX relation. Reword only when
both inspected contracts show distinct scopes; a shared topic is not a shared
trigger, and many synonyms for one capability do not justify a split.

## Name the active laws

While reviewing a proposed or existing skill, name every [Law](#the-laws-of-agent-instruction) that
materially constrains its design in a concise advisory record:

```text
Law: Law I — Point at the delta
Target choice: retain the repository-specific test command and its flag
Evidence: package scripts and representative task
```

Use the exact canonical identifier and title, the target-skill choice it
governs, and evidence. Cite
[`Law VII — Enforce or delete mechanical rules`](#law-vii--enforce-or-delete-mechanical-rules),
for example, when verified enforcement makes a prose rule redundant. Keep this
record in the advisory report or handoff, never in the distributed package.
Recommend naming a law in the target runtime only when its title plus local
consequence selects an action for that target skill's agent; never recommend a
bare framework label or a dependency on this package.

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

The command reports mechanical failures (exit 1) separately from network
mentions needing semantic review (exit 2). On the advisory, audit, and
evaluation routes, resolve each `REVIEW` against its surrounding procedure:
inert data is not a dependency; required network access violates isolation.
Record the disposition and evidence in that route's report. Report
`UNVALIDATED` while any required disposition is unresolved; a mechanical pass
alone does not establish semantic isolation.

## Select one route

Choose one primary route before loading references. Load only the references in
that row; return here if the task materially changes.

| Request | Primary procedure | Required validation |
| --- | --- | --- |
| A host skill creator needs design advice before or during creation, revision, restructuring, pruning, or repair | [Advise a skill design](references/build-or-revise.md) | Return the ownership and design recommendation; when a candidate runtime contract exists, [validate changed choices](references/validate-changes.md) |
| Audit or review without editing | [Audit a skill](references/audit-skill.md) | Use the audit completion contract; load [Validate changed choices](references/validate-changes.md) only when runtime outcome evidence is requested |
| Evaluate routing, runtime behavior, or context cost | [Validate changed choices](references/validate-changes.md) | Use its frozen evaluation contract |
| Structural or isolation check only | [Enforce package isolation](#enforce-package-isolation) | Report the validator result, including any `REVIEW` and `UNVALIDATED` lines, and the runtime flow; leave `REVIEW` dispositions to the audit route; give no audit or evaluation verdict |

Return recommendations and evidence to the host skill creator; do not create,
edit, rename, or delete target-package files.

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
rejected alternatives, and component ownership. It opens with the skill's
name, what it provides, and why a reader would use it, and states the problem,
reader, effect, and boundaries before runtime architecture or authoring
mechanics. A missing README is never a blocking finding; when the user asks
for one, return exactly that contract to the host skill creator for
generation. A README holding handoff material (authoring narrative, validation
records, pending work, environment deixis) is repaired by relocating that
content, never by deleting the file.

Demand wording stays out of the description, but a consuming repository may
choose it. A package may ship one optional installation reference, recommended
at `references/installation.md`, reached only through a skill-body pointer
conditioned on installing the skill or verifying its installation, and read for
nothing else. It taps the skill into the repository's processes so it runs at
full power: the agent-instructions rule that names the skill and when to use
it, plus any process wiring the skill's own references define, pointed to
rather than copied. It also carries the review checks that catch, in finished
work, the gains a sloppy agent drops—*only the non-obvious facts were
documented*. The installer verifies that each item landed where the
repository's own instructions deliver it—review checks go to the review file
the root instructions point to—never a fixed destination. An absent reference
is never a finding.

## Complete the review

Complete with an evidence-backed advisory report, audit verdict, or behavioral
evaluation. A clean-context comparison can expose routing or interpretation
regressions but does not establish behavior under accumulated-context stress.
When that stressed effect matters, require a representative target-harness
observation with the plausible wrong default and competing context present.
Report `UNVALIDATED` whenever required evidence cannot be obtained.
