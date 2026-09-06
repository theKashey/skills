# Compass

The compass skill governs a semantic architecture chart under a chart root the
host project declares: one or more human-ratified logical roots, a scoped L0–L4
level stack, a per-root glossary, a tiered registry, viewports, and
`// compass:` implementation coordinates in source. That chart root may hold an
`ABSTRACTIONS.md` for named implementation-design concepts, attached to
code by `// compass-abstraction:` claims. The semantic chart describes what the
system *is*; the optional catalog is not a chart level and does not prescribe
implementations, tests, or requirements.

Two nested things share the name: the skill package and the compass registry
(`COMPASS.md`), the chart's root artifact.

Compass is inspired by DeepWiki and C4 and is neither. DeepWiki regenerates an
explanation from current code and holds no state between builds; Compass holds
ratified state on purpose, and reaches past one repository — several roots and
a registry that records other systems and demoted ones. C4 is a notation humans
draw for humans; Compass is written for an agent mid-task, which is why C4's
code level is replaced by coordinates in source and by gates the agent runs
itself. The closer relative is the sibling Helix skill, which is neither C4 nor
a wiki: both store verdicts and deliberately lose the reasoning that produced
them, and the difference is the axis — Helix persists what is different now
across cycles of work, Compass persists what stays the same across rewrites of
the implementation.

## Why it exists

A repository accumulates pieces — tools, services, docs, decisions — faster
than any reader can hold them, and to a coding agent conventional context docs
are reefs: passive files off the path of work. The agent sails past them, and
the decisions and opportunities they record are missed. Structure that is not
on the path of work does not exist.

The intended impact is that every file, tool, and move has a place and a
purpose. A place is an address in the stack, ultimately a `// compass:`
coordinate in the code itself; a purpose is a documented responsibility with a
boundary. An agent starting a task then meets the relevant decisions on its
way in. The knowledge base is the deliverable; the method is only how it is
produced and kept true. The compass registry comes first because it is the
dot-connector: one page from which every root, external, and demoted
almost-external is reachable.

Compass is meta-code: a persistent logical model with two children, product
behaviour and implementation coordinates. The codebase is one current
realization of that model, not the model itself — which is why the design test
is a rewrite. Delete every source file, rebuild the same product in another
language, framework, layout, and topology, and the semantic chart should stand
while its coordinates are replaced wholesale. Anything that changes merely
because the technology changed was implementation structure that had leaked in.

That framing is what separates Compass from a projection of the repository.
Repository structure is evidence about implementation, never authority over
semantic identity: code proposes hypotheses, and product and domain reality
ratify them. It is also why chart/code disagreement is classified — semantic
change, implementation remapping, or implementation violation — rather than
resolved by trusting either side. A regenerated wiki can always defer to code;
a chart that did so would silently erase the verdicts (ratified boundaries,
recorded demotions, consumer replacement conditions) that are the only thing it
holds which code reading cannot reproduce. Everything in the chart is
agent-generated; the human contributes judgment through checkpoints (teacher,
validator, consultant, ratifier by knowledge state) and never writes chart
content by hand.

Two boundaries follow, and both are about what the chart declines to be. **Its
value scales with how non-local the work is.** Orientation — *which file, which
symbol, which caller* — is something a capable agent reconstructs from the code,
increasingly well, and a chart competing there competes where its advantage is
shrinking. A one-file fix does not want a chart; work that crosses a boundary,
changes a rule, or asks whether something belongs here does — and building a
new capability is that work even when it lands in one file, because that is
the shape duplication takes. Claiming otherwise trains readers to skip it
entirely. **And it does not independently maintain machine-owned truth.**
Build graphs, import and call incidence, CI configuration, ownership data, and schemas stay
with their authoritative sources; the chart links to them or uses generated
views with a source route. Semantic relationships remain authored: what crosses
a boundary and why it matters cannot be recovered from an import alone. A
diagram may project those relationships without becoming another owner of
their meaning. Implementation coordinates also stay authored: they exist so an
agent reaches code without scanning, they are written before any marker is
sealed, and they name entry points no scan produces. Named-abstraction
definitions stay authored too: no command can decide what a local
design concept means, while its declared incidence remains mechanically
searchable in source and is never copied into the catalog. Runtime state, task
memory, and whether the work is correct sit outside the chart entirely — not
carried, and not pointed into.

## Design decisions and rejected alternatives

- **Top-down propagation with per-level word budgets**, instead of one
  architecture document. A single document has no place for a new fact to
  land, so it grows until it drifts; a budgeted level makes oversize a signal
  (scope creep) with a defined response (split down — at L0 and L4, split the
  unit — never raise the budget).
- **Demotion by default at L1.** Level contamination — vendors, SDKs, and
  adapters leaking into the system context — is the most common failure mode,
  so both L1 tests must pass and anything uncertain goes down a level. The
  rejected alternative, listing every integration at L1, turns the context
  diagram into a dependency inventory instead of a boundary statement.
- **Consumers own relationship decisions (BEM)**: why they depend on a
  provider, what they rely on, and what would make them leave. Reverse views
  remain useful for navigation when they link to those consumer-owned entries
  or are generated from an identified source; an independently maintained
  provider-side incidence list would create another owner and drift silently.
- **Coordinates are sealed last (Phase F)**, instead of attribute-as-you-go:
  wiring code to the chart before semantic boundaries stabilize multiplies the
  cost of correcting a boundary that was wrong.
- **Multiple ratified roots**, instead of one primary stack plus an exceptional
  second one. A logical starting point is not a repository, a deployable, or a
  service, and two products in one monorepo — or a substantial domain inside
  wider product scaffolding — are the ordinary case, not the exception. The
  rejected alternative required a second stack to prove itself "a sound C4
  construct", which asked a logical question in structural terms and answered
  it with C4's authority rather than with whether humans reason about the area
  independently. Roots remain human-ratified for the same reason the old rule
  existed: agents that invent orientations produce charts nobody navigates by.
- **Disagreement is classified into three kinds**, instead of one "drift"
  bucket. The single bucket had a default — code is real, so the chart is
  stale — which silently converted every repository reorganization into a
  semantic edit and hid the one case with no structural signature at all: a
  business rule changing inside an otherwise untouched module.
- **Coordinate density opens an investigation; only cohesion or coupling
  evidence closes one.** Non-uniform folders and files serving several places
  were previously a "structural debt map" with standing refactoring pressure —
  a verdict issued by the pattern itself. A logical phenomenon legitimately
  spans frontend, API, workers, storage, and services, so that rule punished
  systems for being shaped like systems. Deleting the signal was the opposite
  error and was rejected too: density is the cheapest standing lead the method
  produces, and it usually points at a real declutter (a stray file, a two-job
  file, a helper that belongs to the floor). Splitting the two halves — a
  signal that may open, evidence that must close — keeps the lead usable
  without letting it sentence.
- **A glossary per root**, instead of vocabulary scattered through domain
  prose. Terminology needs one canonical owner to be checkable at all, and
  recording implementation aliases explicitly is what stops source naming from
  quietly becoming the domain language. `DOMAIN.md` keeps relationships,
  contexts, aggregates, events, and invariants; `GLOSSARY.md` keeps words.
- **`README.md` is every architectural directory's identity document**,
  instead of `SCOPE.md`/`CONTEXT.md`/`BLOCK.md`/`COMPONENT.md`. The layout was
  already directory-as-zoom; naming the landing file `README.md` completes it,
  because opening any chart directory on GitHub then answers *where am I?*
  without knowing Compass's private filenames. Named alternate views
  (`DOMAIN.md`, `GLOSSARY.md`, `CONTAINERS.md`, `VIEWPORTS.md`, `COMPASS.md`)
  keep their names: they are views, not identities.
- **Semantic fields are Markdown headings**, instead of `Field — value` prose
  lines. The pseudo-field form forced every consumer to recover the schema by
  parsing punctuation; headings put it in the Markdown AST where both agents
  and rendering already look.
- **Hybrid lookup reads the live chart**, instead of generating an index or
  claiming semantic search. An address resolves to its directory's identity
  document, and exact headings, entity slugs, and identifiers stay
  deterministic, matched by the query or a phrase inside it;
  BM25 only reranks within direct-match tiers and adds lexically related
  sections, improving the chance that task language finds different chart
  wording. It creates no cache or duplicate owner, and its score is not
  confidence or proof of relevance. Results preserve the owning Markdown
  section boundary and anchor bounded excerpts on the evidence, so glossary
  contexts and named-abstraction discriminators do not silently detach from the
  matched term.
- **An explicit ownership contract with Context Docs**, instead of leaving two
  skills that both preserve "why" to overlap by feel. The rewrite test doubles
  as the classifier, so a reason has exactly one owner and neither skill
  restates the other.
- **One checklist owner** (`references/verification.md`), instead of per-file
  checklists: duplicated checklists diverge, and the divergent copy is the one
  an agent finds.
- **Mutually exclusive Create and Consume flows**, instead of one runtime manual
  that mixes chart production with chart use. Consumption must stay read-only:
  finding a gap does not silently grant authority to rewrite the chart. Creation
  includes maintenance and remapping because all three mutate Compass-owned or
  Compass-installed state and require the same ownership and verification gates.
- **A compact search-and-consult hook**, instead of a route catalog copied into
  every host. The host entry instruction starts live chart search and preserves
  the local-work exclusion; the Consume router reveals task-specific detail only
  after the query identifies a path. This keeps semantic context on the path of
  non-local work without loading every navigation pattern on every activation.
- **Diagrams are mandatory only on the zoom chain**, not on every file: L0 is
  domain prose by design, and a forced diagram there would restate the context
  map without adding structure.
- **A declared chart root**, instead of a hardcoded storage path. Host
  projects own their repository layout, so the chart location is read from the
  project's agent instructions; when none is declared the skill asks rather
  than inventing a directory. The rejected alternative — shipping a fixed
  path — made the skill silently write into repositories that never chose it.
- **Borrowed vocabulary with declared deltas**, instead of an unlabelled
  homegrown stack. Naming C4 recruits what a reader already knows about
  context/container/component zoom, and naming DDD recruits the domain's own
  strategic language at L0; the deltas fence the places those priors
  mis-predict. Neither gets a vote on what the chart means — where a borrowed
  rule and semantic orientation conflict, orientation wins.
- **Chart-baked vocabulary freezes first; gates iterate.** The file layout,
  document names and formats, the marker literal, and the address grammar are
  what every produced chart physically embeds — changing them later rebuilds
  every chart, so they are settled before first use. Checklists and thresholds
  only change how the next pass judges an existing chart, so they may tighten
  release by release without invalidating anything already built. The usage hook
  and the chart check are installed copies a host approved once: a release that
  changes their templates rewrites nothing in a host; the next Create activation
  compares the installed hook with `references/agent-hook.md`, a missing
  instruction is Phase E work, and a stale chart check fails the named-abstraction
  gate's fixture row until it is changed, ask-first.
- **The coordinate marker is `compass: <address>`, written in the host
  language's comment syntax** (`// compass:` in TypeScript, `# compass:` in
  Python). The marker names the Compass-owned address space, so an agent
  meeting it in code can reach the chart that defines the address. Its body is
  a fixed literal in every project — never the host repository's own name —
  because the checks that read it are written once, shipped with the skill,
  and match the body without a comment prefix.
  Inherited scope is explicit in the chart's implementation coordinates:
  the carrier file and covered subtree are recorded together, because a marker
  alone cannot distinguish a file claim from a folder or package claim.
- **Named abstractions are definitions, not an incidence inventory.** An
  optional chart-root `ABSTRACTIONS.md` gives a non-obvious local implementation
  concept a human-readable name, an essential discriminator, and a nearest
  non-example; `compass-abstraction: <slug>` beside a stable source owner makes
  the local claim. Search supplies declared occurrences, so the catalog carries
  no paths, `used-by` lists, edges, flows, or completeness claim. Marker
  presence is an assertion to review and marker absence is unknown. A name is
  retired on task evidence, the conditions `references/named-abstractions.md`
  §Maintenance and retirement lists, through the same ratified Create work that
  admitted it; admission evidence lives in the change that admitted the name and
  retirement evidence in task records, never in the catalog. The rejected
  alternative was shipping the catalog as an opt-in experiment with its own
  evidence record and end date: a consumer installs from main, so a rule that
  calls itself provisional hands its validation to every consumer and is a hedge
  none of them can use.
- **Counts are asserted against a committed minimum**, instead of printed for
  a human to read. A check that scans nothing exits zero exactly like one that
  scans everything, and a printed count nobody reads is a checkbox with extra
  steps. Chart-side minimums move only in the diff that changes the chart;
  source-side ones take 1 once anything is sealed or claimed, because a
  declutter legitimately lowers them.
- **The semantic read is blind**, instead of the author's own re-read. Every
  structural gate passes on a chart that is well-formed and untrue, and an
  author sees what was meant rather than what is written, so the read that
  judges the arguments runs in a fresh context holding only the chart.

## Boundaries

The semantic chart answers what the system is, what its parts are responsible
for, and how they relate. The optional named-abstraction catalog answers only
what a project-specific implementation-design name means and how to distinguish
it from its nearest non-example. It does not explain why a particular owner
uses that design. Implementation guidance, mechanism-specific rationale,
performance, test strategy, deployment topology, business requirements, and how
the repository happens to be arranged are out of scope (§What the Chart Does
NOT Answer in [the Consume guide](references/consume.md#what-the-chart-does-not-answer)). Reader-facing documentation — READMEs,
references, tutorials — is a different craft with a different owner; compass
claims only the chart. The boundary with Context Docs is a stated contract
rather than a disclaimer: reasons that survive a rewrite may be Compass-owned,
reasons that die with the implementation are not, and neither side duplicates
the other. Completion is measured by the verification gates, not by prose
confidence. The skill puts the chart on the path of work — a human-approved
usage hook in the host's agent instructions, installed at Phase B — but whether
agents then follow it is outside the skill's evaluation boundary.

## Runtime architecture

| File | Owns |
| --- | --- |
| [SKILL.md](SKILL.md) | Activation, the minimal shared interpretation contract, and the exclusive Create/Consume route decision |
| [references/create.md](references/create.md) | Create and maintenance entry: rewrite and invariance tests, root admission, level tables, L1 guardrails, file layout, authoring boundaries, and conditional routes to production references |
| [references/consume.md](references/consume.md) | Compact read-only search-and-consult contract and conditional router |
| [references/consume-search.md](references/consume-search.md) | Conditional lookup options, result interpretation, and glossary use |
| [references/consume-investigation.md](references/consume-investigation.md) | Conditional code-rationale, component, and cross-block investigation paths |
| [references/consume-change.md](references/consume-change.md) | Conditional estimation, review, refactor, overreach, and architectural-pull paths |
| [references/consume-named-abstractions.md](references/consume-named-abstractions.md) | Read-only interpretation of existing named-abstraction definitions and claims |
| [scripts/compass_search.py](scripts/compass_search.py) | Live, read-only structured lookup over a host-declared chart root, with deterministic address, exact, heading, and literal tiers and optional BM25-related candidates |
| [references/agent-hook.md](references/agent-hook.md) | Canonical four-line search-and-consult block copied into host agent instructions after human approval |
| [references/structural-signals.md](references/structural-signals.md) | Shared read-only warning signs for level contamination and overreach; both flows may consult it without importing the other's procedure |
| [references/exploration.md](references/exploration.md) | The orient→scan→probe→adjust loop, triangulation and evidence sources, per-state procedures and exits, level calibration, scratchpad format |
| [references/blocks-and-levels.md](references/blocks-and-levels.md) | Roots in practice, the contents of every chart document, the registry and glossary templates, Markdown conventions, promotion criteria with contrast examples; placement stays with `references/create.md` §File Layout |
| [references/coordinate-system.md](references/coordinate-system.md) | Addresses, marker syntax, the coordinate laws with their examples and validation, multiple coordinates |
| [references/growth-and-drift.md](references/growth-and-drift.md) | Phases 0–F, usage-hook installation and maintenance, disagreement classification, and methodology drift |
| [references/named-abstractions.md](references/named-abstractions.md) | Create-only named implementation-abstraction admission, definition schema, source-claim semantics, maintenance, and retirement; loaded only under the conditions `create.md` §Named Implementation Abstractions states, and states none of its own |
| [references/ownership-boundary.md](references/ownership-boundary.md) | The Compass/Context Docs ownership contract in both directions, and the coordinate-first investigation flow |
| [references/verification.md](references/verification.md) | Every completion checklist that exists — root, L0, L1, L2, calibration, L3, coordinates, ownership, named abstractions, navigation, the blind semantic read; other files point there |

Each fact has one canonical owner. `SKILL.md` carries only the facts needed to
choose safely before either route loads: non-local applicability, declared chart
root, code-versus-semantics authority, coordinate meaning, disagreement classes,
and the no-mixing boundary. Create and Consume then leave one another's
procedure unloaded. Completion checklists are deliberately not mirrored: a
condensed checklist diverges, and the divergent copy is the one an agent finds.
