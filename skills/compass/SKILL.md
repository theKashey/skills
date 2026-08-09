---
name: compass
description: Use when establishing, exploring, or maintaining a semantic architecture chart—roots, L0–L4 levels, glossary, viewports, and code coordinates—or classifying chart-vs-code disagreement; not for reader-facing documentation or code changes.
---

# Compass

## Core Principle

Compass answers three questions about a codebase: **where am I, what is this thing, and why does it exist?** It answers them about the *system* — the logical thing the product is — not about the repository that currently realizes it. The codebase is one current realization; a Compass chart that survives a complete implementation rewrite is the one that was describing the system.

Compass is meta-code: a persistent logical model with two children — product behaviour and implementation coordinates — from which implementations can be understood, navigated, validated, discarded, and rebuilt.

Compass owns the logical system — concepts, phenomena, responsibilities, capabilities, rules, invariants, relationships, logical boundaries, ubiquitous language, and the reasons those things exist. Code owns the executable realization of that system. Implementation coordinates connect the two.

**Authority rule.** Repository structure is evidence about implementation, not authority over semantic architecture. Code may suggest architectural hypotheses. Code alone must not ratify L0–L2 semantic identity.

The deliverable is the chart — the architecture knowledge base itself — the first stop for an agent starting work, so recorded decisions sit on the path of work instead of being missed in passing. The method below is only how that information is produced and kept true.

Every chart document is agent-generated. The human teaches, validates, consults, and ratifies through the exploration loop's checkpoints; the human never writes chart content by hand.

Two nested things share the name: the compass skill (this package) and the compass registry (`COMPASS.md`, the L- artifact) — the skill is named after the first file worth having.

## The Rewrite Test

The admission gate for everything semantic. For every proposed root, bounded context, actor, or block, ask:

> If all current source code were deleted and the same product rebuilt in another language, framework, repository layout, and deployment topology, would this thing still need to exist?

**Yes** → strong semantic Compass candidate. **No** → it is implementation metadata, a technical mechanism, a deployment decision, or Context Docs material.

Survive a TypeScript → Rust rewrite: **Eligibility**, **Checkout**, **Document Review**, **Ranking**, **Settlement**. Usually do not, absent a separate logical reason: `ReactQueryProvider`, `CloudflareWorkerRouter`, `PrismaAdapter`, `src/features/orders/`.

**Strong invariant.** A pure implementation rewrite should permit `semantic Compass before == semantic Compass after` while replacing most or all implementation coordinates. The more semantic Compass changes merely because technology or topology changed, the more implementation structure has leaked into the model.

## The Invariance Test

Before creating, deleting, splitting, merging, promoting, or renaming any L0–L2 entity:

1. Describe what it represents without referring to source topology.
2. State its logical responsibility or phenomenon.
3. Identify important rules, inputs, outputs, effects, or invariants.
4. Identify how humans recognize it in the product or domain.
5. Only then map today's implementation locations.

Then ask: *would this boundary still make sense after a structure-only refactor?* If no, it is probably not a semantic boundary.

## Chart Root

The chart lives in one directory the host project declares in its agent instructions (`AGENTS.md`, `CLAUDE.md`, or equivalent) — for example a `.compass/` directory at the repository root. Read the declared root before any chart work. If no chart root is declared, ask the user to configure one; never invent a location or write chart files to an undeclared path. All layouts below are relative to `{chart-root}`.

## Quick Reference: Levels

| Level | Name | Contains | Kind | Volatility | Budget |
|-------|------|----------|------|-----------|--------|
| L- | Compass | Registry of roots and externals | semantic | org changes | ≤100w/entry |
| L0 | Domain | Bounded contexts, aggregates, context map. No tech. | semantic | years | ≤500w/context |
| L1 | System Context | Actors + external systems. Human-ratified. | semantic | quarters | ≤400w + diagram |
| L2 | Isolated Blocks | Major internal blocks. Tech enters here. | semantic identity, coordinate detail | months | ≤300w + diagram + component table |
| L3 | Components | Logical modules mapped to code paths. | coordinate | weeks | ≤200w |
| L4 | Viewports | Cross-cutting flows. 3–4 active max. | either | weeks | ≤500w/viewport |
| L5 | Infrastructure | Shared code. Not documented. | — | — | — |

**Kind decides who may change a thing and what evidence is required.** Semantic identity (L0–L2) must pass the rewrite test and follows the human ratification path. Coordinates (an L2 block's technology and implementation coordinates, all of L3, every `compass:` marker) are expected to churn as the implementation changes; an agent may remap them without a semantic ratification.

The zoom vocabulary is Simon Brown's C4 model — read context/container/component with that prior — bent at both ends. Deltas: L0 (DDD's strategic layer) sits below the stack; L2 "isolated blocks" **are** C4 containers, and the file layout keeps C4's name (`CONTAINERS.md`); C4's Level 4 (code diagrams) is replaced by viewports — code diagrams rot fastest, so the chart stops at L3 and wires to code by coordinates instead; L- and L5 bracket the stack, above and below C4's reach. C4 supplies notation and zoom vocabulary; it does not define Compass's source of truth. Re-evaluate any C4-derived rule that conflicts with semantic orientation.

Propagation: top → down only. If L3 contradicts L0, L3 is wrong.

## Scope and Roots

Declare before anything: `Scope: [what is the system]`.
- Scope defines internal (L2–L4) vs external (L1 box).
- Levels are relative to the chosen scope, not absolute.
- The method is fractal: every external system is someone else's L1.

A chart exposes one or more **roots** — stable logical starting points from which *where am I?* has a useful independent answer. Roots do not need to correspond to repositories, deployables, services, folders, or C4 systems. A Python backend and a TypeScript frontend are two blocks of one root unless each carries independent logical identity.

**Root admission test — all five required:**

1. Humans recognize it as a coherent area of reasoning or work.
2. Its logical identity survives implementation restructuring (rewrite test).
3. It has meaningful internal responsibilities or phenomena.
4. Independent *where am I?* navigation is useful.
5. A human ratifies the root.

The strong challenge: *if this repository were rebuilt from scratch, would humans still say "I am working on X"?*

Roots may overlap. A domain living inside a wider product can also be its own root, and the same code then carries a coordinate in each. Overlap is expected, not a defect. Agents may propose roots; agents must not invent them.

→ Multi-root cases and worked examples: [`references/blocks-and-levels.md`](references/blocks-and-levels.md#roots)

## Compass Registry (L-)

The registry is the first artifact worth having: one page from which every root, external, and demoted almost-external is reachable.

`COMPASS.md` is tiered — roots in one table, external systems in a second, named dependencies that are not external systems in a third — so a demotion stays recorded and nothing gets silently re-elevated.

**The registry describes the system's boundary, never its own approval trail.** Root ratification is a gate on the agent's behaviour (see *Boundaries*), and recording who ratified what, when, or whether a page has an owner puts the chart's production into the chart. Name the fact a reader needs — what a root is, why a thing sits outside the boundary — never the test that decided it.

→ Registry template: [`references/blocks-and-levels.md`](references/blocks-and-levels.md#compass-registry-template)

## Ubiquitous Language

Each root owns `{root}/GLOSSARY.md`, the canonical owner of that root's ubiquitous language. Every local product or domain term used architecturally appears there. Do not fill it with implementation terminology unless humans genuinely use that terminology as part of the domain.

When a glossary-defined term is used semantically in chart prose, render it in **bold**: "A **Matter** contains **Documents** and may produce **Findings**." Never bold filenames, paths, source identifiers, code, or Mermaid syntax.

Terms need not be globally unique. When one word means different things in different bounded contexts, record each meaning with its context explicitly.

Where product language and implementation language differ, the product or domain term is canonical and the code term is recorded as an implementation alias. Source naming never silently wins.

`GLOSSARY.md` owns terminology. `DOMAIN.md` owns relationships, contexts, aggregates, events, and invariants.

→ Glossary format: [`references/blocks-and-levels.md`](references/blocks-and-levels.md#glossarymd-format)

## Exploration Loop

Continuous loop: **orient → scan → probe → adjust**, triangulating three sources rather than comparing two — product/domain reality, the chart, and the implementation. Code yields a candidate model; product and domain reality verify it. Never derive L0/L1 semantics from code shape alone.

| State | What exists | Human role | Exit when |
|-------|------------|------------|-----------|
| 0 Clean slate | Nothing | Teacher | Scope + candidate roots + 2–5 blocks + externals + actors on scratchpad |
| 1 First pass | Scratchpad | Validator | L0 + glossary reviewed, L2 docs, boundaries resolved, levels calibrated |
| 2 Documented | L0–L2 | Consultant | L3 docs, boundary viewport (or L4 skipped) |
| 3 Deep knowledge | L0–L4 | Ratifier | No exit (steady state) |

States can regress per-block (new block → state 0, semantic change → state 1). A pure restructuring does not regress a state — it remaps coordinates.

Always state confidence explicitly: "I believe X based on [evidence]. Confidence: medium."

→ Full procedures, product/domain evidence sources, scratchpad format: [`references/exploration.md`](references/exploration.md)

## Level Calibration

Calibration is about **semantic scale** — breadth of logical responsibility — never lines of code, module count, or implementation complexity. After any decomposition, check whether siblings at one level sit at comparable semantic scale:

- oversized concept → consider promoting it (its own level, or its own root if it passes admission);
- several overly fine-grained concepts → consider grouping them under one named umbrella;
- uneven siblings → verify whether they actually belong at the same semantic zoom.

Run calibration as a pass after discovery. The first decomposition is not assumed correctly scaled.

→ Procedure: [`references/exploration.md`](references/exploration.md#level-calibration)

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

→ Per-level doc formats, the consumer-relationship block, and promotion criteria: [`references/blocks-and-levels.md`](references/blocks-and-levels.md)

## Coordinate System

- Address: dot-separated path from the root down — `root`, `root.block`, or `root.block.component`, as deep as the coordinate is accurate (unique names per parent).
- Coordinate: `compass: <address>` in a code comment, written in the host language's comment syntax (`//`, `#`, `--`, …).
- Validate: address exists, code path still matches, no stale markers.

**Coordinate laws (treat as invariants):**
- **A coordinate is a location, not a definition.** `// compass: checkout.payment.authorisation` means *the logic implemented here participates in this Compass location*. It does not mean *this source file defines that semantic boundary*. Coordinates may change while the place stays the same.
- **Coordinates bubble up.** Prefer one accurate coordinate covering a whole subtree (package > folder > file) — but never manufacture a source boundary solely to make attribution coarse.
- **File-level coordinates are for files whose location differs** from the enclosing one, not a default.
- **Multiple coordinates are legitimate** when code genuinely participates in more than one logical orientation, typically across roots. Prefer the smallest useful set; there is no fixed maximum.
- **Multiple coordinates trigger verification, not refactoring.** The question is whether these are genuinely independent logical orientations.
- **Coordinate density points; it does not sentence.** Where coordinates refuse to bubble up, physical and logical grouping disagree — a real lead, usually toward decluttering (a stray file moved to the subtree that shares its address, a two-job file split, a helper recognized as L5). Follow it, and prefer the move that makes the coordinate coarser when the code is better for it. But only independent cohesion or coupling evidence closes it as debt: a phenomenon may legitimately span packages and services, one module may serve several phenomena, and `repository topology != semantic topology` is the normal condition — never a demand to reshape the implementation until it resembles the chart.
- **Roots are human-ratified.** Agents propose roots; agents never invent one.

→ Full rules, examples, and validation: [`references/coordinate-system.md`](references/coordinate-system.md)

## Classifying Disagreement

Never infer `code != Compass, therefore Compass is stale`. Classify first:

- **Semantic change** — the logical system changed: business rule, invariant, capability, responsibility, domain meaning, actor interaction, meaningful effect. Compass may need to change; high-level semantic change requires the human ratification process.
- **Implementation remapping** — the same logical system is now implemented differently: files moved, package split, service extracted or merged, framework replaced, repository reorganized, database or language changed. Preserve semantic Compass; update coordinates.
- **Implementation violation** — the executable implementation contradicts ratified Compass semantics. Investigate whether the implementation is wrong, or whether an intentional semantic change happened without ratification.

Source code is authoritative evidence of what currently executes. It is not automatically authoritative evidence of what the system means or is intended to do.

→ Detection, response priority, and the full classification table: [`references/growth-and-drift.md`](references/growth-and-drift.md)

## Boundary with Context Docs

Both skills preserve "why", at different levels. The classifier is the rewrite test:

> Would this reason still matter if we threw away the implementation and rebuilt the same logical product?

**Yes** → Compass is a candidate canonical owner (*why does Payment Authorisation exist? why must Eligibility obey this invariant?*). **No** → if the reason still constrains the current implementation, it belongs to Context Docs or the code (*why must this acknowledgement happen after persistence? why is this retry here?*).

This is an ownership test, not a writing-style preference. Do not duplicate in either direction: Compass does not carry implementation fences, and implementation docs do not restate semantics Compass already owns — a coordinate is often the whole breadcrumb a local reader needs.

→ Both directions, the investigation flow, and worked cases: [`references/ownership-boundary.md`](references/ownership-boundary.md)

## Growth Pattern

- **0** — Scope + chart root + compass registration
- **0.5** — Explore (state 0 loop) → scratchpad; roots proposed, then ratified at the state-0 checkpoint, never before there is evidence
- **A** — Establish domain (L0 + `GLOSSARY.md`), human-checkpointed
- **B** — Frame system (L1 + L2); closes by installing the human-approved usage hook into the host's agent instructions
- **C** — Map components (L3), agent-driven
- **D** — Define viewports (L4, if needed)
- **E** — Maintain: re-run exploration on diffs, classify disagreement
- **F** — Seal coordinates, after semantic boundaries stabilize

→ Full phase details, disagreement procedures, and rules: [`references/growth-and-drift.md`](references/growth-and-drift.md)

## File Layout (directory-as-zoom)

Architecture docs live at `{chart-root}/`. **The directory structure IS the zoom hierarchy** — descending into a subfolder = zooming in one level. Every folder is named after the entity it describes, and **the identity document of every architectural directory is its `README.md`**, so opening any Compass directory on GitHub immediately answers *where am I?*

```
{chart-root}/
  README.md                   ← chart identity: scope + the roots below
  COMPASS.md                  ← registry (roots / L1 externals / demoted externals)
  externals/                  ← one doc per L1 external, linked from its COMPASS.md row
    {external-name}.md
  {root}/                     ← one ratified logical root of orientation
    README.md                 ← L1: the root as a black box + actors + externals
    DOMAIN.md                 ← L0: bounded contexts, aggregates, context map — no tech
    GLOSSARY.md               ← the root's ubiquitous language
    CONTAINERS.md             ← L2: opens the root — all blocks wired together
    VIEWPORTS.md              ← L4: cross-cutting flows (3–4 active max)
    {block}/                  ← L2 folder (one per block/container)
      README.md               ← L2 self-doc: responsibility, logical role, boundary,
                                coordinates, communicates-with, components, diagram
      {component}/            ← L3 folder (one per component)
        README.md             ← L3 self-doc: stereotype, context, I/O, depends-on,
                                used-by, boundary, coordinates, diagram
```

Three constraints the tree cannot carry: `{root}/README.md` is a black box — actors and external systems only, never internal structure; `DOMAIN.md` carries domain language only, never technology or coordinates; and a demoted external gets no `externals/` doc at all — it lives in the adapter that uses it.

`README.md` is promoted, never duplicated: an entity's identity document *is* its `README.md`. There is no `SCOPE.md`, `CONTEXT.md`, `BLOCK.md`, or `COMPONENT.md`. Explicitly named alternate views — `COMPASS.md`, `DOMAIN.md`, `GLOSSARY.md`, `CONTAINERS.md`, `VIEWPORTS.md` — keep their names because they are views, not identities.

**Semantic fields are real Markdown.** Use headings for fields, lists for sets, tables for homogeneous collections, links for navigation, Mermaid for diagrams. Never pseudo-fields (`Responsibility — …`) — the Markdown AST should expose the schema instead of forcing an agent to infer it from prose punctuation.

**Zoom chain (never skip a level):**
```
{chart-root}/README.md
  └→ COMPASS.md — which roots exist
       └→ {root}/README.md (L1)
            ├→ {root}/DOMAIN.md + GLOSSARY.md (L0 + language)
            ├→ {root}/CONTAINERS.md (L2 overview — opens the root)
            │    └→ {block}/README.md (L2)
            │         └→ {block}/{component}/README.md (L3)
            └→ {root}/VIEWPORTS.md (L4)
```

**Five document kinds require a Mermaid diagram:** `{root}/README.md`, `CONTAINERS.md`, every block `README.md`, every component `README.md`, and `VIEWPORTS.md` — each showing inputs, outputs, and key relationships at its level of abstraction. The rest of the chain carries none: `DOMAIN.md` (L0) stays prose, where a mermaid context map is acceptable but never required, and `{chart-root}/README.md`, `COMPASS.md`, and `GLOSSARY.md` have nothing to draw.

## L1 Abstraction Guardrails (Hard Rules)

Violations here are the most common lead/bleed failure mode. Memorise these before writing any L1 diagram.

**The single-box rule:** The L1 system context diagram must contain exactly **one** system node inside the boundary — the root itself. Count the nodes inside the subgraph: if the answer is not 1, the diagram is wrong.

**Allowed at L1:**
- The root (one box)
- Actors (people, organisations, roles that interact with it)
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

An external system is admitted because the product or operator reality shows it, not because a dependency manifest names it. A declared dependency is evidence of a mechanism; only the two tests admit an L1 node.

**Critical distinction — engine vs. store:**
- **Database engine** (SQLite, Postgres process, embedded library) → always L3 or lower — it's the mechanism
- **Database / data store / file** (the data at rest, user-owned, survives process restart) → L1 if the user consciously owns it and it outlives the system process

The same product can be L1 in one root and L3 in another. The test is always relative to the chosen scope and control boundary — never a fixed lookup table. Worked contrast examples: [`references/blocks-and-levels.md`](references/blocks-and-levels.md#level-promotion-criteria).

The runnable form of these rules is the L1 checklist in [`references/verification.md`](references/verification.md) — the canonical owner of all completion checklists.

## How to Use the Chart

→ Full guide: [`references/how-to-use.md`](references/how-to-use.md)

Quick patterns:
- **Starting a task** → read `{chart-root}/README.md` → `COMPASS.md` → `{root}/README.md` → `{root}/CONTAINERS.md` → find block → read `{block}/README.md` → find component → read `{component}/README.md`
- **Changing domain meaning** → `{root}/DOMAIN.md` + `{root}/GLOSSARY.md`
- **Debugging a flow** → open `{root}/VIEWPORTS.md` → find the viewport that covers the flow → trace participants
- **"Why is this code weird?"** → follow its `compass:` coordinate first; if the reason is implementation-specific and unresolved, continue under Context Docs
- **Reviewing a PR** → classify any chart/code disagreement before changing either side

## Verification

Before declaring a root, L0, L1, L2, L3, or Phase F complete, run the mandatory checks:

→ Full checklists, lead/bleed detection, spot check: [`references/verification.md`](references/verification.md)

There is no summary of those checklists here. A condensed second copy is what
diverges, and the divergent copy is the one an agent finds — read the gate.

## Boundaries

✅ Always: read the declared chart root before chart work; declare scope before L0; apply the rewrite test to every semantic candidate; propagate top → down; document relationships in consumers; keep within size budgets; classify disagreement before repairing it; state confidence explicitly.

⚠️ Ask first: proposing, promoting, or retiring a root; changes to scope or compass ownership; introducing viewports beyond 3–4; L0 boundary changes; renaming a glossary term; writing or updating the usage hook in the host's agent instructions (the only file the skill touches outside the chart root and source-code comments).

🚫 Never: write chart files outside the declared chart root or invent a root when none is configured; invent a logical root without human ratification; let code alone ratify L0–L2 semantic identity; document infrastructure as architecture (L5); contradict higher levels; treat a moved code path as evidence the semantics are wrong; demand implementation reshaping because topology and chart differ; seal coordinates before boundaries stabilize; skip human checkpoint at state 0 exit — when no human is available, stop there and report; do not proceed past any checkpoint unattended.
