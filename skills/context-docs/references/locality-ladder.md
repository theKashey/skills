# Documentation locality ladder

Use this guide only when documentation existence, ownership, governed scope, or
placement remains unresolved. Locality can explain or propose a fit; the
environment's established owner and submission route decide the actual home.
The ladder is not a folder tree, document inventory, measure of importance, or
persona catalog.

## Pass the existence and ownership gates

1. When the purpose of an existing choice or structure is unknown, treat it as
   Chesterton's Fence and investigate before changing or removing it. Once the
   rationale is verified, name the decision the reader must make and the
   invisible reef—the non-local cause and material consequence—that changes it.
2. List only context the reader actually encounters before that decision:
   nearby code, types, tests, package metadata, system access, and canonical
   documentation reached through the project's normal route.
3. Add nothing when that context already makes the decision safe. An unfamiliar
   abstraction normally needs a route to its owner, not a second explanation at
   every use.
4. Follow the established owner. If it cannot be updated, return a placement
   proposal for that owner instead of inventing a fallback record.
5. For line, block, or file comments, first apply the [selective-context
   authoring decision](api-jsdoc-examples.md#selective-context-authoring-decision).
   Place only an explanation that passes that admission gate.

## Connect encounter points to the owner

One canonical owner holds the complete contract and remote mechanics; it need
not be the only place that names the relationship. Map the independent paths
the repository actually puts before an affected reader: a symbol or diff,
folder-local instructions, package documentation, and the canonical owner. Do
not count repository-wide semantic search or indexing as available context
unless the actual workflow reliably supplies the relevant result before the
decision.

When an encounter path does not reach the owner and the gap would cause an
unsafe action or repeated reconstruction, leave a compact breadcrumb at the
narrowest existing or authorized surface. Include only:

- the local decision and invisible reef with its material consequence;
- the shortest verified causal edge showing why the remote owner matters; and
- a direct, descriptive route to the canonical detail.

Keep procedure, configuration, and implementation mechanics with the owner.
Multiple breadcrumbs are intentional when each serves an independent encounter
path; the number of callers alone proves nothing. Prefer one broader local
breadcrumb when every affected reader receives it, but retain a code-local one
when a symbol or diff reader can bypass that context.

**Illustrative topology, not a required file layout:** a pipeline field is the
likely entry for configuring a pull-request trigger, while the working hook
mechanics live in a remote webhook or deployment service. Keep the full hook
pattern with that service, put a short route in the pipeline area's local
instructions, and add a field comment only when the selective-context gate
establishes a hidden local consequence. These are three encounter surfaces but
one mechanics owner.

## Use the project's reader context

Load a project-owned reader cast when one exists. Do not substitute built-in
roles. When no durable cast is available, keep the decision task-local and
record only:

- the entrant who reaches the surface;
- context available at that encounter;
- the decision or task they control;
- the material fact still missing; and
- the point at which they need it.

When several durable classes share an entry surface, follow the project's
frequency and service priority: keep the highest-frequency applicable path
direct and compact, then route lower-frequency deltas to their canonical deeper
owner. Use [casting](casting.md) when the class or priority itself is in doubt.

**Illustrative example, not a default persona model:** a project may find that
most package-page entrants need the supported contract and first use, while a
smaller maintainer group needs lifecycle rationale. The package page can serve
the common path directly and link maintainers to the established lifecycle
owner. Another project may have the opposite distribution and should reverse
that priority.

## Choose the narrowest fitting scope

Use the narrowest existing or authorized surface encountered by every affected
reader before the governed decision.

| Scope | Use it when the missing fact governs |
| --- | --- |
| Line | One expression, argument, branch, or assignment. |
| Block | One guard, transformation, loop, or sequence. |
| File | The implementation unit's responsibility, lifecycle, or non-local relationship. |
| Folder | An implementation area's ownership, organization, boundary, or local route. |
| Package or module | A reusable unit's contract, integration conditions, failures, or compatibility boundary. |
| Domain or service | Cross-unit responsibility, flow, lifecycle, operations, or escalation boundary. |
| Top level | System or repository scope, major boundaries, and routes to canonical detail. |

Broader scopes orient and route; narrower scopes preserve the local
consequence. Keep detailed truth with one canonical owner. Exported-symbol
JSDoc is a public-contract overlay, not another scope. Implementation altitude
is also not a scope: low-level, business, and orchestration code can each
contain a Chesterton's Fence or a verified invisible reef, but any explanation
belongs at the scope that owns the decision.

Physical layout may overlap logical scope: a module can be a file and a package
can be a folder. Co-locate scopes only when they genuinely coincide, and do not
manufacture files to mirror the ladder. When the distinction among a technical
README, documentation home, and public presentation page is unresolved, load
[content architecture](content-architecture.md#classify-technical-documents-and-public-sites).

## Form the result

Return one of:

- `No-op` — the reader can already act safely;
- `Update established owner` — the owner and fitting scope are known; or
- `Placement proposal` — state the reader, available context, missing fact,
  governed scope, proposed owner, and unresolved authority.

For an update or proposal, write the smallest verified fact that changes the
decision. Preserve the local causal edge and consequence; leave remote
mechanics with their owner. Check that every evidenced encounter path reaches
the local consequence and canonical detail before action, without copying a
narrower or broader contract or claiming authority to create or move a surface.
