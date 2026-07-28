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

## Run the mapping loop

1. **Set the decision.** State the outcome, proof, boundary, and question the
   map must help decide. If materially different outcomes remain plausible,
   stop with `NEEDS-HUMAN-DECISION`.
2. **Read the available work record.** Use the user's current planning,
   history, evidence, and work systems as sources of truth. Preserve their
   identifiers and read current dependencies, status, and task detail at the
   point of use. Do not copy a task roster, ready-work list, or remaining-work
   count into the map.
3. **Choose one operating route.**
   - When no usable living graph exists, or supplied work and history are
     unlinked fragments, read
     [Create or reconstruct a map](references/create-or-reconstruct.md).
   - When a graph already has an identifiable outcome root and labeled
     relationships, read
     [Consume or update a map](references/consume-or-update.md) to reconcile
     current state or apply a supplied result.
   - When the request spans both, complete creation first, return here, and
     load the consume route only for the remaining work.
4. **Move through the work-shape ladder.** At product or work scope, connect
   job subgraphs and cross-cutting context as a mind map. For the focused job,
   expose every direction required by its completion contract as a fishbone.
   Within a direction, express only genuine unit dependencies as a linear
   sequence.
5. **Audit the graph.** Label contribution, requirement, evidence,
   contradiction, and association edges explicitly. Reject cycles in
   contribution and dependency edges. Keep unsupported parents, uncovered job
   directions, and unresolved relationships on the extension frontier.
6. **Choose one next extension.** Rank open edges by consequence, uncertainty
   reduced, dependency readiness, and bounded cost or risk. Select the
   smallest map repair or work move whose result can change the decision. Use
   the current work system when it supplies readiness; the map does not become
   a second queue.
7. **Gate implementation.** Before inspecting implementation, require the
   focused outcome, required directions, live hypothesis, bounded move,
   contribution backlink, and frozen readback to pass the code gate. Passing
   the gate does not authorize access or mutation. When inspection is
   authorized, follow the code-inspection branch in
   [Consume or update a map](references/consume-or-update.md).
8. **Read back and return.** When a completed result is supplied, follow the
   result-update branch in
   [Consume or update a map](references/consume-or-update.md). Append without
   rewriting its expectation, update only affected nodes and edges, rerun the
   extension scan, and return the current map plus the selected next move or
   explicit block.

The map is usable when the current decision is explicit, every admitted move
has a supported path to its job outcome, every completion-required job
direction is represented or marked unknown, all uncertain cross-links are
labeled, and one bounded next move or decision block is visible.

## Apply the work-shape ladder

Use the level of work to choose the primary view:

| Working level | Primary view | Operating rule |
| --- | --- | --- |
| Product or body of work | Mind map | Connect job subgraphs, outcomes, evidence, constraints, history, and unresolved cross-cutting relationships. Label the edges; layout does not imply order or cause. |
| Job | Fishbone | Put the job outcome on the spine and expose the distinct directions its completion contract requires. Directions may advance in parallel, but parallel does not mean optional. |
| Unit of work | Linear sequence | Order only steps or moves with a real `requires` or `unlocks` dependency. A unit with no such dependency remains one bounded move. |

Start at the level named by the user. Descend when the current node is too
broad to act on; ascend when a unit lacks a supported reason or a job lacks
product context. Do not flatten the three levels into one task tree. The ladder
selects the working view; evidence still determines every edge type.

## Use one living graph

Within each focused job subgraph, use one outcome root and four kinds of
descendants:

```text
Product/work context: [labeled links among job subgraphs and shared context]
Job/Epic E1: [outcome and key result]
  Indicator I1 --contributes to--> E1: [attack angle, current signal, target, and gap]
    Hypothesis H1 --explains possible movement in--> I1:
      [why this gap may move and what would refute it]
      Move/task M1 --tests or advances--> H1:
        [bounded action and expected readback]
        Result R1 --is readback for--> M1:
          [actual action, observation, effect, explanation, consequence, next]

History: M1 --produces--> R1 --updates--> H1 and the graph
Extension frontier: [consequential incomplete nodes and open edges]
Selected next move: [one bounded M# or map repair, derived from current evidence]
```

This is the canonical accountability subgraph, not a required diagram layout.
A prospective node without a contribution path to its job epic is an orphan,
not admitted work. A job without a labeled relationship to the product or work
context is a product-level gap. Preserve supplied historical fragments with
missing return edges as reconstruction gaps; do not discard them, treat them
as ready work, or invent their lineage. History and forward direction are
views over the same graph, not separate narratives. An open edge marks where
that graph may need another ordinary indicator, hypothesis, move, result, or
job relationship; it is not a new task type.

The extension frontier contains the consequential locations where the map is
missing or weak. It is not a duplicate queue. Derive the selected next move
from current evidence, dependencies, and authoritative work state each time
the map is used.

Use the surrounding system's identifiers when they exist. Otherwise use
temporary labels such as `E1`, `I1`, and `M1` only to keep relationships
unambiguous. Allow a shared move to backlink to several indicators when the
contributions are distinct, but name one primary path. In the shorthand
`M# -> H# -> I# -> E1`, arrows mean contribution backlinks, never execution
order. Label dependencies as `requires` or `unlocks`. Reject cycles in
contribution and dependency relationships; allow clearly labeled associative
cross-links that assert neither order nor cause.

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

Keep the ranked open locations as the **extension frontier**. Select one
bounded map repair or move from the highest-consequence ready location. State:

- the open node or edge and why it matters now;
- the ordinary node or backlink that will extend it;
- the actual prerequisite or current work-state evidence that makes it ready;
- which result would change the ordering; and
- the frozen readback and decision rule.

The extension frontier may contain several independent entries; the selected
next move is singular. When comparison itself is the evidence sought, represent
that comparison as one bounded move. Do not hide a roadmap inside one oversized
task, mistake the longest branch for the most important extension, or present a
ready task as proof that its parent edge is sound.

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
Prospective orphans / reconstruction gaps / cycles: [count / count / count]
Extension frontier: [location, kind, and candidate addition]
Selected map extensions: [open edge -> new or repaired I#/H#/M#/R#]
Selected next move: [M# or map repair / readiness evidence / frozen readback]
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
9. the extension scan identifies the extension frontier and one selected next
   move, or explicit `none` when the request ends with the map.

This gate never blocks non-code moves. Mark it `NOT_APPLICABLE` when code is
irrelevant, unavailable, or outside the request. An open gate does not by
itself authorize a mutation.

## Preserve the readback boundary

Append a completed result before releasing dependent moves, never rewrite its
frozen expectation, and keep observation separate from interpretation. Update
only affected nodes and edges, preserve disconfirming evidence and explicit
uncertainty, then rerun the extension scan. The consume route owns the detailed
readback, retry, retirement, and completion rules.

## Return the living map

Render the map in the user's chosen surface. When none is specified, return a
compact set of tables for structured facts and short prose for judgment, not a
flat plan, mixed diagram styles, or experiment log. Make the applicable views
scannable:

- contribution paths through `E`, `I`, `H`, `M`, and `R`;
- real move sequences labeled `requires` or `unlocks`, including terminal
  points;
- associative cross-links and unresolved relationship or reconstruction gaps;
- history annotations on the affected branches; and
- the extension frontier and one selected next move with its readback.

Do not prescribe or create tickets, specifications, files, diagrams, or a
persistence system merely to store the graph. When an existing work system
owns identifiers, status, dependencies, or readiness, point to its current view
instead of reproducing it.

Backlinks establish accountable lineage. They do not prove that the epic is
valuable, an indicator is causal, a move is sufficient, or an implementation
is correct.
