---
name: context-docs
description: Use when creating, revising, or auditing a README, tutorial, how-to, API or configuration reference, changelog, migration guide, docs site, landing page, example, code comment, working document, or handoff; not for changing code behavior.
---

# Context Docs

Treat an existing choice, constraint, boundary, relationship, or structure
whose purpose is not yet understood as **Chesterton's Fence**: investigate its
rationale before changing or removing it. Once evidence verifies a non-local
cause with a material consequence, preserve that **invisible reef** where the
reader must act; omit the **visible cliff**—meaning already recoverable from the
reader's context. When no material gap remains, add nothing.

## Keep the cross-route contract

- Ground every claim in source, exported types, tests, generated artifacts, or
  an explicit decision. If a Chesterton's Fence remains unresolved, preserve
  its current form and record accepted uncertainty instead of inventing a
  rationale. Recovering the reason does not by itself justify prose; the reader
  must still have a material gap.
- For product documentation, describe the authorized completed contract; temporary
  delivery state does not redefine it. Working records instead preserve verified
  current state, pending work, and uncertainty needed to continue. Keep historical
  claims in their historical domain and verify them with durable evidence.
- Rank upstream sources by what they can establish. PRDs, product contracts,
  RFCs, ADRs, and plans are strong evidence of intent, non-goals, constraints,
  and rationale; code, exported types, tests, and generated artifacts outrank
  them for current behavior; explicit current decisions outrank both for
  product policy. Intent never implemented and never revoked is not
  documentable behavior; record it as a non-goal or roadmap item only with an
  explicit decision. Upstream validation suppresses re-litigating a decision
  only while later decisions preserve its material reader, distribution,
  scope, and product assumptions; a decision that breaks one re-opens exactly
  the consequences it created, never the validated intent itself.
- When product or distribution decisions may change an external consumer's
  context, apply [product evidence and topology](references/locality-ladder.md#product-evidence-and-topology)
  before keeping the established route. Delivery state alone does not trigger
  recasting; code comments and repository-only orientation do not enter it.
- Follow the environment's established owner and submission route. Locality can
  explain or propose a fit; it cannot authorize a surface, displace an owner,
  or widen the requested topology or mutation scope.
- Keep complete truth and remote mechanics with one canonical owner, not one
  physical mention. For each independent symbol/diff, folder, or package path
  that lacks the owner's context before action, leave the smallest local
  consequence and direct route. Caller count alone does not justify multiple
  breadcrumbs: prefer one broader breadcrumb when every affected reader
  receives it, and retain a code-local route only when a symbol or diff reader
  can bypass that context. Count search or indexing only when the actual
  workflow supplies the relevant result before action.
- Orient before mechanism. Lead an entry surface or owning section with the
  reader-relevant purpose, pressure, consequence, responsibility, or boundary;
  keep the governed subject inferable there.
- Make a selective map, not an implementation transcript. Preserve invisible
  causes, relationships, contracts, and boundaries that change a decision;
  omit visible mechanics and facts the reader can safely recover.
- Admit the minimum verified information the reader needs for the decision,
  task, or continuation. Subtract assumed general knowledge, facts actually
  encountered before action, and verified guarantees that already prevent the
  wrong action. A merely reachable source is not received context. Keep exact
  local contracts, defaults, failures, setup, and safety boundaries; another
  subject's internal details earn only a material local consequence and route.
  Recruit shared concepts by name. Teach prerequisites only when the surface's
  reader and authorial goal require it.
- Choose Guided for an explicit teaching responsibility, Balanced for a mixed or
  unspecified reader, and Compressed for a known expert or model. Density changes
  representation, never facts or guarantees; do not re-teach established priors.
- Preserve the established reader contract: technical orientation, documentation
  navigation, browser-visitor action, or a working record's reconstructable
  decision trace. For an unresolved role or continuation contract, use
  [content architecture](references/content-architecture.md). A decision trace
  keeps facts, reasons, evidence routes, live alternatives, unknowns, and next
  actions; it is not an exhaustive thought transcript.
- For a new, substantially reworked, or challenged story, test the supplied
  reader, goal, subject, and surface before drafting. A bounded revision with an
  explicit, unchallenged story keeps that contract.
- Follow a project-owned reader cast and service priority when one exists. With
  no durable cast, serve the explicit task reader; do not import a universal
  persona taxonomy.
- Treat prompts, conversations, interviews, and working notes as evidence and
  intent, not publishable wording. Use the authorized surface's register;
  preserve exact voice or attribution only when its durable contract requires
  that voice or provenance. Do not import a conversational `we` whose referent
  the durable reader cannot recover.
- Document the governed subject, not the drafting or validation process. Add a
  framework distinction only when it changes the reader's decision.
- Review finished non-inline documentation once at wrap-up. Never run that
  review for line, block, or file comments; JSDoc on an established
  public-contract symbol remains a public-contract surface. Once an audit or
  release route selects the full quality scorecard, that scorecard owns
  terminal completion; do not return to the compact wrap-up guide.

## Select one route

Choose one primary route and load only its references. Combine routes only when
the requested artifact genuinely spans them.

| Task | Load and follow |
| --- | --- |
| Bounded revision to an established README, landing page, documentation home or site, tutorial, how-to, explanation, working document, or handoff note | Follow the [routine current-document path](#edit-an-established-current-document). Load a specialist guide only for a condition named there. |
| New, substantially reworked, or challenged story—including a working document, implementation handoff, or continuation note; unresolved authorial goal; conflicting reader paths; uncertain surface role; or a revoked topology on an external-consumer surface | Follow [casting](references/casting.md). After `PROCEED`, load [content architecture](references/content-architecture.md) only while a story, surface-role, working-document contract, scan-path, or multi-reader alignment decision remains live. Load the [locality ladder](references/locality-ladder.md) only when existence, ownership, scope, or placement is unresolved. |
| API or configuration reference, public JSDoc/TSDoc, or standalone public API, configuration, or code example | Follow [Document a public contract or standalone example](references/public-contracts.md#document-a-public-contract-or-standalone-example). Load the [locality ladder](references/locality-ladder.md) only when existence, ownership, scope, or placement is unresolved. Finish non-inline work with [Review documentation at wrap-up](references/review-documentation-at-wrap-up.md). |
| Line, block, or file comment | Apply the [selective-context authoring decision](references/code-comments.md#selective-context-authoring-decision). Load the [locality ladder](references/locality-ladder.md) only when the owner or line/block/file placement remains unresolved. Stop after the code-local disposition; do not run documentation review. |
| Documentation audit, review, release check, or maintenance plan | Follow [Audit documentation](references/quality-maintenance.md#audit-documentation), which names the additional guide required by each in-scope surface. Review only; do not edit unless the user separately authorizes changes. |
| Changelog, migration guide, or release documentation | Apply the [change triggers and dispositions](references/quality-maintenance.md#change-triggers), keep historical and current time domains separate, and route each affected current surface through the applicable row above. Finish with [Review documentation at wrap-up](references/review-documentation-at-wrap-up.md). |

For a mixed deliverable, assess only documentation truth, coverage, reader
paths, and locality. Do not present that result as verification of the
non-documentation parts.

## Edit an established current document

Use this path only when the authorized surface, owner, reader task, and story
are already settled. If one becomes disputed, return to the route table and
take the named conditional path.

1. Freeze the requested scope, current source evidence, and state expected when
   the work completes. Keep product intent distinct from observed
   implementation.
2. Check the material gap from the context the reader actually has at the
   decision, subtracting the cast's assumed priors, the governed subject's
   speciality boundary, and any verified delegated guarantee before drafting.
   Use the established owner and topology; on an external-consumer surface,
   apply the conditional product-evidence and topology rule above; return to
   casting when a decision revokes the topology. If the reader can
   already act safely, add nothing; if the owner cannot be updated, return a
   proposal for that owner instead of creating a fallback.
3. Preserve the established through-line. Write the minimum missing purpose,
   behavior, evidence, boundary, and next route without repeating recoverable
   facts. Give the project-prioritized reader a compact direct path; route a
   materially different lower-frequency need to its canonical detail.
4. Load [public contracts, JSDoc, and
   examples](references/public-contracts.md) only when the requested change
   affects a public API, configuration contract, or non-trivial code example.
   After completed non-inline work, follow [Review documentation at
   wrap-up](references/review-documentation-at-wrap-up.md) once.

## Complete the selected route

Write the minimum explanation that exposes purpose, behavior, evidence, and
boundary without repeating facts already available to the reader. At final
wrap-up for non-inline authoring, follow the compact wrap-up guide once against
the completed artifacts; load the full quality scorecard only when that guide
requires it. An audit or release route already using the full scorecard ends
there instead.

Complete with the authorized documentation change, an evidence-backed no-op, a
proposal for the established owner, or the smallest unresolved decision. Never
turn missing truth or authority into plausible prose.
