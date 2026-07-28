# Consume or update a map

Use this procedure after `SKILL.md` selects the consume route because the
supplied graph already has an identifiable outcome root and enough labeled
relationships to audit without inventing structure. Explicit open edges do not
make a graph unusable.

## Reconcile the current graph

Read current task state, dependencies, evidence, and results from their
authoritative sources at the point of use. Mark affected nodes stale when the
current record contradicts the graph; preserve still-supported nodes and
observations.

If the supplied artifact is only unlinked fragments with no recoverable outcome
root, stop and use
[Create or reconstruct a map](create-or-reconstruct.md). If a usable graph has
one or more explicit reconstruction gaps, keep this route and let
[Find where to extend](../SKILL.md#find-where-to-extend) decide whether repairing
one is the most consequential next move.

When no new completed result is supplied, consumption is complete once current
state is reconciled, stale nodes and open edges are explicit, and the graph is
ready for the shared
[extension scan](../SKILL.md#find-where-to-extend).

## Inspect code through a move

Use this branch only after the shared code gate is open and the user has
authorized implementation inspection. Select an active move and state its code
question and scope before searching. Inspect only implementation evidence that
can answer that question.

Attach each finding as evidence or a result on the active move. Represent each
proposal or authorized change as a delivery move with
`M# -> H# -> I# -> E1`, an expected indicator effect, and a disconfirming
readback. Reject or reframe a change that cannot explain this contribution
path.

When code evidence contradicts the map, identify the disproved assumption and
revise the affected node or edge explicitly. Preserve still-supported
ancestors, mark dependent descendants stale, and rerun the shared
[code gate](../SKILL.md#open-the-code-gate). Never silently rewrite the epic to
match convenient repository structure.

After recording the inspection evidence, return to the shared
[extension scan](../SKILL.md#find-where-to-extend) and
[living-map return](../SKILL.md#return-the-living-map).

## Update the map from a completed move

Use a scientific readback to turn a completed move into a result and decide
which nodes or edges change. This maintains and extends the map; it does not
define a parallel experiment workflow or require every move to prove a causal
mechanism.

Append the result before releasing dependent moves. Do not overwrite the
move's original expectation. Record:

- **What we did:** the actual action, boundary, and deviations;
- **What happened:** the observations and guardrails, separate from
  interpretation;
- **Did the expected effect appear?:** `expected`, `disconfirming`, `mixed`, or
  `inconclusive` against the frozen readback;
- **Do we know why?:** which alternatives the evidence distinguishes, or
  `unknown` or `confounded`;
- **What follows?:** the hypothesis update, branch decision, and changed
  extension entries or selected next move, or explicit `none`.

Treat “worked” as a bounded readback, not a universal verdict. An expected
effect with an unknown explanation is an association under the observed
conditions, not proof of cause or safe generalization. A result with invalid
execution, insufficient sensitivity, missing comparison, or a material
confound is inconclusive where those gaps prevent the frozen readback.
Treat an explanation as distinguished only relative to the named next decision,
never as universal causal truth.

Use the effect and explanation together:

| Readback | Required graph action |
| --- | --- |
| Expected effect; alternatives distinguished | Support the hypothesis only within the observed boundary. Continue only to the level evidenced. |
| Expected effect; explanation unknown or confounded | Keep the mechanism uncertain. If scaling, transfer, safety, or an irreversible decision depends on why, add a discriminating or bounded replication move; otherwise continue only within observed conditions and guardrails. |
| Disconfirming effect under valid conditions, with any explanation status | Weaken or refute the hypothesis against its frozen falsifier and retire its unexecuted dependent moves. Select a different live hypothesis, or add a bounded explanation move only when its possible results separate plausible explanations and would change a consequential decision; otherwise retire the branch, block, or ask. |
| Mixed effect | Preserve favorable, unfavorable, and guardrail signals. Narrow the claim or split competing hypotheses; do not cherry-pick the favorable observation. |
| Inconclusive effect | Keep the hypothesis unresolved. Repair execution or observation only when a bounded move can make the next result interpretable. |

A disconfirming effect can falsify an operational prediction while its
underlying mechanism remains unknown. Preserve that explanation gap instead of
using it to keep the falsified prediction alive.

A retry is a new `M#`, never a rewrite of the old move. Admit it only when it
is a planned replication with a predeclared threshold, or it changes a named
condition, execution defect, or observation whose outcomes distinguish live
hypotheses. Keep it within explicit attempt, time, cost, and safety bounds.
Reject an unchanged “try again” whose possible outcomes would not change the
next decision.

Keep an executed move `done`. Retire its unexecuted dependents and stop
selecting its tactic or hypothesis branch when a valid result meets its frozen
falsifier, an indicator guardrail or safety bound is breached, the review bound
expires without discriminating evidence, or no live hypothesis predicts a
useful different result. Retiring one tactic does not retire its indicator or
epic; an open epic does not justify endless retries.

After deciding, update the hypothesis state, the indicator's current signal,
and dependent move states from the result. Set `Next` to the newly selected
move or explicit `none`, then rerun the extension scan against current work
state.

When the epic, indicator, or hypothesis changes, mark affected descendants
stale before relinking them. Preserve still-supported history so the current
direction remains explainable. A correction supersedes an earlier result with
an explicit edge; it does not erase it.

Keep completion claims at their own level:

- **Move done:** its result exists.
- **Readback closed:** its actual action, observation, effect, explanation
  uncertainty, consequence, and next edge are recorded; dependent moves were
  not released first.
- **Hypothesis resolved:** a result supports, weakens, or refutes it enough to
  select a different forward choice.
- **Indicator branch mapped:** its current state, target, gap, hypothesis, and
  forward move or explicit block are present.
- **Indicator target met:** its signal reaches its stated target.
- **Indicator branch retired:** its decision owner deliberately stops pursuing
  it with evidence; this is not target achievement.
- **Epic reached:** its external proof meets the key result.

An inconclusive readback can close when its uncertainty and next decision are
explicit. Closure means the decision loop is complete, not that certainty was
achieved.

Finishing or merging code does not establish any higher-level claim. When an
indicator does not move as predicted, retain the observation, retire or revise
the contribution hypothesis, and renew only the affected branches.

Result update is complete when the result and closed readback exist, affected
states and edges reflect the observation without erasing history, dependent
moves were not released early, and uncertainty plus the next decision are
explicit. Return to
[Find where to extend](../SKILL.md#find-where-to-extend).
