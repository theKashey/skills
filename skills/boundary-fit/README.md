# Boundary Fit

Boundary Fit evaluates whether the relationships around a module, service,
cell, team, or system boundary match the separation and locality that boundary
is expected to provide. It gives a practitioner or coding agent a compact way
to distinguish a meaningful boundary from a box that looks independent only
on a topology diagram.

## Why it exists

Architecture creates boundaries at many levels, but the boundary alone does
not make the relationships around it safe. Two components can live inside one
module or deployable while having little reason to share their fate, and two
components on opposite sides can still require synchronized changes, share
hidden state, or propagate failures across the system.

Those mismatches are easy to miss when review starts from adjacency, service
count, or dependency count. The affected practitioner needs to trace what a
relationship actually carries and which effects travel through it before
deciding that components belong together or can evolve independently.

The intended effect is a falsifiable boundary assessment: the claimed
isolation, the material relationships that test it, their structural shapes,
and one explicit verdict for each frozen boundary cut and promise. The
assessment makes conditions and unknowns visible instead of turning
architectural neatness into proof.

## Structural vocabulary

The skill uses four deliberately local terms:

| Shape | Meaning |
| --- | --- |
| **Local bundle** | Closely related elements keep their necessary coordination inside the boundary. |
| **Boundary bridge** | Separate units interact through a narrow, explicit relationship. |
| **Boundary knot** | A boundary-spanning relationship creates lockstep change or propagates an effect the boundary should contain. |
| **Topology passenger** | An element is colocated by the standard deployment shape without thereby becoming cohesive with its neighbours. |

These names describe relationships at a declared level; they do not assign one
permanent label to a service or system. The same relationship can be local at
one level and boundary-spanning at a narrower level.

Intended duplication is not a fifth shape. Repeated local implementations may
protect locality when they can safely diverge and cost less than a shared
dependency. Copies that must remain semantically identical still have a
relationship: one explicit semantic owner and enforced distribution or
cross-boundary conformance can keep that relationship narrow, while manual
synchronization creates boundary-spanning lockstep regardless of intent. A
one-time comparison, an opt-in check, or agreement with another unauthoritative
copy establishes current equality, not maintained identity.

## Design choices and tradeoffs

- **Boundary promises before topology.** The current arrangement cannot prove
  the isolation it is supposed to provide. An explicit requirement or product
  decision supplies that promise.
- **Effects before dependency counts.** One contract bridge may be safer than
  many local relationships, while one boundary knot can defeat an otherwise
  clean architectural cut.
- **Colocation is not cohesion.** Fixed topology can be valuable for production,
  capacity, compliance, or cost even when some occupants are topology
  passengers. The skill preserves that reason instead of prescribing a split
  for conceptual purity.
- **Change pressure permits bounded pragmatism.** A difficult cross-boundary
  relationship may be tolerable when it is demonstrably stable, its
  consequences are bounded, and drift or failure can be credibly detected and
  recovered. Infrequency alone does not make severe harm safe; the accepted
  condition and reassessment trigger remain part of the result.
- **Duplication is judged by divergence harm.** Similarity alone does not earn
  centralization. The relevant evidence is whether copies may evolve
  independently, what inconsistent behavior drift would cause, and how any
  required semantic identity is owned and enforced.
- **The analysis is fractal.** The reviewer declares the observed level so a
  system-level conclusion does not conceal a module-, service-, or team-level
  mismatch. Materially different boundary cuts or promises receive separate
  verdicts rather than one averaged conclusion.

Rejected shortcuts include treating every boundary-crossing call as a defect,
centralizing every repeated implementation for tidiness, calling manually
synchronized copies safe because their duplication is intentional, declaring
today's matching copies maintained because one comparison passes, declaring
every colocated dependency cohesive, inferring quality from a diagram, and
recommending service or module splits without evidence about the effects that
would move.

## Evaluation boundary

The skill evaluates structural fit from the evidence it receives. It does not
prove runtime isolation, reliability, security, compliance, performance, or
correct tenant placement. Those claims require their own tests, telemetry, and
authoritative controls.

It does not choose a universal module, service, cell, or system size; require
every capability to become local; or treat shared infrastructure as inherently
wrong. It reports when a relationship contradicts the boundary's stated
promise and keeps missing evidence visible as `UNRESOLVED`.

It evaluates repeated content only when that repetition tests the frozen
boundary promise; similarity outside that frame is out of scope.

An assessment does not authorize a restructure. Review, conceptual design, and
implementation remain separate authority levels.

## Relationship to Compass

Compass records the semantic system, its responsibilities, and the boundaries
humans have ratified. Boundary Fit evaluates whether relationships around a
candidate boundary support the separation and locality that boundary claims to
provide. It can use a chart as evidence, but it neither creates nor requires
one. The two skills remain independently installable and neither invokes the
other.

## Ownership

| File | Owns |
| --- | --- |
| [SKILL.md](SKILL.md) | Runtime assessment frame, relationship trace, structural vocabulary, locality tests, response selection, and verdicts |
| [README.md](README.md) | Durable rationale, tradeoffs, evaluation boundary, and package relationship |

Use the [runtime assessment](SKILL.md) when a module, service, cell, team, or
system boundary is being designed or reviewed.
