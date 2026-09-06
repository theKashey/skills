# Assess a change through a Compass chart

Use the applicable section after the core Consume search and zoom path identify
the affected roots, blocks, components, and boundaries.

## Estimate relative scope

The chart supplies ordering, not duration. Let project history provide calendar
scale after counting semantic scope:

| Scope | Relative cost |
| --- | --- |
| 1 component, 0 boundary crossings | Baseline |
| 1–2 components, 1 boundary crossing | Above baseline — one contract to agree |
| 3+ components, 2+ boundary crossings | Well above — coordinated change |
| New block or external system | Different in kind — needs a spec and human decision |

Count components from their documents and distinct block folders from
`CONTAINERS.md`; every additional block is one boundary crossing. If
`VIEWPORTS.md` exists and the change lies on a viewport's critical path, include
that end-to-end impact. Count logical boundaries, not files or directories.

## Review a change

1. Map each changed file through its coordinate to the owning component and block.
2. Check whether the change stays within the component boundary, adds an
   undeclared dependency, or changes a recorded rule, invariant, or capability.
3. Classify every disagreement before proposing a fix:
   - moved file, extracted service, or framework swap → **implementation remapping**
   - changed rule or responsibility → **semantic change** requiring ratification
   - the executable implementation contradicts ratified Compass semantics →
     **implementation violation**; which side is wrong is decided in Create,
     so record the class and stop (`SKILL.md` §Choose exactly one flow)

Direct store access around an owning interface, reaching into another block's
internals, and one component serving two bounded contexts are common boundary
violation leads. A rule-only change may move no file or import; compare behavior
with the chart, not only topology.

## Plan a refactor

1. Read affected block `README.md` files and any viewport crossing the boundary.
2. List the `communicates-with` entries that change and find each consumer-owned
   `Uses` relationship.
3. Decide whether the refactor changes meaning or only implementation structure.

A structure-only refactor requires coordinate maintenance and no semantic edit
above L2; record that maintenance as separate Create work. A change to L0, L1,
or a block's logical role is a semantic change requiring ratification. Do not
start until the before and after state of each affected block is explicit.

## Assess overreach and architectural pull

Read the component responsibility, dependencies, consumers, boundary, and
diagram, then the block relationships, boundary, and logical role. Apply
[structural signals](structural-signals.md) as leads, not permission to redraw
the chart. A logical role expressible only as a directory name is a particularly
strong lead that the block lacks semantic identity.

Architectural pull exists only after evidence establishes a healthier direction:

- **Refactoring** — correct a component boundary that obstructs the task.
- **Extraction** — recognize a component emerging from an existing one.
- **Consolidation** — join overlapping components.
- **Decluttering** — move code whose coordinate does not fit its location.
- **Chart work** — report code with no place in the chart.

Name the Compass level and parent boundary before judging cohesion or coupling.
Record current reality separately from the evidence-backed direction, then close
the lead as **legitimate**, **declutter**, or **debt**. Coordinate density may
open the investigation; only independent cohesion or coupling evidence closes
it as debt. When the team acts on declutter or debt, capture it in the project
tracker. The chart never requires repository topology to mirror semantic
topology or schedules the resulting work; a phenomenon spanning packages or a
bridge serving two roots may be legitimate.
