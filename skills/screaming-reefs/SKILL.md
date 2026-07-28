---
name: screaming-reefs
description: Use when an authorized change must turn a verified documented repository constraint into visible code, types, APIs, ownership boundaries, or filesystem structure.
---

# Screaming Reefs

Turn documented reefs into visible terrain.

## Freeze the reef

1. Identify the documented reef and the decision that depends on its
   explanatory prose or a hard-to-find repository relationship. Read the affected
   code, names, types, exports, tests, configuration, callers, and nearby
   documentation before choosing a shape.
2. Write a compact evidence record for the current state:

   ```text
   Constraint: [what must remain true]
   Evidence: [source, test, contract, history, or explicit decision]
   Unsafe inference: [what a reader could reasonably do incorrectly]
   Authorized scope: [files, symbols, topology, and allowed behavior change]
   Readback: [what will show that the constraint is visible and preserved]
   ```

3. Preserve the shortest verified `X because Y` statement before editing. If
   the reason is still unknown, the evidence conflicts, or the requested
   change does not authorize code or topology mutation, return `BLOCK` or
   `NEEDS-HUMAN-DECISION` and keep the existing explanation.

## Choose the visible owner

Select the smallest stable repository structure that lets the affected reader
make the decision safely in selective context:

- Use domain names or a vocabulary boundary when the missing meaning is a
  concept that callers must recognize.
- Use types, states, invariants, or constructors when an invalid state should
  become difficult or impossible to express.
- Use an API shape, export, route, or capability boundary when callers need a
  contract instead of a warning.
- Use module, package, or ownership boundaries when responsibility is being
  inferred from remote knowledge.
- Use filesystem topology when discovery, selective loading, or agent context
  depends on where the truth lives.

Prefer the narrowest owner that carries the constraint for every affected
reader. Do not redesign adjacent architecture, rename unrelated concepts, or
move files merely to make the tree look orderly. If the significance remains
irreducibly non-local, keep the explanation and return `NO-OP` for this skill.

## Confirm authority and make the change

1. Compare the proposed owner with the frozen authorized scope. Treat behavior,
   public contracts, generated outputs, paths, and ownership as preserved by
   default; a breaking change requires explicit authority.
2. Apply the smallest structural change that makes the constraint selectable
   from local context. Update tests, generated artifacts, imports, exports,
   and repository-native indexes only when the authorized change requires
   them. Keep unrelated cleanup out of the diff.
3. Re-read the changed decision as a human or coding agent would encounter it.
   The local names, types, API, boundary, or topology must carry the constraint
   without requiring the original remote explanation.

## Retire only redundant prose

Remove or shorten documentation only after the structure passes the readback.
Delete a sentence when its meaning is now fully carried by the changed code or
repository topology and the remaining text would repeat a visible cliff.
Retain the causal edge, consequence, failure mode, ownership relationship, or
remote contract that the repository still cannot express. Update nearby prose
when the change makes it false; do not replace a reef with a vague summary.

## Verify the completed terrain

Run the repository's native formatter, typecheck, lint, tests, generators, or
documentation checks that cover the changed surface. Then verify all of the
following:

- the documented constraint has a current structural owner;
- a reader with only the relevant local context can identify the constraint,
  the safe action, and the boundary it protects;
- behavior and public contracts are unchanged unless the authorized scope says
  otherwise;
- no stale names, imports, paths, ownership claims, or duplicate instructions
  remain;
- remaining prose is limited to significance the structure cannot express;
- the diff contains no unauthorized files or opportunistic refactoring.

Return:

- `PASS` when the constraint is locally visible, preserved, and covered by
  representative checks;
- `NO-OP` when the current repository already exposes the meaning or the reef
  must remain documented because it is irreducibly non-local;
- `BLOCK` when evidence, checks, or the local readback do not establish the
  constraint;
- `NEEDS-HUMAN-DECISION` when authority, ownership, scope, or a breaking
  contract choice is unresolved.
