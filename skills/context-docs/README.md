# Context Docs

Context Docs starts with Chesterton's Fence: do not change or remove an existing
choice, constraint, boundary, relationship, or structure before understanding
why it is there. After investigation, it preserves a verified **invisible
reef**—a non-local cause and material local consequence—and omits the **visible
cliff**, meaning the reader can already recover safely from current context.

Locality is how Context Docs resolves an explanation whose existence, owner,
scope, or placement is still uncertain. Its compact ladder can support a
placement proposal; routine work follows the established owner and story
without loading that branch. The environment's ownership and submission route
decide the actual home.

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

The opposite default fails the same way. A consistent shape can be accumulated
evidence of a sound decision or of a repeated mistake, and repetition alone
does not distinguish them: a reader that aligns with whatever recurs—including
earlier generated work—promotes an inherited mistake into apparent precedent.
The Fence is therefore investigated, not merely followed.

Unknown purposes and invisible constraints appear differently across
implementation levels:

- **Low-level code** is their usual home. Syntax exposes an operation but not
  the platform, representation, ordering, concurrency, ownership, or algorithmic
  constraint that makes an apparent alternative unsafe.
- **Business logic** can look foolish for no visible reason, but its domain
  names, conditions, and nearby policy more often make the reason recoverable.
  When they do, there is no documentation gap.
- **Orchestration and system code** hide non-local causes especially often. A lower
  implementation detail, parallel process, lifecycle transition, or event that
  happened earlier or will happen later can constrain a decision without
  appearing in its local source.

These are implementation abstraction levels, not documentation scopes. At
every level, ask the Chesterton's Fence question first: is the purpose of the
present form understood? When investigation verifies a cause that is not
locally visible and has a material effect here, preserve that invisible reef's
causal edge and local consequence; keep remote mechanics with their canonical
owner.

Prose duplicates system truth and can decay independently from it. Prose about
a remote action is especially fragile because its owner can change without the
copy beside this decision changing. Prefer code, names, types, API shape, or
structure when they can make the constraint locally visible. Robert C.
Martin's rule that a comment exists to "compensate for our failure to express
ourself in code" marks the same boundary; the invisible reef is the case where
the failure is not the author's, because the cause is real but non-local and
code here cannot express it. When the significance remains irreducibly
non-local, retain only the stable causal edge and its local consequence.

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

Context Docs addresses that explanation gap across the full documentation
lifecycle. At broader surfaces, investigation may uncover a hidden purpose,
contract, failure, interaction, or ownership boundary. At code level, the
result may be a verified non-local cause that makes a locally selectable,
apparently reasonable alternative unsafe. Context Docs leaves that explanation
with its established owner and omits facts the reader can already recover.

The intended pressure is inherited or long-running work where the relevant
cause competes with accumulated context and a plausible invented rationale can
sound coherent. A clean isolated prompt makes the evidence unusually prominent
and is therefore only a routing or preservation check. Whether this procedure
improves agent behavior under that pressure remains an evaluation question for
representative target-harness work.

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

Those reader classes and their expected frequency belong to the project, not
the distributed skill. A project can keep its highest-frequency classes on
compact direct paths and route lower-frequency deltas to deeper canonical
owners. The direct set stops growing when another complete path costs more
recurring attention than a contextual route saves; frequency changes exposure,
not facts, guarantees, or safety boundaries.

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
meaning into the surface's established register; exact voice or attribution
remains only when the durable contract requires that voice or provenance.

## Technical role

Chesterton's Fence investigation is the first preservation decision across the
documentation cycle. The module first asks why an existing choice, constraint,
boundary, relationship, or structure has its present form, and does not casually
alter or remove it while that purpose remains unknown. It establishes the
reason from evidence and discovers its established owner. When ownership is
unresolved, locality supports a placement proposal; progressive disclosure
determines how much explanation the reader needs.

After investigation, an **invisible reef** is the verified non-local cause and
material consequence that can make an apparently reasonable action unsafe. A
**visible cliff** is meaning already visible and safely recoverable from the
reader's local context. Context Docs documents only a verified invisible reef
or records explicitly accepted uncertainty—using `TODO` or `FIXME` for code—
and never invents rationale.

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

The package does not assume that adding JSDoc improves an agentic workflow by
itself. JSDoc is useful here as a delivery surface: a host can extract it with
the exported symbol, index it, and retrieve the public semantics into the
agent's actual working context. Any behavioral benefit depends on the factual
quality of that contract and on the host providing that retrieval path.

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
already provides. One canonical owner does not mean one physical mention. When
another surface owns a fact, keep the detailed record and remote mechanics
there, then leave a compact local consequence and route at each evidence-backed
symbol, diff, folder, or package encounter that would otherwise strand the
reader. Several such breadcrumbs do not create parallel records because none
owns or repeats the remote procedure. The breadcrumbs prevent repeated
cross-folder reconstruction; the canonical owner prevents mechanics from
drifting. The skill does not choose those surfaces, replace an owner with a
preferred document, or create an unauthorized fallback.

## Architecture and ownership

| File | Owns | Change it when |
| --- | --- | --- |
| [SKILL.md](SKILL.md) | Cross-route contract, compact established-document path, and direct conditional workflow pointers. | A change affects every activation, the routine path, or which deeper workflow loads. |
| [casting](references/casting.md) | Reader discovery, goal scaffolding, class-frequency evidence, top-`N` service priority, casting outcomes, and durable cast boundaries. | A change affects how a reader, goal, subject, surface, or service priority is challenged before drafting. |
| [content architecture](references/content-architecture.md) | Deep alignment for authorial intent, story contracts, reader paths, document roles, procedure structure, and progressive disclosure. | A change affects a new or challenged story, surface role, scan path, or multi-reader alignment decision. |
| [locality ladder](references/locality-ladder.md) | Compact existence, ownership, scope, and placement reasoning from a line comment to top-level documentation; the documentation-topology, delivered-versus-reachable, external-consumer, and effective-root definitions. | A change affects unresolved existence, ownership, scope, or placement without overriding an established owner, or how topology is defined. |
| [API, JSDoc, and examples](references/api-jsdoc-examples.md) | Public-contract workflow, JSDoc/TSDoc, code-local rationale, and example framing and integrity. | A change affects API semantics, snippets, or code comments. |
| [review at wrap-up](references/review-documentation-at-wrap-up.md) | One-time minimum completion checks, the compact end-state gate, and the condition for loading the full scorecard. | A change affects routine non-inline completion. |
| [quality and maintenance](references/quality-maintenance.md) | Audit workflow and evidence, change triggers, and release and drift checks. | A change affects audits, releases, or how documentation quality is assessed or maintained. |

Keep each behavior in one canonical owner. Link to it from other files rather
than restating it with slightly different wording.

## Principles and design rationale

The skill's durable principles are:

- **Investigate Chesterton's Fences before alteration.** Recover the purpose of
  the existing form from evidence, preserve it while unresolved, record any
  accepted uncertainty, and never manufacture rationale.
- **Preserve invisible reefs; omit visible cliffs.** Keep the verified reason
  and consequence that code or the current surface does not reveal; omit
  mechanics and meaning already visible to the reader.
- **Orient before mechanism.** State purpose, relevant effect, and boundary at
  the subject's owning scope before internal method or detail.
- **Cast before committing to the story.** Treat every supplied reader class,
  task, and surface as a hypothesis when the story is new or challenged. Use
  project evidence to find who controls the decision, keep reader goal separate
  from authorial goal, and honor a result that changes the reader, goal,
  surface, subject, or need for documentation.
- **Prioritize the project cast.** Record measured frequency when available or
  label a qualitative expectation. Give the smallest high-frequency set direct
  paths, route the long tail to canonical detail, and keep one primary
  through-line per surface.
- **Keep truth with its established owner.** Keep complete mechanics there and
  route from each evidenced encounter that would otherwise strand its reader;
  a compact local consequence is not a second owner. When ownership is
  unresolved, use locality to propose the lowest stable surface that reaches
  every affected decision; do not treat the proposal as authority.
- **Follow reader-visible consequences of decisions, not repository
  structure.** An authorized product or distribution decision can change who
  consumes a subject, where they enter, what is delivered to them, and what
  obligations they hold, without any file becoming individually wrong—a
  package published from a monorepo turns its README into an effective root
  for a consumer who never receives the repository. On surfaces serving an
  external consumer, such a decision revokes the established topology and
  re-enters casting; the validated upstream intent is not re-litigated, only
  the consequences the new decision created. A mandatory provenance pass on
  every task was rejected: routine bounded work keeps the compact path, and
  the trigger fires only on a decision-backed change to an external
  consumption boundary—never on registry, tag, or deployment state alone, and
  never for code comments or an orientation surface whose every material
  reader receives the repository itself.
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
- **Use explanations as clarity signals.** Protect an invisible reef
  first, then notice when code, types, an API, or structure could expose it
  directly. Keep the explanation when the significance remains non-local; do
  not treat every documented reef as a mandatory refactor.
- **Treat documentation as a completed-system claim.** Use present artifacts to
  implement and verify the authorized finished contract, not to promote a
  temporary checkout, delivery, or publication mismatch into reader-facing
  content. At wrap-up, verify the claim against the finished code and artifacts,
  and exercise representative reader paths to expose context gaps. Do not review
  line, block, or file comments.

The package separates the frequent runtime path from conditional alignment and
maintenance detail. [Casting](references/casting.md) owns reader selection,
frequency evidence, and goal shifts; the [locality
ladder](references/locality-ladder.md) owns unresolved existence, scope, and
placement; [content architecture](references/content-architecture.md) owns deep
reader-path and document-role alignment after the cast survives; [API, JSDoc, and
examples](references/api-jsdoc-examples.md) owns public-contract and code-local
detail; [review at
wrap-up](references/review-documentation-at-wrap-up.md) owns routine completion;
and [quality and maintenance](references/quality-maintenance.md) owns audits,
release evidence, and drift checks.

This split keeps an established-document edit on the compact runtime and
wrap-up path. It exposes content architecture, locality, casting, specialist
contract guidance, and comprehensive audit doctrine only when the choice they
own becomes live. It also keeps technical
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
