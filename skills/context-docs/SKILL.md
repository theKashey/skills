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

The first group binds every route. The second binds only non-inline
surfaces; a line, block, or file comment stops after the first group.

### On every route

- Ground every claim in source, exported types, tests, generated artifacts, or
  an explicit decision. If a Chesterton's Fence remains unresolved, preserve
  its current form and record accepted uncertainty instead of inventing a
  rationale: a `TODO` or `FIXME` for code, an untested assumption or remaining
  risk in the completion report for prose, never a placeholder in the finished
  document. Recovering the reason does not by itself justify prose; the reader
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
- Write for a capable reader with the context actually delivered and the
  attention the surface can reasonably demand. Supply missing orientation and
  reduce scan or working-memory cost without diluting precise names, concepts,
  causal links, consequences, or boundaries. Treat delivered context, subject
  familiarity, available attention, and cognitive ability as independent;
  never infer the last from the others. Use analogy only as a bounded bridge to
  the real concept. A distinctive voice does not authorize a sustained analogy;
  use one only when the surface contract explicitly requires that device, keep
  precise terms adjacent, and never make it the sole carrier of a decision or
  boundary.
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
- Treat prompts, conversations, interviews, and working notes as evidence and
  intent, not publishable wording. Use the authorized surface's register;
  preserve exact voice or attribution only when its durable contract requires
  that voice or provenance. Do not import a conversational `we` whose referent
  the durable reader cannot recover.
- Document the governed subject, not the drafting or validation process. Add a
  framework distinction only when it changes the reader's decision.

### On non-inline surfaces

- When product or distribution decisions may change an external consumer's
  context, apply [product evidence and topology](references/locality-ladder.md#product-evidence-and-topology)
  before keeping the established route. Delivery state alone does not trigger
  recasting; code comments and repository-only orientation do not enter it.
- Orient before mechanism. Lead an entry surface or owning section with the
  reader-relevant purpose, pressure, consequence, responsibility, or boundary;
  keep the governed subject inferable there.
- Write published prose to the [published prose
  register](references/content-architecture.md#published-prose-register); read
  only that section unless the route loads the rest of the guide. Also read
  [Reader entry and scan
  path](references/content-architecture.md#reader-entry-and-scan-path) when
  writing a lead or a section that states the subject's distinction, and
  [Meaningful visuals](references/content-architecture.md#meaningful-visuals)
  when adding a figure.
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
- Follow a project-owned reader cast and service priority when one exists—by
  convention a `CONTENT-PERSONAS.md` under the project's `.agents` or
  `.context-docs` directory. With no durable cast, serve the explicit task
  reader; do not import a universal persona taxonomy.
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
| New, substantially reworked, or challenged story; unresolved authorial goal; conflicting reader paths; uncertain surface role; or a revoked topology on an external-consumer surface | Follow [casting](references/casting.md). After `PROCEED`, load [content architecture](references/content-architecture.md) only while a story, surface-role, working-document contract, scan-path, or multi-reader alignment decision remains live. Load the [locality ladder](references/locality-ladder.md) only when existence, ownership, scope, or placement is unresolved. |
| New working document, implementation handoff, or continuation note whose resume reader and purpose are explicit and unchallenged | Keep the working-document contract that the cross-route contract's reader-contracts rule states and follow [Working documents and handoffs](references/content-architecture.md#working-documents-and-handoffs). Load [casting](references/casting.md) only when the reader kind, authorial goal, or evidence route is in doubt. |
| JSDoc or TSDoc on a public-contract symbol, with no reference page, contract inventory, or example in the change | A symbol outside the task- or owner-supplied public-contract scope takes no public docblock; for one inside it, follow [symbol JSDoc](references/symbol-jsdoc.md), whose consumer-surface check is the wrap-up for that change. Load [public contracts](references/public-contracts.md) only when a page, inventory, or example enters scope. |
| API or configuration reference, or standalone public API, configuration, or code example | Follow [Document a public contract or standalone example](references/public-contracts.md#document-a-public-contract-or-standalone-example). Load the [locality ladder](references/locality-ladder.md) only when existence, ownership, scope, or placement is unresolved. Finish non-inline work with [Review documentation at wrap-up](references/review-documentation-at-wrap-up.md). |
| Line, block, or file comment | Keep only the every-route group of the cross-route contract and follow the [code-comment gate](#decide-a-code-comment). Load [code comments](references/code-comments.md) only once that gate holds, and the [locality ladder](references/locality-ladder.md) only when the owner or line/block/file placement remains unresolved. Stop after the code-local disposition; do not run documentation review. |
| Documentation audit, review, release check, or maintenance plan | Follow [Audit documentation](references/quality-maintenance.md#audit-documentation), which names the additional guide required by each in-scope surface. Review only; do not edit unless the user separately authorizes changes. |
| Changelog, migration guide, or release documentation | Apply the [change triggers and dispositions](references/quality-maintenance.md#change-triggers), keep historical and current time domains separate, and route each affected current surface through the applicable row above. Finish with [Review documentation at wrap-up](references/review-documentation-at-wrap-up.md). |

For a mixed deliverable, assess only documentation truth, coverage, reader
paths, and locality. Do not present that result as verification of the
non-documentation parts.

## Edit an established current document

Use this path only when the authorized surface, owner, reader task, and story
are already settled. Treat one as disputed when the request or the frozen
evidence contradicts the surface's current reader, subject, authorial goal,
owner, or opening claim; then return to the route table and take the named
conditional path.

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
   materially different lower-frequency need to its canonical detail. On a
   published surface, write to the published prose register as the
   cross-route contract states, with its entry and visuals sections when
   they apply.
4. Load [symbol JSDoc](references/symbol-jsdoc.md) only when the change
   touches a public-contract symbol's docblock, and [public
   contracts](references/public-contracts.md) only when it affects an API or
   configuration reference, a contract inventory, or a non-trivial code
   example. After completed non-inline work, follow [Review documentation at
   wrap-up](references/review-documentation-at-wrap-up.md) once.

## Decide a code comment

Settle this route here; load a reference only once the gate holds. Work as if
only the changed symbol, nearby lines, search matches, and the local context the
reader actually receives were visible:

1. Name the code decision this site owns.
2. Identify an alternative that is selectable and appears reasonable under the
   types, interfaces, control flow, and established patterns visible here. An
   imagined redesign is not enough.
3. Establish the implementation detail, parallel process, lifecycle state, past
   event, or future event that is not locally visible and makes that alternative
   unsafe. State its material consequence here.

A step that fails ends the route: add nothing. Missing local information alone
is not a gap—inevitable behavior, callee semantics without a separate local
consequence, and hypothetical alternate architectures create no comment
obligation. When all three hold, load [code
comments](references/code-comments.md) for ownership, placement, the
invisible-reef-to-visible-cliff disposition, and worked examples.

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
