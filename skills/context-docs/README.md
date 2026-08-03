# Context Docs

Context Docs preserves verified explanations for fences: choices, constraints,
boundaries, relationships, and structures whose reason is not visible in the
code or system surface where a reader encounters them. It documents reefs, not
cliffs—the hidden why and consequence, not mechanics already in view.

Locality is how Context Docs makes those explanations useful. Its ladder
explains how an explanation fits a reader and scope, and can support a placement
proposal when ownership is unresolved. The environment's established ownership
and submission route decide the actual home.

- [Why Context Docs exists](#why-context-docs-exists)
- [Technical role](#technical-role)
- [Architecture and ownership](#architecture-and-ownership)
- [Principles and design rationale](#principles-and-design-rationale)
- [Boundaries](#boundaries)

## Why Context Docs exists

Code and system structure usually expose what happens. They often cannot expose
the non-local cause that makes a surprising choice, constraint, boundary, or
relationship necessary here. Without that causal edge, a maintainer or coding
agent can make a locally reasonable change that violates an invisible
requirement.

Fences appear differently across implementation levels:

- **Low-level code** is their usual home. Syntax exposes an operation but not
  the platform, representation, ordering, concurrency, ownership, or algorithmic
  constraint that makes an apparent alternative unsafe.
- **Business logic** can look foolish for no visible reason, but its domain
  names, conditions, and nearby policy more often make the reason recoverable.
  When they do, there is no fence to document.
- **Orchestration and system code** contain fences especially often. A lower
  implementation detail, parallel process, lifecycle transition, or event that
  happened earlier or will happen later can constrain a decision without
  appearing in its local source.

These are implementation abstraction levels, not documentation rungs. At every
level, the fence is the same shape: a cause not locally visible has a material
effect here. Document the causal edge and local consequence; keep remote
mechanics with their canonical owner.

Prose duplicates system truth and can decay independently from it. Prose about
a remote action is especially fragile because its owner can change without the
copy beside this decision changing. Prefer code, names, types, API shape, or
structure when they can make the constraint locally visible. When the
significance remains irreducibly non-local, retain only the stable causal edge
and its local consequence.

Documentation density is therefore a diagnostic signal, not proof of bad code.
It can reveal accidental opacity, essential concurrency or lifecycle
complexity, or a genuinely non-local influence. An explanation protects the
decision now and may expose an opportunity to make the constraint visible
later.

Context Docs is also a filesystem-level context-engineering practice. Code and
domain structure should expose what they can—[“If your code-base doesn’t scream
its domain, AI will whisper
nonsense.”](https://asdlc.io/concepts/context-engineering/#references)—while
documentation supplies only the hidden reasons that remain. What is omitted
matters too: in evaluated repository-level context-file settings, [Gloaguen et
al. (2026)](https://arxiv.org/abs/2602.11988) found that agents generally
followed the instructions, explored and reasoned more, and incurred higher
inference cost without significantly improved task performance. Unnecessary
instruction is therefore active context, not neutral background.

Context Docs closes that explanation gap across the full documentation
lifecycle. At broader surfaces, a fence may be hidden purpose, contract,
failure, interaction, or ownership boundary. At code level, it is the verified
non-local cause that makes a locally selectable, apparently reasonable
alternative unsafe. Context Docs leaves that explanation with its established
owner and omits facts the reader can already recover.

Reader need establishes whether a broader document is relevant, but it does not
choose why the project wants that document to speak. The supplied reader can
also be wrong: a job title, package, task, or existing page may disguise who can
actually make the intended decision. Without a separate authorial goal, several
coherent sections—or several complete drafts—can each optimize a different
story while appearing locally correct.

Context Docs therefore casts before it commits to a new or substantially
reworked story. It derives the smallest evidence-backed reader classes from
recurring decision rights and context, keeps the reader's goal separate from
the document's authorial goal, and tests whether documentation is the right
intervention. Casting can replace the reader, revise the goal, change the
surface or subject, or conclude that no document is needed. Only a surviving
contract earns a full draft and one verified through-line.

For a new or substantially reworked reader-facing surface, the skill spends one
small alignment move before a full draft: a task-local story contract and the
smallest opening-and-heading slice that can disconfirm it. This makes an early
strategic correction cheap while preserving one final documentation review for
the finished artifact. Routine bounded revisions keep the established story and
avoid that ceremony.

Authoring sources create another selective-context boundary. A live
conversation can rely on shorthand, emotion, shared referents, and an informal
voice that a durable reader-facing surface does not own. Copying that register
can turn a private exchange into the apparent subject, turn a participant's
provisional wording into a durable attributed statement, or force readers to
reconstruct a conversation they never saw. Context Docs carries the verified
meaning into the surface's established register; exact voice and attribution
remain only when their provenance is part of the durable contract.

## Technical role

Fence discovery and explanation is the organizing decision across the complete
documentation cycle. The module first decides whether a material, non-visible
reason affects a reader's decision, then establishes that reason from evidence
and discovers its established owner. When ownership is unresolved, locality
supports a placement proposal; progressive disclosure determines how much of
the explanation the reader needs.

A fence is a present choice, constraint, boundary, relationship, or structure
whose reason is not locally visible. Its reef is the material hidden cause and
consequence that can make an apparently reasonable action unsafe. A cliff is
meaning already visible and safely recoverable from local context. A
Chesterton's Fence is a fence whose reason remains unresolved. Context Docs
investigates that uncertainty; it records only a verified explanation or an
explicit accepted `TODO` or `FIXME`, never an invented rationale.

A coding agent may enter through a task, diff, README, public contract, symbol,
or search match without tacit organizational memory. The same selective-context
problem affects human readers. At code level, Context Docs preserves
evidence-backed causes that rule out a locally reasonable alternative. It does
not narrate visible mechanics, inevitable effects, or remote behavior that has
no material consequence for the decision here.

Human-facing entry surfaces also have an attention boundary. During reading,
eyes alternate between [fixations and
saccades](https://pmc.ncbi.nlm.nih.gov/articles/PMC10084433/), and [visual
salience](https://pmc.ncbi.nlm.nih.gov/articles/PMC5206280/) helps determine
where overt attention moves next. Correct information can therefore remain
effectively hidden when a surface gives the reader no meaningful fixation or
scan anchors. Attention management is part of information exposure, not
decoration: hierarchy, spacing, typography, links, and visuals can direct the
reader toward the primary subject, route, and boundary. Those anchors serve the
surface's established reader contract; they do not create a presentation page
or give a technical document promotional intent.

Source evidence supports documentation while it is authored, but documentation
review and deterministic completion checks happen once at wrap-up. Line, block,
and file comments are admitted and written from evidence but never enter
documentation review; exported-symbol JSDoc remains a public contract.

Local documentation is part of that context engineering. A local `AGENTS.md`,
README, package document, or linked contract can turn a model-surprising use
into a normal repository primitive when the intended reader actually encounters
it before acting. First route an unfamiliar local abstraction to its existing
canonical documentation; do not explain every invocation. When a familiar
primitive has a durable, verified local convention that cannot otherwise be
recovered, promote the smallest explanation to the local context owner that
governs the convention. This keeps context living: it is revised or removed
when code, structure, tooling, or a higher canonical owner makes it redundant,
while code-local rationale remains for readers who do not receive the broader
context.

Context Docs composes with the ownership and record surfaces an environment
already provides. When another surface owns a fact, keep the detailed record
there and add only a route or local consequence when the affected reader still
needs one. The skill does not choose that surface, replace it with a preferred
document, or create a parallel fallback that both owners must keep consistent.

## Architecture and ownership

| File | Owns | Change it when |
| --- | --- | --- |
| [SKILL.md](SKILL.md) | Universal laws, request routes, procedures, and completion criteria. | A change affects every invocation or execution order. |
| [casting](references/casting.md) | Reader discovery, goal scaffolding, reject/merge/split tests, casting outcomes, and durable cast boundaries. | A change affects how a reader, goal, subject, or surface is challenged before drafting. |
| [content architecture](references/content-architecture.md) | Authorial intent, story contracts, reader paths, README roles, procedure structure, and progressive disclosure. | A change affects documentation surfaces, their intended story, or reader journeys after casting. |
| [locality ladder](references/locality-ladder.md) | Scope vocabulary for explaining or proposing how facts fit from a line comment to top-level documentation. | A change affects placement reasoning without overriding established ownership. |
| [API, JSDoc, and examples](references/api-jsdoc-examples.md) | Public contracts, JSDoc/TSDoc, code-local rationale, and examples. | A change affects API semantics, snippets, or code comments. |
| [quality and maintenance](references/quality-maintenance.md) | Audit evidence, change triggers, drift checks, and the end-state exit gate. | A change affects how documentation quality is assessed or maintained. |

Keep each behavior in one canonical owner. Link to it from other files rather
than restating it with slightly different wording.

## Principles and design rationale

The skill's durable principles are:

- **Document fences; preserve reefs, not cliffs.** Keep the verified reason and
  consequence that code or the current surface does not reveal; omit visible
  mechanics.
- **Investigate Chesterton's Fences.** Recover the reason from evidence or mark
  accepted uncertainty explicitly; never manufacture rationale.
- **Orient before mechanism.** State purpose, relevant effect, and boundary at
  the subject's owning scope before internal method or detail.
- **Cast before committing to the story.** Treat every supplied reader class,
  task, and surface as a hypothesis when the story is new or challenged. Use
  project evidence to find who controls the decision, keep reader goal separate
  from authorial goal, and honor a result that changes the reader, goal,
  surface, subject, or need for documentation.
- **Keep truth with its established owner.** Link rather than duplicate. When
  ownership is unresolved, use locality to propose the lowest stable surface
  that reaches every affected decision; do not treat the proposal as authority.
- **Treat supplied context as living terrain.** Route readers to the established
  owner before adding local prose. Add only a durable, verified local
  consequence that changes a safe action, and retire it when the reader can
  recover the same boundary from the established owner.
- **Prefer a map to a transcript.** Preserve non-obvious constraints,
  interactions, and rationale that protect a real decision the reader cannot
  safely infer; omit visible or inevitable mechanics, callee-owned behavior,
  and unneeded surface area.
- **Separate source register from artifact register.** Treat informal prompts,
  conversations, interviews, and working notes as sources of meaning rather
  than the document's default voice. Preserve exact wording, profanity, or
  speaker attribution only when the established surface contract requires that
  voice or provenance.
- **Use explanations as clarity signals.** Protect an invisible constraint
  first, then notice when code, types, an API, or structure could expose it
  directly. Keep the explanation when the significance remains non-local; do
  not treat every documented fence as a mandatory refactor.
- **Treat documentation as a completed-system claim.** Use present artifacts to
  implement and verify the authorized finished contract, not to promote a
  temporary checkout, delivery, or publication mismatch into reader-facing
  content. At wrap-up, verify the claim against the finished code and artifacts,
  and exercise representative reader paths to expose context gaps. Do not review
  line, block, or file comments.

The package separates runtime decisions from their maintenance rationale.
[Casting](references/casting.md) owns reader selection and goal shifts; the
[locality ladder](references/locality-ladder.md) owns the reader-context model;
[content architecture](references/content-architecture.md) owns reader paths
and document roles after the cast survives; [API, JSDoc, and
examples](references/api-jsdoc-examples.md) owns public-contract and code-local
detail; and [quality and maintenance](references/quality-maintenance.md) owns
verification and drift checks at wrap-up.

This split prevents a routine documentation task from carrying unrelated
contract, code-comment, or maintenance doctrine. It also keeps technical
READMEs, public documentation homes, and product presentation pages distinct
because they serve different readers and entry contexts. Diátaxis supplies a
reader-question vocabulary, not a required file tree.

## Boundaries

Context Docs guides documentation work. It does not independently decide product
behavior, preserve or remove code, invent facts, or authorize a documentation
restructure. It may report a code-clarity or placement opportunity, but acts on
code or topology only when that change is already authorized and in scope.
It follows an established external owner without requiring knowledge of that
owner's implementation; when the native submission route is unavailable, it
returns the proposed content and target instead of inventing another store.
