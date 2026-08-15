---
name: carry-the-load
description: Use after an engineering outcome or move is selected, before implementation expands, to shape one value-bearing increment with bounded failure; not for choosing the move, multi-cycle planning state, or interrogating a finished claim.
---

# Carry the Load

Move one selected engineering outcome through a complete feedback loop.
Thinness is not an objective.

## Freeze the load

Record only fields that can change the implementation, and freeze them before
the first mutating action. A card produced after implementation has already
started is a protocol violation: return `BLOCK` instead of backfilling the
card.

```text
Value: [recipient and observable effect]
Current flow: [entry, material handoffs or queues, verification, delivery]
Constraint: [the one condition limiting the next verified increment]
Increment: [smallest complete change and maximum scope]
Misfire: [credible wrong result]
Containment: [fallback, rollback, degradation, or blast-radius boundary]
Readback: [expected signal, disconfirming signal, and review point]
Learning owner: [none / implementation / gate / local instructions / unresolved — the harvest may revise it]
```

Do not restate the entire task or map a value stream whose additional steps
cannot change the increment. When Value, authority, or the completed-state
contract — what must be observably true of the result when the increment is
complete — has materially different plausible meanings, return
`NEEDS-HUMAN-DECISION` instead of selecting one.

## Move one increment through the flow

1. **Start at value.** Name the effect the recipient can observe. An artifact,
   tool call, merged patch, or passing proxy is not value unless it establishes
   that effect.
2. **Find the current constraint.** Inspect only enough of the path from request
   to verification to identify the queue, handoff, unknown, defect source, or
   missing capability currently limiting delivery.
3. **Define one complete increment.** Keep one increment in flight and make it
   cross implementation, integration, and the first trustworthy readback. Do
   not replace a vertical slice with the fewest lines or a disconnected stub.
4. **Pull what the increment needs.** Load context, invoke tools, introduce
   abstraction, and add protection when the current constraint or credible
   consequence requires them. Preserve deliberate capacity, rollback paths,
   and optionality whose load is named.
5. **Build quality into the path.** Put the check at the earliest owner capable
   of observing the property. Stop on contradiction, failed verification, or a
   broken containment boundary; do not continue and explain the result into
   passing.
6. **Read back before opening more work.** Compare the external result with the
   frozen expected and disconfirming observations. An unchanged retry is not a
   new increment.

Use established repository checks and consumer surfaces. Do not add a new
framework, service, abstraction, or review layer when an existing path can
produce the required readback at lower total cost.

When a problem surfaces outside the frozen Increment's maximum scope, do not
expand the increment to absorb it and do not repair it inside the current
context: the increment's accumulated context biases how the side problem is
scoped and corrected. When the problem gates the increment's readback and the
harness provides subagents, delegate it as a self-contained brief — the
problem, its observed signal, and its own scope boundary, without the
increment's working context. The brief carries only authority the executor
already holds; a problem whose repair exceeds that authority takes the
deferral or `NEEDS-HUMAN-DECISION` path instead. Otherwise record the problem
as an explicit deferral in the completion report; when a readback-gating
problem cannot be delegated, exit through a terminal status with the deferral
recorded rather than repairing it in place. A mutating action outside the
frozen maximum scope in the current context is a scope violation, not
initiative.

When an intended mutating action is not plainly covered by the frozen
Increment's maximum scope, or a completion report is about to omit
noticed-but-not-done work, load the moorings in
[STAYING-PUT.md](STAYING-PUT.md) before proceeding.

## Make wrong cheap

Before committing to an uncertain heuristic, rule, migration, rollout, or
generated interpretation:

1. State the smallest credible way it can be wrong and the affected recipient.
2. Bound the failure by input, row, tenant, request, component, time, release,
   or another observable partition.
3. Preserve the previous behavior as fallback when it remains valid and doing
   so does not conceal an unsafe state.
4. Label the result no more strongly than the evidence supports. Prefer a local
   weak claim that can be discounted over a universal rule fitted to the
   examples in view.
5. Define how the misfire will be detected and how the affected partition will
   recover before widening exposure.

Fallback and rollback establish resilience. Claim antifragile learning only
after the readback changes a future choice, gate, invariant, evaluation, or
routing decision.

## Audit protection

For each test, fallback, buffer, abstraction, compatibility path, instruction,
or duplicated implementation added by the increment — or challenged by it,
meaning anything the increment deletes, weakens, bypasses, or duplicates — ask:

```text
Load: What present value or credible failure does it protect?
Reach: Which affected path receives or enforces it?
Cost: What delay, complexity, attention, or maintenance does it add?
Evidence: What observation shows it works?
Retirement: What changed condition would make it unnecessary?
```

- Retain it when the named load and consequence justify the total cost.
- Narrow or relocate it when only part of its reach is justified.
- Replace it with a deterministic owner when prose or convention carries a
  mechanical invariant, the replacement stays inside authorized scope, and a
  fresh reader can still recover the constraint from the changed structure.
  Discovery is not authorization; when the smallest sufficient owner exceeds
  that scope, return `NEEDS-HUMAN-DECISION` rather than widening silently.
- Delete it only when evidence shows it carries no current load, duplicates a
  stronger owner, or its cost exceeds the consequence it contains.
- Preserve it as Chesterton's Fence while its purpose or affected paths remain
  unresolved.

Do not add tests merely to license deletion, and do not treat missing tests as
evidence that code provides no value.

## Harvest material learning

After a disconfirming readback, classify what should survive:

| Observation | Disposition |
| --- | --- |
| Incidental execution error with no recurring choice | Repair within scope; persist nothing |
| Mechanically detectable invariant or forbidden state | Put it in code, a type, schema, test, lint rule, or CI gate |
| Local implementation or operational fact | Keep it with the narrowest established owner |
| Recurring or high-consequence model judgment with no deterministic owner | Load and follow [behavior principles](references/behavior-principles.md) |
| Product, risk, ownership, or scope choice | Return `NEEDS-HUMAN-DECISION` |

Do not make every failure leave a permanent instruction. The improvement is a
better future choice at lower total cost, not a larger memory of everything
that went wrong.

The behavior-principle procedure returns its own status; report it alongside
the increment status. An `UNVALIDATED` principle leaves the learning owner
established but its effect unproven — report it as such rather than as
validated.

## Complete the increment

Return one status:

- `PASS` — the recipient-visible effect passed its readback within the frozen
  scope; containment held; material learning has an established owner.
- `NO-OP` — the current flow already delivers the effect, or the proposed
  machinery carries no additional load.
- `BLOCK` — the effect, verification, or containment failed and no authorized
  repair can establish it, or the load card was not frozen before
  implementation began.
- `NEEDS-HUMAN-DECISION` — value, authority, risk ownership, or a material
  completed-state choice remains unresolved.

Report the Value, Increment, observed Readback, protection disposition,
learning owner, any deferred side problems, and status. The reported Readback
must quote an executed observation — a test run, command output, or rendered
surface; `PASS` is invalid when the readback is a prediction rather than an
observation. Keep the visible response proportional to the decision; do not
turn the load card into the deliverable when the result is already clear.
