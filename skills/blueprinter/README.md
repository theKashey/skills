# Blueprinter

Blueprinter turns a change request into a blueprint before the agent changes
code, checks it, and builds it. **Orient** builds a guided, task-shaped
understanding of the existing system: what already does part of the job, and
the vertical slices the task touches, traced as far as the task needs.
**Operate** then proposes the surgery on those slices and
places every part of the change on one block map: what already exists and
stays, what must be modified, what must be built because nothing supports it,
what must be brought in from outside, what must be removed, and which existing
documents govern it. Each amendment is one block's direction, stated in the
application's concepts; the diff that carries it out is checked against it.
The developer corrects that structure one block at a time while the whole
block map stays in view, and the same map then tracks the change as it is
built, block by block, until every block has landed.

It pays most on work that crosses several parts of a system: a new
capability, a rule that touches more than one owner, a change whose right
location is not obvious. A small task gets a small orientation, not a
different procedure.

## Why the skill exists

A change lives at a level of the system, and the task names that level. In
the application's own vocabulary, a request for a new capability is about
which parts take part and what passes between them; a request to alter one
rule is about the states and transitions of the blocks that hold it. The
agent reasons at the level the task names, in that level's language — blocks,
flows, transitions — and not in code. What passes below that level is
direction: what a block must do differently, which the developer can correct
in one sentence. The code that carries the direction out is produced by the
build and checked against the direction; it is not what the developer judges
the change by. The next section's three layers, the grain rule among the
design decisions, and the scale rule for evaluation are this principle
applied.

Four moves carry it, and the sections below say where each one runs:

- **Verification by simplification.** Whatever is judged is first reduced to
  a form that can be found true or false: a block with a mark, an amendment
  in one sentence, a verdict of yes, no, or misframed with one piece of
  evidence. A small claim can be checked and a verdict counted; a diff or a
  page of findings can only be read.
- **Context isolation by separating the steps.** Discovery, review, and the
  check of each built block run in fresh contexts that receive only their
  inputs, so no context judges its own proposal.
- **Five whys and fishbone, as questions rather than diagrams.** The agent
  asks why up the layers until it reaches the problem, and sorts what stands
  in the way of an answer — a wrong premise, a source it cannot read, a
  convention, a system nobody knows yet — before it chooses a way around, so
  a decision is clarified by its causes instead of patched at the block.
- **Explanation in plain words.** The change is stated in the application's
  concepts, so everyone involved — the developer who corrects it and the team
  that reads the pull request — can follow it.

An agent given a non-local task reports its understanding as prose and its
result as a diff spread across many files, neither of them at the level where
the change lives. The decisions that matter are inside both and visible in
neither: which existing system it reused or missed, where the change lands,
whether one new thing should be two, and what must be extracted before
anything is built. The developer is left asking why this file, which
assumption, and how the agent decided, and can answer only by reading the
diff after the work is done.

Two common answers move the cost without removing it. A long specification
written before the work has the detail but not the structure, and adds another
document to read. A separate plan mode with an approval step adds a mode
switch and a hand-off. Blueprinter keeps plan mode's investigate-before-code
step without its separate mode or its whole-plan approval.

Neither answer removes the failures that recur in a large codebase: new code
written without consulting the old, an existing feature that could be
extended left undiscovered, and a plan that nothing validates. All three
share a cause. One context that investigates, proposes, and checks its own
work poisons itself: once it has settled on a solution, it reads the code to
confirm that solution and checks the result against its own intent. Asking
that context a reuse question does not help, because the context that wants
to build answers it. Blueprinter therefore splits the work into steps and
runs each step that judges another step's output in a fresh context that
never sees the proposal: discovery of what exists runs before anything is
proposed, review of the blueprint receives only its blocks, and the check of
each built block receives only the amendment and the diff. Where a check can
be a script, it is one, so a blueprint whose new block cites no search for
existing capability fails mechanically instead of by judgment.

Blueprinter exists so that the developer can correct the structure in the
vocabulary of structure: "you missed the existing system that does this",
"change it here, not there", "make two blocks, not one", "extract this
first". **Each correction lands on one named block, and the agent redraws the
blueprint instead of rewriting a plan.** The intended effect is that a wrong
placement, a missed existing system, or a wrong split is found while it is
still one sentence of correction, not after it is a diff across many files.

A small, clean task is weak evidence for that effect. It has no hidden
existing system to miss and no competing places for the change to land.
Evaluation needs representative multi-part changes in real codebases, where
the agent's first placement is plausible and wrong, and it must exercise
corrections: whether the first blueprint exposed the consequential mistake,
and whether one correction repaired it through the other layers while IDs and
unaffected decisions stayed put. Producing every view is not that evidence.
Read the evidence at each change's own scale: a change inside one top-level
part is judged by where it lands inside that part, and a change across parts
by the dependencies it adds or removes between them. Pooling both hides the
rare change that rewires the system.

## Three layers: strategy, logistics, tactics

The blueprint separates three questions, following the split between
strategy, logistics, and tactics in the factory-building game Factorio. Each
layer has its own view, so a correction changes one layer and the agent checks
only what that correction breaks in the others.

- **Strategy** answers which blocks the change touches, what happens to each,
  and in what order. It is the block map with a mark on every block and the
  build order, for example "extract first, then build".
- **Logistics** answers what flows between blocks: signals, calls, and data
  contracts. Coupling and bottlenecks are visible here, and "route it through
  the queue, not a direct call" is a logistics correction.
- **Tactics** answers what happens inside one block. Where the block holds
  logic, the tactical view is its state machine, and the block's amendment
  also names the transitions it adds, changes, or removes.

Tactics are drawn only for blocks that hold logic and change or are new.

## Orientation before surgery

A task often names a solution rather than the problem it answers, and a
premise carried only downward gets placed faithfully and still solves the
wrong problem. Orientation therefore states the problem first and treats it
as the layer above strategy. The agent questions its own change at every
layer, down to ask how the layer above is achieved and up to ask what an
answer solves there. A finding low down — a state machine that cannot take
the transition, a flow that crosses an owner — is often evidence that a layer
above, or the problem itself, was stated wrongly, so the agent goes back up
and redraws before the developer has to correct it.

Before any block is proposed, discovery restates the task as capabilities in
the application's own vocabulary, each concept the task names among them, and
searches the whole codebase for each one, classifying what it finds as
something to use, extend, or change, or nothing. A block that already holds a
concept counts whether or not the change passes through it: that is where the
change's representation of the concept comes from, and the name it goes by
there is the name the blueprint uses. A searcher that already knows the
intended solution looks where that solution would go; one that knows only the
task looks everywhere. Discovery's results set the starting marks, and a block
built from scratch, or one that adds to a block found fit to use as it is,
must name the capability it serves and answer whatever discovery found for
it.

It then checks the task's claims against the code. A task description is
often older than the code it describes: part of the work may already exist,
and the description may contradict what the code does. The agent reads the
code behind each claim and records where the task really stands, so the
blueprint plans only the work that remains.

Orientation then asks the questions this task raises, not a fixed list: what
the agent must know, need, or do; how it reaches, proves, or deploys the
result; whom it must read or inform; and where the data, state, or
information comes from. The task sets the depth. A change that alters what
others read — another service, a published name or interface, a document or
test that quotes it — sends the agent to read those readers, including for a
fallback it proposes. An input a block already receives is traced only until
its meaning and provenance are known, because receiving a value does not show
who set it or what it may be trusted for; a change that makes the input decide
access or trust, or moves what established that trust, needs the guarantee
shown, not assumed.
Tracing stops where more reading could not change the surgery, and the
blueprint shows where it stopped, so the developer can send the agent
further. When a claim covers every instance of something, an instance that
takes the same fix still widens the change, and one whose content is computed,
passed in, or looked up is invisible to a search over written text; a partial
sweep reports a claim met that is only partly met. The agent may also research
online, for example a vendor API, and cites what it read.

Every answer ends in **ok, now what** or **yes, but**. An ok raises the next
question. A yes-but names what stands in the way: a source the agent cannot
read, a convention that forbids the obvious route, a system neither the
developer nor the agent knows yet. The agent may research the obstacle or ask
why until the requirement behind it is clear, then takes a way around and
records it. A block that rests on an unsettled yes-but carries a warning, so
the developer sees which placements depend on knowledge nobody holds yet.

Surgery comes only after that map exists. The developer corrects a wrong
reading of the system before it becomes a wrong placement.

## Block marks

Every block on the block map carries one mark. Most marks follow Factorio's
construction planning, where planned work is drawn over the running factory
before robots build it.

| Mark | Meaning |
| --- | --- |
| **Existing** | The block exists and the change uses it as it is. |
| **Upgrade** | The block exists and the change modifies it. |
| **Extract** | The block does not exist as a unit; the change separates it out of an existing block so that more than one caller can share it. |
| **Ghost** | The block does not exist; the change builds it because nothing supports this part of the change. |
| **Acquire** | The block does not exist in the codebase; the change brings in an external library, service, or vendor instead of building it. |
| **Deconstruct** | The block exists and the change removes it. |
| **Document** | An existing document, decision, or specification governs this part of the change and stays unchanged. A document the change edits is an Upgrade. |

Each block names where it lives. An Existing, Upgrade, or Deconstruct block
names its source path, or its Compass address when the host project keeps a
Compass chart. An Extract names the block it comes from and where it will be
placed. A Ghost names where it will be placed, an Acquire names its source,
and a Document names its document. An Existing, Upgrade, Extract, or
Deconstruct block that the agent cannot locate, or an Acquire whose source it
cannot confirm, is drawn as a guess, so a confident diagram cannot hide a
block that does not exist.

## From ghost to built

In Factorio a ghost becomes a built entity on the same map. Blueprinter keeps
its map through the build for the same reason: a plan that ends at the first
draw leaves the developer comparing a diff against memory, and what building
reveals — an amendment that does not fit, a landed block that shows a layer
above was wrong — has nowhere to go. Each block carries a status beside its
mark, and each finding returns through the same per-block corrections, so the
map stays true while the work moves, one block at a time.

A mark is intent; a status is an observation. The agent reads the host tree
for each status instead of declaring it: a block is landed only when a commit
holds its whole amendment, tests included, and the agent has read it against
that amendment, with a check it ran that observes what the status states. A
declared status cannot fail, and a tracker that cannot fail reports progress
that may not exist. For the same reason the blueprint fingerprints every file
it cites, so a file edited again while it is already uncommitted still sends
the agent back to re-read it. A landed block is history: correcting landed
work adds a new block rather than rewriting one the developer already
accepted, and the agent never rewrites an amendment to match what was built,
because that would erase the difference the developer needs to see.

When the task asks for the change, the agent builds it in build order once
the first checked blueprint is shown, without waiting for approval; a
correction that arrives meanwhile is taken first, and nothing is committed on
the agent's own initiative. Building each block and judging it are separate
steps: the context that wrote the code does not decide that it landed. The
blueprint stays out of version control, so the team sees progress through
views pasted into a pull request, not through a shared board.

## Why state machines carry the tactics

State machines make complex logic visible, traceable, observable, and, as a
result, simple. Much more of a codebase is a state machine, or close to one,
than its structure shows: a status column with values that only some code
paths check, a group of boolean flags that are only valid in some
combinations, a retry loop with a backoff counter, an approval flow spread
across handlers. Blueprinter's orientation looks for these hidden machines
and draws them. Drawing one shows the states and transitions the change must
respect.

A transition-level amendment is also easier to judge than a raw diff. "Add a
`retrying` state between `failed` and `cancelled`" can be accepted or
corrected before any code exists.

## Diagrams for the human reader

The agent draws every diagram. The reader is human, and that sets the
constraint: every view must be readable at a glance. The blueprint uses the
established UML forms a developer already reads, in the style of Rational Rose
and Telelogic Tau: packages and components with marks for strategy, sequence
charts for logistics, and state charts for tactics.

The views have two readers. The developer correcting the change reads them
while the blueprint is being drawn; the team reads them when a view is pasted
into a pull request or issue. Both read Mermaid in Markdown, so the views stay
Mermaid source and avoid what GitHub's renderer drops or misreads: click
directives, inline HTML, a theme that ignores dark mode, a `+` placed where a
sequence chart reads it as activation.
[`scripts/render.py`](scripts/render.py) checks for those and renders the
blueprint as one offline page — Markdown, the views drawn as SVG, a legend of
marks and verdicts, and each block's card on hover — using only the Python
standard library. Its layout is plainer than GitHub's and draws a subset of
Mermaid. A view it cannot draw whole, with every word of its source visible,
stays as source on the page: a dropped note can carry the very constraint the
developer needed to correct. The Markdown stays the source. Bundling a
JavaScript renderer would give a closer picture at the cost of megabytes of
vendored code, and loading one from a network would break a skill that must
work installed alone.

## Design decisions and rejected alternatives

- **Structure before prose**, instead of a specification document. The
  developer judges placement and boundaries from the block map and reads
  prose only for the block under discussion.
- **Corrections per block**, instead of one approval for the whole plan.
  Approving a whole plan asks the developer to judge everything at once and
  then treats the plan as fixed; a block-level correction keeps the rest of the
  block map as it is.
- **Blocks located in the codebase**, instead of a diagram generated from
  the task description. A diagram that is not tied to code can be well drawn
  and wrong.
- **Proceed and list assumptions**, instead of waiting for an answer. When
  the developer does not answer about a block, the agent keeps its placement
  and lists it as an assumption the developer can still correct by block. A
  yes-but follows the same rule: it ends in a way around, never in waiting.
- **Orientation bounded by the task**, instead of a full scan of the codebase
  or a fixed depth. What the task needs decides how far each slice is traced.
- **Grain follows the change's scale**, instead of a fixed depth or a node
  count. Inside one top-level part, inner placement is where a change drifts,
  so the blocks are drawn there. Across parts, inner detail buries the
  dependency the change adds or removes between them, so the strategy view
  shows the parts and those dependencies, and inner views wait in the file.
- **Questions factored per task**, instead of a fixed checklist. A fixed list
  asks the same things of a local change and a cross-service change, and
  misses what only this task raises.
- **Questions that move between layers**, instead of a problem statement
  asked once at the start. A premise checked only on the way down is never
  tested by what the lower layers find.
- **Isolated steps**, instead of one context from task to commit. Discovery,
  blueprint review, and the check of each built block run in fresh contexts
  that receive only their inputs, and their findings return as corrections
  the agent takes, not as gates that wait for the developer. Without
  subagents the steps still run as separate passes, and the blueprint says
  they were not isolated. The steps classify rather than write: each judged
  item is yes, no, or misframed, with one line of evidence. A verdict can be
  wrong, compared, and counted by a script; findings prose cannot. Misframed
  separates a false item from one whose question is wrong, which must be
  corrected in the layer above it, not patched at the block.
- **Scripted checks first**, instead of review by reading alone. Citations,
  IDs, marks, locations, the link to what discovery found from each new block
  and from each block that adds to what already serves, and each landed
  block's check verdicts are checked by a script before a reviewer reads the
  blueprint.
- **No gate between the phases.** One blueprint holds orientation and
  surgery; a correction to orientation redraws the surgery instead of waiting
  for a separate approval.

## Boundaries

- **Conversation is the interface.** The skill ships no web interface,
  server, or editor; the rendered page is read-only. The developer corrects
  the blueprint by naming blocks, and the agent redraws the affected views,
  without handing the work to a separate document or mode. Subagents run
  the isolated steps; they never become a second place to correct the work.
- **Blueprinter draws; it does not govern host code.** It models the state
  machines it finds or proposes. It does not add decorators, markers, or
  runtime tracing to the host project.
- **Research reads; it does not change.** Online research reads outside
  sources and never changes them. Blueprinter names the deploy path and the
  people to inform; it does not deploy or send messages.
- **Compass is evidence, not a dependency.** When the host project keeps a
  Compass chart, Blueprinter reads the chart and its `compass:` coordinates to
  find existing blocks. It never creates or changes chart content, and it
  works without a chart.
- **Neighbouring skills keep their decisions.** When they are installed
  separately, Read the Terrain owns the next move when a cause is unclear,
  Boundary Fit judges whether a separation fits its relationships, Carry the
  Load shapes the accepted change into one increment, and Helix keeps state
  across cycles of uncertain work. Blueprinter places one change, builds it,
  and tracks its blocks until they land; it does not choose among branches of
  uncertain work, keep verdicts past the change, or reproduce those
  procedures.
- **A blueprint belongs to one change.** It is a working file, excluded from
  version control by the clone's own exclude file and deleted, with its
  rendered page, when every block has landed or been dropped. It never enters
  history, so nothing has to remember to remove it and a blueprint never
  becomes a standing specification that the code must stay consistent with.
- **A blueprint is not proof.** It shows where a change lands and what it
  touches. It does not prove that the change is correct, valuable, or complete.
