# Review documentation at wrap-up

Finished non-inline documentation can still contradict its completed contract,
omit an affected surface, or strand its reader on an untested path. Use this
guide to decide whether the finished documentation is publishable and expose
the smallest remaining defect or risk.

Exclude line, block, and file comments; JSDoc on an established
public-contract symbol remains a public-contract surface.

For an audit, release, or a material risk requiring a detailed gate—including
changed cross-surface contracts, ownership, or reader paths—load [quality and
maintenance](quality-maintenance.md) and apply its evidence scorecard. Once
delegated, return only that workflow's terminal result and do not come back to
this compact guide. Surface count alone does not require escalation; bounded
mechanical edits across several surfaces use the applicable minimum:

1. Check documented claims against source, exported types, tests, generated
   artifacts, and explicit decisions in the surface's time domain: completed
   product behavior, historical facts, or a working record's observed state.
   Resolve or report contradictions.
2. Account for every item, example, and documentation surface in the stated
   scope. When public-contract coverage is in scope, use the member set supplied
   by the task or its established owner rather than deriving membership. In a
   change-set scope, account for every changed or affected item and each
   justified exclusion.
3. Confirm that each surface gives its intended reader enough relevance,
   behavior, evidence, and boundary to act without unsafe inference. When a
   task-local story contract governed the change, verify the opening, major
   sections, proof, limits, and completion route against it. Apply the
   [separation test](content-architecture.md#separation-tests) for each
   surface's mode.
4. When public JSDoc or TSDoc is in scope, verify that its semantics remain on
   the intended in-scope symbol in the actual extracted, emitted, generated, or
   IDE-visible surface. A successful build alone is not proof.
5. Build or typecheck examples and documentation when supported. Classify each
   sample and validate the primary reader path from its documented starting
   state. On a human-facing entry surface, also inspect the rendered or
   delivered form for the [attention
   anchors](content-architecture.md#focus-and-attention-management) that let a
   reader scanning from that entry notice the primary subject, path, and
   necessary boundary before secondary detail. Report any setup, access,
   credential, or environment assumption that remains untested.
6. Check links, navigation, code-fence status, terminology, defaults, historical
   leakage, source-to-artifact register leakage, mid-process wording, and
   copy-paste integrity.
7. Apply the [end-state exit gate](#end-state-exit-gate).

## End-state exit gate

For a working document, handoff, or continuation note, check the
[working-record completion contract](content-architecture.md#working-documents-and-handoffs):
the record must be ready to use, with verified state, open work, uncertainty,
and the next action. Relevant temporary state and pending actions are part of
that result; unfinished record scaffolding is not.

For product documentation, write the contract expected when the requested work is
complete. It may temporarily lead the implementation while both are being
edited, but it must not claim completion until the final code, generated
artifacts, and documented behavior agree.

Reject a product-documentation result that requires another edit merely to:

- replace future tense with the completed contract;
- remove notes about temporary repository, branch, rollout, or access state;
- remove caveats, prerequisites, or version narration caused only by a
  temporary mismatch among checkout, registry, publication, or release state;
- move a secondary demo procedure out of a top-level README's primary scan path
  when an established example or how-to owner can carry the detail;
- delete draft labels, placeholders, commented-out scaffolding, or instructions
  to finish the work later; or
- reveal content that was intentionally hidden during implementation.

A supported transitional state in the finished product is not implementation
residue. Document it when it is part of the verified contract.

Report updated surfaces, intentional omissions, validation run, counts,
wrap-up result, untested assumptions, remaining risks, and future maintenance
triggers. Complete with a publishable result, a bounded defect routed to its
owning workflow, or the smallest unresolved truth or authority decision.

Prefer repository-native link, documentation-build, typecheck, doctest, and
example commands. Add custom automation only after repeated use shows that a
mechanical check cannot otherwise be performed reliably.
