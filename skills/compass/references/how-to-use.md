# How to Use the Chart

The chart answers specific questions faster than reading code. This guide maps common developer tasks to specific navigation patterns. `{chart-root}` is the directory the host project declares in its agent instructions (see `SKILL.md` §Chart Root).

---

## Navigation Patterns

### Starting a new task

Follow the zoom chain — never skip a level:

1. Open `{chart-root}/SCOPE.md` — confirm what is in and out of scope
2. Open `{chart-root}/{system}/CONTEXT.md` — orient: who uses the system, what external systems exist
3. Open `{chart-root}/{system}/CONTAINERS.md` — find which container(s) own the area of work; read the wiring diagram
4. Open `{chart-root}/{system}/{container}/BLOCK.md` — read responsibility, boundary, communicates-with, component list
5. Open the specific `{component}/COMPONENT.md` files that will be touched
6. Check `VIEWPORTS.md` — does any viewport cross the area of change?

**Signal that you're ready:** you can name every component you'll touch and every boundary you'll cross before writing a line.

---

### Estimating a task

Use the component + boundary crossing count as a rough proxy for complexity:

| Scope | Typical effort |
|-------|---------------|
| 1 component, 0 boundary crossings | Hours |
| 1–2 components, 1 boundary crossing | 1–2 days |
| 3+ components, 2+ boundary crossings | Days to week |
| New container or new external system | Week+ (spec required) |

**Boundary crossings are the multiplier.** A change that touches 5 files in one component is simpler than a change that touches 2 files in 2 different containers — because boundary crossings require protocol changes, contract updates, and coordinated testing.

How to count:
1. Open `{system}/CONTAINERS.md` — find the containers your change touches
2. List every `COMPONENT.md` your change touches
3. Count how many distinct container folders those components live in
4. Each additional container = one boundary crossing
5. Check `VIEWPORTS.md` — if your change is on the critical path of a viewport, add complexity for the end-to-end impact

---

### Debugging a cross-block flow

1. Open `{system}/VIEWPORTS.md`
2. Find the viewport whose sequence diagram covers the misbehaving flow
3. Trace the sequence — identify which step produces wrong output
4. Open that step's `{component}/COMPONENT.md` — check boundary and code paths
5. Navigate to the code path listed, add logging/breakpoint at the boundary

**If no viewport covers the flow:** the flow is undocumented. Add a viewport after debugging — that's how architecture docs grow from real pain.

---

### Understanding what a component does

Open its `{component}/COMPONENT.md`. Read in this order:
1. **Stereotype** (`«service»`, `«gateway»`, `«repository»`, etc.) — tells you the pattern
2. **Responsibility** (one sentence) — tells you the job
3. **Boundary** — tells you what it deliberately does NOT do
4. **Mermaid diagram** — shows who calls it and what it calls
5. **Code paths** — where to find it

If any of these are missing or wrong, update the doc — that's drift.

---

### Reviewing a PR / code review

1. For each changed file, find its owning block via `BLOCK.md` Root, then its component via the component table and `COMPONENT.md` code paths
2. Check: does the change stay within the component's declared boundary?
3. Check: does the change add new dependencies not listed in `depends-on`?
4. Check: does the change cross into another block's Root subtree?
5. If any answer is "yes" → flag as boundary question in review

**Boundary violation patterns:**
- A component calls a persistence store directly instead of going through the block's declared interface
- A component reaches into another block's internals instead of the documented communication mechanism
- A component serves two bounded contexts (should be split)

---

### Planning a refactor

1. Read all `{container}/BLOCK.md` files in the affected area
2. Check `VIEWPORTS.md` — which viewports cross the refactor boundary?
3. List the `communicates-with` entries that will change
4. For each: who is the consumer? (consumer docs the relationship — find those files)
5. The refactor plan = updating all affected `communicates-with` + `depends-on` entries

**Refactor readiness check:** if you can't describe the before and after state of every affected `BLOCK.md`, you're not ready to code.

---

### Adding a new component

1. Open `{system}/CONTAINERS.md` — confirm which container the component belongs to
2. Open that container's `{container}/BLOCK.md` — confirm it fits the boundary statement
3. Create `{chart-root}/{system}/{container}/{component-name}/COMPONENT.md`
4. Fill: stereotype, responsibility (1 sentence), bounded context, I/O, depends-on, used-by, boundary, code paths
5. Add Mermaid diagram
6. Add entry to parent `BLOCK.md` component table
7. Update the `BLOCK.md` diagram to show the new component
8. If it crosses a container boundary: update the `CONTAINERS.md` container table and diagram + check if a viewport needs updating

---

### Adding a new container

Requires human decision (L2 boundary change). Before creating:
1. Can it be a component within an existing container? If yes, do that instead (YAGNI)
2. Does it have a clear boundary statement (what it does NOT do)?
3. Does it have a clear owner in the team?

If yes to all:
1. Create `{container}/BLOCK.md`
2. Add to `CONTAINERS.md` — container table and diagram
3. Attribute the container at its coarsest accurate level — normally one `compass: {system}.{container}` on its domain controller, not one per file (Phase F)
4. Update `CONTEXT.md` only if it requires a new L1 external system

---

### Detecting that a component is doing too much

Signs visible in `COMPONENT.md`:
- Responsibility sentence requires "and" → split candidate
- `depends-on` list has 4+ entries from different blocks → boundary pressure
- `used-by` list has callers from 3+ different blocks → shared-library smell (demote to L5 or split, or record why it stays)
- Mermaid diagram has 6+ arrows → too many relationships, decompose

Signs visible in `BLOCK.md`:
- `communicates-with` list longer than 5 entries → block is doing too much
- Block boundary statement is longer than 2 sentences → boundary is unclear

---

## Architectural Pull

"Pull" is the pressure that architecture creates toward certain kinds of work — distinct from attribution gravity, which is about where a marker sits. When reading C4 docs before a task, you may feel pull toward:

- **Refactoring** — a component boundary is wrong, making the task harder than it should be
- **Extraction** — a new component is trying to emerge from an existing one
- **Consolidation** — two components are doing overlapping work
- **Documentation** — a component exists in code but not in docs (drift)

Capture these signals as tasks in the project's tracker. They are architectural debt made visible — not urgent, but not invisible either.

---

## What the Chart Does NOT Answer

- **How to implement** — the chart describes what exists and how it connects, not how to build new things
- **Performance characteristics** — measure with the project's evaluation tooling, don't document here
- **Test strategy** — the chart shows boundaries, which inform test boundaries, but does not prescribe tests
- **Deployment topology** — document only if a viewport question requires it
- **Business requirements** — live in the project's task tracker and decision log, not in C4 docs
