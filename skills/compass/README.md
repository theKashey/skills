# Compass

The compass skill governs a semantic architecture chart under a chart root the
host project declares: one or more human-ratified logical roots, a scoped L0–L4
level stack, a per-root glossary, a tiered registry, viewports, and
`// compass:` implementation coordinates in source. It describes what the
system *is*; it does not prescribe implementations, tests, or requirements.

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
changes a rule, or asks whether something belongs here does. Claiming otherwise
trains readers to skip it entirely. **And it never carries a fact a command can
answer.** Build graphs, dependency edges, CI configuration, ownership data,
schemas, test results: where an authoritative machine-readable
source exists the chart points into it, because a summary of a live source is a
second copy with no owner and it is wrong from the next commit. Implementation
coordinates are the deliberate exception and stay authored: they exist so an
agent reaches code without scanning, they are written before any marker is
sealed, and they name entry points no scan produces. Runtime state, task
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
- **Consumers own relationships (BEM)**, instead of provider-side lists: a
  provider cannot know why it is used, and provider-side lists rot silently.
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
- **An explicit ownership contract with Context Docs**, instead of leaving two
  skills that both preserve "why" to overlap by feel. The rewrite test doubles
  as the classifier, so a reason has exactly one owner and neither skill
  restates the other.
- **One checklist owner** (`references/verification.md`), instead of per-file
  checklists: duplicated checklists diverge, and the divergent copy is the one
  an agent finds.
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
  release by release without invalidating anything already built.
- **The coordinate marker is `compass: <address>`, written in the host
  language's comment syntax** (`// compass:` in TypeScript, `# compass:` in
  Python). The marker names the Compass-owned address space, so an agent
  meeting it in code can reach the chart that defines the address. Its body is
  a fixed literal in every project — never the host repository's own name —
  because the checks that read it are written once, shipped with the skill,
  and match the body without a comment prefix.

## Boundaries

The chart answers what the system is, what its parts are responsible for, and
how they relate. Implementation guidance, mechanism-specific rationale,
performance, test strategy, deployment topology, business requirements, and how
the repository happens to be arranged are out of scope (§What the Chart Does
NOT Answer in the how-to guide). Reader-facing documentation — READMEs,
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
| [SKILL.md](SKILL.md) | Activation, chart root contract, the rewrite and invariance tests, root admission, level tables, L1 guardrails, file layout, and the always-loaded mirrors of the coordinate laws and the disagreement classification |
| [references/exploration.md](references/exploration.md) | The orient→scan→probe→adjust loop, triangulation and evidence sources, per-state procedures and exits, level calibration, scratchpad format |
| [references/blocks-and-levels.md](references/blocks-and-levels.md) | Roots in practice, the contents of every chart document, the registry and glossary templates, Markdown conventions, promotion criteria with contrast examples; placement stays with SKILL.md §File Layout |
| [references/coordinate-system.md](references/coordinate-system.md) | Addresses, marker syntax, the coordinate laws with their examples and validation, multiple coordinates |
| [references/growth-and-drift.md](references/growth-and-drift.md) | Phases 0–F, the usage hook, the disagreement classification with its table and priorities, methodology drift |
| [references/ownership-boundary.md](references/ownership-boundary.md) | The Compass/Context Docs ownership contract in both directions, and the coordinate-first investigation flow |
| [references/how-to-use.md](references/how-to-use.md) | Task-to-navigation patterns over finished docs |
| [references/verification.md](references/verification.md) | Every completion checklist that exists — root, L0, L1, L2, calibration, L3, coordinates, ownership, navigation; other files point there |

Each fact has one canonical owner, and `SKILL.md` mirrors what an agent must
not miss before it decides whether to open a reference at all — the rewrite
test, the coordinate laws, and the three-way classification most of all,
because an agent that never opens a reference would otherwise attribute per
file and repair every disagreement by rewriting the chart, the two failures
those rules exist to prevent.
A mirror summarises; it never adds a rule of its own, and where a mirror and
its owner disagree, the owner wins. Completion checklists are deliberately not
mirrored: a condensed checklist diverges, and the divergent copy is the one an
agent finds. The runtime router may point to a reference, but nothing at
runtime points here.
