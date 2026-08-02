---
name: context-docs
description: Use when creating, revising, or auditing a README, tutorial, how-to, API or configuration reference, changelog, migration guide, docs site, landing page, example, or code comment; not for changing code behavior.
---

# Context Docs

Document fences: recover and preserve the verified reason for a choice,
constraint, boundary, relationship, or structure when that reason is not
visible where a reader encounters it. Document reefs, not cliffs—keep the
hidden why and consequence, not mechanics already in view. Use locality to
explain how each explanation fits the supplied ownership and reader context,
and to propose placement only when ownership is unresolved. The ladder does not
authorize a new surface or override an established owner. When no material gap
remains, add nothing.

## Universal laws

1. **Document fences; preserve reefs, not cliffs.** Explain the verified cause
   that is not locally visible and the material constraint it creates here. The
   cause may live in lower-level implementation, another process, or an earlier
   or later event. Preserve its local consequence, not remote mechanics. The
   hidden reason may govern a code-local choice or a wider purpose, contract,
   failure, interaction, or ownership boundary. Phrase a remote cause at the
   stable contract edge that remains true while its implementation changes. Do
   not transcribe mechanics already visible at the reader's encounter.
2. **Ground claims; never invent.** During authoring, use source, exported
   types, tests, generated artifacts, or an explicit product decision as
   evidence. An unexplained Chesterton's Fence triggers investigation, not a
   plausible story. Put evidence beside evaluative or comparative claims.
3. **Describe the finished state.** Current documentation represents what is
   true when the requested work is complete, not the temporary state or
   sequence used to get there. At wrap-up, verify that account against the
   finished code and artifacts. Changelogs, migration guides, and release
   documentation explain what changed or used to be true.
4. **Lead with reader-relevant why; orient before mechanism.** Open a
   reader-facing surface with the pressure, consequence, responsibility,
   supported outcome, boundary, or changed decision its entering reader needs.
   Make the governed subject and capability inferable, but do not let artifact
   self-description displace the reason to care. A compact chooser or catalog
   entry uses `name: what and why` so a reader can select among subjects. Before
   methodology, taxonomy, workflow, or components, establish the affected
   reader or system, intended observable effect or changed decision, and
   boundary at the subject's owning section. A parent summary does not replace
   local orientation on a standalone subject page.
5. **Make a map, not a transcript.** Select and relate the present truths the
   reader needs; do not mirror the implementation. Add the different angle
   appropriate to the rung: technical orientation, system responsibility, or
   non-obvious local why.
6. **Fit fence explanations to established ownership.** Within the supplied or
   authorized topology, keep each verified hidden reason where every affected
   reader, including a coding agent working from selective context, encounters
   it before the decision, task, or boundary it governs. A fence is relative to
   that reader's genuinely available context, not to the model's general
   knowledge. Follow the environment's established owner and submission route;
   keep detail there and add only the smallest route or local consequence an
   affected reader still needs. Use the ladder to explain or propose a fit when
   ownership is unresolved, never to create a competing owner.
7. **Earn every surface.** Apply the [locality ladder's existence
   gate](references/locality-ladder.md#existence-gate) before adding a README,
   page, reference, or comment. Add nothing when it finds no material reader
   gap.
8. **Keep reader contracts distinct.** Classify technical READMEs, public
   documentation homes, and visitor presentation pages by their actual reader;
   [content architecture](references/content-architecture.md) owns the
   boundary details.
9. **Preserve supplied topology and ownership.** Give each detailed fact one
   established owner. Do not create, move, replace, or duplicate pages, records,
   folders, or navigation without authority. A README may host several content
   modes when it is already the authorized surface; it is not a default owner.
10. **Disclose progressively.** Add material only when it enables a priority
   task, closes a contract or operational risk, or makes an example safe.
   Delete it when removal costs no safety, clarity, findability, or support,
   including when code or canonical local context actually available to the
   affected reader now carries the same decision and boundary.
11. **Leave non-inline documentation publishable.** At wrap-up, meet the
    [end-state exit
    gate](references/quality-maintenance.md#end-state-exit-gate). Code-local
    gaps follow the code-local authoring route, not this gate.
12. **Review once at wrap-up.** Use source evidence while authoring, but run
    documentation review and deterministic documentation completion checks only
    after the in-scope implementation and documentation are complete. Review
    the final non-inline documentation once. Never review line, block, or file
    comments.
13. **Keep construction outside the document.** Document the governed subject,
    not the process used to document it. Do not publish generic claims about
    why a document exists, its maintenance role, or the drafting, review, or
    validation process; nor a bare declaration that it follows Diátaxis or
    another framework. Keep those build-time facts in the authoring record or
    handoff. Include a concrete component map, ownership boundary, or framework
    distinction when it changes the reader's decision or is part of the
    reader's subject or contract.

## Route the request

Choose one primary path. Start its procedure before loading branch-specific
references; the procedure names each reference at the decision where it is
needed. Combine paths only when the request genuinely spans them.

For a post-generation readiness gate over a mixed deliverable, keep this
procedure scoped to documentation truth, coverage, reader paths, and locality.
Do not present its result as verification of the non-documentation parts.

| Request | Start here |
| --- | --- |
| Top-level repository or project README | [Create or revise current documentation](#create-or-revise-current-documentation) |
| Public website landing page | [Create or revise current documentation](#create-or-revise-current-documentation) |
| Public documentation home or docs-site navigation | [Create or revise current documentation](#create-or-revise-current-documentation) |
| Internal folder, package, module, domain, or service README or technical overview | [Create or revise current documentation](#create-or-revise-current-documentation) |
| Tutorial, how-to, explanation, or examples within them | [Create or revise current documentation](#create-or-revise-current-documentation) |
| API or configuration reference, or public JSDoc/TSDoc | [Document a public contract](#document-a-public-contract) |
| Line, block, or file comments | [Document code-local rationale](#document-code-local-rationale) |
| Documentation audit, review, release check, or maintenance plan | [Audit documentation](#audit-documentation) |
| Changelog, migration guide, or release documentation | [Document a change](#document-a-change) |

Apply another path only when its artifact is also in scope.

## Create or revise current documentation

Close a material gap for the named reader in an existing or authorized
non-inline surface so the completed purpose, behavior, boundary, and next route
are safely recoverable. Do not create a surface or publish work-in-progress
merely to satisfy this path.

1. Establish the verified starting truth and the authorized state expected when
   the work is complete from package metadata, public exports, types,
   configuration, defaults, errors, tests, explicit decisions, and
   repository-native documentation tooling. Write current documentation toward
   that completed state. At wrap-up, verify that the finished implementation
   matches it. Do not publish a mid-process snapshot or treat an example,
   private helper, or identifier name as proof of public behavior.
2. Before adding a surface or comment, establish a material reader gap. If
   readable code, types, tests, metadata, local context, or an existing
   canonical surface already lets that reader act safely, add nothing; do not
   manufacture a layer because a project, package, public source, or reader role
   exists. Read `references/locality-ladder.md`. Classify the governed scope and
   the surface's actual role from its reader, available context, and
   responsibility before writing. Identify the reader's prior knowledge, task or
   question, smallest successful outcome, prerequisites, dangerous assumptions,
   and next useful detail. Record the reader, available context, need, scope,
   and placement rationale before outlining; do not infer any of them from a
   filename, root location, public visibility, source host, or license.
   Treat applicable local context as part of the decision surface. Discover the
   repository's established owner and submission route from the instructions,
   links, surfaces, and tooling already supplied to the task; do not assume what
   kind of system owns the record. An unfamiliar local abstraction is a route to
   its owner, not a reason to document each caller. When an owner exists, update
   it within the granted authority or return a proposal for that owner. Do not
   promote the fact into a preferred artifact or create a parallel fallback.
   Add no generic model tutoring, and remove no narrower explanation unless the
   replacement context reliably reaches its reader before the decision.
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
4. For a new or substantially reworked reader-facing non-inline surface, or
   whenever the proposed reader, goal, subject, or surface is questioned, read
   `references/casting.md` and run its intervention gate before outlining.
   Honor its result. Do not draft after `RECAST_READER`, `REVISE_GOAL`,
   `CHANGE_SURFACE`, `CHANGE_SUBJECT`, `NO_DOCUMENT`, or
   `NEEDS_HUMAN_DECISION`; perform or report the required shift first. A bounded
   revision with an explicit, unchallenged cast and story skips this gate.

   Then read `references/content-architecture.md`. Use Diátaxis as a lens for
   the reader's question, not as a required file or folder structure. Work in
   the documentation topology supplied by the environment. A rung or reader
   role never requires a new document. If an existing README is the authorized
   technical surface, improve it in place. Apply visitor-presentation guidance
   only to an actual existing or authorized presentation surface; its absence
   creates no landing-page task. Propose a split with benefits and maintenance
   cost only when the user requests or authorizes restructuring.

   After a `PROCEED` result for a new or substantially reworked reader-facing
   non-inline surface, apply the [authorial intent and story
   contract](references/content-architecture.md#authorial-intent-and-story-contract)
   before outlining, full prose, or visual implementation. Evidence determines
   what the subject can truthfully claim; an explicit user or project decision,
   or an established surface contract, determines why the document should
   speak. If that authority is missing, return the smallest contract-level
   decision instead of inferring intent from mechanics or generating complete
   variants. Once the contract is resolved, align one opening-and-heading
   semantic slice, collapse its readback into one contract, and produce one
   complete route. A bounded revision with an explicit, unchallenged story
   proceeds directly. This alignment is authoring evidence, not the final
   documentation review.
5. When an existing or authorized README is the right owner, treat it as
   technical orientation at its governed rung. Use the reader-contract boundary
   in `content-architecture.md`; do not infer its role from public visibility,
   an open-source license, or the existence of a source repository.
6. For a top-level repository or project README that is the right owner, start
   with technical why:
   what the system or repository is for, its scope, major boundaries, intended
   technical reader, and the verified route relevant to that reader's task.
   Include installation, cloning, or a source quickstart only when it is a
   necessary technical instruction in that route; do not add one as a
   promotional default. A top-level README for an internal product remains a
   technical surface; do not give it product-evaluation or advertising posture.
7. For an actual existing or authorized public website landing page, start with
   visitor-facing why and lead
   to a verified web-native visitor action, such as using the product, trying a
   demo, reading public docs, downloading a client, or contacting the team. Do
   not add a prominent source quickstart, install, clone, package-manager, or
   code path merely because source exists. Keep source as a secondary route
   only when it is verified useful for contribution or self-hosting; when no
   web-native action is verified, use a neutral deeper route rather than invent
   a conversion call to action.
8. For a public documentation home, start with the documentation reader's
   subject, available navigation, and route to the relevant tutorial, how-to,
   explanation, or reference. Browser delivery does not make it a product
   presentation page. At wrap-up, validate a documentation-navigation or
   reference task, not a browser-product conversion path.
9. For an internal folder, package, module, domain, or service surface that is
   the right owner, start with technical why: its responsibility in the
   containing system, owned boundary, interactions, and constraints. Do not
   inject project-level sales copy. Include external installation only when the
   unit is independently published and that instruction is necessary for its
   technical reader.
10. Write the minimum sufficient explanation. For a repository, collection, or
    other chooser surface, lead with why that collection matters to its reader,
    including any organizing relationship needed to interpret it. Present each
    independently selectable subject in compact `name: what and why` form. Before
    internal mechanism, make the fuller situation, impact, and boundary
    inferable at each subject's owning section. A compact catalog entry does not
    need to carry the full diagnosis. Put evidence beside evaluative or
    comparative claims. Add material only when it enables a priority task,
    closes a contract or operational risk, or makes an example safe. Apply a
    deletion test to everything else.
11. For API or configuration reference, continue with [Document a public
   contract](#document-a-public-contract). For an example inside another
   document, read the example section of `references/api-jsdoc-examples.md` and
   apply only steps 6–7 of [Document a public
   contract](#document-a-public-contract). Defer review and deterministic
   documentation checks until [Review documentation at
   wrap-up](#review-documentation-at-wrap-up).

## Document a public contract

Make material public semantics safely recoverable by the contract's consumer at
their established owner. Account for every stable item without paraphrasing
source-owned truth or creating an unauthorized surface.

1. Inventory every stable public option, export, route, command, relevant
   error, and example in scope. Determine stability from declared package
   exports, generated interfaces, route or command schemas, tests, support
   policy, or an explicit product decision. Treat unclear accidental or
   experimental status as a decision gap, not a silent exclusion.
2. Read `references/locality-ladder.md` to identify the established owner or
   form a placement proposal when ownership is unresolved, then read
   `references/api-jsdoc-examples.md`. For each public item, account for the
   applicable purpose, use case, inputs, required or default state, observable
   behavior, failures, interactions, and boundary. Treat readable signatures,
   types, schemas, generated reference, and existing canonical surfaces as
   coverage when they expose those semantics safely. Add the smallest precise
   prose only for a material contract gap; do not give every field equal prose.
3. Put each detailed fact in its established existing surface. Orient and link
   elsewhere. Do not create a new reference page, record, folder, or navigation
   entry unless authorized. When an existing or authorized README is the
   established public owner, it may contain the required reference section; do
   not choose it over another supplied owner.
4. Use public JSDoc or TSDoc for semantics a signature cannot encode reliably,
   such as runtime defaults, errors, lifecycle, ownership, security boundaries,
   and important interactions. Do not paraphrase types or duplicate the
   reference manual.
5. For public JSDoc or TSDoc, at wrap-up verify that the semantics appear on
   the actual exported symbol through re-exports, overloads, inheritance, and
   the repository's generated-reference, emitted-declaration, or IDE-visible
   surface. A successful code or documentation build alone is not proof.
6. Explain a non-trivial example before its code: state the reader goal,
   prerequisites, and why its meaningful choices exist. Keep runnable code
   complete and free of commentary readers must delete. After it, state the
   result, relevant limit, and next path.
7. At wrap-up, classify each sample as Runnable, Illustrative, Partial, or
   Pseudocode using the reference requirements. Never call a sample Runnable
   unless it was validated unchanged with its imports, setup, public names,
   options, and expected behavior.
8. During authoring, record explicit, justified exclusions as they are
   identified. Defer the wrap-up items above (steps 5 and 7), inventory
   accounting, review, and deterministic documentation checks until [Review
   documentation at wrap-up](#review-documentation-at-wrap-up).

## Document code-local rationale

Protect a maintainer or coding agent from an unsafe local edit by preserving an
admitted non-local cause at the decision it governs. Add nothing for visible
mechanics, and never turn this path into documentation review.

1. Inspect the governed symbol or block, nearby lines, relevant types and tests,
   search matches, and any applicable local context the intended reader actually
   receives before editing. Assume the next maintainer or coding agent may see
   only the selective context of a symbol, diff, or search match; do not credit
   it with a README or `AGENTS.md` it would not naturally encounter.
2. Apply the canonical selective-context authoring decision in the code-local
   documentation section of `references/api-jsdoc-examples.md`; it owns
   detailed admission, remote ownership, stability, and the reef-to-cliff
   disposition. If it rejects prose, add no comment. Then use
   `references/locality-ladder.md` to place an admitted explanation.
3. Treat code whose reason for existing or taking its present form is unknown as
   a Chesterton's fence. Search history, callers, tests, runtime effects, and
   neighboring invariants for its rationale, then return to the canonical
   admission decision. Discovering a reason does not by itself justify prose.
4. Place an admitted explanation at the line, block, or file rung that owns the
   decision. Treat exported-symbol JSDoc as a public-contract overlay, not
   another locality rung.
5. Protect the verified constraint in the completed result. When a code, type,
   API, structural change, or canonical local context explanation makes the
   meaning available to the affected reader before this decision, prefer that
   cliff and remove only the prose it makes redundant. An unknown called
   abstraction belongs with its established owner; a durable local convention
   belongs in the repository-provided context owner when one is supplied.
   Otherwise retain the smallest fence explanation and report the clarity
   opportunity when useful. Do not turn every admitted fence into a refactoring
   task.
6. If the reason remains unknown and the gap is accepted, record that
   uncertainty with an explicit `TODO` or `FIXME`. Do not manufacture rationale.
7. Internal symbols need no JSDoc by default. Stop after the evidence-backed
   local disposition is complete. Do not run documentation review or completion
   checks for line, block, or file comments, during authoring or at wrap-up.

## Audit documentation

Decide whether finished non-inline documentation agrees with its current
contract and lets its named reader act safely. Report evidence, coverage, and
remaining risk without editing a review-only scope or inspecting line, block,
or file comments.

1. Run this path only at final work wrap-up or release, or when the user
   explicitly requests a non-inline documentation audit or review; that request
   is the wrap-up task. State the audit mode and scope. For a change-set audit,
   inventory every changed public item and affected non-inline surface. For a
   completeness audit, inventory every stable public item and relevant
   non-inline surface in the stated boundary. Establish current truth,
   canonical facts, examples, and repository-native verification commands.
   Exclude line, block, and file comments. Exported-symbol JSDoc remains a
   public-contract surface.
2. Read `references/locality-ladder.md` and
   `references/quality-maintenance.md`. When the scope includes a README,
   tutorial, how-to, explanation, or reader path, also read
   `references/content-architecture.md`. If the audit questions the current
   reader, goal, subject, or surface, also read `references/casting.md`, run the
   intervention gate, and report its outcome before judging story coherence;
   do not silently validate the supplied cast. When the scope includes a public
   contract, configuration reference, JSDoc or TSDoc, or examples, also read
   `references/api-jsdoc-examples.md`. Compare the evidence with the
   documentation for currentness, contract coverage, locality fit, minimum
   sufficient explanation, reader paths, claim evidence, example integrity,
   and navigation health.
3. Distinguish present-contract defects from missing change history. Do not
   recommend the same prose in both places.
4. Report evidence and counts by surface, plus intentional exclusions, untested
   assumptions, and remaining risks. Do not claim completeness from tone,
   length, or a generic readability score.
5. Do not edit during a review-only request. If changes are authorized, route
   each defect to the applicable procedure above before editing. Use [Review
   documentation at wrap-up](#review-documentation-at-wrap-up) as this path's
   completion procedure.

## Document a change

Keep the current contract and any historical transition accurate for affected
readers by routing each verified impact to its canonical time domain and
existing or authorized surface.

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
5. Record the affected non-inline documentation during the work. At wrap-up,
   read `references/quality-maintenance.md`, perform the applicable drift and
   release checks, and use [Review documentation at
   wrap-up](#review-documentation-at-wrap-up).

## Review documentation at wrap-up

Establish whether the completed non-inline documentation is publishable for its
named readers, and expose any unverified assumption or remaining risk.

Run this procedure once, only after the in-scope implementation and
documentation are complete. A user request specifically for a non-inline
documentation audit or review is itself a wrap-up task. Never invoke this
procedure on intermediate work. Exclude line, block, and file comments,
including from wrap-up review.

For audits, release preparation, or work spanning multiple non-inline
documentation surfaces, read `references/quality-maintenance.md` for the
complete scorecard. For the final non-inline documentation, verify the
applicable minimum:

1. Check the completed behavior against code, types, tests, generated artifacts,
   or an approved product decision.
2. Account for every public export, option, route, error, command, and
   documentation surface in the stated scope. In a change-set scope, this means
   every changed or affected item.
3. Confirm that each unit in scope gives its reader enough relevance, behavior,
   evidence, and boundary to act without unsafe inference. For a new or
   substantially reworked reader-facing surface, also confirm that its opening,
   major sections, proof and limits, and completion route agree with the
   task-local story contract.
4. Confirm that public JSDoc or TSDoc semantics remain attached to the intended
   exported symbol in the actual extracted or IDE-visible surface.
5. Build or typecheck examples and documentation when supported. Validate the
   primary path from its documented starting state: the stated technical task
   for any README; a web-native visitor action for a public website landing
   page; a documentation-navigation or reference task for a public
   documentation home; entry points and technical workflows for an internal
   surface. Otherwise report the assumptions that remain untested.
6. Check links, code-fence status, terminology, defaults, historical leakage,
   mid-process wording, and copy-paste integrity.
7. Apply the [end-state exit
   gate](references/quality-maintenance.md#end-state-exit-gate).
8. Report updated surfaces, intentional omissions, validation run, counts,
   wrap-up result, remaining risks, and future maintenance triggers.

Prefer repository-native link, documentation-build, typecheck, doctest, and
example commands. Add custom automation only after repeated use shows that a
mechanical check cannot otherwise be performed reliably.
