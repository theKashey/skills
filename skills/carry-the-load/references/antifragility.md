# Antifragility

This reference expands the compact doctrine statement in the package README
("Antifragility governs learning"). The README statement is the binding
definition; this file explains why the discipline works and how it
maps to AI-assisted software development. It is maintainer and reader support,
never a runtime dependency: the runtime rules derived from it already live in
[SKILL.md](../SKILL.md).

## What it is

Antifragility is Taleb's third category in a triad:

- **Fragile** — harmed by disorder; wants stability and predictability.
- **Robust / resilient** — indifferent to disorder up to a bound; absorbs the
  shock and returns to its prior state.
- **Antifragile** — improved by disorder up to a bound; each stressor leaves
  the system better positioned than before it.

A rollback path makes a deployment robust. The deployment becomes part of an
antifragile system only when the failure it survives changes something — an
evaluation gets sharper, an invariant becomes explicit, a routing decision
flips, an overconfident claim gets weakened. Robustness returns to zero;
antifragility compounds.

## Why it works

- **Convex payoffs beat prediction.** When the downside of an attempt is
  bounded and the upside is open, being wrong often and cheaply outperforms
  being right by forecast. The discipline is therefore not to avoid error but
  to shape errors so they stay small, local, and informative.
- **Stressors are the only honest probe.** A real failure is direct evidence
  about the system actually in front of you; a prediction is evidence about
  the model of it. Systems denied small stressors accumulate hidden fragility
  and meet their first real one at full size.
- **Optionality preserves the upside.** A fallback, a reversible step, or a
  weakly-labeled claim keeps the option to discard a wrong commitment at low
  cost. Optionality is bought before the outcome is known; after the misfire
  it is too late to add.
- **Via negativa degrades gracefully.** Removing a wrong assumption or an
  unjustified safeguard makes fewer new claims than adding machinery, so its
  own failure mode is smaller. Subtraction is the intervention with the least
  iatrogenic surface.

## How it maps to AI-assisted software development

- **State the misfire before committing.** A credible wrong result, named in
  advance with its affected recipient, converts a surprise into a checked
  hypothesis. This is the load card's `Misfire` field.
- **Bound the blast radius on an observable partition.** Input class, tenant,
  request, component, release, time window — a failure confined to a named
  partition is bounded evidence; an unbounded one is an incident. This is the
  `Containment` field.
- **Preserve the previous behavior as the option.** Keeping the established
  path as fallback, when it remains valid, is the cheap option that makes the
  new path safe to be wrong.
- **Label claims no more strongly than the evidence.** A heuristic fitted to
  the examples in view, stated as a local weak claim, is convex: where it
  fails it is discounted and the system falls back. The same heuristic stated
  as a universal rule is fragile: its first counterexample is a cliff, or a
  permanent warning every later activation must carry.
- **Harvest, or the failure was only survived.** Fallback and rollback close
  the incident; antifragile learning exists only when the readback changes a
  future choice, gate, invariant, evaluation, or routing decision. The
  harvest table in [SKILL.md](../SKILL.md#harvest-material-learning) decides
  where that change lives.
- **Model-generated confidence is the fragilizer to watch.** An agent
  produces fluent universal rules from small samples by default; the
  antifragile counter-move is scoping, weak labeling, and preserved fallback
  — not more confidence checking after the fact.

## What antifragility is not

It is not manufacturing failure for its own sake: a stressor earns its cost
only when its evidence is captured and bounded. It is not turning every
failure into a permanent rule — an instruction that outlives its evidence is
itself accumulated fragility. And it is not a license for interventionism;
when no bounded, informative attempt is available, the antifragile move can be
to do less.
