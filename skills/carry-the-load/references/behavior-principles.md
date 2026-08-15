# Preserve a behavior principle

Use this procedure only after a material misfire exposes a recurring or
high-consequence model judgment, or when the user explicitly asks to teach a
repository a supported engineering behavior. Do not use it for an incidental
error, a local fact, or a mechanically enforceable invariant.

## Pass the admission gate

Freeze this evidence before proposing prose:

```text
Condition: [observable situation that activates the choice]
Supported move: [what the agent should choose]
Plausible default: [locally attractive wrong choice]
Consequence: [verified effect of choosing incorrectly]
Scope: [smallest set of agents and work that need the principle]
Gate: [why code, types, lint, tests, schemas, or CI cannot own it]
Observed change: [observable evidence that the behavior changed]
Retirement: [condition that would make the instruction unnecessary]
Authority: [decision allowing the target instruction surface to change]
```

Return `NO-OP` when the supported move is already recoverable, no plausible
default remains, a deterministic gate can own the choice, or the evidence does
not justify recurring context. Return `NEEDS-HUMAN-DECISION` when authority,
risk ownership, or the intended behavior is unresolved.

One incident may justify a principle only when its consequence is material and
the same judgment remains live. Frequency alone does not justify instruction,
and a framework name alone does not select a move.

## Select the owner

Use the narrowest stable owner encountered by every affected agent before the
choice:

| Owner | Use it when |
| --- | --- |
| Implementation, type, schema, test, lint, or CI | The condition and safe action are mechanically decidable |
| Existing local documentation | The fact belongs to a human or operational contract rather than model behavior; its admission and placement follow the repository's documentation discipline, not this procedure |
| Nested `AGENTS.md` | Only work under one repository area encounters the judgment |
| Root `AGENTS.md` | Every material repository task encounters the judgment and no narrower owner reaches all affected agents |
| Skill runtime | The choice exists only after that skill activates |

This procedure admits only recurring model judgments. An independently
installed skill cannot depend on repository-root instructions. Editing
`AGENTS.md` is an explicit repository-policy change, never an automatic side
effect of ordinary execution. If the selected owner is outside authorized
scope, return a placement proposal and `NEEDS-HUMAN-DECISION`.

## Write the smallest choice-changing rule

Prefer this semantic form, not necessarily this exact sentence shape:

```text
When [observable condition], [supported move] because [short verified
consequence]. Verify with [observable check]. Stop or ask when [authority
boundary].
```

Lead with the supported move. Include the wrong route only when it remains
plausible after the positive instruction. Preserve the shortest verified
causal edge needed to transfer the choice to an unseen case. Omit doctrine
definitions, incident narration, apologies, examples that add no branch, and
claims that the agent should merely “be Lean,” “be antifragile,” or “be
pragmatic.”

A valid principle changes behavior beyond the source incident while staying
inside its evidenced scope. Examples of principle shapes include:

- complete one recipient-visible increment and read it back before opening
  another implementation branch;
- for a heuristic fitted to sampled inputs, bound its authority to those inputs,
  preserve an established fallback, and expose a local weaker result when it
  misfires;
- retain a safeguard only while it names a current failure, reaches the
  affected path, and remains cheaper than the consequence it contains;
- place a mechanical invariant in an executable gate and keep `AGENTS.md` for
  judgments the gate cannot select.

These are shapes, not default repository policy. Admit only the instance backed
by the frozen evidence.

## Validate the changed behavior

1. Freeze a representative task containing the plausible default, competing
   context, intended choice, allowed scope, and observable completion signal.
2. Run the target harness from the context an affected agent actually receives.
3. Verify that the principle changes the intended choice without creating an
   unrelated ritual, broader prohibition, or premature stop.
4. Verify an unseen case when the causal rationale is expected to transfer.
5. Record `UNVALIDATED` when the representative harness or observation is
   unavailable; structural placement and literal compliance are not behavior
   evidence.

Return the evidence record, selected owner, exact principle, validation result,
and one status: `PASS`, `NO-OP`, `BLOCK`, `NEEDS-HUMAN-DECISION`, or
`UNVALIDATED`.
