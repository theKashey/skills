# Briefs for the isolated steps

Give a subagent its brief as written, with the inputs it lists and nothing
else: not your proposal, plan, orientation, assumptions, or reasoning. An input
that carries the expected answer turns a search into a confirmation.

Each item a brief asks you to judge gets one verdict and one piece of
evidence — a `path:line`, or a command and its result — not an explanation:

- **yes** — it holds as stated;
- **no** — it is well posed and does not hold;
- **misframed** — what it presumes is false or contradictory, or your inputs
  cannot decide it.

## Discovery

Inputs: the root of the tree the evidence is read in — the worktree, for a
change that already exists — the task text, and the problem statement.

> You find what already exists. You do not design or propose a change, and you
> do not edit files.
>
> 1. State the capabilities the change needs in the application's own terms:
>    the names its glossary, architecture chart, modules, and types use, not
>    the task's words. Each concept the task names is a capability too: to
>    know or represent it. Number them `C1`, `C2`…
> 2. For each capability, search the whole repository, not only where the task
>    points, by at least two methods: by name, and by behavior — the operation
>    it performs or the interface it would expose. Read each candidate. A
>    block that already holds a capability counts even when the change need
>    not pass through it: the change can reuse its representation instead of
>    adding one.
> 3. Classify each candidate: **use** (fits as it is), **extend** (fits with a
>    change), **change** (existing code the task requires to differ), or
>    **none** when nothing fits. Quote the evidence with `path:line` and the
>    name the application gives it.
> 4. List every code path in the affected area that reaches the problem, with
>    `path:line`.
> 5. For each claim the task makes, give a verdict: did you observe it?
>
> Return: a table of ID, capability, result, `path:line`, and evidence; the
> paths; a table of claim, verdict, and evidence; every search you ran; and
> what those searches could miss.

## Review

Inputs: the root of the tree the evidence is read in — the worktree, for a
change that already exists — the block cards, the build order, and the
strategy view.

> You check a proposed change you did not write. Do not edit the host tree;
> you may work in a scratch copy.
>
> 1. For each amendment that changes what others read, or that applies to
>    every instance of something, enumerate every affected reader and instance
>    by two independent methods: run the affected tests before and after
>    applying the amendment in a scratch copy where you can, and search. Mark
>    each site with the method or methods that found it.
> 2. For each site, give the block that covers it, or none.
> 3. For each Ghost and Acquire, give a verdict: is it needed — does no
>    existing code already do its job or nearly do it?
> 4. For each test an amendment names, give a verdict: would it fail without
>    what it was written for?
> 5. For each block, give a verdict: does its amendment fit its card, its
>    location, and the capability it serves?
>
> Return: a table of site, methods, and covering block; a table of ID,
> question, verdict, and evidence; your methods; and what they could miss.

## Check

Inputs: the host repository root, one block's card and amendment, and the
diff or commit that builds it.

> You check built work against its amendment. You did not build it. Do not
> edit files.
>
> 1. Split the amendment into parts: each representation, transition, test,
>    and claim it states.
> 2. For each part, give a verdict: does the diff or commit build it? What the
>    commit says about itself, in its message or comments, is a claim to
>    check, not evidence.
> 3. For each claim, run a check that observes it — a test that asserts the
>    stated symptom, or a reproduction — and give its verdict with the command
>    and result. A test that does not assert the symptom does not count.
> 4. Add a part for each thing the diff does that the amendment does not
>    name, and give a verdict: does a part the amendment names require it?
>
> Return: a table with the columns ID (the block's), part, verdict, and
> evidence.
