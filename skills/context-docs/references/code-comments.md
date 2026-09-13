# Code comments

A line, block, or file comment earns its place only by preserving a cause the
code around it cannot show. Load this reference once SKILL.md's code-comment
gate holds: it settles where the comment belongs, who owns the choice, and
whether clearer code can retire the prose instead. JSDoc on an in-scope
public-contract symbol is a public surface rather than a code comment; it is
governed by [symbol JSDoc](symbol-jsdoc.md).

- [Where a comment belongs](#where-a-comment-belongs)
- [Selective-context authoring decision](#selective-context-authoring-decision)
- [Chesterton's Fence test](#chestertons-fence-test)

## Where a comment belongs

Code, types, names, nearby tests, and applicable local context documentation
usually reveal local what and how. Make code-local documentation earn its place
by preserving public semantics or rationale that a selective reader cannot
recover reliably. Assume a maintainer
or coding agent may inspect only one symbol, nearby lines, and search matches
rather than read every related file. An unfamiliar effect of a called
abstraction is not automatically a gap at its caller; inspect its canonical
local documentation and route the reader there. That abstraction owns its
contract and implementation. A durable, repository-specific convention around
an otherwise familiar abstraction may instead earn a concise local explanation
at the smallest context owner that the affected reader receives before acting.

Use the code-specific placement below. Read the [locality
ladder](locality-ladder.md) only when the owner or line/block/file scope remains
unresolved:

| Locality | Document | Omit |
| --- | --- | --- |
| Line | Which non-locally-visible cause makes a selectable, apparently reasonable local alternative unsafe. | A paraphrase of the expression, an inevitable effect of the selected operation, or remote mechanics with no material consequence here. |
| Block | Why a parallel process, lifecycle state, or other non-local invariant rules out an apparently reasonable reordering, omission, algorithm, or guard. | A translation of the statements or an imagined alternative that current interfaces do not permit. |
| File | Why the file exists, the boundary it owns, and a non-obvious relationship to another subsystem. | A tour of declarations or imports. |

## Selective-context authoring decision

SKILL.md holds the first three steps—the site's decision, a selectable and
apparently reasonable alternative, and the non-visible cause that makes it
unsafe—and most candidates end there. Continue once all three hold:

4. Confirm that this site owns the choice. If the fact only explains how a
   called abstraction stores, emits, or implements the selected operation, do
   not comment its caller. If remote behavior constrains a distinct caller-owned
   choice, preserve only the causal edge and local consequence that remain true
   while the remote implementation changes under the same contract. Keep deeper
   mechanics with their owner.
5. Protect the verified constraint in the completed result, then settle the
   invisible-reef-to-visible-cliff disposition: ask whether clearer names,
   code, types, API
   shape, structure, or an already-authorized canonical local context
   explanation can turn the invisible reef into a visible cliff by making the
   choice and consequence locally recoverable:
   - When that change is already authorized and in scope, prefer the visible
     constraint and remove only the prose made redundant.
   - Otherwise, place the smallest durable explanation at the decision. An
     established context owner can replace it only when the affected reader
     encounters that context before acting; otherwise retain code-local
     rationale and report the clarity opportunity when useful.
   - Do not turn every admitted invisible reef into a refactoring task. Clear
     mechanics
     may still carry non-local system meaning that code at this site cannot
     expose.

Documentation clustered around an area is evidence of uncertainty, not proof
of bad code. It may reveal accidental opacity, essential concurrency or
lifecycle complexity, or an irreducibly non-local influence. Apply the
authoring decision to each candidate invisible reef rather than creating an
automatic comment-removal or refactoring queue.

Useful rationale connects a constraint to its non-local cause and, when useful,
the consequence of the apparent alternative. This illustrative comment omits
surrounding imports and definitions; it is a rationale pattern, not a complete
program:

```ts
// Canonicalize before hashing: adapters do not guarantee iteration order, but
// replicas must derive the same digest.
const digest = hash(canonicalize(entries));
```

`Sort before hashing` would merely narrate the code. The example preserves the
cross-adapter reason a local scan would otherwise miss.

Business logic more often explains itself. A guard such as
`if (order.isCancelled) return` needs no comment when the domain state and
surrounding policy already reveal why processing stops.

At orchestration level, a future observation in another process can create an
invisible reef here:

```ts
// Publish the index before exposing its pointer; readers resolve new pointers immediately.
await publishIndex(next);
await switchPointer(next.id);
```

Both orders may be locally selectable. The comment preserves the non-local
reader behavior and its consequence here, not the reader process's mechanics.

By contrast, this call needs no comment saying that timings are stored on the
end event:

```ts
await endMeasurement(0, { timings });
```

That statement would describe the selected abstraction's contract, not a
caller-owned choice. If the contract is unclear, its owning API is the
documentation location.

## Chesterton's Fence test

When the reason for code's existence or present form is unknown, treat it as
Chesterton's Fence and preserve the current form while investigating:

1. Inspect history, callers, tests, runtime effects, and neighboring invariants.
2. If the rationale is verified, return to the selective-context authoring
   decision. Add prose only when a locally reasonable alternative, non-visible
   cause, material consequence, and local owner pass that gate.
3. If the rationale remains unknown and the knowledge gap is accepted, add an
   explicit `TODO` or `FIXME` recording that uncertainty.

Never replace missing knowledge with invented rationale.
