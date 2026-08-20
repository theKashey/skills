---
name: boundary-fit
description: Use when designing or reviewing a module, service, cell, team, or system boundary to decide whether shared knowledge, change, failure, lifecycle, and ownership relationships fit the separation.
---

# Boundary Fit

Declare the observed level before judging the structure. A boundary is fit only
when its material relationships align with the separation and locality it
promises; diagram adjacency is evidence, never the verdict.

## Freeze the boundary claim

Record the smallest assessment frame that can be checked:

```text
Observed level: [method, object, module, service, cell, team, or system]
Candidate boundary: [the structural cut or repeated unit being assessed]
Boundary promise: [which knowledge, changes, or effects should remain local]
In-scope relationships: [the named relations that can test the promise]
Evidence: [contracts, code, topology, ownership, runtime observations, decisions]
Authority: [review only, conceptual design, or an explicitly authorized change]
```

Use an explicit architecture requirement or product decision for the boundary
promise. If none is available, report `UNRESOLVED`; do not turn the current
topology into its own justification.

One assessment yields one verdict for one boundary cut and one promise. Split
materially different cuts or promises into separate frames; multiple
relationships may remain in one frame when they test the same promise.

## Trace what crosses

Inspect every material relationship that touches the candidate boundary. A
relationship is material when a consumer could reasonably act on its change,
failure, data, lifecycle, or ownership consequences.

For each relationship, record:

- **Endpoints:** the source, target, and direction.
- **Dependency content:** whether the relationship carries only a boundary
  contract, also shares domain language or schemas, duplicates a rule or
  workflow, or depends on private state or implementation.
- **Duplication contract:** when behavior, data, or a representation is
  repeated, whether the copies may diverge, what concrete harm divergence
  causes, and—when identity is required—which semantic owner and relevant trust
  transition govern alignment. Distinguish identity observed now from identity
  enforced before independently changed copies become trusted, through
  authoritative distribution or cross-boundary conformance. A comparison with
  another unauthoritative copy is corroboration, not an oracle.
- **Effects that travel:** change, failure, data placement, migration,
  deployment, provisioning, retirement, policy, capacity, or operator action.
- **Structural span:** which code, module, deployable, cell, runtime, and team
  boundaries it crosses.
- **Change pressure:** why the relationship is expected to change frequently,
  rarely, or at an unknown rate. Use domain and platform evidence, not commit
  counts alone.
- **Evidence and unknowns:** the source for each claim and what remains
  inferred.

Trace the same relationship at the level named in the frame. Two services may
be close at system level and still be distant at module or team level; do not
mix those judgments in one classification.

## Classify the structural shape

Classify relationships, not whole systems, with this local vocabulary:

| Shape | Evidence pattern | Structural reading |
| --- | --- | --- |
| **Local bundle** | Closely related elements share rules or operational fate and remain inside the boundary. | Their proximity makes required coordination local. |
| **Boundary bridge** | Separate units exchange a narrow, explicit contract and can change or fail without hidden lockstep. | Distance is supported by a deliberately small relationship. |
| **Boundary knot** | A relationship crosses the boundary while sharing rules, internal models, private state, synchronized change, or cascading failure. | The apparent separation is contradicted by boundary-spanning lockstep. |
| **Topology passenger** | Elements are colocated by a standard deployment shape but share little purpose or fate. | Proximity is not evidence of cohesion. |

Intended duplication is a relationship disposition, not a fifth shape. Local
copies that may safely diverge can remove a cross-boundary coordination need.
Copies that must remain semantically identical still carry a relationship: an
explicit semantic owner with enforced distribution or cross-boundary
conformance can support a boundary bridge. A current comparison, opt-in check,
or self-consistency against another unauthoritative copy does not establish
maintained identity; hidden or manual synchronization is evidence of a boundary
knot. Judge that relationship against the frozen promise.

A topology passenger is not automatically a defect: uniform production,
compliance, capacity, or cost may justify the placement. A boundary knot can
also be tolerated when verified low change pressure, bounded consequences, and
credible detection and recovery make its cost acceptable. Infrequency alone
does not make severe divergence or failure harm safe. Record the reason and the
condition that would force reassessment; do not call either shape healthy by
default.

## Test the promised locality

Ask only the locality questions relevant to the frozen promise:

1. **Change locality:** Can one side evolve without a coordinated change on
   the other side?
2. **Duplication locality:** When content is repeated, may the copies diverge?
   If not, is semantic ownership explicit, where is identity enforced before
   the copies become trusted, and does the mechanism distribute from an
   authority or exercise the actual boundary copies or public contracts?
3. **Failure locality:** Can unavailability, corruption, overload, or a bad
   rollout cross the boundary?
4. **Data locality:** Can the bounded unit place, migrate, restore, and retire
   its data without hidden references or shared state outside it?
5. **Lifecycle locality:** Can the bounded unit be built, provisioned,
   deployed, validated, migrated, and retired without per-neighbour
   orchestration?
6. **Ownership locality:** Does ordinary work stay with one accountable owner,
   or require recurring cross-team coordination?
7. **Policy locality:** When the promise includes security, compliance, or
   tenancy, can the boundary enforce it without trusting an unrelated local
   convention?

Distinguish a relationship that merely communicates across a boundary from one
that transfers the effect the boundary claims to contain.

## Select the smallest response

- Keep closely related elements local when they genuinely need to change or
  fail together and independent lifecycle brings no compensating value.
- When separation must remain, reduce the relationship to an explicit boundary
  contract and place translation at the boundary so neither side imports the
  other's internal model.
- Use intended duplication when its local availability, ownership, or coupling
  benefit is evidenced and either divergence is safe or one semantic owner plus
  enforced distribution or cross-boundary conformance preserves required
  identity. Copies that merely match today or depend on manual coordination
  remain a boundary knot.
- Preserve a topology passenger when standardization, capacity, compliance, or
  cost is the verified reason for colocation; do not split it for diagrammatic
  purity.
- Accept a boundary knot only as an explicit condition with evidence, an owner,
  bounded consequences, credible detection and recovery, and a reassessment
  trigger.
- When evidence is missing, choose the smallest observation that can distinguish
  local effects from boundary-spanning ones before recommending a redesign.
- When several issues are evidenced in one frame, address the smallest
  high-consequence seam first rather than bundling unrelated repairs.

A review authorizes findings, not restructuring. A conceptual design may
recommend a shape; implementation requires a separate user-authorized task and
its applicable workflow.

## Return the assessment

Return one block for each frozen boundary cut and promise.

```text
Boundary: [candidate]
Observed level: [level]
Promise: [effects expected to remain local]

Relationships:
- [source -> target] | [shape] | [effects that travel] | [evidence]

Fit: [what aligns with the promise]
Mismatch: [what contradicts it]
Recommendation: [smallest supported response]
Conditions: [accepted assumptions, owners, and reassessment triggers]
Evidence gaps: [unknowns that prevent a stronger conclusion]

Verdict: FIT | CONDITIONAL | MISFIT | UNRESOLVED
```

- `FIT` — material relationships support the stated boundary promise.
- `CONDITIONAL` — fit depends on a named, evidenced condition and trigger.
- `MISFIT` — a material relationship contradicts the stated promise.
- `UNRESOLVED` — evidence, authority, level, or the boundary promise is missing
  or conflicting.
