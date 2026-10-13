---
name: blueprinter
description: Use when planning, scoping, placing, or making a change in existing code — finds blocks to use, extend, change, or create, with evidence; checks in isolation; builds each block; not for shaping the accepted increment or architecture charts.
---

# Blueprinter

Lay out a change, check it, and build it. **Orient** traces the existing
system as far as the task needs and finds what already does part of the job.
**Operate** proposes the surgery on what Orient traced, as marked blocks. The
blueprint is checked, then tracks the change while it is built, until every
block has landed. The developer judges and corrects structure; prose and diffs
appear only for the block under discussion.

**The context that proposes never judges its own proposal.** Discovery (§1),
review of the blueprint (§4), and the check of each built block (§6) each run
in a fresh subagent that receives only the inputs its brief in
[references/briefs.md](references/briefs.md) lists — never your proposal or
reasoning. A context that has settled on a solution reads the code to confirm
it and checks its own work against its own intent. When the host offers no
subagents, run each step as a separate pass before the work it judges, and
record "not isolated" as a yes-but on what it informs.

**Isolated steps classify; they do not write findings.** Each item they judge
gets one verdict with one `path:line` or command as evidence: **yes** — it
holds; **no** — it is well posed and false: correct that block under §5;
**misframed** — what the question presumes is false or contradictory, or the
inputs cannot decide it: correct the layer the block rests on under §5, then
judge the block again. A verdict can be wrong and be caught; prose cannot.

Do not edit host code before §6. Until then, the blueprint file, the page
rendered from it, its exclude entry, and the worktree §1 names for a change
that already exists are the only things you write.

## 1. Orient

**First, state the problem the change solves**, apart from the solution the
task proposes; when the task names only a solution, infer it and list the
inference under Assumptions. The problem is the layer above strategy. While
orienting and while drawing, question your own change at every layer: going
down asks how the layer above is achieved; going up asks what this answer
solves there. When an answer at any layer changes or ends in yes-but, go up
and re-ask whether each layer above still holds, up to the problem, then back
down, redrawing what changes as §5's steps 1 and 2 do. If the problem itself
changes, keep planning the task as asked and list the revised problem under
Assumptions.

**A change that already exists, wholly or in part, is built work, not
evidence.** Orient and draw against the task's starting commit — the parent
of the change's first commit, a branch's merge base with its target, a pull
request's declared base, or HEAD for uncommitted work — in a worktree at that
commit, and list the commit you chose under Assumptions. Record the evidence
there, and do not read the diff from that commit until the first checked draw
is shown: a tree without the change cannot be read to confirm it. From then
on the diff is built work, judged as §6 judges it.

**Then check the task's claims against the code.** A task description is often
older than the code. For each claim, requirement, or "done when" item, read the
code that would satisfy it — including its logic, not only its signature — and
record one of: met, partly met, not met, contradicted. Plan only what remains.
When nothing remains, or only a check that it holds, the blueprint is the stands
table, the orientation behind it, and that check. A claim that reaches an
Existing block is the reason to read that block's logic; this is how a defect in
"unchanged" code is found.

**Then find what already does the job, before proposing anything.** Give a
discovery subagent the discovery brief, the task text, and the problem as you
stated it. It restates the task as capabilities in the application's own
terms, each concept the task names among them, numbered `C1`, `C2`…, and
returns for each one what to use, extend, or change, or none, with the name
the application gives it, `path:line`, and the searches behind it, and a
verdict on each claim of the task. A block that holds a capability counts as
a result whether or not the change passes through it: the change reuses its
representation instead of adding one. Read each result it cites before you
rely on it; a cited result you have not read is a yes-but. Its paths feed the
questions below, and its names are the words the blueprint uses for the
change; a claim you record differently from its verdict is a yes-but.

**Then ask the questions this task raises.** They are not a fixed list. Factor
them from the task, drawing on four directions:

- **what** you must know, need, or do;
- **how** you reach it, prove it, or deploy it;
- **who** you must read or inform — documents, owners, people;
- **where** its data, state, or information comes from.

Give each question a permanent ID (`Q1`, `Q2`…) under the same rule as block
IDs, so the developer can say "go further at Q4".

Answer each question by reading. Start from the project's own map: a Compass
chart (`.compass/`, `// compass:` markers) when present, then docs, then source.
For a system outside the codebase — a vendor API, a public service, a library
you might bring in — you may research online; cite the URL you read on the
answer it informs. A source you did not read is a yes-but, not a citation.
Research reads outside sources; it never changes them.

While reading, look for:

- **blocks** — units with identity, boundary, and interface: a module, a
  service, a component, a document that governs behavior;
- **how they combine** — the calls, events, and data contracts between the
  blocks the task touches;
- **state machines** in blocks that hold logic, including hidden ones: a
  status field checked in some paths, boolean flags valid only in some
  combinations, retry or backoff loops, approval flows, `if` chains on a kind
  or phase value. "Not far from a state machine" counts;
- **what could be brought in** — a library, service, or vendor instead of
  building.

**Every answer ends in one of two verdicts.**

- **ok, now what** — the answer holds. Ask the follow-on question it raises,
  if any: "the data is already available — now which part does the task
  need?"
- **yes, but …** — something stands in the way: a source you cannot read, a
  convention that forbids the obvious route, an unfamiliar system, an unread
  document. Before moving on, you may put a question in front of it: research
  the obstacle, or ask why until the requirement behind it is clear. Then take
  the way around and record it. A yes-but never stops the work.

**Trace what the task needs, as far as it needs.** If an amendment, including a
fallback, changes what something else reads — another service, a published name
or interface, a document or test that quotes it — find and read those readers.
An input the block already receives needs tracing upstream only until its
meaning and provenance are established: who sets it, whether it was validated,
and what it identifies. Stop there when the change relies on nothing more. When
the change makes the input carry a decision it did not carry before, such as
an access or trust decision, trace until the guarantee that decision needs is
shown, or record it as a yes-but. The same holds when the change moves or
removes what establishes a guarantee the block relies on.
When a claim or amendment applies to every instance of something, find them
all: each instance widens the amendment and the claim's coverage, even when it
takes the same fix. A search over written text misses instances whose content
is computed, passed in, or looked up; follow where that content comes from
too. Every match joins a block or is recorded with why it is left out. Stop
following a question when more reading cannot change the surgery, and
record where you stopped and how you searched, so the developer can judge what
the search could have missed.

Orient draws the system as it is. The only marks it sets are Existing and
Document; change marks belong to Operate.

## 2. Operate: mark every block

Propose the surgery on the slices Orient traced. Every block the change
touches carries one mark.

| Mark | Meaning | Location it names |
| --- | --- | --- |
| Existing | on the change path, used unchanged | source path or Compass address |
| Upgrade | modified | source path or Compass address |
| Extract | separated out of an existing block so callers share it | origin block, and where it will be placed |
| Ghost | built, because nothing supports it | where it will be placed |
| Acquire | brought in instead of built | package, service, or vendor |
| Deconstruct | removed | source path or Compass address |
| Document | governs this part of the change and stays unchanged; a document the change edits is Upgrade | document path |

Whether existing code already does what the task asks is a claims-check
result, not a mark.

**Discovery sets the starting marks.** A use result is an Existing block; an
extend or change result is an Upgrade or an Extract. A Ghost or Acquire names
the capability it serves. When that capability's discovery found a candidate
and you build or bring in anyway, an Assumptions line names the capability and
why its candidate does not fit. An Upgrade on a capability discovery found
fit to use as it is takes the same line: it adds to what already serves.

An Extract's amendment includes the origin's switch to calling it. Mark the
origin Upgrade only when it also changes for another reason.

**One block or two:** if two parts would get different marks or different
amendments, they are two blocks. Two files that change together for one reason
are one block, unless one block would hide an ownership, trust, or persistence
boundary, or a different lifecycle.

**Every block traces to a claim, and every claim to the problem.** A block
that serves no claim, or a claim that serves no part of the problem, is a
scope expansion: list it under Assumptions with the do-nothing alternative.

An Existing, Upgrade, Extract, or Deconstruct block you cannot locate, or an
Acquire whose source you cannot confirm, is a **guess**: draw it with `?` and
say what would confirm it. Never draw a confident block you have not located.

**IDs are permanent.** Number blocks `B1`, `B2`… whatever their mark. Never
renumber or reuse one: a split keeps the ID on the part that stays and gives the
new part the next free ID; a dropped block's ID is retired. The developer's
earlier references must keep pointing at the same thing.

**Marks are intent; status is observed.** Every block also carries a status:
planned, in progress, landed, or dropped. Never set one by declaring it. In
progress means a file at the block's location changed since the evidence
record, so a change that already existed when the record was taken at its
starting commit reads as in progress, never as landed.
Landed means a commit holds the block's whole amendment, its tests included, and
every row of the block's §6 check is yes; cite the commit. Until every part
has landed, the block stays in progress and its card names each part still
open. A check counts only if it was run and it observes
what the status or claim states; cite its command and result. A test that does
not assert a claim's stated symptom does not pin that claim. What a commit says
about itself, in its message or comments, is a claim to check, not evidence.
Dropped means the developer removed the block. When built code differs from its
amendment, that is a yes-but on the block's card, corrected under §5; never
rewrite the amendment yourself to match what was built. A landed block is
history: a correction to landed work adds a new block at the landed code under
the next free ID.

## 3. Draw the blueprint

Write one blueprint per change to `.blueprints/<change-slug>.md` in the host
repository. In the conversation, show the direction, the stands table, the
discovery table, and the strategy view on the first draw, and the direction,
the strategy view, and the delta after each correction; the other views stay
in the file. Revise that file in place.
Start it with the commit the evidence was read at — the starting commit, for
a change that already exists — and an `evidence` fence: one
line per file you cite or locate a block in, printed by `python3 "<this skill's
directory>/scripts/evidence.py" record <path>...` from the root of the tree the
evidence was read in: the host root, or the worktree root for a change that
already exists; a path not yet created is recorded as absent. Before each
redraw, run `evidence.py check .blueprints/<change-slug>.md` from the host
root, whatever tree the record came from, so the files the change touched
report as changed; it lists each of those files whose content changed,
including one edited again while already uncommitted; when it exits 2, treat
every cited file as changed. Re-read them, update the status of blocks
located there, refresh their lines, and say so in the delta. For a change that
already exists, the first host-root check comes after the first checked draw
is shown; redraws before it re-read the worktree, and from then on a changed
file sets the status of the blocks located there while the citations keep
pointing at the worktree, the tree the record and the lint read. It is a working
file, never committed: before the first write, make sure `.blueprints/` is
listed in the clone's exclude file — the path `git rev-parse --git-path
info/exclude` prints — so it cannot be committed by accident. Earlier revisions
live in the deltas you report.

Use Mermaid in ` ```mermaid ` fences, so a view pasted into a pull request or
issue renders on GitHub. Every view must be readable at a glance. A view with
nothing to show is one line saying why. Draw only blocks that change, that the
change path runs through, or that govern it.

After each write, run `python3 "<this skill's directory>/scripts/render.py"
.blueprints/<change-slug>.md` and give the developer the page path it prints.
It writes `<change-slug>.html` beside the blueprint and lists each line that
GitHub would not render. Exit 1 means such lines: fix them in the Markdown and
run it again before showing the views. Exit 2 means it could not read the
blueprint or write the page; say so and go on with the Markdown.

**Where the task stands** — one line: the problem, and where it was stated or
that it was inferred. Then a table: claim, state (met / partly / not met /
contradicted), evidence with `path:line`.

**Discovery** — a table: ID, capability, result (use / extend / change /
none), evidence with `path:line`. Under it, the searches discovery ran and
what they could miss, and "not isolated" when it ran in your context.

**Orientation** — one view per vertical slice the task touches, without change
marks.
- A `flowchart TB` of the slice's questions in reading order, each node
  `ID short label`, styled `ok` or `yesbut`.
- A table under it: ID, question, answer with `path:line` or URL, verdict. A
  yes-but names the obstacle and the way around.
- **Stopped at** — where tracing stopped, how you searched and what that
  search could miss, each match left out and why, and why more reading could
  not change the surgery, so the developer can say "go further here".

**Direction** — the change in the application's concepts, before the surgery
views: the cards' amendment sentences for the blocks whose amendment changes
what a concept is, does, or where it is held — a representation or a
transition added, changed, or removed, or a block moved or shared — each
naming the concept in the words discovery found for it; then one line naming
the blocks whose amendment only carries the change through. Existing and
Document blocks are not listed. No paths, code names, or diffs. This is what
the developer corrects with a sentence; a correction here redraws the layers
under it.

**Strategy** — the touched blocks with their marks.
- Use `flowchart TB`. Group blocks in `subgraph`s by Compass container or
  package.
- Set the grain by the change's scale. A top-level block is a Compass container,
  or a top-level package or service when there is no chart. When the change
  stays inside one, draw its blocks directly: placement inside it is where a
  change drifts. When it crosses two or more, the strategy view is an overview
  of the touched top-level blocks, and one view per touched top-level block
  holds its blocks in the file until the developer names one.
- A view inside one top-level block that passes about a dozen nodes splits by
  that block's own parts, never at an arbitrary node.
- Edges carry dependencies or data only. Label each block `ID name «mark»`, and
  add `⚠` when the block depends on an open yes-but. Label an overview node for
  an existing top-level block with its name and Compass address or path; it
  takes no ID and no mark, because it groups the change's blocks and is not one
  of them. A new top-level block is a Ghost block like any other, with its ID
  and mark. Label a dependency the change adds between top-level blocks `+`, and
  one it removes `−`. Each `+` gets an Assumptions line naming the alternative.
  When a chart or document governs those dependencies and does not declare this
  one, draw it as a Document block and say so on that line; the chart stays its
  owner's.
- Style marks and verdicts with these classes:

```
classDef existing fill:#eee,stroke:#888,color:#333
classDef upgrade fill:#dbeafe,stroke:#2563eb,color:#1e3a8a
classDef extract fill:#e0f2fe,stroke:#0891b2,stroke-width:3px,color:#164e63
classDef ghost fill:#fff,stroke:#16a34a,stroke-dasharray:5 5,color:#14532d
classDef acquire fill:#f3e8ff,stroke:#9333ea,color:#581c87
classDef deconstruct fill:#fee2e2,stroke:#dc2626,color:#7f1d1d
classDef document fill:#fef9c3,stroke:#ca8a04,color:#713f12
classDef ok fill:#dcfce7,stroke:#16a34a,color:#14532d
classDef yesbut fill:#fef3c7,stroke:#d97706,color:#78350f
```

**Build order** — a numbered list under the strategy view, never on edges.
Extract blocks and refactoring first. While the change is built, name the next
block: the first one not landed whose dependencies have landed.

**Block cards** — one table row per block: ID, mark, status, location, the
capability it serves, the amendment in one sentence in the application's
concepts, the open yes-but questions it depends on.

**Checks** — the §6 check's rows, one table for all blocks: ID, part, verdict
(yes / no / misframed), evidence with `path:line` or the command and result.

**Logistics** — one `sequenceDiagram` per flow the change adds or alters.
Start the text of each new or changed message with `+`.

**Tactics** — one `stateDiagram-v2` per Upgrade, Extract, or Ghost block that
holds logic. Show the existing states; label added transitions `+`, removed
`−`, changed `~`. When a machine moves to a new owner unchanged, draw it once
under the new owner without marks and say which callers newly depend on it.

**Assumptions** — every choice you made between plausible alternatives, one
line each, with its block or question ID and the alternative. A yes-but whose
way around settles it moves here and leaves the block cards; it never appears
in both. One that no way around settles stays on the card, and the block
keeps its `⚠`.

## 4. Check the blueprint

Before you show a draw as ready, and after each correction:

1. Run `python3 "<this skill's directory>/scripts/lint.py"
   .blueprints/<change-slug>.md` from the root of the tree the evidence was
   read in — for a change that already exists, from the worktree root, with
   the blueprint's path in the host checkout, so locations and line counts are
   judged against the tree the citations came from. It reports each cited
   `path:line` missing from the evidence fence or past its file's end, each
   reused block ID, each unknown mark, each Existing, Upgrade, or Deconstruct
   file that does not exist, each Ghost or Acquire with no capability or
   with a found candidate that no Assumptions line answers, each Upgrade on
   a capability found fit to use that no Assumptions line answers, each unknown
   verdict in the Checks table, and each landed block whose check rows are
   missing or not all yes. Exit 1: fix each line and run it again. Exit 2:
   say so and go on.
2. On the first draw, and after a correction that adds or re-marks blocks,
   give a review subagent the review brief, the block cards, the build order,
   and the strategy view. Each site it finds that no block covers, and each
   verdict it returns that is not yes, is a correction: take it under §5 at
   once and name the review as its source in the delta.

## 5. Take corrections

The developer corrects by naming a question, block, or layer: "go further at
Q4", "stop at Q7", "yes, but Q2 is owned by another team", "B3 already exists",
"put it in B2, not B5", "split B4", "extract B1 first", "buy, don't build
B6". Or by naming a concept, with no ID: "use what already holds this",
"that is not what the term means here", "almost: this part, not that". Find
the layer such a correction lands on — a discovery result, an orientation
answer, or a block — and take it there; a partial acceptance corrects the
part named and nothing else. What building finds is a correction too: a
block that cannot land as amended, or a landed block that shows a layer above
was wrong. For each correction:

1. Redraw every layer the correction lands on. A correction to orientation
   redraws the orientation first, then every surgery view it changes.
2. Check what it breaks in the other layers and redraw those parts.
3. Report the delta in a few lines: questions added or stopped; blocks added,
   removed, re-marked, moved, and re-scoped (same mark, narrower or wider
   amendment); statuses changed.

If the developer does not answer about a question or block, keep your answer
or placement and leave it under Assumptions. Do not stop to wait.

## 6. Build block by block

When the task asks for the change, not only a plan, start building once the
first checked draw is shown; do not wait for approval. A correction that
arrives meanwhile is taken first. When the developer asks only for a plan or
for one block's amendment, write the amendment and its diff and stop
there.

Take blocks in build order. For each, write its amendment as a section of the
blueprint:

- **Representations** of a concept it adds, changes, or removes — a field, a
  type, a stored attribute — each in the name discovery found for it, or "no
  representations change".
- **Transitions** it adds, changes, or removes. When the block holds logic
  but no transition changes — an extraction, a move — say "no transitions
  change" and name the callers that change.
- **Tests** that verify the block. They belong to the block's amendment, not
  to a block of their own.

Then write the **diff** as a unified patch, apart from the amendment: the
amendment is the direction, the diff is what carries it out, and the check
judges one against the other. Apply it to the host tree when building, or to
a scratch copy or worktree when only writing the amendment, and run the
affected tests and the type check the host has: the patch must apply, and
results must be no worse than before. Report what you ran, and name each
check the host lacks. When the block's diff already exists, take the part of
the built work at the block's location instead of writing one. A hunk at a
location no block names is a site with no covering block: take it under §5 as
a block added under the next free ID that traces to a claim, or as a scope
expansion under Assumptions, and name the diff as its source in the delta.

Then give a check subagent the check brief, the block's card and amendment,
and the diff or commit, and copy its rows into the Checks table, replacing
that block's earlier rows. They set the block's status under §2; each row
that is not yes is a yes-but on the card, corrected under §5 at the block
when no, one layer up when misframed.

## 7. Close the change

The blueprint lives only as long as its change. When every block is landed or
dropped, delete the file and its rendered page. For the change's own work,
follow the host repository's commit rules; do not commit on your own.
