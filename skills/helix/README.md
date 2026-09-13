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

Helix shares a premise with agent-loop techniques such as Geoffrey Huntley's
[Ralph Wiggum loop](https://ghuntley.com/ralph/) and goal-driven loops: long
work should not depend on one heroic context window. It answers a different
question. Ralph persists execution — how the agent keeps working; a goal loop
persists intent — what it keeps working toward; Helix persists learning — what
is different now. A loop amplifies whatever it preserves, including a
contaminated explanation, and can travel just as far in the wrong direction;
that risk, not storage economy alone, is why the checkpoint carries verdicts
and epitaphs rather than the reasoning that produced them. Nor does that risk
need a long horizon. A loop can accumulate stale branches, dilute its own
attention, and acquire a retrospective story inside a single working day, while
its state stays intact and every cycle closes correctly. Helix does not
compete with or replace such a loop; it disciplines what survives between
iterations.

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

## When success stops moving the outcome

The transition laws already forbid the failure this route detects: Expand must
derive branches from the outcome and latest results, both rather than the
latest alone, and activity volume is not progress. What was missing is a state
in which the violation becomes visible. Every other route that redirects the
loop keys on a defective record or on disconfirming evidence, and an
`Expected` result carries exactly one consequence — continue
inside the observed boundary. So a loop whose every result is `Expected`
reaches no state where any rule fires, while each cycle derives its next branch
from the last one's closure and the outcome is never revisited.

The trip is the second consecutive collapse leaving the proof unmoved. One is
ordinary: a move can confirm something inside its boundary without advancing
the outcome, which is exactly what a matching readback is warned not to prove.
Two is the first point at which it describes the loop rather than a move. This
bound is not the one the sibling skills Read the Terrain and Retrospective use
after repeated inconclusive moves; theirs are calibrated to a dead observation
channel, and this channel is live.

The resulting move reads the checkpoint, not the work. That keeps it inside
what Helix already owns — it authors an unrequested next whenever its own
record is defective — and clear of the upstream classification Read the Terrain
owns. The discriminator is the observation source every move must name anyway.

A circuit breaker was rejected. Halting the loop or returning the question to
its user replaces a stalled loop with a stalled human, and the loop can retire
the branch itself; nothing on this route escalates.

The trip depends on the run staying legible in one checkpoint read. It does
while the branch producing it remains active, because moves and results are
appended there and never rewritten. A loop that terminally closes each cycle
and starts the next from its successor sends those records to their store of
record, leaving nothing to count — that shape is uncovered, and covering it
would mean storing a tally the tense law does not allow.

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
among them or offer a default. Nor does it choose a lifetime: a scratch file
opened for one session's work and deleted at the end of it is a checkpoint,
because the loop reads and rewrites it by reference. Without configuration, it
asks the user to configure the surface instead of storing state in a
transcript.

Helix does not prove an outcome is valuable, a branch is causal, or an
implementation is correct, and it does not replace a routine task with a
planning ritual.
