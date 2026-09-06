# Investigate through a Compass chart

Use the applicable path after the core Consume search identifies the owning
root, block, component, or coordinate.

## Explain why code has its shape

1. Resolve the file's coordinate for each relevant root using the shared
   inheritance contract in [`SKILL.md`](../SKILL.md#shared-contract). Consult
   the chart's implementation-coordinate sections for declared carriers and
   scopes; a marker in an adjacent entry file is not implicit folder coverage.
2. Follow the address into the chart. If the code enforces a documented
   invariant, boundary, or responsibility, that is the semantic reason; stop.
3. If the chart explains the *what* but the mechanism remains surprising, keep
   that implementation-specific reason with the code under Context Docs.

Checking the coordinate first prevents the same domain intent from being
reverse-engineered repeatedly.

If a `compass-abstraction: <slug>` marker or definition affects the task, use
[the named-abstraction Consume route](consume-named-abstractions.md).

## Debug a cross-block flow

1. If `{root}/VIEWPORTS.md` exists, find the viewport covering the flow and
   identify the step producing the wrong output.
2. Open that step's component `README.md`; check its boundary and implementation
   coordinates.
3. Navigate to the coordinate and instrument the implementation boundary.

If no viewport file or matching viewport exists, report the gap and continue
from component documents and coordinates. Creating a viewport is separate
Create work.

## Understand a component

Open its `README.md` and read in this order:

1. stereotype — the component pattern;
2. responsibility — its one job;
3. boundary — what it deliberately does not do;
4. diagram — its semantic relationships; use reverse-view routes for consumers; and
5. implementation coordinates — where it lives today.

If the coordinates are wrong, classify an implementation remapping. If the
responsibility or boundary is wrong, classify a semantic finding. Do not edit
the chart during Consume.
