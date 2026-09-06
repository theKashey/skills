# The Laws of Agent Instruction

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
