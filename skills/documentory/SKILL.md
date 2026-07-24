---
name: documentory
description: Create, revise, and audit documentation for open-source libraries and packages. Use when working on README files, documentation sites, tutorials, how-to guides, API or configuration reference, examples, JSDoc/TSDoc, inline rationale comments, code documentation for maintainers or coding agents, changelogs, migration guides, documentation reviews, or maintenance planning.
---

# Documentory

Create documentation that lets a reader safely understand and use the library as it exists now.

## Laws

These apply to every path:

1. **Describe present truth.** Current documentation explains what a library,
   API, option, route, or workflow is and does now. Changelogs, migration
   guides, and release documentation explain what changed or used to be true.
2. **Verify; never invent.** Check source, exported types, tests, generated
   artifacts, or an explicit product decision. Put evidence beside evaluative
   or comparative claims.
3. **Describe behavior; do not gesture at it.** State effect, condition, and
   relevant boundary. Do not publish bare claims such as supports, handles,
   secure, configure, use, or works.
4. **Start with the right why.** Public landing documentation explains why the
   reader would choose or use the library. Code-local documentation explains
   only non-obvious why or why-not hidden by selective reading.
5. **Explain before code.** Treat code as evidence, not the explanation. Keep
   runnable examples copyable, put necessary explanation around them, and label
   deliberately incomplete samples.
6. **Cover the public contract.** Document every stable public item in an
   existing canonical surface or record an explicit, justified exclusion.
7. **Preserve topology and ownership.** Give each detailed fact one canonical
   owner. Do not create or move pages, folders, or navigation without the
   user's authorization; a README may own every necessary content mode.
8. **Keep code rationale local and scarce.** Preserve only the non-local
   purpose, invariant, ownership boundary, or rejected alternative needed to
   prevent a plausible wrong change, at the smallest scope it governs. Do not
   narrate visible mechanics.
9. **Disclose progressively.** Add material only when it enables a priority
   task, closes a contract or operational risk, or makes an example safe.
   Delete it when removal costs no safety, clarity, findability, or support.
10. **Prove completion.** Validate currentness, coverage, examples, links,
    copy-paste integrity, and the first-success path. Report evidence, counts,
    exclusions, untested assumptions, and remaining risks.

## Route the request

Choose one primary path. Combine paths only when the request genuinely spans
them, and do not load every reference before starting.

| Request | Start here | Read at the indicated step |
| --- | --- | --- |
| README, documentation site, tutorial, how-to, explanation, or examples within them | [Create or revise current documentation](#create-or-revise-current-documentation) | `references/content-architecture.md` before planning the reader path; the example section of `references/api-jsdoc-examples.md` only when code examples are in scope |
| API or configuration reference, or public JSDoc/TSDoc | [Document a public contract](#document-a-public-contract) | `references/api-jsdoc-examples.md` before drafting the contract |
| File, block, or inside-function comments | [Preserve code-local rationale](#preserve-code-local-rationale) | The code-local section of `references/api-jsdoc-examples.md` after identifying missing context |
| Documentation audit, review, release check, or maintenance plan | [Audit documentation](#audit-documentation) | `references/quality-maintenance.md` before scoring or reporting completeness |
| Changelog, migration guide, or release documentation | [Document a change](#document-a-change) | `references/quality-maintenance.md` before the final drift check |

Go directly to the selected procedure. Apply another path only when its artifact
is also in scope.

## Create or revise current documentation

1. Establish current truth from package metadata, public exports, types,
   configuration, defaults, errors, tests, existing documentation, examples,
   and repository-native documentation tooling. Do not treat an example,
   private helper, or identifier name as proof of public behavior.
2. Identify the reader, prior knowledge, task or question, smallest successful
   outcome, prerequisites, dangerous assumptions, and next useful detail.
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
5. For a library landing surface, start with reader-facing why: the problem,
   intended user or host, supported outcome, scope, and non-goals. Then lead to
   the smallest honest first success. Make the opening and heading path usable
   to a scanning reader without prescribing a fixed layout.
6. Write the minimum sufficient explanation. Describe effect, condition, and
   relevant boundary; put evidence beside evaluative or comparative claims.
   Add material only when it enables a priority task, closes a contract or
   operational risk, or makes an example safe. Apply a deletion test to
   everything else.
7. For API or configuration reference, continue with [Document a public
   contract](#document-a-public-contract). For an example inside another
   document, read the example section of `references/api-jsdoc-examples.md` and
   apply only steps 5–6 of that procedure. Then finish with [Verify every
   completed path](#verify-every-completed-path).

## Document a public contract

1. Inventory every stable public option, export, route, command, relevant
   error, and example in scope. Verify each fact against source, exported types,
   tests, generated artifacts, or an explicit product decision.
2. Read `references/api-jsdoc-examples.md`. For each public item, document the
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
5. Explain a non-trivial example before its code: state the reader goal,
   prerequisites, and why its meaningful choices exist. Keep runnable code
   complete and free of commentary readers must delete. After it, state the
   result, relevant limit, and next path.
6. Classify each sample as Runnable, Illustrative, Partial, or Pseudocode using
   the reference requirements. Never call a sample Runnable unless it was
   validated unchanged with its imports, setup, public names, options, and
   expected behavior.
7. Account for every inventoried item or record an explicit, justified
   exclusion. Then finish with [Verify every completed
   path](#verify-every-completed-path).

## Preserve code-local rationale

1. Inspect the governed symbol or block, nearby lines, relevant types and tests,
   and search matches. Assume the next maintainer or coding agent may see only
   that selective context.
2. Identify the important non-local purpose, invariant, ownership boundary, or
   rejected alternative missing from that view. Name the plausible but wrong
   edit its absence could invite. If there is no such edit, add no comment.
3. Read the code-local documentation section of
   `references/api-jsdoc-examples.md`. Place the smallest durable explanation at
   the smallest scope that governs the decision: file, exported symbol, block,
   or line.
4. Explain why the code deliberately differs from an apparent alternative and,
   when useful, its consequence. Do not narrate mechanics visible in code,
   types, names, or nearby tests. Internal symbols need no JSDoc by default.
5. Remove the comment when clearer code, a type, or the same local context makes
   the rationale reliably recoverable. Finish with [Verify every completed
   path](#verify-every-completed-path).

## Audit documentation

1. Establish current truth and inventory the public contract, existing
   documentation surfaces, canonical facts, examples, code-local rationale,
   and repository-native verification commands.
2. Read `references/quality-maintenance.md`. Compare the evidence with the
   documentation for currentness, contract coverage, minimum sufficient
   explanation, reader paths, claim evidence, example integrity, context
   resilience, and navigation health.
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
3. Keep time domains separate. Current documentation describes what the library
   is and does now. Changelogs, migration guides, and release documentation
   describe what changed or used to be true. Do not leave former names, removed
   behavior, or vague temporal phrases in current reference material.
4. Use only existing or explicitly authorized surfaces. Route current-contract,
   public-API, and code-local updates through their procedures above.
5. Read `references/quality-maintenance.md`, perform the applicable drift and
   release checks, and finish with [Verify every completed
   path](#verify-every-completed-path).

## Verify every completed path

For audits, release preparation, or work spanning multiple documentation
surfaces, read `references/quality-maintenance.md` for the complete scorecard.
For every completed path, verify the applicable minimum:

1. Check changed behavior against code, types, tests, generated artifacts, or an
   approved product decision.
2. Account for every changed public export, option, route, error, command, and
   relevant documentation surface.
3. Confirm that each changed unit gives its reader enough relevance, behavior,
   evidence, and boundary to act without unsafe inference.
4. Confirm that code-local prose preserves necessary non-local context without
   narrating visible mechanics.
5. Build or typecheck examples and documentation when supported. Validate
   installation and first success from a clean supported environment when
   feasible; otherwise report the assumptions that remain untested.
6. Check links, code-fence status, terminology, defaults, historical leakage,
   and copy-paste integrity.
7. Report updated surfaces, intentional omissions, validation run, counts,
   remaining risks, and future maintenance triggers.

Prefer repository-native link, documentation-build, typecheck, doctest, and
example commands. Add custom automation only after repeated use shows that a
mechanical check cannot otherwise be performed reliably.
