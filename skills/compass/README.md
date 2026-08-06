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

## Compass and DeepWiki

[DeepWiki](https://docs.devin.ai/work-with-devin/deepwiki) is the chart's
nearest neighbour: an agent-generated projection of a codebase, regenerated
from current code. The two compete for the same role — the first
architectural explanation an agent should trust when starting work — even
though nothing prevents running both on one repository. This section is for
someone deciding whether Compass earns that role. It is analysis, not
advocacy, and the advantage it claims for Compass is theoretical until
tested (§What would settle it, below).

The selector between them is not repository size. It is:

> Is important architectural purpose recoverable from the current code
> structure?

Two conditions gate the decision:

- **Intent illegibility.** Material architectural purpose cannot be
  reliably inferred from code, folders, exports, dependencies, or tests.
- **Governance capacity.** The organisation can maintain, review,
  invalidate, and re-ratify authoritative architectural verdicts.

Compass is justified as an authoritative layer only when both are true.
When either fails, prefer a regenerated code-derived explanation.

### The structural difference is recursion

```text
DeepWiki_t = f(code_t, steering_t)
Compass_t = g(
  code_t,
  chart_{t-1},
  verdicts_t,
  ratifications_t
)
```

Both systems accept human input; the difference is what happens to it.
DeepWiki's steering — repository notes and page configuration in
`.devin/wiki.json` — is exogenous input to the current regeneration: it
shapes this build, and the next build can replace or drop it without
anything downstream being owed to it. Compass ratifications are endogenous:
a ratified verdict enters the chart's state and becomes input to every
future regeneration. Lower levels must conform to it, drift against it is
classified rather than auto-resolved by trusting code, and Phase F can seal
it into source comments. Everything below follows from this one
difference.

### Where each is strongest

DeepWiki is strongest when current structure honestly expresses
responsibility and relationships. It can regenerate from present code,
recover from stale generated documentation by discarding it, and answer
implementation questions — where is retry handled, what calls this
module — without preserving any prior architectural conclusion as
authority. When the code is legible, statelessness is a feature: nothing
persists that could be wrong tomorrow.

Compass adds unique value exactly where code cannot distinguish:

- an intended extension mechanism from accidental coupling;
- a compatibility contract from temporary legacy code;
- a policy boundary from an implementation detail;
- permitted dependencies from tolerated debt;
- a security or trust boundary from ordinary module structure.

This is not a size distinction. Consider a small plugin host — a protocol
library of a few thousand lines exposing a dozen hooks, of which three are
the supported extension surface and nine are accidents of history. No
reading of the present code separates the three from the nine; the
difference lives in intent, not structure, and any regenerated explanation
will describe all twelve with equal confidence. That small library needs
verdicts. A very large CRUD application whose folders, names, and
dependency edges honestly express its responsibilities may need none:
everything worth knowing is recoverable from structure, and a regenerated
explanation is cheaper and cannot preserve a stale conclusion.

### The correctness risk Compass adds

Criticism of an authoritative layer usually stops at maintenance cost. The
sharper risk is correctness:

> DeepWiki can regenerate a mistaken inference. Compass can preserve a
> mistaken verdict as authority.

Because propagation is top → down, a wrongly ratified boundary does not
stay local. It distorts every lower-level document that must conform to it,
flows into the agent-routing hook installed at Phase B, into the diagrams
on the zoom chain, and — after Phase F — into source attribution, at which
point correcting it is a code change multiplied across every sealed file.

There is also a failure mode that produces no doc–code drift at all:

```text
A verdict remains consistent with the code.
The chart remains consistent with the code.
But a premise supporting the verdict has changed.
Therefore the verdict may now be wrong without producing doc–code drift.
```

Example: authentication policy was kept in the trusted core because
plugins executed in-process and were untrusted. Plugins later execute in
isolated workers with signed capabilities. The code may still respect the
old boundary — nothing drifts on any chart-vs-code comparison — but the
original verdict now requires re-ratification, because the premise that
justified it is gone.

The current drift classification
([growth-and-drift.md](references/growth-and-drift.md)) is mostly
code-vs-document or code-vs-boundary. It does not adequately represent
verdict-vs-premise drift, which is invisible to any comparison of chart
against code.

### Proposed: a first-class verdict ledger

The chart currently records verdicts inside generated prose, which makes a
ratified boundary and an agent's observation typographically identical.
Generated observations and ratified verdicts must not be indistinguishable
within the same prose — the reader (human or agent) needs to know which
sentences carry authority and which merely describe.

The proposal is a verdict ledger separate from generated chart prose. Each
verdict records:

- stable ID;
- normative statement;
- scope;
- status;
- supporting premises;
- evidence for each premise;
- premise invalidation conditions;
- ratification date;
- approving authorities;
- who may amend or revoke it;
- review triggers;
- propagation scope;
- source-attribution (sealing) status.

The layout separates the two kinds of content under the declared chart
root:

```text
.compass/
  generated/   ← replaceable facts derived from current code
  verdicts/    ← durable but reviewable architectural decisions
  rendered/    ← combines them for navigation
```

Regeneration then has defined semantics per kind: overwrite changed
observations; report code–verdict conflicts rather than resolving them;
suspend verdicts whose premises are invalidated; and request
re-ratification before propagating a suspended verdict anywhere.

This is a proposal, not the current layout. It touches chart-baked
vocabulary (file layout, document roles), which under this skill's own
freeze-first criterion must settle before charts embed it — another reason
it waits on the evaluation below rather than shipping by default.

### L0 should be opt-in

L0 currently sits at the top of the stack as if every system deserves a
domain layer. That default is worth reversing. A synthetic domain layer is
actively dangerous because Compass requires lower levels to conform to
higher ones: an incorrectly ratified L0 can distort every lower
description while remaining difficult to falsify from code — domain prose
has no code paths to check against.

L0 should be opt-in with three explicit states:

- `absent` — no domain layer; the stack starts at L1;
- `deferred` — a domain layer is expected but not yet ratified; nothing
  below may cite it;
- `declared` — a domain layer exists, and each of its boundaries is
  represented as a verdict with evidence and invalidation conditions.

The burden of proof is on declaring. An L0 that cannot state what evidence
supports each bounded context, and what change would invalidate it, is a
liability wearing the costume of rigor.

### Phase F is an authority escalation

Phase F's stated rationale is maintenance cost: seal only when comments
cost less than the navigability they buy. That framing is incomplete.
Source attribution seals architectural verdicts back into the codebase —
it escalates their authority and multiplies the cost and reach of
correcting a wrong one, because every sealed file becomes part of the
blast radius.

Do not seal a verdict into source comments unless:

- it is explicitly represented in the verdict ledger;
- its premises and invalidation conditions are recorded;
- responsible authorities are identified;
- it has survived a relevant architectural change;
- its navigation value exceeds both maintenance cost and correction blast
  radius.

### Reading DeepWiki accurately

A fair comparison must distinguish three surfaces:

- generated DeepWiki wiki pages (public repositories on deepwiki.com,
  private ones in the Devin app);
- public DeepWiki Q&A on those pages;
- Ask Devin's indexed code search, available in the full app.

Limits are per surface: a configured wiki page limit bounds the generated
wiki, not the code search index, and is not evidence that repository code
search has the same limit. Numeric limits change; verify current figures
against the [official documentation](https://docs.devin.ai/work-with-devin/deepwiki)
at decision time rather than trusting any figure written down here.

### Decision table

| Purpose recoverable from structure | Verdict governance capable | Recommendation |
| --- | --- | --- |
| Yes | Either | Prefer regenerated code-derived explanation |
| No | Yes | Compass may add unique value |
| No | No | Neither tool solves the architectural problem |
| Yes | Yes | Compass must justify duplicated authority |

The fourth row is the honest one: even when both gates pass, an
authoritative layer duplicates what structure already says and must earn
its keep against the correctness risks above.

### What would settle it

The claims in this section are falsifiable by a same-repository
comparison. Test at least:

1. implementation discovery — find where behaviour lives;
2. intent discrimination — separate supported surface from accident (the
   plugin-host case);
3. change review — does a proposed change violate a real boundary;
4. verdict-premise drift — is the invalidated-premise case detected;
5. deliberately wrong ratification — how far does a planted false verdict
   propagate before something catches it;
6. correction cost after propagation or source attribution.

Compare three configurations: DeepWiki with neutral steering; current
Compass with human checkpoints; Compass with the proposed verdict ledger.

Score with metrics such as implementation accuracy, verdict accuracy,
false-authority rate, appropriate uncertainty, premise-drift detection,
human maintenance cost, recovery cost, and attribution blast radius. The
product to watch is:

```text
false-authority rate × correction cost
```

A generated-wiki error and a persistent authoritative Compass error must
not be scored equally: the first costs one regeneration, the second costs
whatever its propagation already touched.

### The bounded claim

> Compass may provide information that code-derived tools cannot recover
> when architectural purpose is structurally illegible and the
> organisation can govern durable verdicts. Its recursive authority also
> creates failure modes that stateless regeneration does not have.
