---
name: blueprinter
description: Orient in an existing system as far as a task needs, then lay out the change as marked blocks before code — what exists, changes, is extracted, built, bought, removed, or still in question — for the developer to correct block by block. Use to plan, scope, or place a feature, or to map what a task touches.
---

# Blueprinter

Lay out a change in two phases before writing code. **Orient** traces the
existing system as far as the task needs. **Operate** proposes the surgery on
what Orient traced, as marked blocks. The developer judges and corrects
structure; prose and diffs appear only for the block under discussion.

Do not edit host code while orienting or operating. The blueprint file is the
only thing you write.

## 1. Orient

**First, check the task's claims against the code.** A task description is
often older than the code. For each claim, requirement, or "done when" item,
read the code that would satisfy it — including its logic, not only its
signature — and record one of: met, partly met, not met, contradicted. Plan
only what remains. A claim that reaches an Existing block is the reason to read
that block's logic; this is how a defect in "unchanged" code is found.

**Then ask the questions this task raises.** They are not a fixed list. Factor
them from the task, drawing on four directions:

- **what** you must know, need, or do;
- **how** you reach it, prove it, or deploy it;
- **who** you must read or inform — documents, owners, people;
- **where** its data, state, or information comes from.

Give each question a permanent ID (`Q1`, `Q2`…) under the same rule as block
IDs, so the developer can say "go further at Q4".

Answer each question by reading. Start from the project's own map: a Compass
chart (`.compass/`, `// compass:` markers) when present, then docs, then
source. For a system outside the codebase — a vendor API, a public service, a
library you might bring in — you may research online; cite the URL on the
answer it informs. Research reads outside sources; it never changes them.

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

**Trace what the task needs, as far as it needs.** If the task changes what
other services see, read those services. If it only uses input the block
already receives, there is nothing to trace. Stop following a question when more
reading cannot change the surgery, and record where you stopped.

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
| Document | governs this part of the change | document path |

Whether existing code already does what the task asks is a claims-check
result, not a mark.

An Extract's amendment includes the origin's switch to calling it. Mark the
origin Upgrade only when it also changes for another reason.

**One block or two:** if two parts would get different marks or different
amendments, they are two blocks. Two files that change together for one
reason are one block.

**Every block traces to a claim.** A block that serves no claim in the task is
a scope expansion: list it under Assumptions with the do-nothing alternative.

An Existing, Upgrade, Extract, or Deconstruct block you cannot locate, or an
Acquire whose source you cannot confirm, is a **guess**: draw it with `?` and
say what would confirm it. Never draw a confident block you have not located.

**IDs are permanent.** Give blocks short IDs (`B1`, `D1`…). Never renumber or
reuse one: a split keeps the ID on the part that stays and gives the new part
the next free ID; a dropped block's ID is retired. The developer's earlier
references must keep pointing at the same thing.

## 3. Draw the blueprint

Write one blueprint per change to `.blueprints/<change-slug>.md` in the host
repository, and show its views in the conversation. Revise that file in
place; version history holds earlier revisions.

Use Mermaid. Every view must be readable at a glance.

**Where the task stands** — a table: claim, state (met / partly / not met /
contradicted), evidence with `path:line`.

**Orientation** — one view per vertical slice the task touches, without change
marks.
- A `flowchart TB` of the slice's questions in reading order, each node
  `ID short label`, styled `ok` or `yesbut`.
- A table under it: ID, question, answer with `path:line` or URL, verdict. A
  yes-but names the obstacle and the way around.
- **Stopped at** — where tracing stopped and why more reading could not change
  the surgery, so the developer can say "go further here".

**Strategy** — the touched blocks with their marks.
- Use `flowchart TB`. Group blocks in `subgraph`s by Compass container or
  package.
- When a view passes about a dozen nodes, split it by container — one view per
  container plus one overview of containers — never at an arbitrary node.
- Edges carry dependencies or data only. Label each node `ID name «mark»`, and
  add `⚠` when the block depends on an open yes-but.
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
Extract blocks and refactoring first.

**Block cards** — one table row per block: ID, mark, location, the amendment
in one sentence, the open yes-but questions it depends on.

**Logistics** — one `sequenceDiagram` per flow the change adds or alters.
Prefix new or changed messages with `+`.

**Tactics** — one `stateDiagram-v2` per Upgrade, Extract, or Ghost block that
holds logic. Show the existing states; label added transitions `+`, removed
`−`, changed `~`. When a machine moves to a new owner unchanged, draw it once
under the new owner without marks and say which callers newly depend on it.

**Assumptions** — every choice you made between plausible alternatives, one
line each, with its block or question ID and the alternative. A yes-but whose
way around settles it moves here and leaves the block cards; it never appears
in both. One that no way around settles stays on the card, and the block
keeps its `⚠`.

## 4. Take corrections

The developer corrects by naming a question, block, or layer: "go further at
Q4", "stop at Q7", "yes, but Q2 is owned by another team", "B3 already exists",
"put it in B2, not B5", "split B4", "extract B1 first", "buy, don't build
B6". For each correction:

1. Redraw every layer the correction lands on. A correction to orientation
   redraws the orientation first, then every surgery view it changes.
2. Check what it breaks in the other layers and redraw those parts.
3. Report the delta in a few lines: questions added or stopped; blocks added,
   removed, re-marked, moved, and re-scoped (same mark, narrower or wider
   amendment).

If the developer does not answer about a question or block, keep your answer
or placement and leave it under Assumptions. Do not stop to wait.

## 5. Amend one block

When the developer asks for a block's amendment, produce it for that block
only, as a section of the blueprint:

- **Transitions** it adds, changes, or removes. When the block holds logic
  but no transition changes — an extraction, a move — say "no transitions
  change" and name the callers that change.
- **Tests** that verify the block. They belong to the block's amendment, not
  to a block of their own.
- **Diff** as a unified patch. Before presenting it, apply it to a scratch copy
  or worktree and run the affected tests and the type check the host has: the
  patch must apply, and results must be no worse than before. Report what you
  ran, and name each check the host lacks. Do not apply the diff to the host
  tree unless the developer asks.

## 6. Close the change

The blueprint travels with the change, like a changeset. Commit it with the
change's work when the developer commits. When the last block has landed,
remove the file in the closing commit. Follow the host repository's commit
rules; do not commit on your own.
