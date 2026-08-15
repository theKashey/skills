# Carry the Load

Carry the Load shapes a selected engineering change into one complete,
value-bearing increment, makes a plausible misfire cheaper than unchecked
success, and retains only the machinery justified by the load and evidence in
front of it.

It is for the point after an outcome or move has been selected but before the
work expands into a large batch, speculative architecture, success-only
rollout, or accumulating safeguards. It governs how work flows through
implementation and verification; it does not choose the product outcome or
diagnose an unknown cause.

## Why the skill exists

An agent can produce a locally impressive solution while making the engineering
system worse. It can optimize code volume instead of lead time to a verified
outcome, open several unfinished branches, add protection without naming the
failure it protects, or fit a confident rule to the examples currently visible.
When the rule fails, the system falls off a cliff or acquires another warning
that every later activation must carry.

Carry the Load exists to keep one selected outcome moving through a short,
closed feedback loop. The intended result is the smallest complete change that
delivers observable value, contains its credible failure, and leaves the next
execution better informed without turning every incident into permanent
process.

A clean isolated exercise is weak evidence for that effect. It removes the
queues, inherited safeguards, competing work, and attractive overbuilding that
make the wrong route plausible. Evaluation needs representative engineering
work in the target harness, including the success-only or comprehensive default
the skill is meant to change.

## Keep the doctrines distinct

The skill combines three disciplines without treating them as synonyms.

### Lean governs flow

Lean means the Toyota-derived discipline of customer value, value stream,
flow, pull, constrained work in progress, quality at the source, and continuous
improvement. The unit of flow here is a verified engineering increment, not a
token, file, task, or model response.

Lean does not mean thin, stripped-down, or *obezhirennoe*. The useful Russian
translation is *berezhlivoe proizvodstvo*: careful stewardship of value,
capacity, attention, and material. Removing code can improve flow, but code
volume is not the objective.

### Antifragility governs learning

A rollback, fallback, or bounded blast radius makes an execution resilient. The
engineering system becomes antifragile only when a material failure improves a
future response: it sharpens an evaluation, exposes an invariant, changes
routing, weakens an unjustified claim, or removes a bad assumption.

Expecting to be wrong therefore changes the shape of the deliverable. A rule
fitted to the current examples should misfire locally, degrade to established
behavior, carry no stronger label than its evidence earns, and be discountable
where it fails. Failure remains bounded evidence rather than a global verdict.

### Pragmatic engineering governs proportion

Build the smallest mechanism that carries the demonstrated load, but do not
confuse smallest with fewest lines. A test, fallback, buffer, abstraction, or
second implementation may be the cheapest sufficient design when consequence
or reversibility demands it.

“Delete what protects nothing” belongs here as a protection audit, not as the
definition of Lean. A protection stays when it names a current load or credible
failure, reaches the affected path, and is cheaper than the consequence it
contains. It becomes a deletion candidate when no such relationship survives.

## What changes in agent behavior

Without this skill, a plausible default is to build a comprehensive candidate,
protect it broadly, and verify it near the end. Carry the Load instead makes the
agent:

- start from the recipient-visible effect and identify the current constraint;
- keep one complete value-bearing increment in flight;
- pull context, tools, abstraction, and protection when the increment demands
  them rather than accumulating them in advance;
- state a credible misfire and containment before committing to the change;
- verify at the first surface capable of observing the promised effect;
- distinguish resilience from learning and persist only material learning;
- place a learned constraint in code or a deterministic gate when possible,
  and in `AGENTS.md` only when a recurring judgment choice needs model context;
- remove a protection only after its load and affected paths are understood.

## Behavior principles and `AGENTS.md`

An execution may reveal a durable model choice that future work would otherwise
repeat. Carry the Load can propose or, with authority, add a behavior principle
to the narrowest `AGENTS.md` received by every affected agent.

This is not automatic self-installation. A single tool error, local fact, or
mechanically enforceable invariant does not earn recurring model context. The
principle must name an observable condition, the supported move, the plausible
wrong default it replaces, the verified consequence, and a completion or stop
signal. The runtime loads the conditional
[behavior-principle procedure](references/behavior-principles.md) only when a
material misfire or explicit repository-learning request makes that choice
live.

## Relationship to the suite

Read the Terrain chooses one bounded evidence-producing move when cause and
effect are unclear. Carry the Load assumes the move or outcome has already been
selected and shapes its implementation, containment, and learning.

Helix persists verdicts and sequences moves across uncertain cycles. Carry the
Load governs the engineering flow inside one selected increment and does not
own a planning checkpoint. Helix also declares that it never edits `AGENTS.md`
during ordinary use; Carry the Load diverges deliberately by carrying an
authority-gated write path, and the authority gate, not the skill, decides.

Context Docs decides whether an explanation is truthful, necessary, and local,
and owns admission and placement of reader-facing facts — including local
`AGENTS.md` conventions that record human or operational contracts. The
behavior-principle procedure admits only recurring model judgments; when a
learning turns out to be a fact for a human or operational contract, it belongs
to documentation admission, not to this skill.

Screaming Reefs turns a verified prose constraint into structure under an
explicit authorization test and a fresh-context readback. When it is installed,
route the structural replacement of a documented constraint to it. Carry the
Load applies the same authorization and fresh-reader discipline only to the
mechanical invariant its own increment just learned, and it does not redesign
a repository merely to delete an instruction.

Skill Guidance owns the Laws of Agent Instruction that govern instruction
wording and placement. The behavior-principle procedure deliberately restates
several of those Laws in procedural form so the package works when installed
alone; this is a recorded divergence, not an accidental paraphrase, and
skill-guidance's `LAWS.md` remains the canonical statement. The procedure's
validation step checks its own principle's effect; it is self-validation, not
the advisory review Skill Guidance provides.

These are external compositions of separately installed skills, not runtime
dependencies; the package completes alone. One maintenance invariant follows
from the overlap: the load card's Readback field in [SKILL.md](SKILL.md) is a
deliberate verbatim duplicate of Read the Terrain's terrain-card Readback
field, and read-the-terrain remains its canonical owner. Keep the two fields
identical when either changes, or record a deliberate divergence; an
accidental paraphrase between them is a defect.

## Ownership

| File | Owns |
| --- | --- |
| [SKILL.md](SKILL.md) | Activation boundary, load card, flow, containment, protection audit, learning harvest, and completion |
| [Behavior principles](references/behavior-principles.md) | Conditional admission, placement, wording, and validation of learned agent behavior |

## Boundaries

Carry the Load does not decide whether the requested outcome is valuable,
discover causality, maintain a multi-cycle plan, or prove the final product is
desirable. It does not equate low token use, few files, or deleted code with
Lean. It does not manufacture failure for its own sake, turn every failure into
a rule, silently weaken safety boundaries, or edit `AGENTS.md` without authority.

## Runtime contract

[SKILL.md](SKILL.md) is the package's only runtime entry point; it contains the
load card, flow, containment, protection audit, learning harvest, and terminal
statuses, and conditionally loads the behavior-principle procedure. The
rationale above is maintainer support and is not required to run the skill.
