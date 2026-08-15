# Content architecture

Use this guide when a new or challenged story, surface role, scan path, or
multi-reader route needs alignment.

Start with the reader's task and governed scope; do not infer a document's role
from its filename, repository visibility, or marketing posture.

- [Reader contexts](#reader-contexts)
- [Authorial intent and story contract](#authorial-intent-and-story-contract)
- [Prior and speciality admission](#prior-and-speciality-admission)
- [Detail level](#detail-level)
- [Procedure paths](#procedure-paths)
- [Classify technical documents and public sites](#classify-technical-documents-and-public-sites)
- [Technical README roles](#technical-readme-roles)
- [Public documentation homes](#public-documentation-homes)
- [Public website presentation pages](#public-website-presentation-pages)
- [Working documents and handoffs](#working-documents-and-handoffs)
- [Reader entry and scan path](#reader-entry-and-scan-path)
- [Focus and attention management](#focus-and-attention-management)
- [Progressive disclosure](#progressive-disclosure)
- [Explain-before-code pattern](#explain-before-code-pattern)
- [Meaningful visuals](#meaningful-visuals)
- [Separation tests](#separation-tests)

## Reader contexts

Start with the reader's question, entry context, and task. Diátaxis names content
modes; it does not require separate files, folders, or navigation.

| Reader need | Diátaxis mode | Possible existing or authorized home | Useful success condition |
| --- | --- | --- | --- |
| Orient in a repository, system, or documentation set | Explanation | Top-level technical README or documentation home, if needed | Identify purpose, scope, boundaries, and the technical route relevant to the reader's task. |
| Understand a package or module | Explanation and reference | Package/module README, in-page contract, or API reference | Identify contract, integration conditions, and the next technical detail. |
| Work safely inside a repository area | Explanation | Existing folder overview or authorized technical overview | Identify ownership, conventions, boundary, and local validation. |
| Learn a capability | Tutorial | Tutorial or guided README section | Reach a visible working result by following one stated path. |
| Solve a known problem | How-to | How-to page or procedural README section | Complete the task with stated prerequisites and expected result. |
| Find an exact fact | Reference | API, configuration, or in-page reference | Locate a precise answer without a narrative detour. |
| Understand a design | Explanation | Concept or architecture section | Understand the mental model, trade-off, and boundary. |
| Evaluate or access a browser-based product | Presentation or product guidance | Actual public website page, not a README | Recognize the supported outcome and take a verified browser-native next action. |
| Resume or hand off unfinished work | Outside Diátaxis: working record | Working document, implementation handoff, or continuation note | Recover current state, live decisions, open questions, and the next action without the previous conversation. |

Apply modes within the documentation surfaces the repository already uses. If a
README is the only surface, keep the necessary modes as clear technical README
sections. Do not create or move pages unless the user requested a new structure
or explicitly accepts a proposed split.

These are candidate homes after the locality existence gate, not a required
inventory. A package, public repository, unfamiliar reader, or code location is
not a documentation gap by itself. If readable code, types, tests, metadata, or
an existing canonical surface already lets the named reader act safely, add
nothing.

## Authorial intent and story contract

For a new or substantially reworked non-inline reader-facing surface, form a
task-local story contract before outlining, full prose, or visual
implementation. A bounded revision may keep an explicit, unchallenged contract
and proceed directly.

For new, challenged, or substantially reworked stories, first run
[casting](casting.md). It owns reader discovery, goal scaffolding, the
intervention gate, class formation, and durable persona storage. Continue here
only after `PROCEED`; another outcome changes or stops the documentation task.

A content persona is the smallest durable reader class that survives casting,
not the entrant's current task or an identity inferred from a job title, skill,
package, page, workflow phase, or document type. Keep any proven modifier and
the current task episode below the class. Choose one class-goal pair for the
primary through-line and route materially different secondary goals without
creating alternate versions of the same truth.

Keep the reader goal—why this entrant arrives in the current episode—separate
from the authorial goal—why the project chooses to speak at this surface. The
story is the verified progression that joins them and produces the intended
reader change. Evidence establishes what the subject can truthfully claim; an
explicit user or project decision, or an established surface contract,
establishes the authorial goal. If none is available, return
`NEEDS_HUMAN_DECISION` with the smallest missing choice. Never let a filename,
surface type, source mechanics, or a generic desire for polished documentation
choose a product or editorial intent.

Record only the contract needed to control the draft:

- surface role, existing owner, and authority;
- primary content-persona class, proven modifier if any, task-local episode,
  and reader goal, plus secondary goals to route;
- the governed subject and its speciality boundary, the class's assumed priors,
  and the representation contract this document owes that reader;
- authorial goal, its decision source, and the intended reader change;
- one evidence-backed proposition or through-line and the proof that earns it;
- boundary or non-fit, unsupported stories to exclude, and one completion
  decision, task, or next route;
- expected and disconfirming readback.

When the evidence and supplied decisions resolve one contract, continue without
reconfirmation. When a strategic field remains open, present only the smallest
contract-level alternatives that expose the missing decision and stop before a
full draft.

For a judgment-heavy new surface or substantial rewrite, align the resolved
contract with one semantic slice before expanding it:

1. Freeze the expected reader change and the observation that would disconfirm
   the proposed through-line.
2. Produce only the opening claim and support, an ordered heading spine with
   each section's contribution, the necessary proof and boundary, and the
   completion route.
3. Classify the readback as expected, disconfirming, mixed, or inconclusive;
   collapse what survives into one contract before writing body prose or visual
   implementation.

Complete documents are not story probes. After alignment, produce one full
route. Every major section must advance the intended reader change, supply
necessary proof or boundary, or serve a materially distinct routed goal. Keep
the contract and slice as construction records, not published scaffolding. This
alignment does not replace the single final documentation review.

Story is purposeful selection and progression, not a mandatory narrative voice
or fixed outline. A technical README connects technical purpose and boundary to
the reader's route. A presentation page moves a verified visitor situation
through supported outcome, proof and limits to an honest action. A documentation
home makes a navigation promise. A tutorial or how-to progresses toward a
working result; explanation progresses toward a mental model; reference makes a
lookup promise and needs no book-like arc.

## Prior and speciality admission

Run this gate on every candidate statement before choosing a detail level or a
home for it. Locality decides where an admitted fact belongs; it never decides
whether generic knowledge deserves restating.

Three inputs bound the gate:

- **Assumed priors** come from the cast: the stable general knowledge, named
  concepts, and ordinary tool or platform competence the cast reader brings to
  this document. [Casting](casting.md#4-freeze-and-prioritize-the-smallest-cast)
  owns them and keeps them task-local.
- **Subject speciality** comes from the governed subject: the contracts,
  choices, guarantees, boundaries, and failure modes it owns or intentionally
  exposes. A technology the subject uses internally is not part of its
  speciality.
- **Delegated guarantees** come from the system: verified behavior supplied by
  an underlying abstraction or executable gate that already prevents the wrong
  action without prose at this surface. A gate the reader must invoke or
  interpret is not one; document that local action or result and route to the
  gate's owner.

For each candidate statement:

1. Name the reader decision, action, or continuation need it changes.
2. Name the plausible wrong action or repeated investigation it prevents.
3. Determine whether the fact is inside the governed subject's speciality.
4. If it is outside, keep it only where it leaks across the abstraction
   boundary and produces a material local consequence.
5. Subtract meaning already recoverable from visible or reachable project
   context, the assumed priors, and verified delegated guarantees.
6. Keep only the remaining exact local contract, deviation, causal edge,
   boundary, or continuation breadcrumb.

Return one disposition:

| Disposition | Return it when | Result |
| --- | --- | --- |
| `No document` | The prior, visible context, or a delegated guarantee already selects the safe action. | Add nothing. |
| `Recruit the prior` | The cast reader holds the concept and its precise name selects the action. | Name the concept without restating its generic theory; add a local consequence only when the name does not select the action. |
| `State the speciality contract` | The subject owns the behavior, default, failure, or boundary. | Preserve the exact local truth. |
| `Preserve a boundary leak` | An out-of-speciality fact still changes a local decision. | Leave the smallest local consequence and route to the external owner. |
| `Teach the prerequisite` | Teaching this generic material is part of the explicit reader and authorial goal. | Explain it to the depth that goal requires, and only on the surface that owns it. |

Being true or relevant is not admission. Every admitted explanation must avert
a named wrong turn, repeated investigation, or unsafe continuation; when no
such turn can be named, the disposition is `No document` and existing prose is
a deletion candidate.

The gate suppresses generic explanation, not exact project truth. A public API
or configuration reference still exposes its in-scope signatures, defaults,
errors, compatibility limits, and security boundaries: a frontier model knowing
the generic concept is not evidence that it knows the current repository
contract. Changing the cast may change terminology, scaffolding, ordering,
examples, and compression; it never changes verified facts, guarantees, or
required safety boundaries.

## Detail level

Choose Guided, Balanced, or Compressed for the intended reader, but only for
what [prior and speciality admission](#prior-and-speciality-admission) already
kept. Density is a representation mode: it cannot readmit a subtracted prior or
drop an admitted contract. Use Balanced when the audience is mixed or
unspecified.

| Level | Include | Avoid |
| --- | --- | --- |
| Guided | A short mental model, defined unfamiliar terms, explicit prerequisites, one primary path, and expected results. | Background history, multiple equivalent paths, and line-by-line code narration. |
| Balanced | The reader outcome, non-obvious choices, important boundaries, and contextual links. | Repeating the reference contract, or treating absent repository prose as evidence that generic theory is needed. |
| Compressed | The exact local answer, required conditions, meaningful boundary, evidence route or decision trace, and a descriptive link to detail. | Introductions, examples, or explanations the named expert or model audience can safely infer. |

Guided lowers the assumed prior only for prerequisites this surface is
explicitly responsible for teaching; it does not make every page a tutorial.
Compressed recruits a shared concept by its precise name instead of restating
its theory. Do not use Compressed to hide a failure mode, security condition,
required setup, or public API contract. Assume ordinary shared knowledge as a
prior; require supporting evidence only before assuming specialist knowledge
the cast does not establish. Keep code samples copyable at every level; change
surrounding prose, not the amount of commentary inside the code.

## Procedure paths

Use a procedure only when a sentence, example, or link cannot carry the action
safely.

- A tutorial controls its starting conditions and follows one reproducible route
  to a visible result. State the expected result at meaningful checkpoints; defer
  variants.
- A how-to serves a reader who knows the goal. Name real prerequisites and
  branch only when a condition changes the action or recovery path.

For either, let the heading state the task. Put the location, condition, or
purpose before the action. Give each numbered step one meaningful action,
combining only trivial actions in the same context. Put required warnings or
decisions in the normal flow immediately before they matter.

## Classify technical documents and public sites

Classify only a surface that exists or whose creation or change is authorized,
by its governed scope, reader, available context, and task. If existence,
ownership, governed scope, or placement is unresolved, read the [locality
ladder](locality-ladder.md) first:

- A top-level repository or project README, when present, is technical orientation for the
  whole technical system or repository.
- A package README, when present, is technical orientation and contract for
  the package. When an authorized decision distributes the package
  independently, that README is also the effective root for its external
  consumer, who receives it without ancestor surfaces; it remains a child
  surface on the repository path.
- A folder or module README, when present, is technical orientation for the governed area.
- A public documentation home, when present, is navigation and orientation for readers already
  seeking documentation.
- A public website or product landing page is a separate presentation surface
  for browser visitors; it is not a README and is not implied by public source.
- A working document, implementation handoff, or continuation note, when
  present, is a task-scoped record for whoever resumes the work; it is not a
  reader-facing product surface and does not become one by being committed.

README is never an advertising landing page. Do not import landing-page section
order, persuasion goals, browser calls to action, or source-versus-browser
routing into a README. This does not ban verified technical commands,
installation instructions, or routes for the README's named reader. Public
access, root placement, a source host, and a license establish availability, not
the reader's task. A top-level README for an internal product remains technical;
its position does not create a product-presentation role.

A document can host several technical modes when it is the authorized surface,
but its sections must remain scannable by role. Do not create a split just to
make the taxonomy tidy.

## Technical README roles

### Decide whether a README is needed

A package, repository, public source, or unfamiliar reader does not require a
README. Use or revise one only when a named technical reader needs scope,
boundary, contract, or route that they cannot safely recover from readable code,
types, tests, metadata, existing canonical documentation, and their actual
context. If no gap remains, add none.

### Top-level repository or project README

Where a top-level README is the right owner, help a named technical reader orient
in the whole repository or system. Do not assume the reader is a prospective
customer, a contributor, or an integrator; derive the actual technical task from
the request and verified context.

State only what that reader needs at top level:

1. What the project or system is for in technical terms, its scope, and important
   non-goals.
2. Its major components, boundaries, and any system-wide constraints that change
   a safe technical decision.
3. The technical audience or audiences served by the documented routes.
4. The route in the authorized completed contract that is relevant to the task:
   using the system or a package, running it, contributing, operating it, or
   finding deeper documentation.
5. Links to canonical package, domain, API, configuration, operation, and
   contribution material as applicable.

A source or package start belongs here only when it is the verified technical
task for the reader. It is an instruction, not a conversion call to action.
Do not add a generic source quickstart merely because source exists, and do not
infer the route from temporary checkout, registry, rollout, or release state.
Keep the opening scan path on purpose, scope, boundaries, and the primary
technical route. When an established example or how-to owner contains a
secondary demo, give it a concise contextual link instead of copying its setup
or procedure into that critical space. Retain the procedure only when the demo
is itself the verified primary task and this README is its established owner.
Do not turn this README into a product advertisement or a monorepo manual.

### Package README

A package README is optional. Readable exports, types, package metadata, and an
existing reference may already cover the integrator's need. Where a remaining
reader gap makes an existing or authorized package README the right owner, help
an integrator or consumer use the bounded technical unit. Give its purpose,
supported contract, prerequisites, installation when verified and relevant,
smallest safe use, configuration, defaults, failures, compatibility boundaries,
and routes to deeper reference.

A published package can serve readers outside the repository without becoming a
landing page. It remains a technical contract. Keep marketing claims and
product-wide narrative outside it; keep exhaustive API detail with its canonical
reference owner.

### Folder, module, domain, and service README

Use the [locality ladder](locality-ladder.md) only when a scope-wide existence,
ownership, or placement gap remains. Then explain responsibility, boundary,
interactions, and the technical route appropriate to the project-defined
reader's actual context. Do not borrow assumptions from a broader or narrower
scope.

## Public documentation homes

Where a public documentation home exists or is authorized, help a reader who has
already arrived to find documentation. Start with the documentation subject, its
available navigation, and a route to the relevant tutorial, how-to, explanation,
or reference. Browser delivery does not make it a product presentation page or
give it a conversion goal.

At wrap-up, validate that the reader can navigate to a relevant topic or locate
an exact fact from the stated entry. Keep product evaluation and browser-product
actions on a separately classified public website presentation page.

## Public website presentation pages

Use this route only for an actual existing or authorized public website or
product page. Its browser
visitor may need a decision or verified web-native action, so it has a different
reader contract from every README.

Describe verified purpose, supported outcome, relevant limits, and the smallest
honest browser-native next step. Keep source secondary unless contribution or
self-hosting is a verified visitor task. If no browser action is verified, route
to neutral deeper material rather than inventing a call to action.

A public documentation home is not automatically a marketing page. Classify it
by whether its reader needs documentation navigation, technical reference, or a
product decision.

When no presentation page exists or is authorized, stop this route. Its absence
does not create a landing-page task or a required follow-up proposal.

## Working documents and handoffs

A working document, implementation handoff, or continuation note serves whoever
resumes unfinished work. Cast that reader like any other: a human maintainer
and a frontier model need materially different starting context, representation,
proof, and success conditions. A frontier-model document defaults to a
compressed representation contract until the project or user selects another.

What it must leave is a **reconstructable decision trace**—the smallest durable
record from which the intended reader can recover current state and continue:
verified local facts, decisions and their causal edges, evidence routes,
still-plausible rejected alternatives, unresolved questions, and the next
action. A request to preserve a chain of thought asks for that trace, not a
verbatim or exhaustive thought transcript.

Preserve:

- current state and completed decisions;
- the shortest verified `X because Y` causal edge needed to prevent reversal;
- direct evidence and the route back to its source;
- rejected alternatives only while they remain locally plausible and likely to
  be reopened;
- unresolved uncertainty, including what has and has not been established;
- the next decision, verification step, or action.

Omit:

- generic language, framework, platform, and engineering theory;
- definitions of named concepts the cast reader can recruit;
- chronological narration of the exploration;
- dead branches whose removal cannot change continuation;
- mechanics recoverable directly from code, types, tests, or a reachable owner;
- motivational prose and restatement of the task.

The completion test is whether a fresh intended reader can recover what is
true, why the live decisions were selected, what remains unknown, and what to
do next without receiving the previous conversation. It fails in both
directions: a record whose reader must re-derive a decision the work already
settled is incomplete, and a record that narrates an exploration nobody needs
to repeat is a transcript, not a trace.

## Reader entry and scan path

Model the reader at the surface where they first encounter the documentation.
Assume only context genuinely available at that surface. When material entry
paths deliver different context to the same surface, assume only the
delivered-context intersection defined in the [locality
ladder](locality-ladder.md): orient the least-contextualized material external
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

## Progressive disclosure

Give enough context before each link to answer why it applies. Move detail only
to an existing or authorized surface. Otherwise disclose it progressively in the
current document through headings and local navigation.

Use a canonical-owner rule within the existing documentation topology. The
following modes may be sections in one README:

- Put exact defaults, type shapes, error details, and exhaustive option facts in reference.
- Put task-specific setup and procedure in their established how-to or example
  owner when one exists.
- Put concepts and trade-offs in explanations.
- Put only a short contextual summary plus a link in other surfaces.

Delete repeated prose if a reader can still determine purpose, behavior, and
boundary. Add only the smallest missing explanation at the reader's present
level.

## Explain-before-code pattern

For a non-trivial example, follow [Prepare a non-trivial
example](api-jsdoc-examples.md#prepare-a-non-trivial-example). That section owns
example framing and code-comment admission; this reference owns where the
example fits the document's reader path.

## Meaningful visuals

When a diagram, screenshot, or image carries a fact, state, decision, or
relationship needed to act, expose it in concise contextual alt text or nearby
prose. Do not make a contract, requirement, or necessary state visible only in
the visual.

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
