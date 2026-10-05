# Blueprinter

Blueprinter turns a change request into a blueprint before the agent changes
code, in two phases. **Orient** builds a guided, task-shaped understanding of
the existing system: the vertical slices the task touches, traced as far as
the task needs. **Operate** then proposes the surgery on those slices and
places every part of the change on one block map: what already exists and
stays, what must be modified, what must be built because nothing supports it,
what must be brought in from outside, what must be removed, and which existing
documents govern it. Each amendment is one block and its diff. The developer
corrects that structure one block at a time while the whole block map stays in
view.

It pays most on work that crosses several parts of a system: a new
capability, a rule that touches more than one owner, a change whose right
location is not obvious. A small task gets a small orientation, not a
different procedure.

## Why the skill exists

An agent given a non-local task reports its understanding as prose and its
result as a diff spread across many files. The decisions that matter are
inside both and visible in neither: which existing system it reused or missed,
where the change lands, whether one new thing should be two, and what must be
extracted before anything is built. The developer is left asking why this
file, which assumption, and how the agent decided, and can answer only by
reading the diff after the work is done.

Two common answers move the cost without removing it. A long specification
written before the work has the detail but not the structure, and adds another
document to read. A separate plan mode with an approval step adds a mode
switch and a hand-off. Blueprinter keeps plan mode's investigate-before-code
step without its separate mode or its whole-plan approval.

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
the agent's first placement is plausible and wrong. Read the evidence at each
change's own scale: a change inside one top-level part is judged by where it
lands inside that part, and a change across parts by the dependencies it adds
or removes between them. Pooling both hides the rare change that rewires the
system.

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

Orientation starts by checking the task's claims against the code. A task
description is often older than the code it describes: part of the work may
already exist, and the description may contradict what the code does. The
agent reads the code behind each claim and records where the task really
stands, so the blueprint plans only the work that remains.

Orientation then asks the questions this task raises, not a fixed list: what
the agent must know, need, or do; how it reaches, proves, or deploys the
result; whom it must read or inform; and where the data, state, or
information comes from. The task sets the depth. A change that alters what
others read — another service, a published name or interface, a document or
test that quotes it — sends the agent to read those readers, including for a
fallback it proposes; a change that only uses input a block already receives
needs no tracing at all.
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
- **No gate between the phases.** One blueprint holds orientation and
  surgery; a correction to orientation redraws the surgery instead of waiting
  for a separate approval.

## Boundaries

- **Conversation is the interface.** The skill ships no web interface,
  server, or editor. The developer corrects the blueprint by naming blocks,
  and the agent redraws the affected views, without handing the work to a
  separate document, mode, or agent.
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
  across cycles of uncertain work. Blueprinter places one change; it does not
  hold a checkpoint across cycles or reproduce those procedures.
- **A blueprint belongs to one change.** It is a working file, excluded from
  version control by the clone's own exclude file and deleted when the change
  lands. It never enters history, so nothing has to remember to remove it and
  a blueprint never becomes a standing specification that the code must stay
  consistent with.
- **A blueprint is not proof.** It shows where a change lands and what it
  touches. It does not prove that the change is correct, valuable, or complete.
