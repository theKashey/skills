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

The division of labor is deliberate. Reasoning — candidate generation,
second-order tests, ranking — is performed fresh each cycle against current
evidence and is never stored; stored reasoning goes stale, re-derived
reasoning cannot. The checkpoint stores only verdicts: the outcome, surviving
branches, moves with their readbacks, appended results, open links, and one
next.

## What survives a collapse

- The outcome, with its proof and boundary — until the user changes it.
- Branches that evidence has not retired.
- Moves and their results — appended, never rewritten; a retry is a new move,
  so repeated work cannot masquerade as a new experiment.
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
