# Consume a Compass chart

Use an existing chart to orient non-local work without changing the chart or
its installed integration. `{chart-root}` is the directory the host project
declares in its agent instructions (see `SKILL.md` §Shared contract).

The chart describes the logical system. The code is one realization of it. Read a mismatch as information about the mapping, not as a fault in either side, until you have classified it.

---

## Navigation Patterns

### Starting a new task

Follow the zoom chain when the work is not local (`SKILL.md` §Shared contract)
— and never skip a level:

1. Open `{chart-root}/README.md` — confirm scope and see which roots exist
2. Open `{chart-root}/COMPASS.md` — see which roots exist and which externals were demoted; where more than one root could own the work, pick the orientation that matches how you're thinking about the task
3. Open `{chart-root}/{root}/README.md` — orient: who uses this, what external systems exist
4. Open `{root}/CONTAINERS.md` — find which block(s) own the area of work; read the wiring diagram
5. Open `{root}/{block}/README.md` — read responsibility, logical role, boundary, communicates-with, component list
6. Open the specific `{component}/README.md` files that will be touched
7. Check `VIEWPORTS.md` — does any viewport cross the area of change?

Beside the chain, not in it: if the task builds a new capability and `{chart-root}/ABSTRACTIONS.md` exists, scan its `##` headings for a concept the new code would instantiate. On a match, read [consume-named-abstractions.md](consume-named-abstractions.md) before writing — it confirms the claim is valid before anything is interpreted.

**Signal that you're ready:** you can restate the task in semantic terms, name every component you'll touch and every boundary you'll cross, name any existing component or named abstraction the new code would otherwise duplicate, and classify any chart/code disagreement. Keep reproduction details and the implementation plan with the project task, not in the chart. Every *report* in this guide lands there too — in the task's own record, never only in the conversation (`SKILL.md` §Choose exactly one flow).

---

### Understanding what something means

1. Open `{root}/GLOSSARY.md` — find the term, its meaning in the relevant bounded context, how it appears in the product, and which code names alias it
2. Open `{root}/DOMAIN.md` — find the context, its concepts, invariants, and relationships to other contexts

If the code uses a word the glossary lists as an alias, the glossary term is the one to use in any chart document, commit message, or discussion of intent.

---

### "Why is this code like this?"

1. Find the coordinate covering the file — its own `compass:` comment, or the nearest enclosing folder/package one
2. Follow the address into the chart. Is the strange code enforcing a documented invariant, boundary, or responsibility? If yes, you have the reason — stop
3. If the chart explains the *what* but the mechanism is still surprising, the remaining reason is implementation-specific: it lives with the code, and Context Docs owns where it goes

Checking the coordinate first is what stops the same domain intent being reverse-engineered over and over.

If an existing `compass-abstraction: <slug>` marker or definition affects the
task, or the beside-the-chain scan above matched, read
[consume-named-abstractions.md](consume-named-abstractions.md). This is the
only named-abstraction procedure in the Consume flow.

---

### Estimating a task

The chart supplies an ordering, not a duration. It knows how many components and boundaries a change touches; it knows nothing about this team, language, or codebase, so it cannot turn that into hours or days — any calendar figure printed here would be invented. Count, rank, and let the project's own history supply the scale:

| Scope | Relative cost |
|-------|---------------|
| 1 component, 0 boundary crossings | Baseline |
| 1–2 components, 1 boundary crossing | Above baseline — one contract to agree |
| 3+ components, 2+ boundary crossings | Well above — coordinated change |
| New block or new external system | Different in kind — needs a spec and a human decision |

**Boundary crossings are the multiplier.** A change that touches 5 files in one component is simpler than a change that touches 2 files in 2 different blocks — because boundary crossings require protocol changes, contract updates, and coordinated testing.

How to count:
1. Open `{root}/CONTAINERS.md` — find the blocks your change touches
2. List every component document your change touches
3. Count how many distinct block folders those components live in
4. Each additional block = one boundary crossing
5. Check `VIEWPORTS.md` — if your change is on the critical path of a viewport, add complexity for the end-to-end impact

Count logical boundaries, not directories. A phenomenon spread across six packages is one boundary crossing if the change stays inside it.

---

### Debugging a cross-block flow

1. Open `{root}/VIEWPORTS.md`
2. Find the viewport whose diagram covers the misbehaving flow
3. Trace the sequence — identify which step produces wrong output
4. Open that step's `{component}/README.md` — check boundary and implementation coordinates
5. Navigate to the coordinate listed, add logging/breakpoint at the boundary

**If no viewport covers the flow:** report the gap and continue from component
documents and coordinates. Creating a viewport is a separate Create task.

---

### Understanding what a component does

Open its `{component}/README.md`. Read in this order:
1. **Stereotype** (`«service»`, `«gateway»`, `«repository»`, etc.) — tells you the pattern
2. **Responsibility** (one sentence) — tells you the job
3. **Boundary** — tells you what it deliberately does NOT do
4. **Mermaid diagram** — shows who calls it and what it calls
5. **Implementation coordinates** — where to find it today

If the coordinates are wrong, classify and report an implementation remapping.
If the responsibility or boundary is wrong, classify and report a semantic
finding. Do not edit the chart in the Consume flow.

---

### Reviewing a PR / code review

1. For each changed file, find its owning block via the block document's implementation coordinates, then its component
2. Check: does the change stay within the component's declared boundary?
3. Check: does the change add new dependencies not listed in depends-on?
4. Check: does the change alter a rule, invariant, or capability the chart records?
5. Classify anything that disagrees with the chart before proposing a fix:
   - files moved, service extracted, framework swapped → **implementation remapping**; report that coordinates need a separate Create task
   - a rule or responsibility now differs → **semantic change**; needs ratification
   - the code crosses a ratified boundary → **implementation violation**; one side is wrong, decide which

**Boundary violation patterns:**
- A component calls a persistence store directly instead of going through the block's declared interface
- A component reaches into another block's internals instead of the documented communication mechanism
- A component serves two bounded contexts (should be split)

Point 4 is the one reviewers skip. A pure rule change moves no file and breaks no import; only comparing behaviour against the chart catches it.

---

### Planning a refactor

1. Read all `{block}/README.md` files in the affected area
2. Check `VIEWPORTS.md` — which viewports cross the refactor boundary?
3. List the communicates-with entries that will change
4. For each: who is the consumer? (consumer docs the relationship — find those files)
5. Decide up front whether this refactor changes *meaning* or only *structure*

A structure-only refactor implies implementation-coordinate maintenance and no
change above L2. Record that maintenance as a separate Create task. If the plan
would alter L0, L1, or a block's logical role, report a semantic change that
requires ratification.

**Refactor readiness check:** if you can't describe the before and after state of every affected block document, you're not ready to code.

---

### Detecting that a component is doing too much

Read the component's responsibility, depends-on, used-by, and diagram, then the
block's communicates-with entries, boundary statement, and logical role. Treat
any apparent overreach as a lead to report, not permission to redraw the chart.
Use the applicable thresholds in
[structural-signals.md](structural-signals.md); it is the shared read-only owner
for level-contamination and overreach signals.

The one sign with no numeric threshold, and the most decisive: **a logical role that can only be stated by naming a directory.** That block has no semantic identity — it is a folder with a document.

---

## Architectural Pull

Architectural pull is the gradient from documented reality toward a healthier arrangement. It appears only after evidence establishes a direction; a chart observation alone creates a lead, not pull. When reading the chart before a task, the evidence may point toward:

- **Refactoring** — a component boundary is wrong, making the task harder than it should be
- **Extraction** — a new component is trying to emerge from an existing one
- **Consolidation** — two components are doing overlapping work
- **Decluttering** — a file sits where its coordinate does not, so the folder cannot carry one coordinate for its subtree
- **Chart work** — code exists that has no place in the chart

Name the Compass level and parent boundary under observation before judging cohesion or coupling. The same relationship may be internal at one level and cross the highest-distance boundary at the next. Record the current arrangement first, then the evidence-backed direction; do not blend observations from different levels into one finding.

Close each lead as **legitimate** (no move), **declutter** (with the useful move), or **debt** (with the independent evidence and healthier direction). When the team chooses to act on declutter or debt, capture it in the project's tracker. Compass makes the opportunity visible; it neither schedules nor enforces the work.

**Decluttering is the cheapest of these**, and coordinate density is what surfaces it: a folder whose files carry three addresses often has one file filed in the wrong place, and moving it lets the coordinate bubble up on its own. Take that direction of travel whenever the code is better for it.

**Where the pull stops:** at the demand that the repository mirror the chart. A phenomenon spanning six packages, a module participating in two ratified roots, a bridge file legitimately carrying two coordinates — each is a lead worth a look, none is a defect on its own, and none obliges a move. Open the investigation on the density observation; close it as debt only on independent cohesion or coupling evidence at the selected level, and record that evidence rather than the coordinate count as the reason.

---

## What the Chart Does NOT Answer

- **How to implement** — the chart describes what the system is and how its parts relate, not how to build them
- **Why this particular mechanism** — implementation-local rationale lives with the code
- **Performance characteristics** — measure with the project's evaluation tooling, don't document here
- **Test strategy** — the chart shows boundaries, which inform test boundaries, but does not prescribe tests
- **Deployment topology** — document only if a viewport question requires it; topology never defines roots or blocks
- **Business requirements** — live in the project's task tracker and decision log
- **How the repository is arranged** — that is what the repository is for. The chart records where logic *participates*, not how files happen to be filed today
