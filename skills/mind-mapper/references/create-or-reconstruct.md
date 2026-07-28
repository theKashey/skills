# Create or reconstruct a map

Use this procedure after `SKILL.md` selects the create route because no usable
living graph exists, or because supplied work and history are still unlinked
fragments. This route constructs accountable lineage; it does not update an
already admitted move from a new result.

## Choose the construction direction

Use two construction directions on the same graph:

1. **Build outward:** start with the epic and decompose only as far as supported
   into indicator branches, live hypotheses, bounded moves, and result slots.
2. **Reconstruct inward:** start with supplied results, changes, decisions, or
   tasks and trace each one back through its intended hypothesis and indicator
   to the epic. Preserve an explicit unknown node or edge when the connection
   cannot be recovered; do not invent lineage.

For a new initiative, build outward first. For inherited or partially completed
work, reconstruct inward first, anchor the recovered branches to the epic, and
then build the missing siblings. For a proposed solution, hold it as a
candidate move, reconstruct the hypothesis and indicator it assumes, and build
alternative branches before selecting an extension.

Do not create separate planning, history, and experiment trees. A partial map
is valid when its unknowns and open edges are explicit. Completeness here means
the map can explain its current position and justify its next extension, not
that it predicts every future task.

## Anchor the map

Freeze one job epic at a time. Keep materially different job outcomes in
separate subgraphs and connect them at product or work level instead of hiding
them under one implementation theme.

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
- **Forward:** the desired indicator movements, real dependencies, extension
  frontier, and selected next move.

Do not confuse a long history with good orientation. Retain only history that
changes an indicator, hypothesis, constraint, or forward choice.

## Reconstruct supplied work and history

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
- **Next:** which node states, open edges, or selected next move changed, or
  explicit `none`.

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

Create the materially different directions required by the focused job beneath
its epic. Treat `indicator` as the common planning role for an attack angle,
pillar, SLI, OKR measure, leading or lagging signal, or qualitative decision
criterion; preserve the user's narrower terminology when supplied.

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

A fishbone direction is required only when the job's completion contract makes
it necessary. Required directions may advance independently, but the job does
not complete until each reaches its criterion or the decision owner explicitly
waives it. Keep optional ideas and unexplained associations at product level
or as conditional moves instead of presenting them as required bones.

When a collection of skills, methods, specialties, or workstreams is in scope,
classify every supplied member as a candidate attack-angle capability. Attach
each selected capability to the indicator it can influence and state its
boundary; list an unselected capability with the reason it does not contribute.
Never promote a capability to the epic, treat running it as progress evidence,
or force the collection into a mandatory sequence.

Finish this layer when every completion-required direction is represented or
marked unknown, every represented indicator has a distinct current state,
target, gap, and contribution backlink, overlapping branches have been merged
or distinguished, and uncovered assumptions remain explicit.

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

Creation is complete when the epic passes, every completion-required direction
is represented or marked unknown, every open or unknown gap has a live
hypothesis and bounded move or an explicit block, and every historical fragment
has supported lineage or an exact reconstruction gap. Return to
[Find where to extend](../SKILL.md#find-where-to-extend).
