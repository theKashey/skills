---
name: read-the-terrain
description: Use when uncertain or changing work needs a bounded next move, a fresh signal, or a check that an artifact still addresses the recipient's problem.
---

# Read the Terrain

Turn an uncertain situation into one justified move and one useful readback.
Treat orientation as a living model of the environment, not as a planning
phase to finish once.

## Build the terrain card

Capture only fields that can change the next move:

```text
Aim: [user-visible change or decision]
Field: [relevant boundary, constraints, hazards, and time window]
Roles: [intended beneficiary / actor or solver / decision owner]
Signals: [observed facts / interpretations / consequential unknowns]
Regime: [clear / complicated / complex / chaotic / unresolved]
Pattern: [recognized situation, cues, anomaly, and simulated consequence—or none]
Move: [action, maximum scope, and safety or rollback]
Readback: [expected signal, disconfirming signal, and review point]
```

Keep observations distinct from interpretations. A symptom, a correlation, and
a cause occupy different places on the card. Omit history, context, and options
that cannot alter the current move.

When a fresh signal contradicts the card—or the Move changes while Signals do
not—mark the affected fields stale instead of defending them. Preserve
still-supported observations; rebuild the Aim, Regime, Pattern, or Move that
the new signal disproved.

## Choose the causal regime

Classify the present relationship between action and outcome. Do not classify
the difficulty of the task, the competence of a person, or the permanent nature
of a system.

| Regime | What the signals support | Move shape |
| --- | --- | --- |
| **Clear** | A stable, visible relationship and a proven response | Apply the known response; watch for exceptions; verify |
| **Complicated** | A relationship exists but needs deliberate comparison | Separate plausible explanations by their predictions; choose and verify |
| **Complex** | Interaction changes the situation and useful causality appears mainly after intervention | Select bounded safe-to-fail probes; amplify useful patterns; dampen harmful ones |
| **Chaotic** | Harm or instability prevents a trustworthy causal reading | Contain first; establish constraints and observability; then reclassify |
| **Unresolved** | No discriminating signal exists or coupled parts fit different regimes | Stage the cheapest useful signal or split the field into separately classifiable parts |

Record the nearest plausible alternative when confidence is weak. Choose a move
safe across both regimes or gather a signal that separates them. Treat a regime
shift as the result of the move: newly stable signals can narrow the next
method, while containment can restore a readable field.

## Separate plausible explanations

Use this procedure for Complicated terrain and whenever recognition leaves more
than one credible Pattern:

1. Name two to four explanations that fit the observed Signals. Merge
   explanations that predict the same next state.
2. For each explanation, state one near-term prediction and one observation
   that would count against it.
3. Select the lowest-cost signal whose possible outcomes divide the
   explanations. Reject a signal when every possible result leaves the choice
   unchanged.
4. Make obtaining that signal the Move, then retire explanations contradicted
   by its result.
5. Continue when one remaining explanation selects a distinct safe Move, or
   when all remaining explanations support the same bounded Move. Otherwise
   mark the Regime Unresolved.

A surviving explanation is still a hypothesis. Do not call it a cause merely
because alternatives were eliminated.

## Audit recognition

Use recognition to propose a move when relevant experience or repeated evidence
makes a familiar pattern plausible. Do not use it as evidence by itself.

1. Name the cues that evoke the pattern.
2. State what should happen next if the pattern is correct.
3. Find one anomaly, missing cue, or competing pattern.
4. Mentally run the first plausible move through the actual constraints.
5. Keep it only if it stays within authority, has a recoverable path, and
   produces a readable result.

When the situation is novel, high-consequence, or weakly observed, replace
recognition with the explanation-separation procedure or a safe-to-fail probe.
When the simulation fails, discard the move rather than rationalizing the
pattern.

## Take a second-order action

Use an isolated problem check when a candidate move, decision, plan, or artifact
exists and at least one condition holds:

- it is about to cross a costly, irreversible, or trust boundary;
- the candidate may be a solution searching for a problem;
- the current context keeps confirming its own framing;
- the Aim cannot be distinguished from the producer's explanation of it.

Treat this as an action that produces a new observation, not as another pass of
private reflection:

1. Freeze the exact candidate the recipient would receive.
2. Separately freeze the producer-side comparison baseline: the current Aim,
   relevant Field and Signals, Move boundary, and Readback. Keep it outside the
   reader context.
3. Instantiate an isolated reader whose entire context is the candidate and the
   neutral question below.
4. Give it only the candidate and this neutral question:

   ```text
   From the candidate alone, infer:
   - What change is this candidate trying to produce?
   - What present friction or risk makes that change worthwhile?
   - What conditions must already be true for this approach to make sense?
   - What would a recipient observe if the candidate had its intended effect?
   - Which consequential choice is left implicit or unresolved?
   ```

5. Give no Aim, terrain card, producer baseline, rationale, source facts, validation
   results, expected answer, or intended repair. The reader reviews only; it
   does not edit or consult other sources.
6. Back in the producing context, compare the isolated inference with the
   frozen baseline: claimed change against Aim; assumed friction and conditions
   against Field and Signals; recipient-visible evidence against Readback; and
   the implicit choice against the Move boundary.

Classify the readback:

- **Aligned:** the reconstructed change, terrain assumptions, visible effect,
  and decision boundary support the card; continue.
- **Misaligned:** the candidate implies a different change, terrain, effect, or
  boundary; stop and rebuild the stale fields.
- **Ambiguous:** the candidate leaves a consequential assumption or choice
  unreadable; repair the candidate or ask its owner.
- **Unvalidated:** an isolated reader was required but unavailable; do not
  present alignment as established.

A repaired candidate is a new target. Use a newly isolated reader and do not
provide the prior verdict or repair story.

This check establishes only whether the candidate independently reconstructs
the same problem terrain. It does not establish that the friction is real, the
candidate works, requirements are covered, or downstream consequences are
acceptable.

## Expose opaque execution

Separate two evidence gaps:

- **Problem opacity:** the candidate does not expose its claimed change,
  situational assumptions, recipient-visible effect, or consequential choice.
  Use the isolated second-order action.
- **Execution opacity:** an outcome can be seen, but the divergence inside
  control, data, state, ordering, or time remains hidden. Split the plausible
  transition stories with one observable result.

For execution opacity, make a **signal split** the Move:

1. Sketch two or three short transition stories from the same visible
   precondition to the symptom. Each story must fit current Signals and differ
   from the others in an event, value, state, order, or timing.
2. Find one point where those stories predict incompatible observations.
   Choose the least disruptive way to see only that difference.
3. Observe the affected passage at that point within the Move boundary.
4. If the result leaves the stories tied, add a contrasting passage only when
   the stories predict different changes under that contrast. Otherwise choose
   a new split point instead of collecting more detail.
5. In Orient, delete stories contradicted by the result. Do not promote a
   surviving story from hypothesis to cause without evidence of its mechanism.
6. Restore anything changed solely to make the split visible, then replay the
   passage. If visibility changed the behavior, record the disturbance as a
   Signal and discard the causal reading.

Revise the Regime or Pattern only when the split eliminates a plausible story
or exposes a previously hidden transition. Otherwise the Move produced no new
Signal and the loop must renew with different predictions.

## Run the outer OODA loop

Cycle quickly enough that the card remains current, not so quickly that action
outruns observation:

1. **Observe:** acquire the current signal, including the effect of the previous
   move.
2. **Orient:** update only the terrain-card fields changed by that signal.
3. **Decide:** select the smallest regime-appropriate move that can advance the
   Aim or improve the next orientation.
4. **Act:** execute within the Move boundary.
5. **Read back:** compare external state with both expected and disconfirming
   signals before another action.

Set the review point before acting. Use elapsed time, attempt count, state
transition, budget, or a specific measurement—whichever becomes stale first.
An action without readback is an open loop.

Observe may consume the direct result of an ordinary Move, the isolated
problem check, or the opaque-execution evidence move. If none produces a
discriminating signal, the loop has not completed; narrow the question or
change the observation point before acting again.

## Select the move

Prefer a reversible, evidence-producing move unless:

- the Clear regime supplies a known response;
- the Chaotic regime requires immediate containment; or
- delay is itself the larger irreversible choice.

Use one move, not a disguised roadmap. For Complex terrain, a move may be a
small portfolio of probes only when comparison is the evidence being sought.
For Complicated terrain, separate the explanations against available Signals
before creating a probe.

When a Move contains specialized execution, keep it inside the stated scope
and require its observable result to return under Signals. Do not let naming a
method stand in for taking the Move or reading it back.

An isolated second-order check is itself a valid Move: it changes what is known
about problem alignment even when it does not change the candidate.

## Close or renew the loop

Close the loop only when external evidence shows the Aim was reached. Otherwise
renew it with the changed signal, updated regime, and next review point.

Stop and ask for direction when the Aim has materially different plausible
meanings or the Move exceeds available authority. Escalate when safety bounds
break. Do not widen the Field merely to preserve a failing Pattern.

Keep the visible response proportional to the decision. Show the terrain card
when its distinctions help the user evaluate the move; for routine work, act
through it without turning the frameworks into the deliverable.
