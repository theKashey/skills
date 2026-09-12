# Public contracts, JSDoc, and examples

Types and code can look complete while leaving runtime semantics or a
non-local constraint invisible, and examples can look usable without proving
their setup or result. Use this reference to account for those material gaps,
admit only code-local rationale that protects a real choice, and classify
examples without paraphrasing mechanics already visible to their reader.

- [Document a public contract or standalone example](#document-a-public-contract-or-standalone-example)
- [Contract checklist](#contract-checklist)
- [Prepare a non-trivial example](#prepare-a-non-trivial-example)
- [Code-local documentation](#code-local-documentation)
- [Route an entry-point symbol to its owner](#route-an-entry-point-symbol-to-its-owner)
- [Selective-context authoring decision](#selective-context-authoring-decision)
- [Chesterton's Fence test](#chestertons-fence-test)
- [Example integrity](#example-integrity)
- [Source evidence](#source-evidence)

## Document a public contract or standalone example

Use this workflow for an API or configuration reference, public JSDoc or
TSDoc, or a standalone public API, configuration, or code example.

1. Start with the public-contract scope supplied by the task or the
   environment's established API owner. Inventory its options, symbols, routes,
   commands, relevant errors, and examples. Treat membership as an input to this
   workflow: do not infer or expand it from source-level or barrel exports,
   top-level placement, or the absence of a package export map. When neither the
   task nor an owner supplies the scope, return that missing owner or scope
   instead of classifying symbols.
2. Put each detailed fact in its established existing owner and orient and link
   elsewhere. Read the [locality ladder](locality-ladder.md) only when
   existence, ownership, scope, or placement remains unresolved; return its
   placement proposal rather than creating a reference page, record, folder, or
   navigation entry without authority.
3. Apply the [contract checklist](#contract-checklist) to every inventoried
   item. Count readable signatures, types, schemas, generated references, and
   existing canonical surfaces as coverage when they expose the semantics
   safely. An example, private helper, or identifier name is not proof of
   public behavior.
4. Use public JSDoc or TSDoc only for semantics the signature cannot encode
   reliably. Keep type narration and duplicate reference prose out of the
   symbol contract.
5. For a non-trivial example, follow [Prepare a non-trivial
   example](#prepare-a-non-trivial-example). During authoring, record each
   explicit, justified exclusion when it is identified.
6. After implementation and non-inline documentation are complete, follow
   [Review documentation at wrap-up](review-documentation-at-wrap-up.md). At
   that point, reconcile the inventory, verify public JSDoc on the actual
   in-scope consumer surface, classify examples, and run supported deterministic
   checks.

Complete with accounted-for public semantics, an evidence-backed exclusion or
no-op, a proposal for the established owner, or the smallest unresolved
contract fact or externally owned scope decision.

## Contract checklist

For every option, function, class, type, route, command, or error in the
supplied public-contract scope, account for the applicable facts. Public
membership is established outside this workflow; a language-level export does
not add an item to that scope.

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

## Prepare a non-trivial example

Before the code, state the reader outcome, prerequisites and assumed surrounding
context, and why the selected API or option belongs in this example. Keep
runnable code complete and free of commentary readers must delete.

After the code, state the expected result, a meaningful limit, ownership
boundary, or failure case, and the next useful path. Do not narrate every line.
Apply the [selective-context authoring
decision](#selective-context-authoring-decision) to code comments, and retain an
admitted comment only when it remains true after the sample is copied.

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

JSDoc on an in-scope public-contract symbol has an additional
extracted-reference audience. State what the API does when generated
documentation or IDE help cannot rely on the implementation body, but do not
paraphrase information already encoded precisely by the signature. At wrap-up,
verify the prose on the supplied consumer surface after barrel re-exports,
overloads, inheritance, declaration emission, or reference generation; a
successful build can still lose it.

Use the code-specific placement below. Read the [locality
ladder](locality-ladder.md) only when the owner or line/block/file scope remains
unresolved:

| Locality | Document | Omit |
| --- | --- | --- |
| Line | Which non-locally-visible cause makes a selectable, apparently reasonable local alternative unsafe. | A paraphrase of the expression, an inevitable effect of the selected operation, or remote mechanics with no material consequence here. |
| Block | Why a parallel process, lifecycle state, or other non-local invariant rules out an apparently reasonable reordering, omission, algorithm, or guard. | A translation of the statements or an imagined alternative that current interfaces do not permit. |
| File | Why the file exists, the boundary it owns, and a non-obvious relationship to another subsystem. | A tour of declarations or imports. |
| Public-contract symbol JSDoc | Purpose and public semantics the signature cannot encode: runtime defaults, failures, lifecycle, ownership, security boundaries, and important interactions; and a resolvable route to the page that owns the rest. | Type narration, implementation history, or a reference page restated here instead of linked. |

Symbols outside the supplied public-contract scope need no public JSDoc by
default. Extractability alone does not justify low-value prose. Public-contract
JSDoc is a surface layered on a symbol; it does not sit between file and block
in the locality ladder.

### Route an entry-point symbol to its owner

A page that explains what the signature cannot carry—which layer a requirement
belongs in, what a fact does and does not establish, what an option gives
up—is reachable context, not received context. An editor hover delivers the
symbol's docblock at the decision and nothing else, so the entry-point symbol
carries the route itself:

```ts
/**
 * User-controlled retention durations. Both values must be positive and finite.
 *
 * @see {@link ../../docs/compaction.md | Compaction}
 *   — when `compactAfterMs` makes compaction mandatory, and what happens to a
 *   replica that stays away past `maxOfflineMs`.
 */
```

Use the environment's machine-readable form so tooling delivers it. The line
after the link states what the page settles that the signature cannot; a
boundary is usually its sharpest form. A bare `@see ../../docs/compaction.md`
is a filename, not a route.

Drive coverage from the published pages, not from the symbols: check that every
shipped page has at least one entry-point symbol reaching it. Most symbols take
no route. A page whose every reader arrives through another page that is already
routed needs no second pointer, and one broader route still outranks a copy at
every caller.

Verify each route against the artifact the reader receives rather than the
working tree: resolve it from the emitted declarations, and keep it inside the
unit that ships together. A relative link crossing a published package boundary
resolves in the repository and breaks for an installed consumer.

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

Write the comment only when evidence establishes a locally selectable,
apparently reasonable alternative and the non-visible cause that makes it
unsafe. Missing local information alone is insufficient: inevitable behavior,
callee semantics without a separate local consequence, and hypothetical
alternate architectures do not create a comment obligation.

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

### Chesterton's Fence test

When the reason for code's existence or present form is unknown, treat it as
Chesterton's Fence and preserve the current form while investigating:

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

If behavior, default, error handling, or a contract limit cannot be verified,
do not fill the gap with plausible prose. Mark it as needing product or API
clarification.
