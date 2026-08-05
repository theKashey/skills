# Exploration: Full Procedures

## The Loop

Exploration is continuous — not a phase that completes. It runs at different intensities throughout the life of the documentation.

```
       ┌──────────────────────────────────────┐
       │                                      │
       ▼                                      │
 ┌─────────────┐    ┌─────────────┐    ┌──────────────┐    ┌─────────────┐
 │  State 0    │───▶│  State 1    │───▶│  State 2     │───▶│  State 3    │
 │ Clean slate │    │ First pass  │    │ Documented   │    │ Deep know.  │
 └─────────────┘    └─────────────┘    └──────────────┘    └─────────────┘
       ▲                  ▲                  ▲                    │
       │                  │                  │                    │
       └──────────────────┴──────────────────┴────────────────────┘
                      regression (refactor, new block, rewrite)
```

Forward transitions: exploration and documentation.
Backward transitions: new block (state 0), refactor invalidates L3 (state 1), docs drift (state 2).

Human role shifts:
```
State 0:  Human is the teacher     — agent asks, human explains
State 1:  Human is the validator   — agent proposes, human confirms
State 2:  Human is the consultant  — agent leads, human provides context
State 3:  Human is the ratifier    — agent proposes, human approves
```

At every state, be explicit about confidence: "I believe X based on [evidence]. Confidence: medium. Open questions: [list]."

---

## State 0 — Clean Slate

**What you know:** Nothing. Maybe a repo URL and a one-sentence scope.
**Ambiguity:** Maximum.
**Human role:** Primary source. Ask before assuming.

### Orient

Read only shape, not behavior:

1. Project root: `Package.swift`, `package.json`, `Cargo.toml`, `docker-compose.yml`, `Makefile`, README
2. Directory tree: `ls -R` at depth 2–3, ignore `node_modules/`, `build/`, `dist/`, `.git`
3. Entry points: main files, index files, app delegates, route definitions
4. Config and env: `.env` files, `config/`, CI pipeline definitions
5. Dependencies: lockfiles, import maps, dependency graphs

From this determine:
- What kind of thing (single app, monorepo, monolith with modules)?
- What languages and frameworks? How many runtimes?
- Natural seams (separate dirs, separate configs, separate build targets)?
- Deployment shape (one binary, services, static + API, embedded)?

If orientation takes too long, scope is too wide.

### Scan

Structural signals, not code reading.

**Dependency direction.** Use dependency tooling if available (dependency-cruiser, madge, swift-dependency-graph). Fallback:

```bash
grep -rn "^import\|^from\|^require\|^use " src/   # target codebase source root
```

Filter with `--include` globs for the target's languages (e.g. `--include="*.swift"`).

Build adjacency list. Look for:
- Clusters importing each other heavily → likely components
- Files everything imports → likely infrastructure (L5)
- Files importing across seams → leaks or bridges
- Circular dependencies → boundary confusion

**Naming conventions.** Domain words (`orders/`, `billing/`, `identity/`) → boundaries may exist. Technical words (`services/`, `utils/`) → boundaries must be inferred.

**Size distribution.** Large files → god-files. Deep trees → over-abstraction.

**Tests.** Locations and naming reveal groupings and priorities.

### Probe

Read targeted files — not all code.

Targets: high-traffic files, boundary files, entry points, bridge files, god-files.

For each target, answer:
1. What domain concept does this file serve?
2. What does it depend on?
3. What depends on it?
4. Does it respect its directory boundary, or reach across?

Read just enough to answer. Stop when you have them.

### Adjust

Each step may invalidate the previous.

- **Scope adjustment:** re-declare if too wide or narrow.
- **Block candidates shift:** drop infrastructure masquerading as block, split blocks containing two domains.
- **Domain emerges late:** naming may be inconsistent; L0 gets revised after exploration.
- **Unknown technology:** stop and learn structural implications of unrecognized frameworks.

### Exit to State 1 when

1. State the scope in one sentence
2. Name 2–5 isolated blocks and say what each does
3. Name external systems and how they connect
4. Identify where domain concepts live (tentatively)
5. Point to code paths for each block candidate
6. Actors named by the human (2–5) — collected at the checkpoint below; propose candidates if the code suggests them, but the human decides

If 1–3 but not 4–5: probe more. If can't do 1–3: re-orient. Item 6 comes from the human, not from probing — ask for it at the checkpoint.

### Lead/Bleed Filter (First-Pass Guard)

Before adding any external system candidate to the scratchpad or L1 docs, run the external system checks in [`verification.md`](verification.md) §L1 System Context Verification — this is the gate that prevents implementation details from leaking into L1. Anything that fails is demoted (L3 adapter, internal L2 block, or L5 infrastructure), not added. Run the diagram checks there on any L1 diagram you draft.

### Human Checkpoint

Present the scratchpad with **falsifiable claims** — specific assertions the human can confirm or reject (not summaries). If human skims and says "looks good," ask about the lowest-confidence item specifically.

---

## State 1 — First Pass

**What you know:** Block candidates, tentative domain terms, dependency shape. Scratchpad, not docs.
**Ambiguity:** High but structured — you know the questions.
**Human role:** Validator. Propose, human confirms or corrects. Ask targeted questions, not open-ended.

### Procedure

The orient → scan → probe → adjust cycle runs again, narrower and deeper:

- **Orient from scratchpad.** Open questions become focus targets.
- **Scan within blocks.** Internal structure, deps, naming. Is each block cohesive?
- **Probe ambiguities.** Boundary files, inconsistent terms, unclear responsibilities.
- **Adjust with human input.** Targeted questions with proposed answers:

```
- "The codebase uses two terms for the same concept.
   Which is the domain term?"
- "A module imports from both {domain-a} and {domain-b}.
   Intentional or a boundary leak?"
- "No clear boundary between X and Y. One block or two?
   I think two, because [evidence]."
```

### Exit to State 2 when

1. L0 draft exists and human has reviewed it
2. L2 block documents exist with code path roots
3. No open questions about scope or block boundaries
4. Remaining ambiguity is within blocks (L3), not between them

---

## State 2 — Documented

**What you know:** L0–L2 docs exist. Domain named. Blocks bounded. Externals identified.
**Ambiguity:** Concentrated at L3–L4. Internals and cross-cutting flows.
**Human role:** Consultant. You lead; human provides context for historical decisions, business constraints, deprecated patterns.

### Procedure

- **Orient from documentation.** Read L0–L2 and any linked stacks via compass. If external system has its own stack, read its L0 and L2 — may differ from your L1.
- **Scan for L3 detail.** Dependency tooling within each block. Map components, identify stereotypes (service, repository, gateway).
- **Probe cross-cutting flows.** Data paths crossing block boundaries → viewport territory. Where does data shape change? Where are the seams?
- **Adjust from other stacks.** Misalignment between your L1 and their L0 is a finding — resolve it.
- **Probe historical decisions.** Code patterns that don't make structural sense:

```
- "This module imports directly from the database layer,
   bypassing the repository. Intentional?"
- "Two implementations of the same capability exist. Which is current, and why do both exist?"
- "This directory appears unused. Dead code?"
```

### Exit to State 3 when

1. L3 documentation exists for all blocks
2. Boundary viewport exists, or L4 was explicitly skipped (small, clear, loosely coupled L3)
3. Cross-cutting flows documented or understood
4. You can predict where a domain concept change requires code changes

---

## State 3 — Deep Knowledge

**What you know:** More than most humans. Full L0–L4 stack.
**Ambiguity:** Local and specific — "how should this system change," not "what is it."
**Human role:** Ratifier. You propose; human approves or vetoes.

### Procedure

Exploration is maintenance, triggered by events:

- **New code.** Run orient → scan → probe on the diff. Does it fit L3? New block? Boundary violation?
- **New external system.** Read its stack (if any). Update L1/L2. May create state-0 pocket.
- **Drift detection.** Compare docs vs code proactively. Propose corrections. Human reviews proposals, not raw findings.
- **Architecture proposals.** Propose structural changes (split block, merge components, add viewport, promote infra to L3) with rationale, code evidence, and cross-level impact.

**No exit.** Steady state unless major event (rewrite, acquisition) drops back to earlier state.

---

## Scratchpad Format

```markdown
# Scratchpad: [system name]

## Scope
[one sentence]

## Block Candidates

### [Block Name]
- Claim: [what this block does — one sentence]
- Evidence: [file paths, import patterns, naming]
- Root: [directory subtree]
- If wrong: [what would change — how to falsify]

### [Block Name]
...

## Domain Terms Found
- [term]: appears in [locations], seems to mean [definition]
- [term]: appears in [locations], seems to mean [definition]
- CONFLICT: [term A] and [term B] appear to mean the same
  thing. Used in [locations]. Proposed resolution: [pick one]

## Actors (human-decided — propose candidates, the human confirms or corrects)
- [name]: [person, organisation, or role]. Uses the system to [what they get out of it]

## External Systems
- [name]: detected from [evidence]. Protocol: [if known]

## Open Questions
1. [specific question with proposed answer and evidence]
2. [specific question with proposed answer and evidence]

## Confidence
- Block boundaries: [low/medium/high] because [reason]
- Domain terms: [low/medium/high] because [reason]
- External systems: [low/medium/high] because [reason]
```
