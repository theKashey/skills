# Compass

The compass skill governs a C4-inspired architecture chart under a chart root
the host project declares: a scoped L0–L4 level stack, a tiered compass
registry, viewports, and `// compass:` code attribution. It documents what
exists and how it connects; it does not prescribe implementations, tests, or
requirements.

Two nested things share the name: the skill package and the compass registry
(`COMPASS.md`), the chart's root artifact. The package is deliberately named
after the first file worth having.

## Why it exists

A repository accumulates pieces — tools, services, docs, decisions — faster
than any reader can hold them, and to a coding agent conventional context docs
are reefs: passive files off the path of work. The agent sails past them, and
the decisions and opportunities they record are missed. Structure that is not
on the path of work does not exist.

The intended impact is that every file, tool, and move has a place and a
purpose. A place is an address in the stack, ultimately a `// compass:`
comment in the code itself; a purpose is a documented responsibility with a
boundary. An agent starting a task then meets the relevant decisions on its
way in. The knowledge base is the deliverable; the method is only how it is
produced and kept true. The compass registry comes first because it is the
dot-connector: one page from which every system, external, and demoted
almost-system is reachable.

The chart is a second projection of the system, kin to generated code wikis:
code projects mechanics onto files, the chart projects place and boundary onto
addresses. The map is not the territory, and this map is valuable for exactly
what the territory cannot show: verdicts — ratified boundaries, recorded
demotions, consumer replacement conditions — that no amount of code reading
can reproduce. That is also why drift between the two is classified rather
than resolved by trusting either side: a purely regenerated wiki can always
defer to code, but a chart that did so would silently erase its verdicts. Everything in the chart is
agent-generated; the human contributes judgment through checkpoints (teacher,
validator, consultant, ratifier by knowledge state) and never writes chart
content by hand.

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
- **Attribution is sealed last (Phase F)**, instead of attribute-as-you-go:
  wiring code to docs before boundaries stabilize locks in wrong boundaries
  and makes every rename a documentation change.
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
- **C4 by name, with declared deltas**, instead of either C4 verbatim or an
  unlabelled homegrown stack. Naming the model recruits everything a reader
  (human or model) already knows about context/container/component zoom; the
  declared deltas fence the three places that prior mis-predicts. C4's code
  level is replaced by viewports plus attribution because code diagrams are
  the fastest-rotting artifact in the method; L0 is added because agents need
  the domain's own language (DDD, Evans) before they can name blocks; the
  registry and the undocumented floor bracket the stack because charts live
  in fleets and codebases have plumbing.
- **Chart-baked vocabulary freezes first; gates iterate.** The file layout,
  document names and formats, the marker literal, and the address grammar are
  what every produced chart physically embeds — changing them later rebuilds
  every chart, so they are settled before first use. Checklists and thresholds
  only change how the next pass judges an existing chart, so they may tighten
  release by release without invalidating anything already built.
- **The attribution marker is `compass: <address>`, written in the host
  language's comment syntax** (`// compass:` in TypeScript, `# compass:` in
  Python), instead of `c4:` after the methodology. The marker names the system
  that owns the address space, so an agent meeting it in code can reach the
  chart that defines the address; the methodology name explains where the
  level stack came from and answers no question at a call site. The marker
  body is a fixed literal in every project — never the host repository's own
  name — because the checks that read it are written once, shipped with the
  skill, and match the body without a comment prefix.

## Boundaries

The docs answer "what exists and how it connects". Implementation guidance,
performance, test strategy, deployment topology, and business requirements are
out of scope (§What the Chart Does NOT Answer in the how-to guide). Reader-
facing documentation — READMEs, references, tutorials — is a different craft
with a different owner; compass claims only the chart. Completion is measured
by the verification gates, not by prose confidence. The skill puts the chart
on the path of work — a human-approved usage hook in the host's agent
instructions, installed at Phase B — but whether agents then follow it is
outside the skill's evaluation boundary.

## Runtime architecture

| File | Owns |
| --- | --- |
| [SKILL.md](SKILL.md) | Activation, chart root contract, level tables, L1 guardrails, file layout, and the always-loaded mirror of the attribution laws |
| [references/exploration.md](references/exploration.md) | The orient→scan→probe→adjust loop, per-state procedures and exits, scratchpad format |
| [references/blocks-and-levels.md](references/blocks-and-levels.md) | The contents of each level's documents, the registry template, promotion criteria with contrast examples; placement stays with SKILL.md §File Layout |
| [references/coordinate-system.md](references/coordinate-system.md) | Addresses, marker syntax, the attribution laws with their examples and validation, domain controllers, dual-stack limit |
| [references/growth-and-drift.md](references/growth-and-drift.md) | Phases 0–F and both anti-drift procedures |
| [references/how-to-use.md](references/how-to-use.md) | Task-to-navigation patterns over finished docs |
| [references/verification.md](references/verification.md) | Every completion checklist that exists — L1, L2, L3, Phase F; other files point there |

Each fact has one canonical owner, and `SKILL.md` mirrors what an agent must
not miss before it decides whether to open a reference at all — the attribution
laws most of all, because an agent that never opens `coordinate-system.md`
would otherwise attribute per file, the failure those laws exist to prevent.
A mirror summarises; it never adds a rule of its own, and where a mirror and
its owner disagree, the owner wins. Completion checklists are deliberately not
mirrored: a condensed checklist diverges, and the divergent copy is the one an
agent finds. The runtime router may point to a reference, but nothing at
runtime points here.
