# Public contracts and examples

Types and code can look complete while leaving runtime semantics or a non-local
constraint invisible, and examples can look usable without proving their setup
or result. Use this reference to account for those material gaps on a public
surface and to classify examples without paraphrasing mechanics already visible
to their reader. A docblock on one in-scope symbol is governed by [symbol
JSDoc](symbol-jsdoc.md), which this workflow reaches for each inventoried
symbol; line, block, and file comments are governed by [code
comments](code-comments.md).

- [Document a public contract or standalone example](#document-a-public-contract-or-standalone-example)
- [Contract checklist](#contract-checklist)
- [Prepare a non-trivial example](#prepare-a-non-trivial-example)
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
4. Follow [symbol JSDoc](symbol-jsdoc.md) for each in-scope symbol's docblock.
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
Put each comment in the sample through the code-comment gate, continuing into
[code comments](code-comments.md#selective-context-authoring-decision) when it
holds, and retain an admitted comment only when it remains true after the sample
is copied.

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
