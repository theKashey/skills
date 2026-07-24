# Public contracts, JSDoc, and examples

Public contracts, JSDoc, and examples let readers use an API safely without
reconstructing behavior from implementation. They expose purpose, constraints,
and failures that types and a local code scan cannot reliably show.

Use this reference for public exports, configuration, API documentation, JS or TS JSDoc, and code examples.

- [Contract checklist](#contract-checklist)
- [Code-local documentation](#code-local-documentation)
- [Chesterton's fence test](#chestertons-fence-test)
- [Example integrity](#example-integrity)
- [Verification evidence](#verification-evidence)

## Contract checklist

For every stable public option, function, class, type, route, command, or error, document the applicable facts:

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

Do not give every field equal prose. State the smallest precise contract needed for safe use.
Use a predictable field order and stable terms for comparable entries. Omit
inapplicable fields rather than filling them with vague prose.

## Code-local documentation

Code, types, names, and nearby tests usually reveal local what and how. Make
code-local documentation earn its place by preserving public semantics or
rationale that a selective reader cannot recover reliably. Assume a maintainer
or coding agent may inspect only one symbol, nearby lines, and search matches
rather than read every related file.

Public JSDoc has an additional extracted-reference audience. State what the API
does when generated documentation or IDE help cannot rely on the implementation
body, but do not paraphrase information already encoded precisely by the
signature. Verify the prose on the exposed symbol after barrel re-exports,
overloads, inheritance, declaration emission, or reference generation; a
successful build can still lose it.

Read `locality-ladder.md` before choosing placement. The code-specific rungs
are refined here:

| Locality | Document | Omit |
| --- | --- | --- |
| Line | The external constraint, rejected alternative, or failure consequence at the exact decision it governs. | A paraphrase of the expression or branch. |
| Block | Why ordering, duplication, an unusual algorithm, or a guard is necessary across the statements. | A translation of the statements. |
| File | Why the file exists, the boundary it owns, and a non-obvious relationship to another subsystem. | A tour of declarations or imports. |
| Exported symbol JSDoc | Purpose and public semantics the signature cannot encode: runtime defaults, failures, lifecycle, ownership, security boundaries, and important interactions. | Type narration, implementation history, or a duplicate reference page. |

Internal symbols need no JSDoc by default. Extractability alone does not justify
low-value prose. Exported-symbol JSDoc is a public-contract surface layered on a
symbol; it does not sit between file and block in the locality ladder.

### Selective-context test

Review code-local documentation as if only the changed symbol, nearby lines,
and search matches were visible:

1. Identify the important purpose, invariant, ownership boundary, or rejected
   alternative that disappears from that view.
2. Name the plausible but incorrect edit its absence could invite.
3. Place the smallest durable explanation at the decision the fact protects.
4. Remove the comment when clearer code, a type, or the same local context makes
   it reliably recoverable.

A comment passes when it exposes information unavailable locally, prevents a
concrete plausible mistake, sits beside the governed decision, and remains true
when incidental implementation details change.

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

### Chesterton's fence test

When the reason for code's existence or present form is unknown, treat it as a
Chesterton's fence:

1. Inspect history, callers, tests, runtime effects, and neighboring invariants.
2. If the rationale is verified, explain its non-local cause and consequence at
   the governed decision.
3. If the rationale remains unknown and the knowledge gap is accepted, add an
   explicit `TODO` or `FIXME` recording that uncertainty.

Never replace missing knowledge with invented rationale.

## Example integrity

Classify each fenced sample before publication:

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
example test, do not infer that a sample is runnable. Validate as much as the
repository permits, then classify the sample Illustrative or Partial unless it
has been independently executed unchanged. Report the missing harness as an
open maintenance risk.

## Verification evidence

Treat source, exported types, tests, generated artifacts, and approved decisions as evidence. Record enough source evidence in the task handoff that another maintainer can re-check contested claims.

If behavior, default, error handling, or scope cannot be verified, do not fill the gap with plausible prose. Mark it as needing product or API clarification.
