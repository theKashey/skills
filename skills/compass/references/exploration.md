# Exploration: Full Procedures

## The Loop

Exploration is continuous — not a phase that completes. It runs at different intensities throughout the life of the chart.

States run 0 (clean slate) → 1 (first pass) → 2 (documented) → 3 (deep knowledge), and any state can fall back.

Forward transitions: exploration and documentation.
Backward transitions: new block (state 0), semantic change invalidates L3 (state 1), unclassified disagreement (state 2).

A refactor, an extraction, or a full reimplementation is **not** a regression trigger: it remaps coordinates and leaves the state where it was.

Human role shifts with the state: **0 teacher** (agent asks, human explains) → **1 validator** (agent proposes, human confirms) → **2 consultant** (agent leads, human supplies context) → **3 ratifier** (agent proposes, human approves).

At every state, be explicit about confidence: "I believe X based on [evidence]. Confidence: medium. Open questions: [list]."

---

## Triangulate, Don't Compare

High-level exploration has three sources, not two: product/domain reality, the chart, and the implementation. Code yields a **candidate model**; product and domain reality **verify** it.

Never derive L0/L1 semantics from code shape alone. A codebase can name, group, and layer its files in ways that have nothing to do with what the system is, and any model read straight off the file tree inherits those accidents.

### High-level exploration order

At early states, run this order — evidence before boundaries, boundaries before coordinates:

1. Establish scope and candidate roots.
2. Collect product and domain vocabulary.
3. Identify human-recognizable phenomena.
4. Inspect rules and responsibilities.
5. Inspect code for evidence.
6. Propose logical boundaries.
7. Map them to product appearance.
8. Map them to implementation coordinates.
9. Populate or update `GLOSSARY.md`.
10. Record code/product terminology differences as implementation aliases.
11. Surface uncertainty.
12. Obtain the required human ratification.

Steps 1–4 come before step 5 deliberately. Reading code first anchors the model to file structure, and every later step then argues against that anchor instead of from evidence.

### Product and domain evidence

"Observable" does not mean "one visible UI thing", and a GUI is not required. Depending on the system, inspect:

UI · navigation · workflows · product vocabulary · business rules · state transitions · externally visible effects · CLI behaviour · APIs as humans understand and use them · reports · exports · notifications · operator workflows · documentation · human explanation.

A phenomenon may span many implementation modules and remain one thing:

```text
**Document Review**

upload
+ parser
+ extraction
+ workers
+ persistence
+ permissions
+ rendering
```

The source tree contains many technical things. The product contains one phenomenon: **Document Review**. Compass must preserve that logical unity rather than mirroring the seven directories.

---

## State 0 — Clean Slate

**What you know:** Nothing. Maybe a repo URL and a one-sentence scope.
**Ambiguity:** Maximum.
**Human role:** Primary source. Ask before assuming.

### Orient

Start with what the product is, then read only shape:

1. What does this system do for whom? Ask the human, read the product surface, read user-facing docs.
2. Project root: `Package.swift`, `package.json`, `Cargo.toml`, `docker-compose.yml`, `Makefile`, README
3. Directory tree: `ls -R` at depth 2–3, ignore `node_modules/`, `build/`, `dist/`, `.git`
4. Entry points: main files, index files, app delegates, route definitions
5. Config and env: `.env` files, `config/`, CI pipeline definitions
6. Dependencies: lockfiles, import maps, dependency graphs

From this determine:
- What areas of reasoning does the human name when describing their work? (candidate roots)
- What kind of thing is the repository (single app, monorepo, monolith with modules)? — a fact about packaging, not about roots
- What languages and frameworks? How many runtimes?
- Deployment shape (one binary, services, static + API, embedded)?

Items 2–6 are evidence about the implementation. They can suggest where a boundary might be; they never establish one.

If orientation takes too long, scope is too wide.

### Scan

Structural signals, not code reading.

**Dependency direction.** Use dependency tooling if available (dependency-cruiser, madge, swift-dependency-graph). Fallback:

```bash
grep -rn "^import\|^from\|^require\|^use " src/   # target codebase source root
```

Filter with `--include` globs for the target's languages (e.g. `--include="*.swift"`).

Build adjacency list. Look for:
- Clusters importing each other heavily → candidate components
- Files everything imports → likely infrastructure (L5)
- Files importing across seams → bridges (or leaks — decide later, with the chart)
- Circular dependencies → boundary confusion

**Naming conventions.** Domain words (`orders/`, `billing/`, `identity/`) → the product's vocabulary may be visible in code. Technical words (`services/`, `utils/`) → the vocabulary lives elsewhere; go get it from the product.

**Size distribution.** Large files → god-files. Deep trees → over-abstraction. Neither says anything about semantic scale.

**Tests.** Locations and naming reveal groupings and priorities, and often carry domain vocabulary the source hides.

### Probe

Read targeted files — not all code.

Targets: high-traffic files, boundary files, entry points, bridge files, god-files.

For each target, answer:
1. What domain concept or phenomenon does this file serve?
2. What does it depend on?
3. What depends on it?
4. Does it participate in more than one logical place?

Read just enough to answer. Stop when you have them.

Question 4 replaces "does it respect its directory boundary": a file reaching across directories is a mapping fact to record, not a verdict.

### Adjust

Each step may invalidate the previous.

- **Scope adjustment:** re-declare if too wide or narrow.
- **Root candidates shift:** a candidate that only exists because a package exists is not a root; a domain the human keeps describing independently may be one.
- **Block candidates shift:** drop infrastructure masquerading as block, split blocks containing two phenomena.
- **Domain emerges late:** code naming may be inconsistent; L0 gets revised after exploration, and the product term wins.
- **Unknown technology:** stop and learn structural implications of unrecognized frameworks.

### Exit to State 1 when

1. State the scope in one sentence
2. Name the candidate root(s) and, for each, the five admission answers
3. Name 2–5 blocks per root and say what each does — as logical responsibilities, not directories
4. Name external systems and how they connect
5. Identify the domain vocabulary and where terms differ between product and code
6. Point to implementation coordinates for each block candidate
7. Actors named by the human (2–5) — collected at the checkpoint below; propose candidates if the product suggests them, but the human decides

If 1–4 but not 5–6: probe more. If you can't do 1–4: re-orient. Items 2 and 7 are ratified by the human, not concluded from probing — bring them to the checkpoint.

### Lead/Bleed Filter (First-Pass Guard)

Before adding any external system candidate to the scratchpad or L1 docs, run the external system checks in [`verification.md`](verification.md) §L1 System Context Verification — this is the gate that prevents implementation details from leaking into L1. Anything that fails is demoted (L3 adapter, internal L2 block, or L5 infrastructure), not added. Run the diagram checks there on any L1 diagram you draft.

### Human Checkpoint

Present the scratchpad with **falsifiable claims** — specific assertions the human can confirm or reject (not summaries). Root proposals need explicit ratification, not a nod: name each candidate, its independent orientation, and what would falsify it. If the human skims and says "looks good," ask about the lowest-confidence item specifically.

---

## State 1 — First Pass

**What you know:** Root candidates, block candidates, tentative domain terms, dependency shape. Scratchpad, not docs.
**Ambiguity:** High but structured — you know the questions.
**Human role:** Validator. Propose, human confirms or corrects. Ask targeted questions, not open-ended.

### Procedure

The orient → scan → probe → adjust cycle runs again, narrower and deeper:

- **Orient from scratchpad.** Open questions become focus targets.
- **Scan within blocks.** Internal structure, deps, naming. Does each block carry one logical responsibility?
- **Probe ambiguities.** Boundary files, inconsistent terms, unclear responsibilities.
- **Adjust with human input.** Targeted questions with proposed answers:

```
- "The codebase says `Tenant`; the product UI says Workspace.
   Which is the domain term? I propose **Workspace**, with
   `Tenant` recorded as an implementation alias."
- "A module imports from both {domain-a} and {domain-b}.
   Is it serving two phenomena, or bridging them?"
- "No clear boundary between X and Y. One block or two?
   I think two, because [product evidence]."
- "Upload, parsing, extraction, and rendering live in four
   directories. Is that four things to the business, or one
   phenomenon called **Document Review**?"
```

- **Calibrate.** Run the level calibration pass below before writing L2 documents.

### Exit to State 2 when

1. L0 draft and `GLOSSARY.md` exist and the human has reviewed both
2. Each root is ratified and recorded in `COMPASS.md`
3. L2 block documents exist with logical roles and implementation coordinates
4. Levels are calibrated — siblings sit at comparable semantic scale
5. No open questions about scope, roots, or block boundaries
6. Remaining ambiguity is within blocks (L3), not between them

---

## Level Calibration

Run after any decomposition, before the decomposition is written into documents. Calibration is about **semantic scale** — the breadth of logical responsibility a concept carries — and never about lines of code, module count, file count, or implementation complexity. A 30-line module and a 30,000-line module can be honest siblings; a whole product area and a single validation rule cannot.

### Procedure

1. List the siblings at one level under one parent.
2. For each, state its logical responsibility in one sentence, without naming any directory, package, or technology.
3. Compare the sentences. Ask: *does a human reasoning about this area treat these as things of the same kind?*
4. Apply the rebalancing move that fits:

| Deformation | Move |
|---|---|
| One concept is far larger in logical scope than its siblings | Promote it — its own level below, or its own root if it passes root admission |
| Several concepts are far finer-grained than their siblings | Group them under one umbrella that names their shared responsibility |
| Siblings are simply unlike each other | Verify whether they belong at the same semantic zoom at all; one of them probably sits a level up or down |

5. Re-run the invariance test on anything you moved, and re-run calibration on the level you changed — a promotion creates a new sibling set.

### Rules

- **Evidence must be semantic.** "This block has 40 files and that one has 4" is not a calibration finding. "This block owns everything a customer can do and that one validates a postcode" is.
- **A synthetic umbrella must earn a name.** If you group fine-grained siblings under a new concept, that concept needs a glossary entry and human ratification like any other semantic entity. An umbrella introduced only to tidy the chart, with no name a human recognizes, is chart furniture — record it as a grouping with no semantic claim, or don't create it.
- **Calibration never moves code.** It changes where a concept sits in the chart and which coordinates point at it.
- **The first decomposition is not assumed correct.** Discovery produces whatever grain the evidence arrived in; calibration is the pass that normalizes it.

---

## State 2 — Documented

**What you know:** L0–L2 docs exist. Domain named, glossary written. Blocks bounded. Externals identified.
**Ambiguity:** Concentrated at L3–L4. Internals and cross-cutting flows.
**Human role:** Consultant. You lead; human provides context for historical decisions, business constraints, deprecated patterns.

### Procedure

- **Orient from documentation.** Read L0–L2 and any linked charts via the registry. If an external system publishes its own chart, read its L0 and L2 — its model may differ from your L1.
- **Scan for L3 detail.** Dependency tooling within each block. Map components, identify stereotypes (service, repository, gateway).
- **Probe cross-cutting flows.** Data paths crossing block boundaries → viewport territory. Where does data shape change? Where are the seams?
- **Adjust from other charts.** Misalignment between your L1 and their L0 is a finding — resolve it, usually as a vocabulary difference to record in the glossary.
- **Probe historical decisions.** Code patterns that don't make structural sense:

```
- "This module imports directly from the database layer,
   bypassing the repository. Intentional?"
- "Two implementations of the same capability exist. Which is
   current, and why do both exist?"
- "This directory appears unused. Dead code?"
```

When a strange pattern turns out to enforce a Compass-owned invariant, record it there and stop — see [`ownership-boundary.md`](ownership-boundary.md). When the reason is specific to this implementation, it belongs to Context Docs, not to the chart.

### Exit to State 3 when

1. L3 documentation exists for all blocks
2. Boundary viewport exists, or L4 was explicitly skipped (small, clear, loosely coupled L3)
3. Cross-cutting flows documented or understood
4. You can predict where a domain concept change requires code changes

---

## State 3 — Deep Knowledge

**What you know:** More than most humans. Full L0–L4 chart.
**Ambiguity:** Local and specific — "how should this system change," not "what is it."
**Human role:** Ratifier. You propose; human approves or vetoes.

### Procedure

Exploration is maintenance, triggered by events:

- **New code.** Run orient → scan → probe on the diff. Does it fit L3? New block? Or is it a semantic change to something ratified?
- **Restructuring.** Files moved, service extracted, framework replaced → remap coordinates, preserve semantics.
- **New external system.** Read its chart (if any). Update L1/L2. May create a state-0 pocket.
- **Disagreement detection.** Compare chart against code proactively, then **classify** every finding — semantic change, implementation remapping, or implementation violation — before proposing anything. Human reviews classified proposals, not raw findings.
- **Architecture proposals.** Propose structural changes (split block, merge components, promote a root, add viewport) with rationale, product and code evidence, and cross-level impact.

**No exit.** Steady state unless a major event drops back to an earlier state — an acquisition, a change in what the product is for, a genuinely new area of the domain. A rewrite is not such an event: it replaces coordinates and leaves the semantic chart standing.

---

## Scratchpad Format

```markdown
# Scratchpad: [system name]

## Scope
[one sentence]

## Candidate Roots

### [Root Name]
- Recognized as: [what humans call this area of work]
- Survives rewrite: [yes/no — why]
- Internal responsibilities: [what is inside]
- Independent orientation: [what "where am I?" answer it gives that no other root gives]
- Ratification: [pending / ratified by {human} on {date}]

## Block Candidates

### [Block Name] (root: [root name])
- Claim: [what this block owns — one logical responsibility]
- Product appearance: [how a human recognizes it]
- Evidence: [product surface, workflow, rules — then file paths]
- Implementation coordinates: [subtree(s), possibly several]
- If wrong: [what would change — how to falsify]

## Phenomena
- [name]: [one human-recognizable thing], currently realized across
  [modules]. Still one thing after a rewrite? [yes/no]

## Domain Terms Found
- [term]: product says [X], code says [Y]. Canonical: [X]. Alias: [Y]
- [term]: appears in [locations], seems to mean [definition]
- CONTEXT-SPECIFIC: [term] means [A] in [context 1] and [B] in
  [context 2]. Record both, do not merge.
- CONFLICT: [term A] and [term B] appear to mean the same thing.
  Used in [locations]. Proposed resolution: [pick one]

## Actors (human-decided — propose candidates, the human confirms or corrects)
- [name]: [person, organisation, or role]. Uses the system to [what they get out of it]

## External Systems
- [name]: passes User-Possession? [y/n]. Passes Control Boundary? [y/n].
  Product evidence: [how the actor encounters it]

## Calibration Notes
- [level]: siblings [A, B, C] — [balanced / A oversized / B+C too fine].
  Proposed move: [promote / group / re-level]

## Open Questions
1. [specific question with proposed answer and evidence]
2. [specific question with proposed answer and evidence]

## Confidence
- Root identity: [low/medium/high] because [reason]
- Block boundaries: [low/medium/high] because [reason]
- Domain terms: [low/medium/high] because [reason]
- External systems: [low/medium/high] because [reason]
```
