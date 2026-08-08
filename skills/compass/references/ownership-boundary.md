# Ownership Boundary: Compass and Context Docs

Both skills preserve *why*. They own different whys, and this file is the contract between them. It is an ownership test, not a writing-style preference — and it decides placement in both directions, so neither skill ends up restating the other.

Context Docs' canonical-owner principle is the rule being honoured here: complete truth and remote mechanics live with **one** owner, and other encounter points get the smallest route to it. This file only establishes that Compass is one of the possible owners.

## The classifier

For any explanation, ask:

> Would this reason still matter if we threw away the implementation and rebuilt the same logical product?

**Yes** → Compass is a candidate canonical owner.
**No** → if the reason still constrains the current implementation, it is a Context Docs or code-local candidate.

This is the rewrite test applied to rationale instead of to entities.

## What Compass owns

Reasons that survive the rewrite test:

- *Why does Payment Authorisation exist?*
- *Why must Eligibility obey this invariant?*
- *Why is Document Review one logical phenomenon rather than seven?*
- *Why is this a boundary between two bounded contexts?*
- *Why does this consumer rely on that block, and what would make it leave?*

These remain meaningful if the system is reimplemented in another language, framework, or topology.

## What Context Docs owns

Reasons local to this implementation:

- *Why must this acknowledgement happen after persistence?*
- *Why is this retry intentionally here?*
- *Why must this adapter preserve this ordering?*
- *Why does this implementation use this otherwise surprising mechanism?*

These may disappear the moment the implementation changes.

## Do not duplicate Compass semantics into Context Docs

When Compass already owns the full semantic reason, do not reproduce that explanation beside every implementation site. A local code reader often needs only a route:

```ts
// compass: applications.eligibility
```

and, when a consequence cannot otherwise be safely understood before acting, the smallest local edge plus the route:

```ts
// Preserve the domain eligibility boundary.
// compass: applications.eligibility
```

The complete semantic truth stays in Compass. Context Docs decides whether the reader needs a local breadcrumb at all — a coordinate that the reader will actually follow is frequently the whole answer.

## Do not pollute Compass with implementation fences

The inverse rule. Do not add an implementation-specific Chesterton's Fence to the chart merely because the reason is surprising. If

```text
same product semantics
+
different implementation
=
reason disappears
```

then that reason does not belong in semantic Compass. Keep it in code, in implementation documentation, or with whatever canonical owner Context Docs selects.

```text
Must acknowledge the queue after transaction commit because
this queue provides at-least-once delivery.
```

is implementation rationale — the queue can be replaced. But:

```text
A **Finding** must never become visible until its source
**Document Review** has completed.
```

is a Compass-owned invariant. The mechanism enforcing it can change; the rule cannot, without a semantic change.

## Compass as an owner during investigation

Compass answers one of Context Docs' own questions: *where is the established owner of this reason?*

When investigating strange code:

```text
code
  ↓
compass coordinate
  ↓
semantic Compass entity
```

First determine whether the strange implementation is simply enforcing a Compass-owned invariant or responsibility.

- **Yes** → Compass owns the semantic rule. Context Docs adds only the smallest necessary breadcrumb, or nothing.
- **No** → continue investigating the implementation-specific fence under Context Docs.

Checking the coordinate first is what stops agents from repeatedly reverse-engineering domain intent the chart already captured.

## Worked case

The chart states, in `DOMAIN.md`:

> A **Finding** must never become visible until its source **Document Review** has completed.

The implementation enforces it by acknowledging a queue message only after the transaction commits.

Correct placement:

| Truth | Owner |
|---|---|
| **Finding** visibility depends on **Document Review** completion | Compass (`DOMAIN.md`, the invariant) |
| Which block enforces it and where it lives today | Compass (block document, implementation coordinates) |
| Why acknowledgement must follow persistence for *this* queue | Context Docs / code-local |
| The full reasoning, restated in both places | Nobody — this is the failure |

If the queue is replaced with a transactional outbox, the third row is rewritten and the first two are untouched. That asymmetry is what the boundary is protecting.
