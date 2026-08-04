# Helix

Helix runs a planning loop for uncertain or inherited work: expand candidate
branches from an outcome, probe one with a bounded spike, collapse the result
into verdicts, repeat. Between cycles the state lives in one small checkpoint,
rewritten at every collapse and reloadable in one read. Every cycle returns to
the same phase and never to the same place.

The loop is a tense machine. Expand foresees the future, which stays cheap
and rewritable; Spike makes one foreseen move present, its readbacks declared
before it runs; Collapse files the ended present into the sorted past —
delivered work to the store of record, retired branches to epitaphs,
everything else disposed. Only the sorted past deserves durable storage.

Helix values cadence over activity velocity. A move is not progress until its
situation or need, outcome contribution, boundary, observation source, review
point, and competing readbacks were frozen before action, and its result was
classified before another action. The freeze is intended to expose fast but
unframed work before it acquires a retrospective justification after its result
is known.

The division of labor is deliberate. Reasoning — candidate generation,
second-order tests, ranking — is performed fresh each cycle against current
evidence and is never stored; stored reasoning can go stale, while re-derivation
reduces commitment to it. The checkpoint stores only verdicts: the outcome, surviving
branches, active moves with their readbacks and appended results, open links,
and one next.

A short isolated cycle cannot reproduce the accumulation Helix is designed for:
stale branches, diluted attention, inherited state, and a tempting retrospective
story across repeated moves. It can verify the checkpoint schema and transition
rules, but the intended reduction in repeated or self-justified work remains to
be evaluated in representative multi-cycle use.

Helix selects the wider branch contribution and sequences a supplied move. It
does not classify the causal regime or design the evidence-producing probe;
when separately installed, Read the Terrain owns that upstream work. This is
external composition rather than a runtime dependency.

## What survives a collapse

- The supplied situation or need and outcome, with its proof, authority, and
  boundary — until the user changes it.
- Branches that evidence has not retired.
- Moves and results while their branch remains active — appended, never
  rewritten; a retry is a new move, so repeated work cannot masquerade as a new
  experiment. At terminal sorting, delivered or closed records move to their
  store of record; a retired branch's killing result remains in its epitaph,
  while its other dependent moves and results leave the active checkpoint.
- An epitaph for every retired branch — what killed it, and what would justify
  a retry. Version history shows only what merged; the epitaph is the only
  trace of work that never landed, and expansion checks new candidates
  against it so the loop cannot re-run its own past.
- Open links: orphans, unknown relationships, blocked dependencies.
- Exactly one next: a move, a repair, a block, or none.

Everything else is deliberately lost. Dropped candidates, ranking arguments,
and spike working context are cheaper to re-derive than to read stale.
Delivered work and closed decisions move to the environment's stores of
record; the checkpoint never becomes a third store that other systems must
stay consistent with.

## Runtime and pre-arrival guidance

The runtime keeps the transition laws and common loop inline because every
activation needs them. Detailed checkpoint and edge-case mechanics load only
when the current state requires them.

Helix does not edit `AGENTS.md` during ordinary use. Repository guidance that
routes uncertain work to Helix is a pre-arrival rule: install it only by an
explicit decision at a scope every intended reader receives. Automatic
self-install cannot cause the first activation and would tax routine work with
Helix-specific context.

## Persistence and boundary

Helix requires an explicitly configured checkpoint surface. The
configuration names its reference, its representation of the checkpoint
semantics, and the available read and write authority. It may use a local
artifact, shared system, or network integration; the skill does not choose
among them or offer a default. Without configuration, it asks the user to
configure the surface instead of storing state in a transcript.

Helix does not prove an outcome is valuable, a branch is causal, or an
implementation is correct, and it does not replace a routine task with a
planning ritual.
