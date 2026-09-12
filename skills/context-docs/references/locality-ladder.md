# Documentation locality ladder

Locality can explain or propose a fit; the environment's established owner and
submission route decide the actual home. The ladder is not a folder tree,
document inventory, measure of importance, or persona catalog.

Documentation topology is the reader-visible result of authorized product and
distribution decisions: each material reader, their entry point, the context
delivered with the artifact, and the surfaces reachable from that entry. It
follows those decisions, not repository structure. An external consumer—a
reader who receives the subject across a distribution or team boundary,
whether an anonymous adopter or a sibling team—can hold a different topology
than a repository reader over the same files.

## Product evidence and topology

For product documentation, freeze the authorized completed product and
distribution contract before gathering evidence. Treat an observation as transient
delivery state when an ordinary publish, tag, deploy, propagation, or rollout
operation could change it without a product or distribution-contract decision.
Exclude that proposition from product-contract evidence, reasoning, findings,
risks, caveats, prerequisites, and route selection regardless of its source.
Inspect current delivery state when it is the task's subject. An explicit
decision that the completed product remains source-only is an enduring boundary.
Working records use the [handoff contract](content-architecture.md#working-documents-and-handoffs)
instead: relevant unfinished state is evidence for continuation, not product policy.

On an external-consumer surface, an authorized product or distribution decision
revokes the established topology when it changes the consumer population, an
entry point, the delivery boundary, what remains reachable, or a consumer-facing
contract. Return to [casting](casting.md) with the post-decision consumer set and
record the per-consumer delta. Upstream validation suppresses re-litigating
intent only while those material assumptions survive; reopen the consequences
of the new decision, not validated intent itself. Registry, tag, or deployment
state alone never fires this trigger. Line, block, and file comments do not
enter it, nor does orientation whose every material reader receives the repository.

## Pass the existence and ownership gates

1. When the purpose of an existing choice or structure is unknown, treat it as
   Chesterton's Fence and investigate before changing or removing it. Once the
   purpose is understood, name the reader's decision, task, or continuation
   need. For code-local rationale, establish the invisible reef—the non-local
   cause and material consequence; broader facts follow
   [prior and speciality admission](content-architecture.md#prior-and-speciality-admission).
2. List only context the reader actually encounters before that decision:
   nearby code, types, tests, package metadata, system access, and canonical
   documentation reached through the project's normal route. Count the cast's
   assumed priors and every verified delegated guarantee as that context too;
   [prior and speciality
   admission](content-architecture.md#prior-and-speciality-admission) defines
   both.
3. Add nothing when that context already makes the decision safe. An unfamiliar
   abstraction normally needs a route to its owner, not a second explanation at
   every use. A fact the reader already holds as a prior, or that an executable
   gate already enforces, does not become a local gap by being absent from
   repository prose.
4. A fact outside the governed subject's speciality—the boundary that [prior
   and speciality admission](content-architecture.md#prior-and-speciality-admission)
   defines—earns local prose only where it leaks across the abstraction
   boundary with a material local consequence; keep the smallest consequence
   here and route the rest to the external owner.
5. Follow the established owner. If it cannot be updated, return a placement
   proposal for that owner instead of inventing a fallback record.
6. For line, block, or file comments, the code-comment gate settles admission
   first; place only an explanation that passes it and its continuation in
   [code comments](code-comments.md#selective-context-authoring-decision).

## Connect encounter points to the owner

One canonical owner holds the complete contract and remote mechanics; it need
not be the only place that names the relationship. Map the independent paths
the repository actually puts before an affected reader: a symbol or diff,
folder-local instructions, package documentation, and the canonical owner. Do
not count repository-wide semantic search or indexing as available context
unless the actual workflow reliably supplies the relevant result before the
decision.

Distinguish delivered context—what arrives in the reader's environment with
the artifact—from reachable context—what a route can still fetch. A
distribution decision can sever delivery while leaving reachability intact: a
package published from a monorepo delivers only its own README, so that README
is an effective root for its external consumer while remaining a child surface
on the repository path. A surface serving several material entry paths may
assume only the context delivered on every one of them. When an encounter path
merely fails to reach the owner, the compact breadcrumb below suffices; when
an authorized decision severs a delivery boundary, the surface's role has
changed—route that re-decision through [casting](casting.md) instead of
patching a root-sized gap with a breadcrumb.

When an encounter path does not reach the owner and the gap would cause an
unsafe action or repeated reconstruction, leave a compact breadcrumb at the
narrowest existing or authorized surface. Include only:

- the local decision, task, or continuation need and its missing fact;
- for rationale, the verified causal edge and material local consequence; and
- a direct, descriptive route to the canonical detail.

A route is only a route where it resolves in the context the reader receives.
Verify it against the artifact that reaches them—emitted declarations, the
published package, the rendered page—not only the repository working tree. A
relative link that crosses a delivery boundary the reader never receives
resolves for a repository reader and fails for the consumer.

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
consequence. Keep detailed truth with one canonical owner. JSDoc on an
established public-contract symbol is a public-contract overlay, not another
scope. Implementation altitude is also not a scope: low-level, business, and
orchestration code can each contain a Chesterton's Fence or a verified invisible
reef, but any explanation belongs at the scope that owns the decision.

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
decision, task, or continuation. Preserve any needed local causal edge and
consequence; leave remote mechanics with their owner. Check that every evidenced encounter path reaches
the local consequence and canonical detail before action, without copying a
narrower or broader contract or claiming authority to create or move a surface.
