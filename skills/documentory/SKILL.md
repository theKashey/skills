---
name: documentory
description: Create, revise, and audit layered software documentation. Use when working on README files, documentation sites, tutorials, how-to guides, API or configuration reference, examples, JSDoc/TSDoc, inline rationale comments, code documentation for maintainers or coding agents, changelogs, migration guides, documentation reviews, or maintenance planning.
---

# Documentory

Create documentation that lets a reader safely understand and use the
completed, verified result.

## Laws

These apply to every path:

1. **Describe the finished state.** Current documentation represents what is
   true when the requested work is complete, not the temporary state or
   sequence used to get there. At exit, verify that account against the
   finished code and artifacts. Changelogs, migration guides, and release
   documentation explain what changed or used to be true.
2. **Verify; never invent.** Check source, exported types, tests, generated
   artifacts, or an explicit product decision. Put evidence beside evaluative
   or comparative claims.
3. **Mark reefs, not cliffs.** Describe invisible behavior, conditions,
   boundaries, failures, and interactions a reader can miss at that rung. Do
   not merely gesture at them, and do not explain mechanics already visible
   there.
4. **Make a map, not a transcript.** Select and relate the present truths the
   reader needs; do not mirror the implementation. Add the different angle
   appropriate to the rung: outsider relevance, internal responsibility, or
   non-obvious local why.
5. **Explain before code.** Treat code as evidence, not the explanation. Keep
   runnable examples copyable, put necessary explanation around them, and label
   deliberately incomplete samples.
6. **Cover the public contract.** Document every stable public item in an
   existing canonical surface or record an explicit, justified exclusion.
7. **Match scope, reader, and placement.** Place each fact at the lowest
   documentation layer that contains every decision, task, or boundary it
   governs. Assume only context available at that layer; orient upward or link
   downward instead of duplicating detail.
8. **Preserve topology and ownership.** Give each detailed fact one canonical
   owner. Do not create or move pages, folders, or navigation without the
   user's authorization; a README may own every necessary content mode.
9. **Expose Chesterton's fences.** A Chesterton's fence is code whose reason for
   existing is unknown: an island of uncertainty. Detect it. If evidence
   verifies the reason, document that rationale; otherwise record the accepted
   uncertainty with an explicit `TODO` or `FIXME`. Never invent rationale.
10. **Disclose progressively.** Add material only when it enables a priority
   task, closes a contract or operational risk, or makes an example safe.
   Delete it when removal costs no safety, clarity, findability, or support.
11. **Leave a publishable result.** Documentation and code must be ready for
    their intended review, merge, or publication without a cleanup operation
    that changes their temporal stance or removes draft scaffolding. Only an
    explicit `TODO` or `FIXME` comment may preserve an accepted gap.
12. **Prove completion.** Validate currentness, coverage, examples, links,
    copy-paste integrity, and the primary reader path at the applicable rung.
    Report evidence, counts, exclusions, untested assumptions, and remaining
    risks.

## Route the request

Choose one primary path. Combine paths only when the request genuinely spans
them, and do not load every reference before starting.

| Request | Start here | Read at the indicated step |
| --- | --- | --- |
| Top-level project or site README or public landing page | [Create or revise current documentation](#create-or-revise-current-documentation) | `references/locality-ladder.md` before classifying the surface; `references/content-architecture.md` before planning the landing path |
| Internal folder, package, module, domain, or service README or technical overview | [Create or revise current documentation](#create-or-revise-current-documentation) | `references/locality-ladder.md` before classifying the governed scope; `references/content-architecture.md` before structuring the technical reader path |
| Tutorial, how-to, explanation, or examples within them | [Create or revise current documentation](#create-or-revise-current-documentation) | `references/locality-ladder.md` before choosing the owning surface; `references/content-architecture.md` before planning the reader path; the example section of `references/api-jsdoc-examples.md` only when code examples are in scope |
| API or configuration reference, or public JSDoc/TSDoc | [Document a public contract](#document-a-public-contract) | `references/locality-ladder.md` before choosing the canonical owner; `references/api-jsdoc-examples.md` before drafting the contract |
| Line, block, or file comments | [Document code-local rationale](#document-code-local-rationale) | `references/locality-ladder.md` before choosing placement; the code-local section of `references/api-jsdoc-examples.md` after identifying missing context |
| Documentation audit, review, release check, or maintenance plan | [Audit documentation](#audit-documentation) | `references/quality-maintenance.md` before scoring or reporting completeness |
| Changelog, migration guide, or release documentation | [Document a change](#document-a-change) | `references/quality-maintenance.md` before the final drift check |

Go directly to the selected procedure. Apply another path only when its artifact
is also in scope.

## Create or revise current documentation

1. Establish the verified starting truth and the authorized state expected when
   the work is complete from package metadata, public exports, types,
   configuration, defaults, errors, tests, explicit decisions, and
   repository-native documentation tooling. Write current documentation toward
   that completed state, then verify that the finished implementation matches
   it. Do not publish a mid-process snapshot or treat an example, private
   helper, or identifier name as proof of public behavior.
2. Read `references/locality-ladder.md`. Classify the governed scope and the
   surface's actual role before writing; do not infer its role from a
   `README.md` filename alone. Identify the reader, available context, prior
   knowledge, task or question, smallest successful outcome, prerequisites,
   dangerous assumptions, and next useful detail.
3. Select explanation density at this decision point:
   - **Guided** for a reader new to the domain or library: define unfamiliar
     terms, make prerequisites and results explicit, and show one safe primary
     path.
   - **Balanced** for a mixed or unspecified audience: give concise orientation,
     non-obvious choices, boundaries, and contextual links. This is the default.
   - **Compressed** for a known expert audience: retain the contract,
     prerequisites, effect, boundary, and only the example or link needed to
     remove ambiguity.
   Density never changes truth. Keep required defaults, failures, security
   boundaries, and setup at every level; do not put Guided explanation inside
   copyable code.
4. Read `references/content-architecture.md`. Use Diátaxis as a lens for the
   reader's question, not as a required file or folder structure. Work in the
   existing documentation topology. If the README is the only public surface,
   improve it in place. Propose a split with benefits and maintenance cost only
   when distinct reader intents justify it; let the user decide unless
   restructuring is already in scope.
5. For a top-level project or site landing surface, start with outsider-facing
   why: the problem, intended audience, supported outcome, scope, and
   non-goals. Make a concise, verified case for relevance before asking the
   reader to take the first action, then lead to the smallest honest first
   success and deeper paths.
6. For an internal folder, package, module, domain, or service surface, start
   with technical why: its responsibility in the containing system, owned
   boundary, interactions, and constraints. Do not inject project-level sales
   copy or external installation unless the unit is also independently
   published.
7. Write the minimum sufficient explanation. Describe effect, condition, and
   relevant boundary; put evidence beside evaluative or comparative claims.
   Add material only when it enables a priority task, closes a contract or
   operational risk, or makes an example safe. Apply a deletion test to
   everything else.
8. For API or configuration reference, continue with [Document a public
   contract](#document-a-public-contract). For an example inside another
   document, read the example section of `references/api-jsdoc-examples.md` and
   apply only steps 5–6 of that procedure. Then finish with [Verify every
   completed path](#verify-every-completed-path).

## Document a public contract

1. Inventory every stable public option, export, route, command, relevant
   error, and example in scope. Determine stability from declared package
   exports, generated interfaces, route or command schemas, tests, support
   policy, or an explicit product decision. Treat unclear accidental or
   experimental status as a decision gap, not a silent exclusion.
2. Read `references/locality-ladder.md` to choose the canonical owner, then
   `references/api-jsdoc-examples.md`. For each public item, document the
   applicable purpose, use case, inputs, required or default state, observable
   behavior, failures, interactions, and boundary. Use the smallest precise
   contract; do not give every field equal prose.
3. Put each detailed fact in one existing canonical surface. Orient and link
   elsewhere. Do not create a new reference page, folder, or navigation entry
   unless the user authorized it. When a README is the only public surface, let
   it own the required reference section.
4. Use public JSDoc or TSDoc for semantics a signature cannot encode reliably,
   such as runtime defaults, errors, lifecycle, ownership, security boundaries,
   and important interactions. Do not paraphrase types or duplicate the
   reference manual.
5. For public JSDoc or TSDoc, verify that the semantics appear on the actual
   exported symbol through re-exports, overloads, inheritance, and the
   repository's generated-reference, emitted-declaration, or IDE-visible
   surface. A successful code or documentation build alone is not proof.
6. Explain a non-trivial example before its code: state the reader goal,
   prerequisites, and why its meaningful choices exist. Keep runnable code
   complete and free of commentary readers must delete. After it, state the
   result, relevant limit, and next path.
7. Classify each sample as Runnable, Illustrative, Partial, or Pseudocode using
   the reference requirements. Never call a sample Runnable unless it was
   validated unchanged with its imports, setup, public names, options, and
   expected behavior.
8. Account for every inventoried item or record an explicit, justified
   exclusion. Then finish with [Verify every completed
   path](#verify-every-completed-path).

## Document code-local rationale

1. Inspect the governed symbol or block, nearby lines, relevant types and tests,
   and search matches. Assume the next maintainer or coding agent may see only
   that selective context.
2. Identify the important non-local purpose, invariant, ownership boundary, or
   rejected alternative missing from that view. Name the plausible but wrong
   edit its absence could invite. If neither hidden rationale nor unexplained
   code exists, add no comment.
3. Treat code whose reason for existing or taking its present form is unknown as
   a Chesterton's fence. Search history, callers, tests, runtime effects, and
   neighboring invariants for its rationale.
4. Read `references/locality-ladder.md`, then the code-local documentation
   section of `references/api-jsdoc-examples.md`. Place the smallest durable
   explanation at the line, block, or file rung that governs the decision.
   Treat exported-symbol JSDoc as a public-contract overlay, not another
   locality rung.
5. If evidence verifies the reason, explain the non-local cause and relevant
   consequence. Do not narrate visible mechanics.
6. If the reason remains unknown and the gap is accepted, record that
   uncertainty with an explicit `TODO` or `FIXME`. Do not manufacture rationale.
7. Remove rationale when clearer code, a type, or the same local context makes
   it reliably recoverable. Internal symbols need no JSDoc by default. Finish
   with [Verify every completed path](#verify-every-completed-path).

## Audit documentation

1. State the audit mode and scope. For a change-set audit, inventory every
   changed public item and affected surface. For a completeness audit, inventory
   every stable public item and relevant surface in the stated boundary.
   Establish current truth, canonical facts, examples, code-local rationale,
   and repository-native verification commands.
2. Read `references/locality-ladder.md` and
   `references/quality-maintenance.md`. Compare the evidence with the
   documentation for currentness, contract coverage, locality fit, minimum
   sufficient explanation, reader paths, claim evidence, example integrity,
   context resilience, and navigation health.
3. Distinguish present-contract defects from missing change history and from
   missing code-local rationale. Do not recommend the same prose in all three
   places.
4. Report evidence and counts by surface, plus intentional exclusions, untested
   assumptions, and remaining risks. Do not claim completeness from tone,
   length, or a generic readability score.
5. Do not edit during a review-only request. If changes are authorized, route
   each defect to the applicable procedure above before editing.

## Document a change

1. Inspect the changed behavior and its evidence. Determine whether it affects
   public exports, types, configuration, defaults, CLI, routes, errors,
   security, persistence, lifecycle, compatibility, installation, supported
   runtimes, examples, or generated API inputs.
2. Record one outcome for each impact: update current documentation; update a
   changelog or migration guide; update public JSDoc or code-local rationale; or
   no documentation impact, with evidence.
3. Keep time domains separate. Write current documentation in present tense as
   the completed change: what the library is and does when the work exits.
   Changelogs, migration guides, and release documentation describe what
   changed or used to be true. Do not leave former names, removed behavior,
   mid-process caveats, or vague temporal phrases in current reference
   material.
4. Use only existing or explicitly authorized surfaces. Route current-contract,
   public-API, and code-local updates through their procedures above.
5. Read `references/quality-maintenance.md`, perform the applicable drift and
   release checks, and finish with [Verify every completed
   path](#verify-every-completed-path).

## Verify every completed path

For audits, release preparation, or work spanning multiple documentation
surfaces, read `references/quality-maintenance.md` for the complete scorecard.
For every completed path, verify the applicable minimum:

1. Check the completed behavior against code, types, tests, generated artifacts,
   or an approved product decision.
2. Account for every public export, option, route, error, command, and
   documentation surface in the stated scope. In a change-set scope, this means
   every changed or affected item.
3. Confirm that each unit in scope gives its reader enough relevance, behavior,
   evidence, and boundary to act without unsafe inference.
4. Confirm that code-local prose preserves necessary non-local context without
   narrating visible mechanics. Every Chesterton's fence in scope has either a
   verified rationale or an explicit accepted `TODO` or `FIXME` recording that
   its rationale is unknown.
5. Confirm that public JSDoc or TSDoc semantics remain attached to the intended
   exported symbol in the actual extracted or IDE-visible surface.
6. Build or typecheck examples and documentation when supported. Validate the
   primary path from its documented starting state: installation and first
   success for a landing surface; entry points and technical workflows for an
   internal surface. Otherwise report the assumptions that remain untested.
7. Check links, code-fence status, terminology, defaults, historical leakage,
   mid-process wording, and copy-paste integrity.
8. Apply the exit gate: the documentation and code can enter their intended
   review, merge, or publication without editing away temporary caveats,
   placeholders, draft scaffolding, or future-tense completion. Permit an open
   gap only when an explicit `TODO` or `FIXME` comment accepts it.
9. Report updated surfaces, intentional omissions, validation run, counts,
   remaining risks, and future maintenance triggers.

Prefer repository-native link, documentation-build, typecheck, doctest, and
example commands. Add custom automation only after repeated use shows that a
mechanical check cannot otherwise be performed reliably.
