# Growth Pattern and Anti-Drift

## Growth Phases

Architecture documentation grows top → down. Each phase builds on the previous.

```
Phase 0   — Scope + compass registration (human decision)
Phase 0.5 — Explore (state 0 loop) → scratchpad
Phase A   — Establish domain (L0)
Phase B   — Frame system (L1 + L2)
Phase C   — Map components (L3)
Phase D   — Define viewports (L4)
Phase E   — Maintain
Phase F   — Seal connections
```

### Phase 0 — Scope + Compass

Human declares scope. If organization has a compass, register the system. If not, create a local compass entry.

### Phase 0.5 — Explore

Run the state 0 exploration loop (see [`exploration.md`](exploration.md)). End with a reviewed scratchpad.

### Phase A — Establish Domain (L0)

Human-checkpointed, agent-written. Agent scans the codebase for domain term candidates, entity names, event patterns, and proposes bounded context candidates with evidence. Human draws the actual boundaries; the agent writes the document.

L0 is prose only. No technology references. This is the hardest document to write and the most stable once written.

### Phase B — Frame System (L1 + L2)

Define actors and external systems (L1). Define isolated blocks (L2). This is where technology enters — each block has a tech stack, a root directory, and a boundary statement.

Agent proposes from project structure. Human confirms or restructures.

Phase B is done only when the L1 and L2 checklists in [`verification.md`](verification.md) pass, including the Cut Loose Ends protocol after every L1 pass. When unsure about an external system, leave it at L3 and document the uncertainty — do NOT elevate by default.

**Close Phase B by installing the usage hook.** A chart that agents are not routed to does not exist — the skill's own founding failure mode. Propose a short block for the host's agent instructions (`AGENTS.md`, `CLAUDE.md`, or equivalent — the same file that declares the chart root) and let the human approve it before writing:

```markdown
## Architecture chart
An architecture chart lives in {chart-root}/ — read it before code work.
- Starting a task: SCOPE.md → {system}/CONTEXT.md → CONTAINERS.md →
  {container}/BLOCK.md → {component}/COMPONENT.md
- Debugging a cross-block flow: {system}/VIEWPORTS.md
- Code carries `compass: <address>` markers; addresses resolve in the chart
- If code and chart disagree — the map is not the territory, but this map
  carries ratified decisions — flag it; either side may be the wrong one
- The chart answers what exists and how it connects — not how to implement
```

Keep the hook this size: it routes, it does not restate the chart. Phase E maintains it — if the chart root moves or a system is added, the hook is part of the diff.

### Phase C — Map Components (L3)

Agent-driven. Use dependency tooling within each block to discover components and their relationships. Map each component to its L0 bounded context.

Human validates and identifies debt, leaks, and historical anomalies.

### Phase D — Define Viewports (L4)

Create only as needed. Start with boundary viewports (if blocks communicate). Add lifecycle viewports when debugging requires tracing full data paths.

3–4 active viewports maximum.

### Phase E — Maintain

Steady state. Re-run exploration on diffs (new code, new integrations, refactors). Keep documentation aligned with code changes.

Triggered by events, not by schedule:
- New code merged → does it fit existing L3? New component? Boundary violation?
- New external system → update L1/L2, may create state-0 pocket for that block
- Refactor → may invalidate L3, regression to state 1 for affected block

### Phase F — Seal Connections

Add `compass: <address>` attribution comments — in the host language's comment syntax — after architecture stabilizes. Not before: premature attribution locks in wrong boundaries.

Attribution is the final step because it creates a hard coupling between code and documentation. Change the architecture → change the code comments. Only seal when the cost of maintaining comments is lower than the value of navigability.

---

## Methodology Anti-Drift (Docs vs Method)

The method itself can drift — the team applies the method but stops following its rules. This section detects and corrects methodology drift.

### The Test

Pick any random code file in the system. Take the attribution covering it — its own, or the nearest enclosing folder/package one — and walk up to L3, to L2, to L1. Can you find the file in the documentation within two hops?

- Yes → method is working.
- No attribution covers it → Phase F incomplete (or too early).
- Attribution exists but L3 is missing → L3 documentation drifted.
- L3 exists but can't reach L2 → naming inconsistency.

### Validation Procedure

The runnable procedure is [`verification.md`](verification.md) §Anti-Drift Spot Check — verification.md owns the checklist. This section owns only the two-hop test above and the drift signs below.

### Signs of Methodology Drift

- L3 components exist in code but not in documentation.
- L2 block documents exist without L3 detail underneath.
- Viewports exist but aren't grounded in L3 components.
- Naming diverges across levels (L2 calls it "Capture", L3 calls it "Ingest").
- Consumer relationships documented in the provider instead of the consumer.
- Infrastructure documented as architecture (L5 masquerading as L3).

Level contamination (internals leaking up to L1, frameworks promoted to peer blocks) has its own signal table: [`verification.md`](verification.md) §Lead/Bleed Detection Checklist.

---

## Implementation Anti-Drift (Docs vs Code)

The map is not the territory: the chart describes intent, code implements reality, and they drift apart — expect it, detect it, classify it. But do not let the prior pick the repair: this map carries ratified verdicts the territory cannot show, so when the two disagree the classification below decides which side is wrong — a stale chart is corrected to match code, a boundary violation is code that must be corrected to match the chart (or the human re-ratifies the boundary).

### What Drifts

- **Code paths move.** File renamed, directory restructured. L3 doc points to a path that no longer exists.
- **Names change.** Class renamed. L3 doc uses old name.
- **New components appear.** Code added without L3 documentation.
- **Dead components remain documented.** Code deleted but L3 doc persists.
- **Boundaries violated.** Component reaches into another block's internals. L2 boundary statement now false.
- **External systems change.** Upstream API version changes. L1 description stale.

### Detection

**Proactive (agent-driven):**
- Compare L3 code paths against actual filesystem.
- Compare L2 communicates-with against the actual import graph.
- Compare L1 external systems against actual network calls, API clients, config references.
- `grep -r "compass:"` and validate every address exists in docs.

**Reactive (event-driven):**
- Large PR merged → check affected L3 docs.
- New dependency added → check L1/L2.
- Refactor PR → check all affected levels.

### Classification

| Finding | Category | Response |
|---------|----------|----------|
| Doc describes code that no longer exists | Stale doc | Update or remove doc |
| Code exists without documentation | Missing doc | Add L3 doc |
| Code violates documented boundary | Boundary violation | Refactor code OR update docs (if intent changed) |
| New external system in code | Missing L1 entry | Add to L1 and compass |
| Viewport describes obsolete flow | Stale viewport | Update or remove |
| Attribution points to removed node | Orphaned attribution | Remove or update comment |

### Response Priority

1. Boundary violations (architecture is wrong or code is wrong — must decide).
2. Missing docs for new components (growing blind spots).
3. Stale docs (misleading but less dangerous than missing).
4. Orphaned attributions (noise but low risk).
