---
name: helix
description: Use when uncertain or inherited work needs a planning loop — expand candidate directions, run one bounded spike, collapse the result into a small rewritten checkpoint; not for a routine task with clear scope and order.
---

# Helix

Run a planning loop that keeps why, what, and how connected by moving work
through three tenses: foresee candidate branches from the outcome, execute
one bounded spike, file the ended present into the sorted past, repeat. The
checkpoint between cycles stores only verdicts and stays reloadable in one
read.

| Transition | Phase | Tense law |
| --- | --- | --- |
| The future is foreseen | Expand | Futures are cheap: re-derive them fresh each cycle; store only survivors. |
| The future becomes present | Spike | The present is singular: one bounded move in flight, its readbacks declared before it runs. |
| The present becomes past | Collapse | The past is immutable and sorted: store of record, epitaph, or deliberate disposal — nothing lingers unsorted. |

## Configure the checkpoint surface

Before the first cycle, require an explicitly configured checkpoint surface.
The configuration must name its durable reference, how it represents the
semantics below, and the available read and write authority. It may be a local
artifact, shared system, or network integration; never select one on the
user's behalf.

If configuration is missing, return `NEEDS-HUMAN-DECISION` and ask the user to
configure the surface. Do not propose a filename, project location, task
system, external service, MCP, or transcript as a fallback.

| Checkpoint semantic | Required content |
| --- | --- |
| Outcome | Intended change, proof, and boundary. |
| Branch | A distinct surviving contribution, or `unknown`. |
| Move | Bounded action, linked branch, and expected plus disconfirming readback. |
| Result | Immutable observation linked to its move, effect, and next decision. |
| Open link | Orphan, unknown relationship, or blocked dependency. |
| Next | One move, checkpoint repair, block, or `none`. |
| Epitaph | Retired branch, the disconfirming result, and the resurrection condition that would justify a retry. |

The checkpoint holds verdicts, not deliberation. Candidate lists, hypotheses,
and ranking rationale are cheaper re-derived at expand time than read stale; a
checkpoint that grows across cycles without a newly admitted branch is storing
deliberation.

Epitaphs are the one append-only region: never rewritten, never pruned, and
not reloaded — they are consulted at expand, so they do not erode the
one-read budget.

## Reload

1. Read the checkpoint whole. When none exists, state one outcome, its proof,
   and its boundary; if materially different outcomes remain plausible, return
   `NEEDS-HUMAN-DECISION`.
2. Reconstruct supplied history as results linked to their moves and branches.
   Keep an unknown or orphan link explicit; never write a retrospective
   rationale just to complete the record.

Reload is complete when the outcome, open links, and latest results are
visible without consulting any other store.

## Expand

Re-derive direction fresh from the outcome and the latest results. Nothing
from this phase survives except the surviving branch set and the selection.

1. List the distinct candidate branches that could change the outcome,
   including repair of an open link.
2. Apply the second-order test to each: what would its result change about
   the next decision? Drop a candidate whose success and failure leave the
   next decision identical.
3. Check the survivors against the epitaphs. A candidate that matches a
   retired branch is admitted only by naming which part of its resurrection
   condition now holds; without that, it is the same dead branch under a new
   title.
4. Select one branch to probe now. Record the survivors as branches; do not
   record the dropped candidates or the ranking argument.

Do not inspect code during expand; code can refine a move, it does not
redefine the outcome. Expand is complete when one branch is selected and the
checkpoint lists only surviving branches.

## Spike

1. Write one bounded move: linked branch, expected readback, disconfirming
   readback. A move without a branch is an orphan — repair the link or leave
   the move out.
2. Give the executor, subagent or self, only the outcome boundary, the move,
   and its readbacks — not the checkpoint history. Context beyond what the
   move needs invites drift from probe into implementation.
3. Execute within the move's boundary. The spike is complete when a readback
   is observed or the boundary is hit, whichever comes first.

## Collapse

Collapse is mandatory after every spike; a spike without a collapse is an
open link, not progress. Every ended move sorts to exactly one destination:
delivered work to the store of record, a retired branch to an epitaph,
everything else disposed with the cycle's deliberation.

1. Append the result beside the move's original readback; never rewrite the
   move. Keep observation separate from interpretation.

   | Result | Checkpoint action |
   | --- | --- |
   | Expected | Continue only within the observed boundary. |
   | Disconfirming | Retire the branch and its dependent moves. |
   | Mixed | Preserve both signals; narrow or split the branch. |
   | Inconclusive | Repair observation only when a different bounded move could decide something. |

2. Prune: write each retired branch an epitaph — the branch, the result that
   killed it, and the condition that would justify a retry — then delete the
   branch and its dependent moves from the checkpoint. Version history shows
   only what merged; the epitaph is the only trace of work that never landed,
   and what stops the same dead branch from returning under a new name. A
   retry is a new move, never a rewrite of the old one — add it only when a
   changed condition, execution defect, or new observation can alter the next
   decision.
3. Move durable exhaust — delivered work, closed decisions — into the
   environment's stores of record. The checkpoint is not a store of record;
   an entry another store can validate belongs in that store. Epitaphs are
   the exception: no other store holds undelivered learnings.
4. Rewrite the checkpoint and select one **Next**: move, repair, block, or
   `none`. After pruning, the rewritten checkpoint is the same size or
   shorter unless expand admitted a new branch.

“Worked” means the recorded readback matched under its boundary, not that the
outcome is proved or the explanation is causal.

## Return

Return the checkpoint reference, the selected **Next**, and any orphan,
unknown, or authority block. A checkpoint with explicit uncertainty is usable;
a task list without outcome lineage is not a valid result.
