# Cast the reader

Use casting when a reader-facing surface is new or substantially reworked, or
when the proposed reader, goal, subject, or surface is in doubt. A bounded edit
with an explicit, unchallenged story contract does not need to recast it.

Casting is allowed to reject the brief. Its purpose is not to make prose fit a
supplied persona; it is to discover whether a document can help a real entrant
make a decision the project has reason and authority to influence.

## Keep the layers separate

A content persona is a durable reader class supported by recurring evidence. A
class groups entrants with materially similar starting context, decision
rights, trust or authority boundary, and generic goal. It is not a biography,
job title, skill route, page type, workflow phase, or individual task.

Keep these lower layers out of the class definition:

- **Modifier:** a proven condition such as selective context, decision
  altitude, or a trust boundary that changes the content treatment.
- **Episode:** the task or question that brought this entrant here now.
- **Reader goal:** why the entrant wants to act or decide in this episode.
- **Authorial goal:** why the project chooses to address that goal at all.
- **Surface:** the established or proposed place where the intervention occurs.

Human versus coding agent is usually a modifier, not a class. Engineer or
architect may describe decision altitude, not identity. Treat every proposed
label as a hypothesis until it survives the procedure below.

## Scaffold the goals

Before drafting, trace the proposed document through this chain:

| Layer | Question |
| --- | --- |
| Project outcome | What real-world change does the project have reason to pursue? |
| Subject promise | What outcome can the product, system, or governed subject actually support? |
| Reader goal | What does the entrant need to decide or accomplish? |
| Authorial goal | Why does the project want this document to tell this reader this story? |
| Document intervention | What belief, decision, or safe action can this surface change? |
| Evidence | What observation would show the intervention worked or that an earlier layer is wrong? |

Do not repair a broken link by polishing the final document. A mismatch may
mean the reader, goal, surface, subject, or document itself is wrong.

## Run the casting procedure

### 1. Frame the authorial wager

Record only what can control the next decision:

- subject hypothesis and supported promise;
- observed problem or pressure;
- affected entrant and stakes;
- desired project outcome and authorial goal;
- evidence, authority, and important non-fit.

This is a wager, not a conclusion. Existing copy proves what a surface says,
not that its reader or intent is correct.

### 2. Audition real episodes

Collect episodes from repository entry points, support or issue evidence,
examples, public contracts, tests, navigation, explicit product decisions, and
observed reader paths. For each material episode, record:

- entrant and trigger;
- context actually available at entry;
- decision or action they control;
- authority or trust boundary;
- stakes and smallest successful outcome;
- observed frequency and measurement window when available, otherwise an
  explicitly unmeasured expected frequency with its decision source;
- next route and supporting evidence.

Do not create a class from one skill, package, page, workflow stage, current
heading, or job title. Mark absent evidence as unknown rather than filling it
with demographics or plausible preferences.

### 3. Call the intervention gate

Test the episode before clustering it:

1. Is the entrant evidenced and reachable at this surface?
2. Can that entrant make the intended decision or action?
3. Will the necessary context and proof be available before that decision?
4. Can the subject truthfully support the desired outcome and boundary?
5. Is documentation capable of changing the result?
6. Is this the established or authorized owner for the intervention?

Return one outcome and follow it; do not draft around a failed gate.

| Outcome | Required next move |
| --- | --- |
| `PROCEED` | Cast the reader and form the story contract. |
| `RECAST_READER` | Replace the assumed entrant or decision holder, then audition again. |
| `REVISE_GOAL` | Change the reader or authorial goal to one supported by the project outcome. |
| `CHANGE_SURFACE` | Route the intervention to the owner the entrant can actually reach. |
| `CHANGE_SUBJECT` | Correct the product, offering, or idea before asking prose to carry it. |
| `NO_DOCUMENT` | Add nothing because no material document intervention remains. |
| `NEEDS_HUMAN_DECISION` | Stop at the smallest missing product, editorial, or ownership choice. |

When several conditions fail, return the outcome for the earliest broken
causal layer and treat later failures as consequences to reassess after that
shift:

1. Resolve the project outcome and subject promise first. Use
   `CHANGE_SUBJECT` when an authorized outcome requires the subject to change;
   use `REVISE_GOAL` when the subject's established boundary governs and the
   proposed goal overshoots it; use `NEEDS_HUMAN_DECISION` when authority does
   not choose between those paths.
2. Then use `RECAST_READER` when the wrong decision holder was assumed.
3. Then use `CHANGE_SURFACE` when the intervention survives but its owner or
   reachable entry point is wrong.
4. Use `NO_DOCUMENT` when the upstream layers are sound but prose has no
   material work left to do.

Record secondary consequences, but do not turn them into parallel drafting or
separate clarification rounds before the primary shift is resolved.

### 4. Freeze and prioritize the smallest cast

Cluster only episodes that share durable starting context, decision rights,
trust or authority boundary, generic goal, and materially similar needs for
proof, boundary, density, and next route.

- **Merge** candidates when those properties and their authoring consequences
  are materially equivalent.
- **Split** only when recurring evidence shows incompatible context, authority,
  trust, success condition, density, proof, or route that progressive
  disclosure cannot serve safely.
- **Reject** a candidate when it merely renames a skill, surface, package,
  workflow phase, task, or profession; when swapping its label produces no
  content decision; or when using it creates per-class variants of the same
  truth.

A valid class changes the assumed starting point, ordering, explanation
density, proof, boundary, or next route while leaving facts and guarantees
unchanged. If the cast cannot admit a recurring entrant without distortion, or
causes contradictory promises or one bespoke narrative per route, recast it.

After the classes survive, rank their expected service frequency for the
project or surface:

- Prefer an observed count or rate with its source and window. Otherwise use a
  qualitative band such as `high`, `medium`, `low`, or `unknown`, label it as
  expected rather than measured, and name the decision source.
- Choose `N` as the smallest highest-frequency set that deserves compact direct
  paths. Stop adding classes when the next class's distinct need can be reached
  through one descriptive route without weakening shared truth or a safety
  boundary.
- Route lower-frequency deltas to an existing or authorized deeper owner.
  Promote one only when delaying its necessary safety boundary behind that
  route would make action unsafe, and record the exception.

Frequency selects exposure order and detail, never facts or guarantees. Keep
one primary class and through-line per surface; project-wide top-`N` support
does not require every page to tell `N` complete stories.

### 5. Form and rehearse one story contract

After `PROCEED`, record:

```text
Primary class:
Frequency evidence and direct/deeper disposition:
Proven modifier, if any:
Task-local episode:
Reader goal:
Authorial goal and decision source:
Intended reader change:
Evidence and boundary:
Completion route:
Expected readback:
Disconfirming readback:
```

Use the smallest opening-and-heading slice described in
[content architecture](content-architecture.md#authorial-intent-and-story-contract)
to test the contract. Classify the readback as expected, disconfirming, mixed,
or inconclusive. When it disconfirms the plan, return to the earliest wrong
layer in the goal scaffold; do not preserve the original deliverable by force.

## Persist only earned cast context

Keep a cast task-local by default. Persist it only when the project explicitly
authorizes a durable owner and recurring evidence makes future selection safer.
The user or project chooses `.agents` or `.context-docs`; never create a persona
catalog at repository root.

Use a compact `CONTENT-PERSONAS.md` as the selector and evidence boundary.
Record each retained class's frequency evidence or explicitly unmeasured band,
direct/deeper disposition, and canonical route. Keep the top-`N` selector
compact. Link a subclass or modifier behind a direct condition only when its
recurring content delta no longer fits there; a child contains only what
differs from its parent. Do not create one record per skill, package, surface,
task, or workflow, and do not load every detail because one applies.

Revisit or retire a durable class when entry evidence, decision rights, trust
boundaries, supported outcomes, or authoring consequences change. A cast is
scaffolding for a better document decision, not a new source of product truth.
