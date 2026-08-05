---
name: compass
description: Use when establishing, exploring, or maintaining a C4-inspired architecture chart—scoped L0–L4 levels, compass registry, viewports, code attribution—or checking chart-vs-code drift; not for reader-facing documentation or code changes.
---

# Compass

## Core Principle

Give every file, tool, and move in the codebase a place and a purpose: a place is an address in the stack, a purpose is a documented responsibility with a boundary. Document architecture as a scoped L0–L4 stack. Scope is chosen first; each level adds fidelity without contradicting higher levels. The map is not the territory — exploration loops keep the chart honest against the code, and drift is classified, never trusted to either side. Viewports answer cross-cutting questions that individual component docs cannot.

The deliverable is the chart — the architecture knowledge base itself — the first stop for an agent starting work, so recorded decisions sit on the path of work instead of being missed in passing. The method below is only how that information is produced and kept true.

Every chart document is agent-generated. The human teaches, validates, consults, and ratifies through the exploration loop's checkpoints; the human never writes chart content by hand.

Two nested things share the name: the compass skill (this package) and the compass registry (`COMPASS.md`, the L- artifact) — the skill is named after the first file worth having.

## Chart Root

The chart lives in one directory the host project declares in its agent instructions (`AGENTS.md`, `CLAUDE.md`, or equivalent) — for example a `.compass/` directory at the repository root. Read the declared root before any chart work. If no chart root is declared, ask the user to configure one; never invent a location or write chart files to an undeclared path. All layouts below are relative to `{chart-root}`.

## Quick Reference: Levels

| Level | Name | Contains | Volatility | Budget |
|-------|------|----------|-----------|--------|
| L- | Compass | Org-wide system registry | org changes | ≤100w/entry |
| L0 | Domain | Bounded contexts, aggregates, context map. No tech. | years | ≤500w/context |
| L1 | System Context | Actors + external systems. Human-ratified. | quarters | ≤400w + diagram |
| L2 | Isolated Blocks | Major internal blocks. Tech enters here. | months | ≤300w + diagram + component table |
| L3 | Components | Logical modules mapped to code paths. | weeks | ≤200w |
| L4 | Viewports | Cross-cutting flows. 3–4 active max. | weeks | ≤500w/viewport |
| L5 | Infrastructure | Shared code. Not documented. | — | — |

The stack is Simon Brown's C4 model — read the levels with that prior — bent at both ends. Deltas from standard C4: L0 (DDD's strategic layer) sits below the stack; L2 "isolated blocks" **are** C4 containers, and the file layout keeps C4's name (`CONTAINERS.md`); C4's Level 4 (code diagrams) is replaced by viewports — code diagrams rot fastest, so the chart stops at L3 and wires to code by attribution instead; L- and L5 bracket the stack, above and below C4's reach.

Propagation: top → down only. If L3 contradicts L0, L3 is wrong.

## Scope

Declare before anything: `Scope: [what is the system]`.
- Scope defines internal (L2–L4) vs external (L1 box).
- Levels are relative to the chosen scope, not absolute.
- The method is fractal: every external system is someone else's L1.
- One deployable product is one system, whatever languages it mixes — a
  Python backend and a TypeScript frontend are two containers, not two
  systems. Declare multiple systems only when the human names multiple scopes.

## Compass Registry (L-)

Organization-wide registry, owned by one principal engineer — and the first artifact worth having: one page from which every system, external, and demoted almost-system is reachable. For single-system use, maintain a local compass of external systems touched.

`COMPASS.md` is tiered — true L1 entries in one table, demoted L2/L3 externals in a second, human-declared lens roots in a third — so a demotion stays recorded, nothing gets silently re-elevated, and every second stack has a named owner.

→ Registry template: [`references/blocks-and-levels.md`](references/blocks-and-levels.md#compass-registry-template)

## Exploration Loop

Continuous loop: **orient → scan → probe → adjust**.
What changes across knowledge states is depth, source of truth, and human role.

| State | What exists | Human role | Exit when |
|-------|------------|------------|-----------|
| 0 Clean slate | Nothing | Teacher | Scope + 2–5 blocks + externals + actors on scratchpad |
| 1 First pass | Scratchpad | Validator | L0 reviewed, L2 docs, boundaries resolved |
| 2 Documented | L0–L2 | Consultant | L3 docs, boundary viewport (or L4 skipped) |
| 3 Deep knowledge | L0–L4 | Ratifier | No exit (steady state) |

States can regress per-block (new block → state 0, refactor → state 1).

Always state confidence explicitly: "I believe X based on [evidence]. Confidence: medium."

→ Full procedures, scratchpad format, and examples: [`references/exploration.md`](references/exploration.md)

## Viewports (L4)

Four viewport types — runtime, domain, boundary, lifecycle — with creation triggers and procedures in [`references/blocks-and-levels.md`](references/blocks-and-levels.md#l4--viewports).

Select by task:
- Work within one block → runtime (if needed)
- Change domain concept → domain + boundary
- Debug wrong output → lifecycle
- Modify bridge → boundary

Create: start with a question → trace L3 participants → mermaid diagram → document seams → name by question.

Skip L4 if L3 components are small and loosely coupled.

## Block Documentation (BEM)

Blocks document themselves. Consumers document relationships: when block A uses block B, the why, the relied capabilities, and the replacement conditions live in A, never in B.

→ Per-level doc formats, consumer-relationship block, shared kernel, and promotion criteria: [`references/blocks-and-levels.md`](references/blocks-and-levels.md)

## Coordinate System

- Address: dot-separated `l1.l2.l3` (unique names per parent).
- Attribution: `compass: <address>` in a code comment, written in the host language's comment syntax (`//`, `#`, `--`, …).
- Gravity: annotate at coarsest accurate level (package > folder > file).
- Domain controllers: composition-only files at L1/L2/L3 that wire the architecture.
- Validate: address exists, code path matches, no stale comments.

**Attribution laws (treat as invariants):**
- **Attribution bubbles up.** Prefer package/folder attribution over file attribution whenever one accurate attribution covers the whole subtree.
- **File-level attribution is exceptional.** Use it only when the file is an imposter or when no sound folder/package attribution can be established.
- **Folder/package attribution is enough** when all files in that subtree belong to the same primitive; exclude tests when they do not belong to that primitive.
- **Dual-stack is exceptional.** Max two attributions from different stacks on one file, typically `product` + `subproduct`.
- **Second stack is human-decided.** Agents must not create parallel stacks; they may only honor an existing human-created lens.
- **Second stack must be objectively sound.** A human-created lens is valid only when it forms a sound C4 construct, which means its L1 is complex enough to deserve its own stack.

→ Full rules, examples, domain controllers, and validation: [`references/coordinate-system.md`](references/coordinate-system.md)

## Growth Pattern

```
0   → Scope + compass registration
0.5 → Explore (state 0 loop) → scratchpad
A   → Establish domain (L0) — human-checkpointed
B   → Frame system (L1 + L2) — closes by installing the usage hook
      into the host's agent instructions (human-approved)
C   → Map components (L3) — agent-driven
D   → Define viewports (L4, if needed)
E   → Maintain — re-run exploration on diffs
F   → Seal connections — attributions after stability
```

→ Full phase details, anti-drift procedures, and rules: [`references/growth-and-drift.md`](references/growth-and-drift.md)

## File Layout (directory-as-zoom)

Architecture docs live at `{chart-root}/`. **The directory structure IS the zoom hierarchy** — descending into a subfolder = zooming in one level. Every folder is named after the entity it describes.

```
{chart-root}/
  SCOPE.md                    ← scope declaration
  COMPASS.md                  ← compass registry (tiered: L1 / L2-L3 / lenses)
  externals/                  ← one doc per L1 external system, linked from its COMPASS.md row
    {external-name}.md
  {system-name}/              ← L1 folder (one per system in scope)
    DOMAIN.md                 ← L0: bounded contexts, aggregates, context map — no tech
    CONTEXT.md                ← L1: black box + actors + external systems only
    CONTAINERS.md             ← L2: opens the system — all containers wired together
    VIEWPORTS.md              ← L4: cross-cutting flows (sequence diagrams, 3–4 active max)
    {container-name}/         ← L2 folder (one per container/block)
      BLOCK.md                ← L2 self-doc: responsibility, root, tech, boundary,
                                communicates-with, components, diagram
      {component-name}/       ← L3 folder (one per component)
        COMPONENT.md          ← L3 self-doc: stereotype, context, I/O, depends-on,
                                used-by, boundary, code paths, diagram
```

**Standard file names per level:**
- L0: `DOMAIN.md` — bounded contexts and context map. Domain language only, no technology.
- L1: `CONTEXT.md` — black box only. Actors + external systems. No internal structure.
- L1 external: `externals/{external-name}.md` — one external-system doc, linked from its compass row. Demoted L2/L3 externals get no doc here; they live in the adapter that uses them.
- L2 overview: `CONTAINERS.md` — opens the black box. All containers + wiring. The zoom-in from L1.
- L2 self-doc: `BLOCK.md` — one container's self-description. Lives inside the container folder.
- L3: `COMPONENT.md` — one component. Lives inside the component folder.
- L4: `VIEWPORTS.md` — cross-cutting sequence diagrams. Lives at system folder level.

**Zoom chain (never skip a level):**
```
CONTEXT.md (L1)
  └→ CONTAINERS.md (L2 overview — opens the system)
       └→ {container}/BLOCK.md (L2 self-doc)
            └→ {container}/{component}/COMPONENT.md (L3)
  └→ VIEWPORTS.md (L4)
```

**Every zoom-chain doc has a Mermaid diagram.** The chart is primarily visual: `CONTEXT.md`, `CONTAINERS.md`, `BLOCK.md`, `COMPONENT.md`, and `VIEWPORTS.md` each require a diagram showing inputs, outputs, and key relationships at their level of abstraction. `DOMAIN.md` (L0) stays prose — a mermaid context map is acceptable, never required — and `SCOPE.md`/`COMPASS.md` carry none.

## L1 Abstraction Guardrails (Hard Rules)

Violations here are the most common lead/bleed failure mode. Memorise these before writing any L1 diagram.

**The single-box rule:** The L1 system context diagram must contain exactly **one** system node inside the boundary — the scoped system itself. Count the nodes inside the subgraph: if the answer is not 1, the diagram is wrong.

**Allowed at L1:**
- The system (one box)
- Actors (people, organisations, roles that interact with the system)
- External systems that pass the User-Possession Test
- Relationships between the above, labelled with what data or action crosses

**Forbidden at L1:**
- Internal blocks (those are L2)
- Internal components or adapters (those are L3)
- SDK names, API version names, endpoint paths, protocol details
- Internal edges between internals
- Anything that runs inside the system boundary or is implemented by you

**Two orthogonal tests — apply both. Both must pass for L1; passing only one is not enough.**

**1. User-Possession Test:** *"Would the primary actor name this as a top-level tool or service they use, independent of this system?"*
- Yes → L1 candidate (name the product/service, not the API)
- No → keep it at L2/L3 as an adapter, gateway, or implementation detail

**2. Control Boundary Test:** *"If this system stopped running, does this thing still exist and belong to the user/operator?"*
- Yes → it lives outside the application control boundary → L1 candidate
- No → it's bundled with or owned by the system → L2/L3

**Critical distinction — engine vs. store:**
- **Database engine** (SQLite, Postgres process, embedded library) → always L3 or lower — it's the mechanism
- **Database / data store / file** (the data at rest, user-owned, survives process restart) → L1 if the user consciously owns it and it outlives the system process

The same product can be L1 in one system and L3 in another. The test is always relative to the chosen scope and control boundary — never a fixed lookup table. Worked contrast examples: [`references/blocks-and-levels.md`](references/blocks-and-levels.md#level-promotion-criteria).

The runnable form of these rules is the L1 checklist in [`references/verification.md`](references/verification.md) — the canonical owner of all completion checklists.

## How to Use the Chart

→ Full guide: [`references/how-to-use.md`](references/how-to-use.md)

Quick patterns:
- **Starting a task** → read `SCOPE.md` → `{system}/CONTEXT.md` → `{system}/CONTAINERS.md` → find block → read `{container}/BLOCK.md` → find component → read `{component}/COMPONENT.md`
- **Debugging a flow** → open `{system}/VIEWPORTS.md` → find the viewport that covers the flow → trace participants
- **Estimating a task** → identify which blocks/components are touched → count boundary crossings → check viewport for surprise dependencies
- **Reviewing a PR** → check if changes fit declared boundaries → if not, update doc OR flag boundary violation

## Verification

Before declaring L1, L2, L3, or Phase F complete, run the mandatory checks:

→ Full checklists, lead/bleed detection, anti-drift spot check: [`references/verification.md`](references/verification.md)

There is no summary of those checklists here. A condensed second copy is what
diverges, and the divergent copy is the one an agent finds — read the gate.

## Boundaries

✅ Always: read the declared chart root before chart work; declare scope before L0; propagate top → down; document relationships in consumers; keep within size budgets; state confidence explicitly.

⚠️ Ask first: changes to scope or compass ownership; introducing viewports beyond 3–4; L0 boundary changes; writing or updating the usage hook in the host's agent instructions (the only file the skill touches outside the chart root and source-code comments).

🚫 Never: write chart files outside the declared chart root or invent a root when none is configured; document infrastructure as architecture (L5); contradict higher levels; attribute files before boundaries stabilize; skip human checkpoint at state 0 exit — when no human is available, stop there and report; do not proceed past any checkpoint unattended.
