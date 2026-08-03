# Public contracts, JSDoc, and examples

Types and code can look complete while leaving runtime semantics or a
non-local constraint invisible, and examples can look usable without proving
their setup or result. Use this reference to account for those material gaps,
admit only code-local rationale that protects a real choice, and classify
examples without paraphrasing mechanics already visible to their reader.

- [Contract checklist](#contract-checklist)
- [Code-local documentation](#code-local-documentation)
- [Selective-context authoring decision](#selective-context-authoring-decision)
- [Chesterton's fence test](#chestertons-fence-test)
- [Example integrity](#example-integrity)
- [Source evidence](#source-evidence)

## Contract checklist

For every stable public option, function, class, type, route, command, or error,
account for the applicable facts:

| Field | Question |
| --- | --- |
| Purpose | What reader outcome or capability does it enable? |
| When to use | Which problem or deployment needs it? |
| Input | What type, values, format, or preconditions apply? |
| Default or required state | What happens if it is absent or invalid? |
| Behavior | What observable effect does it have? |
| Failure | Which errors, statuses, rejections, or disabled behavior occur? |
| Interaction | Which options, routes, lifecycle states, or security rules alter it? |
| Boundary | What does it explicitly not authorize, store, validate, or affect? |
| Example | Does ambiguity remain after the factual contract? If so, show a minimal verified use. |

Readable signatures, types, schemas, generated reference, and existing
canonical surfaces count as coverage when they expose a fact safely. Do not
give every field equal prose. Add only the smallest precise explanation needed
for safe use. Use a predictable field order and stable terms for comparable
entries. Omit inapplicable fields rather than filling them with vague prose.

## Code-local documentation

Code, types, names, nearby tests, and applicable local context documentation
usually reveal local what and how. Make
code-local documentation earn its place by preserving public semantics or
rationale that a selective reader cannot recover reliably. Assume a maintainer
or coding agent may inspect only one symbol, nearby lines, and search matches
rather than read every related file. An unfamiliar effect of a called
abstraction is not automatically a gap at its caller; inspect its canonical
local documentation and route the reader there. That abstraction owns its
contract and implementation. A durable, repository-specific convention around
an otherwise familiar abstraction may instead earn a concise local explanation
at the smallest context owner that the affected reader receives before acting.

Public JSDoc has an additional extracted-reference audience. State what the API
does when generated documentation or IDE help cannot rely on the implementation
body, but do not paraphrase information already encoded precisely by the
signature. At wrap-up, verify the prose on the exposed symbol after barrel
re-exports, overloads, inheritance, declaration emission, or reference
generation; a successful build can still lose it.

Read `locality-ladder.md` before choosing placement. The code-specific rungs
are refined here:

| Locality | Document | Omit |
| --- | --- | --- |
| Line | Which non-locally-visible cause makes a selectable, apparently reasonable local alternative unsafe. | A paraphrase of the expression, an inevitable effect of the selected operation, or remote mechanics with no material consequence here. |
| Block | Why a parallel process, lifecycle state, or other non-local invariant rules out an apparently reasonable reordering, omission, algorithm, or guard. | A translation of the statements or an imagined alternative that current interfaces do not permit. |
| File | Why the file exists, the boundary it owns, and a non-obvious relationship to another subsystem. | A tour of declarations or imports. |
| Exported symbol JSDoc | Purpose and public semantics the signature cannot encode: runtime defaults, failures, lifecycle, ownership, security boundaries, and important interactions. | Type narration, implementation history, or a duplicate reference page. |

Internal symbols need no JSDoc by default. Extractability alone does not justify
low-value prose. Exported-symbol JSDoc is a public-contract surface layered on a
symbol; it does not sit between file and block in the locality ladder.

### Selective-context authoring decision

Before writing code-local documentation, identify the applicable local context
the intended reader actually receives, then work as if only the changed symbol,
nearby lines, search matches, and that genuinely available context were visible:

1. Name the code decision available at this site.
2. Identify an alternative that is selectable and appears reasonable under the
   types, interfaces, control flow, and established patterns visible here. An
   imagined redesign is not enough.
3. Establish the implementation detail, parallel process, lifecycle state,
   past event, or future event that is not locally visible and makes that
   alternative unsafe. State its material consequence here.
4. Confirm that this site owns the choice. If the fact only explains how a
   called abstraction stores, emits, or implements the selected operation, do
   not comment its caller. If remote behavior constrains a distinct caller-owned
   choice, preserve only the causal edge and local consequence that remain true
   while the remote implementation changes under the same contract. Keep deeper
   mechanics with their owner.
5. Protect the verified constraint in the completed result, then settle the
   reef-to-cliff disposition: ask whether clearer names, code, types, API
   shape, structure, or an already-authorized canonical local context
   explanation can turn the hidden reef into a visible cliff by making the
   choice and consequence locally recoverable:
   - When that change is already authorized and in scope, prefer the visible
     constraint and remove only the prose made redundant.
   - Otherwise, place the smallest durable explanation at the decision. An
     established context owner can replace it only when the affected reader
     encounters that context before acting; otherwise retain code-local
     rationale and report the clarity opportunity when useful.
   - Do not turn every admitted fence into a refactoring task. Clear mechanics
     may still carry non-local system meaning that code at this site cannot
     expose.

Write the comment only when evidence establishes a locally selectable,
apparently reasonable alternative and the non-visible cause that makes it
unsafe. Missing local information alone is insufficient: inevitable behavior,
callee semantics without a separate local consequence, and hypothetical
alternate architectures do not create a comment obligation.

Documentation clustered around an area is evidence of uncertainty, not proof
of bad code. It may reveal accidental opacity, essential concurrency or
lifecycle complexity, or an irreducibly non-local influence. Apply the
authoring decision to each encountered fence rather than creating an automatic
comment-removal or refactoring queue.

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

At orchestration level, a future observation in another process can create a
fence here:

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

### Chesterton's fence test

When the reason for code's existence or present form is unknown, treat it as a
Chesterton's fence:

1. Inspect history, callers, tests, runtime effects, and neighboring invariants.
2. If the rationale is verified, return to the selective-context authoring
   decision. Add prose only when a locally reasonable alternative, non-visible
   cause, material consequence, and local owner pass that gate.
3. If the rationale remains unknown and the knowledge gap is accepted, add an
   explicit `TODO` or `FIXME` recording that uncertainty.

Never replace missing knowledge with invented rationale.

## Example integrity

At wrap-up, classify each fenced sample before publication:

| Status | Requirement |
| --- | --- |
| Runnable | Validate unchanged with the closest available build, typecheck, test, doctest, or executable example command. |
| Illustrative | Syntax-check it and state that integration setup is omitted. |
| Partial | Identify omitted surrounding code and link to a complete source example. |
| Pseudocode | Identify it as non-executable before the code fence. |

For a value the reader must substitute, use a descriptive placeholder and
explain it before the fence. Do not call a sample Runnable or copyable if the
reader must delete syntax or infer a replacement. In Partial code, mark an
omission with a language-valid comment rather than an ellipsis.

For runnable samples:

- include or show the imports and definitions needed to paste it;
- use real public names and current option shapes;
- avoid placeholder secrets, paths, or host APIs unless the setup clearly supplies them;
- do not bury essential instructions in comments that a reader may delete;
- state expected behavior and meaningful limitations outside the code fence.

If the repository has no snippet harness, documentation build, or suitable
example test, do not infer that a sample is runnable. At wrap-up, validate as
much as the repository permits, then classify the sample Illustrative or
Partial unless it has been independently executed unchanged. Report the missing
harness as an open maintenance risk.

## Source evidence

Treat source, exported types, tests, generated artifacts, and approved decisions as evidence. Record enough source evidence in the task handoff that another maintainer can re-check contested claims.

If behavior, default, error handling, or scope cannot be verified, do not fill the gap with plausible prose. Mark it as needing product or API clarification.
