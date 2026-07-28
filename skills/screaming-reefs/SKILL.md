---
name: screaming-reefs
description: Use when an authorized change should enforce a documented constraint through names, types, API shape, or structure—for example replacing a warning comment with a checked owner; not when prose must remain the only owner.
---

# Screaming Reefs

Turn a verified reef into a cliff: give a documented constraint a
structural owner the affected reader cannot miss.

- **Reef** — the material hidden cause and consequence behind a documented
  constraint: what makes an apparently reasonable local action unsafe.
- **Cliff** — meaning already visible and safely recoverable from the
  reader's local context: code, names, types, signatures, structure.
- **Readback** — re-reading the changed decision with only the affected
  reader's genuinely available context (a file, diff, symbol, or search
  entry — not the full repository) and confirming the constraint, the safe
  action, and the protected boundary are recoverable from it.

## Authorization test

Authorized scope is the requested outcome plus the files, symbols, contracts,
and behavior changes explicitly named or unambiguously required to achieve it.
Everything else — including adjacent behavior, public contracts, generated
outputs, paths, and ownership — is preserved by default.

Discovery is not authorization: a clarity opportunity reported by a
documentation pass, a reviewer note, or this skill's own analysis
authorizes nothing by itself. When the smallest sufficient owner exceeds
the authorized scope, stop and return `NEEDS-HUMAN-DECISION` naming the
wider scope; never widen silently.

## Freeze the reef

1. Read the affected code, names, types, exports, tests, configuration,
   callers, and nearby documentation before choosing a shape.
2. Write a compact evidence record for the current state:

   ```text
   Constraint: [what must remain true]
   Evidence: [source, test, contract, history, or explicit decision]
   Unsafe inference: [what a reader could reasonably do incorrectly]
   Authorized scope: [files, symbols, topology, allowed behavior change]
   Readback: [what will show the constraint is visible and preserved]
   ```

3. Preserve the shortest verified `X because Y` before editing. An
   unexplained constraint is a Chesterton's Fence: search history,
   callers, tests, and neighboring invariants for its reason. If evidence
   is still absent or conflicting, return `BLOCK` and keep the existing
   explanation.

## Choose the visible owner

Select the smallest stable structure that carries the constraint for
every affected reader:

| Constraint becomes visible as | When it is the right owner |
| --- | --- |
| Domain names and vocabulary | Readers must recognize a concept or responsibility that callers currently infer. |
| Types, states, invariants, constructors | An invalid state or unsafe transition should be difficult or impossible to express. |
| API shape, exports, routes, capability boundaries | Callers need a contract that a warning cannot reliably deliver. |
| Module, package, or ownership boundaries | Responsibility is being inferred from organizational memory instead of the tree. |
| Filesystem topology | Discovery, selective loading, or agent context depends on where the truth lives. |
| Canonical local context documentation | A durable repository convention where the reader's route guarantees receipt before acting: the document governs the decision's directory (`AGENTS.md`, package README) or is loaded by the agent's context rules. A symbol-, diff-, or search-entry reader does not receive it and needs a structural or code-local owner. |

Prefer the narrowest owner that reaches every affected reader. Do not
redesign adjacent architecture, rename unrelated concepts, move files to
make the tree look orderly, or change structure solely to delete a living
local explanation. If the significance is irreducibly non-local, keep the
explanation and return `NO-OP`.

## Make the change

1. Recheck the chosen owner against the frozen authorized scope; a
   breaking change to behavior, a public contract, a generated output, a
   path, or ownership requires explicit authority.
2. Apply the smallest structural change that makes the constraint
   selectable from local context. Update tests, generated artifacts,
   imports, exports, and repository-native indexes only when the change
   requires them; repository-native indexes are generated or convention-bound
   listings such as barrel exports, route tables, codeowners, and manifests.
   Keep unrelated cleanup out of the diff.
3. Give the changed local context to a fresh reader with no drafting history:
   an isolated subagent or new session that receives only the artifact named in
   the Readback field. It must recover the constraint, safe action, and
   protected boundary without the evidence record or producer explanation. If
   it cannot, retain the prose, restore the working tree to the pre-edit state,
   keep the rejected patch out of the deliverable (for example as an unapplied
   diff or unmerged branch), and return `BLOCK` naming any file the restore
   could not safely revert.

## Retire only redundant prose

After a fresh-context readback passes, delete a sentence when its meaning is fully
carried by the changed structure or by canonical local context the
affected reader actually receives. Retain the causal edge structure still
cannot express — the remote cause, consequence, failure mode, ownership
relationship, or external contract — phrased at the stable contract edge
that stays true while the remote implementation changes. Update nearby
prose the change makes false; do not replace a reef with a vague summary.

## Verify and return

Run the repository-native formatter, typecheck, lint, tests, generators,
and documentation checks covering the changed surface. Confirm the
constraint has a structural owner, a fresh-context readback passes for every
affected reader context the change touches (file, diff, symbol, or search
entry), behavior and public contracts match the authorized scope, no
stale names, imports, paths, or duplicate instructions remain, and the
diff contains no unauthorized files.

Whichever section produced the outcome, including an early `NO-OP` or `BLOCK`,
end here: emit the evidence record and one return code as the last line of the
wrap-up report and any PR description:

- `PASS` — an authorized structural change made the constraint locally
  visible, preserved, and covered by the checks above.
- `NO-OP` — structure already exposes the meaning, or the reef is
  irreducibly non-local and stays documented.
- `BLOCK` — evidence, checks, or the readback fail to establish the
  constraint.
- `NEEDS-HUMAN-DECISION` — authority, ownership, scope, or a breaking
  contract choice is unresolved.
