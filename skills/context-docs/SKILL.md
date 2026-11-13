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
- Apply the [published prose register](#published-prose-register) to published
  surfaces, and the [reader entry and scan path](#reader-entry-and-scan-path)
  when writing a lead or a section that states the subject's distinction.
  Load [Meaningful visuals](references/content-architecture.md#meaningful-visuals)
  only when adding a figure.
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
  terminal completion; do not repeat the routine wrap-up review.

## Reader entry and scan path

Model the reader at the surface where they first encounter the documentation.
Assume only context genuinely available at that surface. When material entry
paths deliver different context to the same surface, assume only the
delivered-context intersection defined in the [locality
ladder](references/locality-ladder.md): orient the least-contextualized material external
consumer locally or give them a direct route.

Open with the pressure, consequence, responsibility, supported outcome,
boundary, or changed decision the entering reader needs. Make the governed
subject and capability inferable there when the entry context does not already
supply them. When a surface catalogs several independently selectable
capabilities, services, packages, or concepts, present each in compact
`name: what and why` form so the reader can choose. Do not make the reader cross
methodology, taxonomy, workflow, or a component inventory to discover why the
subject matters.

Give the remaining situation, impact, and boundary needed to choose safely
before detailed methodology or parts. A chooser may own that selection context
for compact catalog entries. A parent summary or sibling section cannot orient
a standalone subject page.

When the subject is something the reader might adopt beside or in place of a
tool they already run, and its value depends on a distinction that tool does not
make, state that distinction in the lead, or in the first sentence of the
section that owns it, before the mechanism. Name it in the reader's terms: the
outcome they would see, not the internal representation that produces it.
Wherever the distinction is stated, bold only the phrase that states it, not
the sentence around it. When adopting the subject could seem to replace a tool the reader
keeps, say which tools stay in place; in a README this is an integration
boundary, not a comparison. Do not manufacture novelty:
a reference remains a reference, and an opening that already states its
uncommon claim needs no slogan added.

For a README, state the technical reader, task, and starting context before
giving a route. Establish that context from the authorized completed product
and distribution contract. Missing current packages, versions, tags, releases,
or deployments cannot redirect the completed package route to a source
checkout; an explicit decision that the product remains source-only can. A
repository checkout, package registry, command line, runtime, credentials, or
source access is available only when the completed contract provides it. For a
public website presentation page, the primary route is browser-native. Do not
swap those contracts. For a public documentation home, the primary route is
documentation navigation or reference lookup, not a product conversion path.

At every reader-facing entry, lead with the reader-relevant reason to care
rather than artifact placement, drafting history, or internal method. Keep
identity, capability or responsibility, selection context, and boundary
inferable at that surface; do not force a fixed order when the entry context
already supplies some of them.

A technical README opening should let its technical reader identify the governed
system or unit, scope, boundary, and the route that fits their task. A public
documentation home should let a documentation reader identify the subject and
next navigation route. A public website presentation opening may instead help a
browser visitor recognize a supported outcome and next action. This distinction
does not prescribe badges, a table of contents, visual position, or a fixed
section order.

At wrap-up, validate the primary reader path from its documented starting state.
Never use this as a mid-work review. For a README, validate its stated technical
task rather than assuming installation or a browser journey. For a public
website presentation page, use a clean supported browser entry with stated
access. For a public documentation home, test the documented navigation or
reference path. For an internal technical surface, use the documented
repository state and repository-native tooling. Do not silently depend on
unstated caches, global tools, credentials, generated files, or maintainer
knowledge. State what remained untested.
## Focus and attention management

On every existing or authorized, in-scope human-facing entry surface, treat
attention as part of information exposure. From the surface's actual reader
contract, identify the primary subject, route or task, and any boundary the
reader must notice before acting. Give those elements perceptually distinct,
semantically meaningful anchors before secondary detail. Detail volume is part
of that hierarchy: a secondary setup or demonstration fails this rule when its
procedure occupies the scan path needed for the primary orientation or task.

Choose anchors that fit the delivered medium and established conventions:
headings, spacing, typography, compact summaries, descriptive links, tables,
diagrams, screenshots, or other layout and visual cues. An anchor passes only
when it helps the reader locate or interpret information; decoration and
promotional emphasis do not substitute for hierarchy. A technical README
anchors technical scope and routes, a documentation home anchors navigation,
and an actual presentation page anchors its verified visitor path.

Attention management never changes the surface's role, authorizes a new
surface, or makes visual treatment the only carrier of necessary meaning. It
does not require an image, badge, fixed section order, or presentation-page
posture.

At wrap-up, inspect the rendered or actual delivered surface. Verify that a
reader scanning from its stated entry can notice the primary subject, path, and
necessary boundary before secondary detail, and that text or contextual
alternatives preserve any meaning carried by visual treatment.
## Published prose register

Apply this to every sentence a published surface delivers. The published set
is what the project renders or distributes to its readers, and the project
decides its membership; a record that sits in the repository is not published
by that alone. Where the project has declared nothing, treat as published what
ships in a package, what renders on its documentation or website, and the
top-level README, and ask the owner about anything else. Inside that set, a
surface may be a README, a documentation home or page, a public website
presentation page, a changelog, a release note, or a migration guide. A public
docblock follows [symbol JSDoc](references/symbol-jsdoc.md) instead. A changelog, release note, or migration
guide keeps its historical time domain and follows every other rule here. A working document follows its own
contract instead. The project's established register decides voice,
punctuation, and which of its own names stay. Where the surface contract
requires a device these rules cut, such as a sustained analogy, the contract governs;
keep the precise terms next to it.

A reader can land on any published page from a search result, a shared link, or
an agent's citation, without the pages before it:

- **Link at first use.** Link each concept the project defines at its first
  use on the page to the one page that owns it, with a section anchor when that
  section answers the immediate question. A term the project coined is
  introduced on its owning page before any other page depends on it; when
  that page is outside the requested scope, do not depend on the term, and
  propose the introduction to its owner.
- **Keep unpublished records off the reader path.** Never route the reader to a
  record the project keeps outside its published set, such as an internal
  decision record, a journal, a specification note, or a working document.
  Pages outside the project, such as a standard or another tool's
  documentation, are not records and stay linkable, and so is contribution
  material on a contributor route, whose reader works in the checkout. When
  the user-facing reader needs the reasoning, state it on the published page,
  or link the published owner of the detail.

Write for the surface's cast reader, who may not know this project and may read
English as a second language. That last condition decides the words.

- **Present tense, named actor.** Outside a historical time domain, describe
  the subject as it is now, and name who acts rather than hiding the actor in
  a passive. The page is not the history of the work: cut a date that records
  when the work happened, a narrated absence, and a comparison with an earlier
  version of the same thing. Keep a date that is part of the contract,
  measurement provenance, or example data.
- **Claims rest on evidence.** Evaluative or comparative claims have adjacent,
  interpretable evidence and measurement conditions; otherwise state observable
  behavior without unsupported adjectives. A timing names the machine it was
  measured on.
- **A word means what it says.** A term of art is free, and a page may use as
  many as it needs. A figure of speech is not. Before writing a general verb,
  ask how many senses it has: a word that fits any sentence makes the reader
  choose one. Use such a word only in its literal sense, and otherwise write
  the verb that names what happened, such as *imports*, *calls*, *changes*, or
  *records*.
- **Plain words, plain sentences.** Use the most common word that still means
  it: *use*, not *utilise*; *enough*, not *sufficient*. Give each clause one
  idea. Leave out idiom, irony, and cultural reference. A hard word is allowed
  when it is a term of art or a name the project defines and links, not when
  it is style.
- **One word, one job.** Never replace a word with a synonym for variety. To a
  reader translating as they go, a new word means a new thing.
- **A limitation is a present-tense boundary.** State what the product does not
  do. Outside a historical time domain, do not narrate an absence or the
  story of an attempt.

Plain language is not a plain subject. Keep every distinction, term of art, and
step of reasoning the page needs; a sentence may be long when each part is plain
and it carries one idea.

Cut these habits:

- compressed syntax: arrows, dropped articles, and abbreviations that the
  reader must decode before reading. The Compressed detail level changes how
  much surrounding explanation appears, never the syntax;
- a point buried in a paragraph where a scanning reader cannot find it; give
  each limit, case, or question its own item, heading, or bold lead;
- an adverb supporting a weak verb, where the number or a stronger verb belongs;
- *serves as*, *features*, or *boasts* where *is* or *has* belongs;
- filler phrases and trailing clauses that add nothing;
- stacked hedges; one hedge, or none;
- a list forced to three items, or *from X to Y* where X and Y share no scale;
- *not just X, but Y*, where Y alone is the claim;
- a bold label that repeats its own line;
- an ending or sentence that would be true of another project's documentation.

To check one sentence, ask who says it, what makes it true, which word is not
meant literally, and which word a good non-native reader would look up. That
last word passes only when it is a term of art or a defined name.

## Select one route

Choose one primary route and load only its references. Combine routes only when
the requested artifact genuinely spans them.

| Task | Load and follow |
| --- | --- |
| Bounded revision to an established README, landing page, documentation home or site, tutorial, how-to, explanation, working document, or handoff note | Follow the [routine current-document path](#edit-an-established-current-document). Load a specialist guide only for a condition named there. |
| New, substantially reworked, or challenged story; unresolved authorial goal; conflicting reader paths; uncertain surface role; or a revoked topology on an external-consumer surface | Follow [casting](references/casting.md). After `PROCEED`, load [content architecture](references/content-architecture.md) only while a story, surface-role, working-document contract, scan-path, or multi-reader alignment decision remains live. Load the [locality ladder](references/locality-ladder.md) only when existence, ownership, scope, or placement is unresolved. |
| New working document, implementation handoff, or continuation note whose resume reader and purpose are explicit and unchallenged | Keep the working-document contract that the cross-route contract's reader-contracts rule states and follow [Working documents and handoffs](references/content-architecture.md#working-documents-and-handoffs). Load [casting](references/casting.md) only when the reader kind, authorial goal, or evidence route is in doubt. |
| JSDoc or TSDoc on a public-contract symbol, with no reference page, contract inventory, or example in the change | A symbol outside the task- or owner-supplied public-contract scope takes no public docblock; for one inside it, follow [symbol JSDoc](references/symbol-jsdoc.md), whose consumer-surface check is the wrap-up for that change. Load [public contracts](references/public-contracts.md) only when a page, inventory, or example enters scope. |
| API or configuration reference, or standalone public API, configuration, or code example | Follow [Document a public contract or standalone example](references/public-contracts.md#document-a-public-contract-or-standalone-example). Load the [locality ladder](references/locality-ladder.md) only when existence, ownership, scope, or placement is unresolved. Finish non-inline work with [Review documentation at wrap-up](#review-documentation-at-wrap-up). |
| Line, block, or file comment | Keep only the every-route group of the cross-route contract and follow the [code-comment gate](#decide-a-code-comment). Load [code comments](references/code-comments.md) only once that gate holds, and the [locality ladder](references/locality-ladder.md) only when the owner or line/block/file placement remains unresolved. Stop after the code-local disposition; do not run documentation review. |
| Documentation audit, review, release check, or maintenance plan | Follow [Audit documentation](references/quality-maintenance.md#audit-documentation), which names the additional guide required by each in-scope surface. Review only; do not edit unless the user separately authorizes changes. |
| Installing Context Docs in a repository, or verifying that installation | Read [installation](references/installation.md) and nothing else. |
| Changelog, migration guide, or release documentation | Apply the [change triggers and dispositions](references/quality-maintenance.md#change-triggers), keep historical and current time domains separate, and route each affected current surface through the applicable row above. Finish with [Review documentation at wrap-up](#review-documentation-at-wrap-up). |

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
   wrap-up](#review-documentation-at-wrap-up) once.

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

## Comment budgets and overflow

By default a file overview carries at most 15 content lines, a block comment
5, and a declaration's docblock 10, public or not; a project may set other limits.
A document's lead has a 15-content-line budget before the first `##`.

The unit of a comment is the cause: adjacent one-line comments preserving one
cause count as one block; separate causes belong beside the decisions they
govern. A heading, measurement, history, or an export's contract reopens
placement even below the numeric budget. Use the [locality
ladder](references/locality-ladder.md) only when existence, ownership, scope, or
placement remains unresolved, then apply the moves below.

### Move overflow to its owner

A surface over its budget has a placement problem, not a length problem: the
count never grades a comment, and it never licenses deleting a verified cause.
Count content lines—what the reader reads—not delimiters, blank lines,
machine-read tags, or pragmas such as `compass:`, linter and `@ts-` directives,
and `/// <reference`. A comment is a docblock or a file overview by attachment,
not position: a docblock sits directly on its declaration, and a blank line
separates an overview from the code below it. Imports and re-exports that
declare nothing are not the first statement. A document's lead stops at its
first `##` outside a code fence. An addition to an existing comment is authored
against the whole comment's budget. A breach collapses the whole surface to
about half its budget, apart from a passage that stays below, so the next edit
does not trip it; shaving lines to just pass is not a fix. Classify each
over-budget passage, then move it; never copy it, and never shorten it into
something that no longer states the cause:

- Narration of the code, or a fact the reader already holds, is removed under
  the Chesterton's Fence rule: with its recovered reason, or kept with a `TODO`
  while the reason is unknown.
- A consequence that governs one function, branch, or guard moves down to that
  site.
- Orientation, boundary, ownership, or a route moves up to the folder,
  package, or domain owner the affected reader encounters.
- History, measurements, and the choice among alternatives move to the host's
  established historical or decision record, where this skill's time-domain
  rule already places them.
- An export's contract moves to that symbol's docblock. The move does not make
  the symbol a public-contract surface; without supplied membership it remains
  a code comment under SKILL.md's gate, still held to the docblock budget.
- A passage stays when it is one rule whose cases depend on each other, the
  usage of a script with no package surface, or a docblock that is itself a
  format contract. Record that reason in the task record, or where the host
  records its exceptions.

Top level has no owner above it: its overflow moves down or into the historical
record. The agent that finds the overflow moves it in the same change. When the
owner that governs the passage does not exist and the change's authorized
scope reaches it, create it through the host's established route, held to its own budget;
that creates the owner, not a fallback beside an established one or a file that
only mirrors the ladder. Where the host keeps an architecture chart, the
missing chart entry or coordinate is part of the same change, under the chart's
own rules. A proposal survives only for content outside the task's authorized
scope, or for an owner the task cannot update, and the change names it as
unfinished work, not a finished placement. The over-budget surface is never the
fallback for content it cannot carry.

## Complete the selected route

Write the minimum explanation that exposes purpose, behavior, evidence, and
boundary without repeating facts already available to the reader. At final
wrap-up for non-inline authoring, follow [Review documentation at
wrap-up](#review-documentation-at-wrap-up) once against the completed artifacts.
Load the full quality scorecard only under its audit, release, or material-risk
condition. An audit or release route already using that scorecard ends there
instead.

Complete with the authorized documentation change, an evidence-backed no-op, a
proposal for the established owner, or the smallest unresolved decision. Never
turn missing truth or authority into plausible prose.

## Review documentation at wrap-up

Finished non-inline documentation can still contradict its completed contract,
omit an affected surface, or strand its reader on an untested path. Use these
checks to decide whether the finished documentation is publishable and expose
the smallest remaining defect or risk.

Line, block, and file comments stop before this review. For a public-contract docblock-only
change, the symbol JSDoc route's consumer-surface check completes the work.

For an audit, release, or a material risk requiring a detailed gate—including
changed cross-surface contracts, ownership, or reader paths—load [quality and
maintenance](references/quality-maintenance.md) and apply its evidence scorecard. Once
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
   sections, proof, limits, and completion route against it. Confirm that the
   opening, and any section that states the subject's distinction, meets
   [Reader entry and scan
   path](#reader-entry-and-scan-path) and that each
   explanatory figure carries one claim under [Meaningful
   visuals](references/content-architecture.md#meaningful-visuals). Apply the
   [separation test](#separation-tests) for each
   surface's mode.
4. When public JSDoc or TSDoc is in scope, run the [consumer-surface
   check](references/symbol-jsdoc.md#verify-on-the-consumer-surface).
5. Build or typecheck examples and documentation when supported. Classify each
   sample and validate the primary reader path from its documented starting
   state. On a human-facing entry surface, also inspect the rendered or
   delivered form for the [attention
   anchors](#focus-and-attention-management) that let a
   reader scanning from that entry notice the primary subject, path, and
   necessary boundary before secondary detail. Report any setup, access,
   credential, or environment assumption that remains untested.
6. Check links, navigation, code-fence status, terminology, defaults, historical
   leakage, source-to-artifact register leakage, mid-process wording, and
   copy-paste integrity. On a published surface, confirm that the page meets
   the [published prose
   register](#published-prose-register), which also
   defines historical leakage there.
7. Apply the [end-state exit gate](#end-state-exit-gate).

### End-state exit gate

For a working document, handoff, or continuation note, check the
[working-record completion contract](references/content-architecture.md#working-documents-and-handoffs):
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

## Separation tests

At wrap-up, apply these review tests:

- Tutorial: can a newcomer complete it without unexplained prior decisions?
- How-to: can an informed reader identify the goal, prerequisites, steps, and result?
- Reference: can a reader find the factual contract without a narrative detour?
- Explanation: does it answer a conceptual or design question rather than conceal procedural steps?
- Technical README: can the named technical reader locate scope, boundary, and
  the route for their task without encountering marketing posture?
- Public documentation home: can a reader find the relevant topic or exact fact
  without a product-presentation detour?
- Public website presentation page: can a browser visitor find only a verified
  web-native path without source setup being made primary?
- Working document or handoff: can a fresh intended reader recover current
  state, live decisions and their reasons, open questions, and the next action
  without the previous conversation, and without reading exploration nobody
  needs to repeat?

Flag a possible split when one page attempts to teach, prescribe, enumerate
facts, and justify architecture with no clear separation. Until the user accepts
restructuring, preserve the current files and improve separation with headings
and local navigation.
