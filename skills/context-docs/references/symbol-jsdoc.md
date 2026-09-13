# Public-contract symbol JSDoc

Use this reference when a change touches JSDoc or TSDoc on a public-contract
symbol and no reference page, contract inventory, or example is in scope; when
one is, follow [public contracts](public-contracts.md) and return here for each
symbol. The docblock is a surface layered on the symbol, not a scope between
file and block in the locality ladder; line, block, and file comments are
governed by the code-comment gate in SKILL.md instead.

- [Establish membership](#establish-membership)
- [Write what the signature cannot encode](#write-what-the-signature-cannot-encode)
- [Route an entry-point symbol to its owner](#route-an-entry-point-symbol-to-its-owner)
- [Verify on the consumer surface](#verify-on-the-consumer-surface)

## Establish membership

Public-contract membership is supplied by the task or the environment's
established API owner, and SKILL.md's route ends for a symbol outside it. A
language-level export, barrel re-export, top-level placement, or absent export
map does not add a symbol to that scope; when neither the task nor an owner
supplies it, return the missing owner or scope rather than deciding it here.
Any comment an out-of-scope symbol still needs is a code comment under
SKILL.md's gate.

## Write what the signature cannot encode

Generated documentation and IDE help deliver the docblock without the
implementation body. Document purpose and the public semantics the signature
cannot encode reliably—runtime defaults, failures, lifecycle, ownership,
security boundaries, and important interactions—plus a resolvable route to the
page that owns the rest. Omit type narration, implementation history, and a
reference page restated here instead of linked; extractability alone does not
justify low-value prose. When the signature and the existing docblock already
expose every fact safely, change nothing. When no
page owns what the docblock cannot carry, that is a placement question for
[public contracts](public-contracts.md), not a reason to write the page into
the docblock.

## Route an entry-point symbol to its owner

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

## Verify on the consumer surface

Before completion, verify that the prose reaches the intended symbol on the
supplied consumer surface after barrel re-exports, overloads, inheritance,
declaration emission, or reference generation; a successful build can still
lose or misplace it. Resolve each route from the
emitted declarations rather than the working tree, and keep it inside the unit
that ships together: a relative link crossing a published package boundary
resolves in the repository and breaks for an installed consumer. For a change
that touched only symbol docblocks, this check is the wrap-up review; load
[Review documentation at wrap-up](review-documentation-at-wrap-up.md) only when
a page or example changed as well.
