# Growth Pattern, Disagreement, and Drift

## Growth Phases

The chart grows top → down. Each phase builds on the previous.

```
Phase 0   — Scope + chart root + compass registration (human decision)
Phase 0.5 — Explore (state 0 loop) → scratchpad
Phase A   — Establish domain (L0 + GLOSSARY.md)
Phase B   — Frame system (L1 + L2)
Phase C   — Map components (L3)
Phase D   — Define viewports (L4)
Phase E   — Maintain
Phase F   — Seal coordinates
```

### Phase 0 — Scope + Compass

The human declares scope and the chart root. The root is declared by writing it into the host's agent instructions (`AGENTS.md`, `CLAUDE.md`, or equivalent) — the file `SKILL.md` reads it from and the file Phase B's usage hook joins; a root that lives only in the conversation is not declared, and `create.md` §Chart Root then asks rather than inventing one. If the organization already keeps a compass, register there; otherwise create a local `COMPASS.md` with its tiers empty.

**Roots are not ratified here.** Root admission needs product and domain evidence, and Root Verification explicitly refuses file-tree evidence — which is all Phase 0 has. Candidate roots are named on the scratchpad during Phase 0.5, brought to the state-0 human checkpoint with their five admission answers, and ratified there. Only then does a root get its `COMPASS.md` row and its `{root}/` directory, whose `README.md` is written in Phase B.

**The ratification is a precondition, not content.** The row records what the root is and the orientation it gives; who approved it and when belong to the commit that added the row. A chart carrying its own approval trail is describing its production rather than the system.

No root exists until a human ratifies it. A package, service, or second language is not a root proposal.

### Phase 0.5 — Explore

Run the state 0 exploration loop (see [`exploration.md`](exploration.md)). End with a reviewed scratchpad. The loop triangulates product/domain reality, the chart, and the implementation — it does not read the model off the file tree.

### Phase A — Establish Domain (L0 + Glossary)

Human-checkpointed, agent-written. The agent collects product and domain vocabulary, proposes bounded contexts with product evidence, and presents them as falsifiable claims. The human draws the actual boundaries; the agent writes `DOMAIN.md` and `GLOSSARY.md` together.

L0 is prose only — no technology, no code paths, no coordinates. Every architecturally used term lands in the glossary; where product and code disagree, a code form identifier-split search cannot reach is a candidate lexicon row in the task record; Phase A completes with the candidates recorded, and a separate admission task turns them into rows (`lexicon.md` §Admission). This is the hardest pair of documents to write and the most stable once written.

### Phase B — Frame System (L1 + L2)

Define actors and external systems (L1). Define isolated blocks (L2). This is where technology enters — each block records its technology and its implementation coordinates alongside its logical role.

Agent proposes from product evidence and structural evidence together. Human confirms or restructures.

Run level calibration ([`exploration.md`](exploration.md#level-calibration)) before writing L2 documents: the first decomposition is not assumed correctly scaled.

Phase B is done only when the root, L1, and L2 checklists in [`verification.md`](verification.md) pass, including the Cut Loose Ends protocol after every L1 pass. When unsure about an external system, leave it at L3 and document the uncertainty — do NOT elevate by default.

**Close Phase B by installing the chart check and the usage hook.** A chart
that agents are not routed to does not exist, and a chart no build checks is
verified by whoever last read a checklist. Install the chart check from
[`verification.md` §First](verification.md#first-the-mechanizable-checks-belong-to-the-hosts-test-suite)
into the host's test suite, ask-first; the `MINIMUM` rule and the recorded
alternative to installing are the L2 row that checks it (`verification.md`
§L2). Copy the four-line block from
[agent-hook.md](agent-hook.md) into the host's agent instructions (`AGENTS.md`,
`CLAUDE.md`, or equivalent—the file that declares the chart root). Substitute
the installed Compass skill and declared chart-root paths, then let the human
approve the block before writing it.

**The non-local trigger is load-bearing, not a hedge** (`create.md` §Core
Principle, Applicability). A hook claiming the chart is worth reading before
every edit is disbelieved after the third one-line fix, and a reader who learns
to skip it skips it for the change that needed it.

Keep the hook compact: it starts search and consultation, while the Consume
router owns task-specific paths. Equivalent host wording is fine when it keeps
the template's trigger, search command, consultation boundary, and local-work
exclusion. Phase E maintains the installed copy when a path or the canonical
template changes.

### Phase C — Map Components (L3)

Agent-driven. Use dependency tooling within each block as implementation evidence, then establish the components' semantic relationships. Map each component to its L0 bounded context and to its current implementation coordinates; keep recoverable import/call incidence with tooling.

Human validates and identifies debt, leaks, and historical anomalies. Record findings and dispositions in the task record; the chart owns the boundaries and mappings, not a defect register.

Phase C is the first point at which the chart has enough argument to be wrong in ways no structural gate sees. When the L3 checklist passes, run the Blind Semantic Read in [`verification.md`](verification.md#blind-semantic-read) before calling the level done, and again whenever a later phase touches more than one document.

### Phase D — Define Viewports (L4)

Create only as needed. Start with boundary viewports (if blocks communicate). Add lifecycle viewports when debugging requires tracing full data paths.

3–4 active viewports maximum.

### Phase E — Maintain

Steady state. Re-run exploration on diffs (new code, new integrations, restructuring). Classify every chart/code disagreement before repairing anything.

Triggered by events, not by schedule:
- New code merged → does it fit existing L3? New component? Or a semantic change to something ratified?
- Restructuring (move, split, extract, merge, framework or language swap) → remap coordinates; semantics stand
- New external system → update L1/L2, may create a state-0 pocket for that block
- Product rule change → semantic change; may need ratification even when no file moved
- A Consume task recorded a classified finding in its PR, issue, or task record
  (`SKILL.md` §Choose exactly one flow) → that record is this Create task's
  entry; respond per the class, never inside the Consume task that found it
- The installed chart check failed → classify each failure before repairing it
  (§Classifying Disagreement); a marker at an absent address is handled by
  `verification.md` §Staleness, not deleted to turn the build green. A failure
  prefixed `template:` is not a chart/code disagreement: it takes the
  document-format trigger below
- Compass release changed the chart check — seen when Create compares the
  installed check with the fence (`verification.md` §First) → update the
  installed check ask-first and run it; its `template:` failures take the next
  trigger
- Compass release changed a document format in
  [`blocks-and-levels.md`](blocks-and-levels.md) — seen when a level checklist
  or the updated chart check reports a `template:` failure on a document
  written to the older form → rewrite that document to the current template,
  ask-first; its semantics stand
- Compass release changed [the usage-hook template](agent-hook.md) — seen when
  Create compares it with the hook beside the chart root → update the installed
  block ask-first, then re-run the L2 hook rows (`verification.md` §L2)

### Phase F — Seal Coordinates

Add `compass: <address>` coordinates — in the host language's comment syntax — after semantic boundaries stabilize. Not before: premature sealing multiplies the cost of correcting a boundary that was wrong.

Sealing creates a coupling between code and chart in one direction only: change the *semantics* and the sealed comments change with them. Moving code changes which files carry which coordinate, which is ordinary maintenance. Only seal when the cost of maintaining the comments is lower than the value of navigability.

---

## Classifying Disagreement

When the chart and the code disagree, do not infer:

```text
code != Compass
therefore Compass is stale
```

Source code is authoritative evidence of what currently executes. It is not automatically authoritative evidence of what the system means or is intended to do. Classify first; the classification decides what changes.

### Semantic change

The logical system changed: a business rule, invariant, capability, responsibility, domain meaning, actor interaction, or meaningful effect is different from what the chart records.

**Response:** Compass may need to change. High-level semantic change (root, L0, L1, L2 identity) requires the existing human ratification process. Low-level semantic change is proposed with evidence.

Note that this class is invisible to any structural comparison. One eligibility rule changing inside an otherwise untouched module produces no moved file, no renamed directory, no altered dependency edge — and is exactly the case the chart exists to catch.

### Implementation remapping

The same logical system is now implemented differently: files moved, package split, service extracted, services merged, framework replaced, repository reorganized, database technology changed, implementation language changed.

**Response:** Preserve semantic Compass. Update implementation coordinates — the block's and component's `## Implementation coordinates` sections and the `compass:` markers in code. A block does not split because it was deployed as three services; a phenomenon does not fragment because its modules were rearranged.

### Implementation violation

The executable implementation contradicts ratified Compass semantics.

**Response:** Investigate which side is wrong:

1. the implementation is wrong — correct the code; or
2. an intentional semantic change happened and Compass was never ratified or updated — take it through ratification.

Do not silently pick one. An unratified semantic change repaired as if it were a bug erases a decision somebody made; a genuine violation repaired by editing the chart erases the boundary the chart existed to hold.

### Classification table

| Finding | Class | Response |
|---------|-------|----------|
| Code path in a document no longer exists on disk | Implementation remapping | Update coordinates |
| Package moved, service extracted, framework replaced | Implementation remapping | Update coordinates; semantics stand |
| Code exists with no place in the chart | Semantic change or missing coordinate | Decide which: a new logical responsibility is semantic; a new module inside an existing one is a coordinate |
| A business rule or invariant differs from the chart | Semantic change | Ratify the change, or correct the code — investigate |
| Component reaches past a ratified boundary | Implementation violation | Refactor code OR re-ratify the boundary |
| New external system appears in code | Semantic change at L1 | Run both L1 tests; add to L1 and the registry, or demote |
| Viewport describes a flow that no longer happens | Semantic change or remapping | Classify, then update or retire |
| A documented block or component has no implementation anywhere | Semantic change (capability withdrawn) or remapping (moved) | Re-read the product surface: if the capability is gone, retire the entity through ratification and remove its coordinates; if it only moved, remap |
| Coordinate points to a place absent from the chart | Unratified semantics or a bad marker | Investigate before deleting the comment |
| Glossary term absent from the product's own language | Semantic change | Re-check the vocabulary with a human |

### Response priority

1. Implementation violations (one side is wrong — must decide).
2. Unclassified disagreements (a finding nobody has classified is the one that gets repaired the wrong way).
3. Missing chart entries for new logical responsibilities (growing blind spots).
4. Stale coordinates (noise, low risk, mechanical to fix).

### Detection

**Proactive (agent-driven):**
- Compare recorded implementation coordinates against the actual filesystem.
- Use imports, events, and runtime interactions as evidence of how block "communicates with" relationships are realized; do not equate semantic edges with imports.
- Compare L1 external systems against actual network calls, API clients, config references — then re-run both L1 tests on anything new; a dependency is not an admission.
- `grep -r "compass:"` and validate every address exists in the chart.
- Re-read the product surface for the rules the chart claims. Structural comparison cannot find a semantic change.

**Reactive (event-driven):**
- Large PR merged → check affected components and any rule the chart records for them.
- New dependency added → check L1/L2.
- Restructuring PR → expect remapping, and verify nothing semantic hid inside it.

---

## The Two-Hop Test

The method itself can drift — the team applies it but stops following its rules. One check finds most of it:

Pick any random code file. Take the coordinate covering it — its own, or the nearest enclosing folder/package one — and walk up to the component, to the block, to the root. Can you find the file in the chart within two hops?

- Yes → the method is working.
- No coordinate covers it → Phase F incomplete, or too early.
- Coordinate exists but the component document is missing → the chart lost a place.
- Component exists but you can't reach its block → naming inconsistency.

That is all this section owns. The runnable version is [`verification.md`](verification.md) §Spot Check, and the level-contamination signals are its §Lead/Bleed Detection Checklist.
