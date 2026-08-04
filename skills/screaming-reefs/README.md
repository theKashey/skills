# Screaming Reefs

Screaming Reefs turns a verified **invisible reef** into a **visible cliff**:
it gives a documented constraint a structural owner — names, types, APIs,
ownership boundaries, or filesystem topology — so humans and coding agents
acting from selective context can recover the constraint without
reconstructing the remote explanation.

The name joins two ideas: screaming architecture (structure should scream
its domain) and "preserve invisible reefs, omit visible cliffs" (prose should
carry only hidden hazards). Where documentation preserves an invisible reef,
this skill makes the constraint visible in structure.

## Why it exists

Important constraints often survive only because a comment, README, or
agent instruction explains them. That prose protects the decision, but it
can be missed in selective context, duplicated away from its owner, or
drift as the repository changes. Screaming Reefs treats the verified
explanation as evidence for an authorized structural change that carries
the same meaning with a local structural owner.

Chesterton's Fence comes first: an existing constraint with an unknown purpose
stays protected while its rationale is investigated. Once verified, the
constraint and its consequence stay protected while the repository is reshaped,
and prose is retired only after the new owner passes a readback from the
affected reader's local context. An invisible reef whose significance is
irreducibly non-local remains documented.

A toy example keeps the remote constraint and structural countermeasure in the
same small context, so it is weak evidence for the intended selective-context
effect. Evaluation needs a fresh reader or agent facing the changed structure
without the producer's explanation, under realistic competing context. Even a
successful local readback establishes recoverability, not safer runtime
behavior in general.

## Worked example

Documented reef at a call site:

```ts
// NOTE: user IDs must be lowercased before comparison — the billing
// exporter lowercases IDs on ingest, so mixed-case comparison silently
// drops rows during reconciliation.
if (a.toLowerCase() === b.toLowerCase()) { ... }
```

Evidence record:

```text
Constraint: user IDs compare case-insensitively everywhere.
Evidence: billing/ingest.test.ts lowercases on ingest; incident PR #482.
Unsafe inference: a new caller compares raw IDs; reconciliation drops rows.
Authorized scope: ids.ts and raw-comparison call sites; no behavior change.
Readback: a coder holding only ids.ts cannot compare unnormalized IDs.
```

Owner: a branded `NormalizedUserId` type whose constructor lowercases and whose
comparison helper accepts that type. The authorized change includes migrating
the named raw-comparison call sites and their tests before restricting the
helper; it does not strand existing callers with a compile error. This is
illustrative pseudocode, not a copyable TypeScript migration.

Retirement: the call-site comment is deleted. One causal edge remains on
the constructor — `Lowercased because the billing exporter lowercases on
ingest; mixed-case comparison drops reconciliation rows.` — because the
remote cause is external to this file and the type cannot express it.

Return: `PASS`.

## Relationship to Context Docs

Context Docs preserves hidden reasons the current structure cannot express
and may report that structure could carry one. Screaming Reefs uses such a
verified explanation as evidence for an explicitly authorized change; the
report itself authorizes nothing. The packages share vocabulary, but
neither runtime package invokes or depends on the other; each defines the
terms it uses.

## Ownership

| File | Owns |
| --- | --- |
| [SKILL.md](SKILL.md) | Activation boundary, vocabulary, authorization test, procedure, owner selection, and return contract |
| [README.md](README.md) | Durable rationale, name provenance, worked example, and boundaries |

## Boundaries

Screaming Reefs does not invent a reason for Chesterton's Fence, decide
product or ownership policy, widen the mutation scope silently, or claim
that structure proves behavior. It preserves existing meaning by default
and stops when authority, evidence, contract compatibility, or the local
readback is unresolved.
