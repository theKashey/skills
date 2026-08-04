# Review documentation at wrap-up

Finished non-inline documentation can still contradict its completed contract,
omit an affected surface, or strand its reader on an untested path. Use this
guide to decide whether the finished documentation is publishable and expose
the smallest remaining defect or risk.

Use this guide once, only after the in-scope implementation and non-inline
documentation are complete. A user request specifically for a non-inline audit
or review is itself a wrap-up task. Never invoke this guide on intermediate
work. Exclude line, block, and file comments; exported-symbol JSDoc remains a
public-contract surface.

If the selected route already loaded the full quality scorecard for an audit or
release, do not use this guide. That scorecard owns terminal completion.

For an audit, release, work spanning multiple non-inline surfaces, or a material
risk that needs a detailed gate, load [quality and
maintenance](quality-maintenance.md) and apply its evidence scorecard. Once
delegated, return only that workflow's terminal result and do not come back to
this compact guide. Otherwise verify only the applicable minimum:

1. Check the completed behavior against source, exported types, tests, generated
   artifacts, and explicit product decisions. Resolve or report contradictions.
2. Account for every public export, option, route, error, command, example, and
   documentation surface in the stated scope. In a change-set scope, account
   for every changed or affected item and each justified exclusion.
3. Confirm that each surface gives its intended reader enough relevance,
   behavior, evidence, and boundary to act without unsafe inference. When a
   task-local story contract governed the change, verify the opening, major
   sections, proof, limits, and completion route against it.
4. When public JSDoc or TSDoc is in scope, verify that its semantics remain on
   the intended exported symbol in the actual extracted, emitted, generated, or
   IDE-visible surface. A successful build alone is not proof.
5. Build or typecheck examples and documentation when supported. Classify each
   sample and validate the primary reader path from its documented starting
   state. Report any setup, access, credential, or environment assumption that
   remains untested.
6. Check links, navigation, code-fence status, terminology, defaults, historical
   leakage, source-to-artifact register leakage, mid-process wording, and
   copy-paste integrity.
7. Apply the [end-state exit gate](#end-state-exit-gate).

## End-state exit gate

Write current documentation as the contract expected when the requested work is
complete. It may temporarily lead the implementation while both are being
edited, but it must not claim completion until the final code, generated
artifacts, and documented behavior agree.

Reject a result that requires another edit merely to:

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
