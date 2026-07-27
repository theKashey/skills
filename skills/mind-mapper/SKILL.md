---
name: mind-mapper
description: Use when a problem, observed effect, or inherited body of work needs one planning graph that can combine real work sequences, parallel contribution branches, uncertain relationships, evidence, actions, and results.
---

# Mind Mapper

Build or reconstruct one living goal graph, then find where it should extend.
Preserve real dependencies, independent contribution paths, and unresolved
relationships without forcing them into one planning shape. Open edges show
what is missing, what is ready, and which next extension can move the wider
goal before implementation details narrow the problem.

Use scientific readback only to decide how a completed move changes the map.
It is branch-update discipline, not a replacement for planning.

## Choose and combine planning shapes

Choose a planning shape for each relationship, not once for the whole graph:

| Condition | Useful view | Relationship asserted |
| --- | --- | --- |
| One move's result is genuinely required before another can begin or be selected. | A linear sequence. | `M1 --unlocks--> M2`; a terminal move has no successor until evidence supports one. |
| Distinct aspects can make independently observable gains toward one outcome without waiting on one another. | Parallel contribution branches; a classic fishbone is one useful rendering. | Separate `contributes to` paths with no invented prerequisite between them. |
| Supplied fragments are connected but their direction, role, or hierarchy is incomplete or cross-cutting. | Associative links; a classic mind map is one useful rendering. | Labeled `related to`, tentative, or unknown edges that do not yet establish contribution, order, or cause. |

Combine the views when the problem requires it. For example, reducing
onboarding failures may have independent instruction, account-access, and
recovery branches. Within account access, locating failures may unlock choosing
an explanation, which may unlock a bounded pilot. Old tickets, an abandoned
experiment, and a metric spike may remain associated fragments until evidence
places them. Keep all of these relationships in the same graph.

## Use one living graph

Use one outcome root and four kinds of descendants:

```text
Epic E1: [outcome and key result]
  Indicator I1 --contributes to--> E1: [attack angle, current signal, target, and gap]
    Hypothesis H1 --explains possible movement in--> I1:
      [why this gap may move and what would refute it]
      Move/task M1 --tests or advances--> H1:
        [bounded action and expected readback]
        Result R1 --is readback for--> M1:
          [actual action, observation, effect, explanation, consequence, next]

History: M1 --produces--> R1 --updates--> H1 and the graph
Extension frontier: [consequential incomplete nodes and open edges]
Action frontier: [ready M# nodes, dependencies, and known remaining count]
```

This is the canonical accountability graph, not a required diagram layout. A
prospective node without a contribution path to the epic is an orphan, not
admitted work. Preserve supplied historical fragments with missing return
edges as reconstruction gaps; do not discard them, count them as ready work,
or invent their lineage. History and forward direction are views over the same
graph, not separate narratives. An open edge marks where that graph may need
another ordinary indicator, hypothesis, move, or result; it is not a fifth node
type.

The extension frontier contains the consequential locations where the map is
missing or weak. The action frontier contains only the dependency-free `M#`
nodes ready to act on selected extension points. Together they describe
forward direction; do not collapse them into a flat task list.

Use the surrounding system's identifiers when they exist. Otherwise use
temporary labels such as `E1`, `I1`, and `M1` only to keep relationships
unambiguous. Allow a shared move to backlink to several indicators when the
contributions are distinct, but name one primary path. In the shorthand
`M# -> H# -> I# -> E1`, arrows mean contribution backlinks, never execution
order. Label dependencies as `requires` or `unlocks`. Reject cycles in
contribution and dependency relationships; allow clearly labeled associative
cross-links that assert neither order nor cause.

## Build, reconstruct, then extend

Use two construction directions and one decision pass on the same graph:

1. **Build outward:** start with the epic and decompose only as far as supported
   into indicator branches, live hypotheses, bounded moves, and result slots.
2. **Reconstruct inward:** start with supplied results, changes, decisions, or
   tasks and trace each one back through its intended hypothesis and indicator
   to the epic. Preserve an explicit unknown node or edge when the connection
   cannot be recovered; do not invent lineage.
3. **Find the extension:** after the outward and inward views agree, scan for
   the first consequential open edge in each branch and select the smallest
   useful additions to the map.

For a new initiative, build outward first. For inherited or partially completed
work, reconstruct inward first, anchor the recovered branches to the epic, and
then build the missing siblings. For a proposed solution, hold it as a
candidate move, reconstruct the hypothesis and indicator it assumes, and build
alternative branches before selecting an extension.

Do not create separate planning, history, and experiment trees. A partial map
is valid when its unknowns and open edges are explicit. Completeness here means
the map can explain its current position and justify its next extension, not
that it predicts every future task.

## Keep implementation behind the map

Start from the user's stated outcome, supplied evidence and constraints, and
any authorized non-code planning or history material. Keep implementation
source out of the reasoning until the graph has an outcome, indicator gaps,
hypotheses, and forward moves with complete backlinks.

Before that gate passes:

- do not open or search source, tests, configuration, generated schemas,
  dependency graphs, or implementation history;
- do not justify work with files, symbols, APIs, frameworks, or inferred
  architecture;
- hold a proposed implementation as a candidate move instead of promoting it
  to the epic, an indicator, or evidence.

Reading or changing code still requires the user's authority. Passing this
skill's gate establishes planning readiness, not permission to inspect or
modify a repository.

## Anchor the map

Freeze one epic at a time. Split materially different outcomes into separate
maps instead of hiding them under one implementation theme.

Record:

- **Outcome:** the user-visible, operational, or organizational change;
- **Key result:** the baseline-to-target movement and horizon, or an observable
  decision state when a numeric target is unsupported;
- **Beneficiary:** who or what experiences the result;
- **Boundary:** relevant constraints and explicit non-goals;
- **Proof:** external evidence that would establish advancement or completion.

The epic passes only when it remains meaningful after replacing the proposed
solution, tool, team, or skill. Do not invent a target to make it measurable.
Keep the code gate closed and surface `NEEDS-HUMAN-DECISION` when materially
different outcomes or success conditions remain plausible.

Orient the graph in three directions:

- **Behind:** supplied moves, decisions, and results that explain the current
  position;
- **Present:** current indicator signals, evidence gaps, live hypotheses, and
  constraints;
- **Forward:** the desired indicator movements, known remaining moves,
  dependencies, extension frontier, and action frontier.

Do not confuse a long history with good orientation. Retain only history that
changes an indicator, hypothesis, constraint, or forward choice.

## Reconstruct the existing map

Turn supplied history into linked observations before inventing new work. For
each completed or attempted move, record:

- **Move:** the intended action and frozen readback, when they are available;
- **Actual:** what was actually done, its boundary, and any material deviation
  from the intended move;
- **Observation:** the signal, source, conditions, sequence or time, and
  guardrails when available;
- **Effect:** whether the observation was `expected`, `disconfirming`, `mixed`,
  or `inconclusive` against the frozen readback;
- **Explanation:** which competing explanations the result distinguishes, or
  `unknown` or `confounded`;
- **Backlink:** the recovered portion of `R# -> M# -> H# -> I# -> E1`, with an
  explicit reconstruction gap at every unavailable layer;
- **Update:** whether the result supported, weakened, refuted, or left the
  hypothesis unresolved;
- **Consequence:** whether to continue, discriminate or replicate, try a
  distinct live hypothesis, retry, retire, block, or ask;
- **Next:** which node states and extension or action frontier entries changed,
  or explicit `none`.

Separate observed results from interpretations. Preserve a result when a
hypothesis fails; mark the hypothesis state instead of rewriting the evidence.
When earlier work lacks a recoverable move, hypothesis, indicator, or epic
contribution, preserve the fragment and mark the exact missing node or edge
instead of inferring a rationale. Put those gaps on the extension frontier;
do not admit descendant forward work until its full epic backlink is supported.
When its expectation, chronology, baseline, or causal boundary is unavailable,
record the gap and classify the effect as inconclusive where necessary. Do not
retrofit a success criterion or manufacture history after seeing the result.

## Build the indicator branches

Create materially different indicator branches beneath the epic. Treat
`indicator` as the common planning role for an attack angle, pillar, SLI, OKR
measure, leading or lagging signal, or qualitative decision criterion; preserve
the user's narrower terminology when supplied.

For each indicator, record:

- **Angle:** the lever, quality, risk, or responsibility it examines;
- **Current:** the latest supported signal and its evidence, or `unknown`;
- **Target:** the desired movement, threshold, or decision boundary;
- **Gap:** the difference between current and target;
- **Contribution:** `I# -> E1` plus why movement here should support the epic;
- **Guardrail:** evidence that would expose gaming, displacement, or a false
  contribution hypothesis.

An activity, deliverable, team, or method is not an indicator until an
observable current-to-target gap and an epic backlink establish its planning
role.

When a collection of skills, methods, specialties, or workstreams is in scope,
classify every supplied member as a candidate attack-angle capability. Attach
each selected capability to the indicator it can influence and state its
boundary; list an unselected capability with the reason it does not contribute.
Never promote a capability to the epic, treat running it as progress evidence,
or force the collection into a mandatory sequence.

Finish this layer when every indicator has a distinct current state, target,
gap, and contribution backlink, overlapping branches have been merged or
distinguished, and uncovered assumptions remain explicit.

## State the hypotheses

Use hypotheses to connect a gap to possible movement. For each hypothesis,
record:

- **Claim:** why a change or discovery could move one indicator toward target;
- **Evidence:** observations for and against the claim;
- **Discriminator:** the strongest live competing explanation and the
  observation that would distinguish it, or `unknown`;
- **Falsifier:** a result that would materially weaken or refute it;
- **State:** `untried`, `supported`, `weakened`, `refuted`, or `unresolved`;
- **Backlink:** `H# -> I# -> E1`.

Keep competing hypotheses when they predict different results or moves. Merge
ones that predict the same forward choice. Never promote a surviving
hypothesis to fact merely because no alternative is currently visible.

## Derive the smaller moves

Turn each live hypothesis into the smallest useful discovery, decision, or
delivery moves. A move is also the neutral task unit; the procedure does not
require a particular ticket or specification type. Before code inspection,
describe the outcome or evidence sought rather than predicted implementation
edits.

For every move, record:

- **Action:** one bounded action and its maximum authorized scope;
- **Supports:** `M# -> H# -> I# -> E1`, including additional genuine backlinks;
- **Purpose:** whether it tests the hypothesis, closes an evidence gap, or
  advances the indicator;
- **Readback:** the done signal, expected and disconfirming effects, conditions
  that would make the result mixed or inconclusive, and review point;
- **Decision rule:** what would permit continuation, an informative retry or
  alternative, or retirement, within any attempt, time, cost, and safety bound;
- **Order:** prerequisites and whether it can run in parallel with other moves;
- **State:** `conditional`, `planned`, `active`, `done`, `blocked`, or
  `retired`; use `conditional` only when a named future result or decision would
  admit the move, and record that activation condition;
- **Code question:** the implementation question to ask after the gate, or
  `none` when code is irrelevant.

Create an implementation-discovery move when the location or mechanism is
unknown. Do not inspect code first merely to make the move sound concrete.
Reject moves whose only result is using a method, producing activity, or
completing code without an indicator-level readback.

Count the known forward inventory by branch and state. Report the minimum known
remaining moves, not a fabricated final total: results may refute hypotheses or
expose new work. Mark a branch `unbounded` when no evidence supports a finite
inventory. Count each shared move once; include `planned`, `active`, and
`blocked` moves in the remaining total and report their states separately.
Report `conditional` moves separately from the minimum unconditional count.
These states are disjoint: when its activation condition occurs, relabel a
conditional move before counting it as planned, active, or blocked.

## Find where to extend

Scan every branch from the epic toward its leaves and mark its first
consequential incomplete node or open edge:

- **Coverage:** an epic condition has no indicator branch.
- **Lineage:** supplied work or a result has no supported path back to the epic.
- **Understanding:** an indicator lacks a supported current state, target,
  contribution, guardrail, or live hypothesis.
- **Choice:** competing hypotheses lack evidence or a discriminator that would
  change the next decision.
- **Action:** a live hypothesis has no bounded move with a frozen readback.
- **Evidence:** a completed move has no result or closed readback.
- **Dependency:** a useful move is blocked or conditional on an unresolved
  node, result, or decision.

Do not extend below an unsupported parent merely because a task is easy to
name. Repair a missing backlink, indicator, or hypothesis from supplied
evidence before adding descendant moves. Keep an explanation gap open when
knowing why would not change the next decision; scientific completeness is not
a reason to grow the map.

Rank extension points by epic consequence, size of the indicator gap,
uncertainty reduced, dependency readiness, and bounded cost or risk. Prefer an
addition that either advances a consequential indicator or distinguishes
forward choices. Apply map-only repairs immediately; represent executable
extensions as ordinary `M#` nodes with complete backlinks.

Keep the ranked open locations as the **extension frontier**. Select every
dependency-free move admitted by that scan as the **action frontier**. State:

- the open node or edge and why it matters now;
- the ordinary node or backlink that will extend it;
- which moves can run in parallel or must wait;
- which result would change the ordering; and
- the known remaining count by branch and state.

Either frontier may contain several independent entries. Do not hide a roadmap
inside one oversized task, mistake the longest branch for the most important
extension, or present a ready task as proof that its parent edge is sound.

## Open the code gate

Report the readiness snapshot before any implementation inspection:

```text
Code gate: OPEN | CLOSED | NOT_APPLICABLE
Epic roots: 1
Indicator branches: [total] ([mapped] mapped / [unmapped] unmapped)
Indicator outcomes: [target met / gap open / unknown / branch retired]
Hypotheses: [untried / supported / weakened / refuted / unresolved]
History: [result count / closed-readback count / completed-move count]
Readback effects: [expected / disconfirming / mixed / inconclusive / open]
Explanation gaps: [unknown / confounded / none]
Forward moves: [planned / active / blocked / conditional / retired]
Minimum unconditional remaining moves: [count or unbounded]
Prospective orphans / reconstruction gaps / cycles: [count / count / count]
Extension frontier: [location, kind, and candidate addition]
Selected map extensions: [open edge -> new or repaired I#/H#/M#/R#]
Action frontier: [ready M# nodes]
Unresolved outcome or contribution decisions: [list or none]
```

Open the gate only when:

1. the single epic states a solution-neutral outcome and external proof;
2. every indicator has a current state, target, gap, contribution, and epic
   backlink;
3. every indicator with an open or unknown gap has at least one live hypothesis
   and a planned move, or an explicit block or decision gap;
4. every prospective move has a bounded action, frozen readback, decision rule,
   state, and complete contribution path; a reconstructed historical move may
   instead carry an explicit unavailable-readback gap without blocking the
   gate;
5. every result in history links through every recoverable layer and marks an
   explicit reconstruction gap at each unavailable layer, while recording its
   actual action, observation, effect, explanation uncertainty, consequence,
   and next edge;
6. every supplied capability in scope is accounted for as a selected or
   unselected attack angle;
7. no pre-gate node depends on source-derived implementation reasoning; and
8. all consequential uncertainty is visible; and
9. the extension scan identifies the extension and action frontiers, or
   explicit `none` when the request ends with the map.

This gate never blocks non-code moves. Mark it `NOT_APPLICABLE` when code is
irrelevant, unavailable, or outside the request. An open gate does not by
itself authorize a mutation.

## Inspect code through a move

After the gate opens, select an active move and state its code question and
scope before searching. Inspect only implementation evidence that can answer
that question.

Attach each finding as evidence or a result on the active move. Represent each
proposal or authorized change as a delivery move with
`M# -> H# -> I# -> E1`, an expected indicator effect, and a disconfirming
readback. Reject or reframe a change that cannot explain this contribution
path.

When code evidence contradicts the map, identify the disproved assumption and
revise the affected node or edge explicitly. Preserve still-supported
ancestors, mark dependent descendants stale, and rerun the readiness gate.
Never silently rewrite the epic to match convenient repository structure.

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
  extension or action frontier entries, or explicit `none`.

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
dependent move states, and the forward count from the result. Set `Next` to the
newly ready action-frontier nodes or explicit `none`, then rerun the extension
scan.

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

Finishing or merging code does not establish any higher-level claim.
When an indicator does not move as predicted, retain the observation, retire
or revise the contribution hypothesis, and renew only the affected branches.

## Return the living map

Render the map in the user's chosen surface. When none is specified, return a
compact labeled graph in the response, not a flat plan or experiment log. Make
the applicable views scannable:

- contribution paths through `E`, `I`, `H`, `M`, and `R`;
- real move sequences labeled `requires` or `unlocks`, including terminal
  points;
- associative cross-links and unresolved relationship or reconstruction gaps;
- history annotations on the affected branches; and
- extension and action frontiers with known remaining counts.

Do not prescribe or create tickets, specifications, files, diagrams, or a
persistence system merely to store the graph.

Backlinks establish accountable lineage. They do not prove that the epic is
valuable, an indicator is causal, a move is sufficient, or an implementation
is correct.
