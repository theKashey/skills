# Verification Procedures

Formal checks that must pass before advancing L1, L2, L3, or Phase F. Run these as a mandatory gate — not optional polish. This file is the canonical owner of every completion checklist; other files point here rather than restating the items. Levels and phases with no section below carry no gate beyond their exit conditions in [`exploration.md`](exploration.md) and [`growth-and-drift.md`](growth-and-drift.md).

---

## L1 System Context Verification

Run before declaring Phase B complete. Every item must pass.

### Diagram checks (structural)
- [ ] **Single-box rule:** count system nodes inside the system boundary — must be exactly **1**
- [ ] **No internals:** no block names, component names, or module names appear inside the system boundary
- [ ] **No tech labels:** node labels contain no framework names, database names, protocol names, or API endpoint names
- [ ] **No internal edges:** all edges connect the system to external actors/systems — no edges between internals
- [ ] **All edges labelled:** every relationship has a verb label describing what crosses (data, action, event)

### Actor checks
- [ ] 2–5 actors are named, and each was supplied or confirmed by the human — never inferred from code alone
- [ ] Each actor is a person, organisation, or role, not a system

### Document checks
- [ ] `SCOPE.md` and `CONTEXT.md` exist, and `CONTEXT.md` carries a diagram
- [ ] Every L1 external system has an `externals/{name}.md` doc, linked from its `COMPASS.md` row

### External system checks (semantic)
For each node in the external systems table, confirm ALL:
- [ ] Passes User-Possession Test: *"Would the primary actor name this as a top-level tool/service they use?"*
- [ ] Passes Control Boundary Test: *"If this system stopped running, does this thing still exist and belong to the user/operator?"*
- [ ] Not implemented inside the system (no code root in this repo)
- [ ] You are naming the **product/service/store**, not an engine, SDK, API version, or client library
- [ ] Not a framework, library, runtime, or OS component (engines are never L1; the stores they serve may be)
- [ ] Would appear in a product description or user-facing documentation
- [ ] Has a compass entry (or local compass note) — created when it first passes these checks, so admissions and demotions both leave a record

### Cut Loose Ends (after every L1 pass)
1. List every external system referenced anywhere in L1 and L2 docs
2. Apply the external system checklist to each
3. Any that fail → demote immediately (usually an L3 adapter; an internal implementation is L2, a shared helper L5); record the demotion in the compass's L2/L3 tier (name, used-by, which L1 test it fails) so it cannot be silently re-elevated
4. Re-run diagram checks after all demotions

---

## L2 Isolated Blocks Verification

Run before declaring Phase B complete.

- [ ] Every block has: name, responsibility (1 sentence), root path, technology, boundary statement, communicates-with list
- [ ] Every external system referenced in L2 is either listed at L1 (passed eligibility) or explicitly marked as "L3 adapter" in the block doc
- [ ] No L3 component is documented as an L2 block (if it maps to a single file or a single class, it's L3)
- [ ] No circular block dependencies (A → B → A)
- [ ] Every block boundary statement says what it does NOT do (missing boundary = incomplete)
- [ ] Block diagram exists and reflects all communicates-with entries
- [ ] `CONTAINERS.md` exists, carries a wiring diagram, and lists every container folder
- [ ] The host's agent instructions carry the usage hook (chart root + entry pattern), human-approved — a chart no agent is routed to does not exist
- [ ] Every block's component table is present, and each L5 entry in it carries the justification Phase F will rely on
- [ ] Every cross-reference in every chart document written so far is a markdown link, not a plain backtick name (`<!-- TODO: link when created -->` is the only sanctioned placeholder) — re-run this item at each level

---

## L3 Component Verification

Run before declaring Phase C complete.

- [ ] Every component has: stereotype, responsibility (1 sentence), bounded context, I/O, depends-on, used-by, boundary, code paths
- [ ] No component names two L0 bounded contexts (if it does → boundary finding, flag it)
- [ ] Every code path exists on disk (`grep` or `ls` to confirm)
- [ ] Every component is owned by exactly one L2 block (it lives in one block folder); callers from other blocks are consumption, not ownership — 3+ consuming blocks is a shared-library smell: demote to L5 or split, or record why it stays
- [ ] No component's depends-on list reaches 4+ entries from different blocks or external systems without a recorded justification — that is boundary pressure: an integration hub, a missing facade, or a hidden block
- [ ] Mermaid diagram exists and matches depends-on/used-by entries
- [ ] Components are listed in their parent BLOCK.md component table

---

## Phase F (Attribution) Verification

Run before declaring Phase F complete on any block. "Code file" means a source file written in one of the technologies the block's `BLOCK.md` declares. Files whose format carries no comment syntax (JSON, lockfiles) and generated files are out of scope — attribute the folder that holds them, not the file.

- [ ] Every code file in the block is **covered** by an attribution — its own, or the nearest enclosing folder/package attribution — or is excluded as a test outside the primitive, or is recorded as L5 infrastructure in the block's component table
- [ ] Every L5 entry in the component table names what makes it infrastructure (formatter, logger, config loader, generic UI, shared types); a subtree recorded as L5 without that justification is an un-attributed component, not infrastructure
- [ ] No file repeats the address its enclosing folder/package attribution already gives it; a file attribution is warranted only when its address differs — see the gravity laws in [`coordinate-system.md`](coordinate-system.md#gravity)
- [ ] Every L3 component documented in the block is named by at least one attribution in code (docs → code); a block attributed only at L2 leaves its components unwired
- [ ] Every attribution address exists in documentation (`grep -r "compass:" {source root}` → validate each address; the marker is the comment body, so match it without a language-specific comment prefix)
- [ ] No file carries two attributions that share an L1 root (same stack → split the file, attribute to the side that owns the contract, or remove attribution if the file is infrastructure)
- [ ] Every file carrying two attributions from **different** L1 roots honors a pre-existing human-created lens — the second root has a row in the compass's lens tier naming its human owner; agents never create a second stack
- [ ] No stale attributions (address exists in code but not in docs)

---

## Lead/Bleed Detection Checklist

Run at any time to detect level contamination. These are warning signs, not errors — each requires investigation.

| Signal | Likely cause | Action |
|--------|-------------|--------|
| L1 diagram has >1 node inside system boundary | Internal block leaked up | Remove internals, move to L2 |
| L1 external systems table has a vendor API or library | Implementation detail leaked up | Demote to L3 adapter |
| L1 external systems table has an adapter used by only one component | Adapter leaked up | Demote to L3 in that component |
| L2 block doc references a framework as a peer block | L5 infrastructure promoted | Demote to L5, remove block doc |
| L3 component has 4+ external dependencies | Possible hidden block boundary or missing facade | Record justification; investigate split |
| File has 2 attributions sharing one L1 root | Level boundary unclear | Document as boundary file or split |
| File has 2 attributions from different L1 roots with no human-created lens | Agent invented a second stack | Remove the invented stack |
| L2 block boundary statement is missing or >2 sentences | Boundary not understood | Clarify before proceeding |
| L3 component responsibility requires "and" | Component doing too much | Split candidate |

---

## Anti-Drift Spot Check

Run periodically (after any significant code change, or at state 3 maintenance cadence).

1. Pick 5 random source files per block
2. For each: is it covered by an attribution (its own, or the nearest enclosing one)? Does that address exist in docs? Can you navigate L3 → L2 → L1 in ≤2 hops?
3. Pick 3 random L3 COMPONENT.md files — do their code paths still exist on disk?
4. Pick 1 BLOCK.md — does its communicates-with list match actual imports?
5. Check VIEWPORTS.md — at most 3–4 active viewports, each still answering its named question with a sequence diagram that describes reality
6. Check document sizes against the level budgets in `SKILL.md` §Quick Reference: Levels — oversize means scope creep within the level; split the content down a level, don't raise the budget. L0 and L4 budgets are per unit (context, viewport): an oversize unit is doing too much — split or retire the unit, since there is no level below to push it into.

**If any check fails:** classify the finding (stale doc / missing doc / boundary violation / orphaned attribution) and respond per the priority order in `growth-and-drift.md`.
