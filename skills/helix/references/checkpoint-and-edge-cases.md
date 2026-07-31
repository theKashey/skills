# Checkpoint and edge cases

Use only the section selected by the current checkpoint state. Return to the
core loop after its completion condition holds.

## Configure or reconstruct the checkpoint

Require a configured checkpoint surface before the first cycle. Its
configuration names a durable reference, how it represents the semantics below,
and the available read and write authority. It may be local, shared, or
network-backed; never choose one for the user.

| Semantic | Required content |
| --- | --- |
| Outcome | Supplied situation or need, intended effect, proof, authority, and boundary. |
| Branch | A distinct surviving contribution, or `unknown`. |
| Move | Linked branch contribution, bounded action, maximum scope, observation source, review point, and frozen expected plus disconfirming readbacks. |
| Result | Immutable observation linked to its move, effect, and next decision. |
| Open link | Orphan, unknown relationship, or blocked dependency. |
| Next | One move, checkpoint repair, block, or `none`. |
| Epitaph | Retired branch, its disconfirming result, and the resurrection condition that would justify a retry. |

When no checkpoint exists, record one outcome. If materially different outcomes
remain plausible or the outcome lacks authority, return
`NEEDS-HUMAN-DECISION`. Reconstruct supplied history as results linked to moves
and branches. Keep missing lineage explicit; never invent retrospective
rationale to complete the record.

Configuration or reconstruction is complete when the outcome, open links, and
latest results are visible in one read.

## Repair an open link

A move without a branch contribution is an orphan. A result without its move or
a branch without a supported outcome contribution remains `unknown`. Repair
only from supplied evidence; otherwise preserve the open link and make
**Next** a repair or block.

Repair is complete when the relationship is supported or its unresolved state
is explicit.

## Resolve a non-binary result

Keep observation separate from interpretation and compare it with both frozen
readbacks.

| Result | Checkpoint action |
| --- | --- |
| Expected | Continue only inside the observed boundary. |
| Disconfirming | Retire the branch and its dependent moves. |
| Mixed | Preserve both signals; narrow or split the branch. |
| Inconclusive | Repair observation only when a different bounded move could change the next decision. |

A readback supported only by the producer's narration is `Inconclusive`, not
success. Resolution is complete when the evidence selects one checkpoint
action.

## Retire, resurrect, or retry

For every retired branch, append an epitaph naming the branch, the result that
killed it, and the changed condition that could justify reconsideration. Delete
the branch and its dependent moves from the active checkpoint.

During Expand, admit a matching retired branch only by naming which resurrection
condition now holds. A retry is a new move, never a rewrite of the old one; add
it only when a changed condition, execution defect, or new observation can
alter the next decision.

This route is complete when dead work cannot return under a new title without
new evidence.

## Dispose and rewrite

Move delivered work and closed decisions to the environment's stores of record.
The checkpoint is not a duplicate store. Epitaphs are the exception because no
other store preserves undelivered learning; keep them append-only and consult
them during Expand rather than ordinary reload.

Dispose of candidate lists, ranking arguments, and spike working context. After
pruning, rewrite the checkpoint to the same size or shorter unless Expand
admitted a new branch, and select exactly one **Next**: move, repair, block, or
`none`.

Disposal is complete when no ended work remains unsorted and the next cycle can
resume from one checkpoint read.
