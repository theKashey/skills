# Briefs for the isolated steps

Give a subagent its brief as written, with the inputs it lists and nothing
else: not your proposal, plan, orientation, assumptions, or reasoning. An input
that carries the expected answer turns a search into a confirmation.

## Discovery

Inputs: the host repository root, the task text, and the problem statement.

> You find what already exists. You do not design or propose a change, and you
> do not edit files.
>
> 1. State the capabilities the change needs in the application's own terms:
>    the names its glossary, architecture chart, modules, and types use, not
>    the task's words. Number them `C1`, `C2`…
> 2. For each capability, search the whole repository, not only where the task
>    points, by at least two methods: by name, and by behavior — the operation
>    it performs or the interface it would expose. Read each candidate.
> 3. Classify each candidate: **use** (fits as it is), **extend** (fits with a
>    change), **change** (existing code the task requires to differ), or
>    **none** when nothing fits. Quote the evidence with `path:line`.
> 4. List every code path in the affected area that reaches the problem, with
>    `path:line`.
> 5. For each claim the task makes, say whether you observed it, and how.
>
> Return: a table of ID, capability, result, `path:line`, and evidence; the
> paths; the claims; every search you ran; and what those searches could miss.

## Review

Inputs: the host repository root, the block cards, the build order, and the
strategy view.

> You check a proposed change you did not write. Do not edit the host tree;
> you may work in a scratch copy.
>
> 1. For each amendment that changes what others read, or that applies to
>    every instance of something, enumerate every affected reader and instance
>    by two independent methods: run the affected tests before and after
>    applying the amendment in a scratch copy where you can, and search. Explain
>    each site one method found and the other did not.
> 2. For each Ghost and Acquire, look for existing code that already does its
>    job or nearly does. Report it with `path:line`, or say how you searched.
> 3. Name each site no block covers, and each test that would still pass
>    without exercising what it was written for.
>
> Return: the sites with `path:line` and the block covering each, or none; the
> refuted Ghosts and Acquires; your methods; and what they could miss.

## Check

Inputs: the host repository root, one block's card and amendment, and the
diff or commit that builds it.

> You check built work against its amendment. You did not build it. Do not
> edit files.
>
> 1. Split the amendment into parts: each transition, test, and file change.
> 2. Read the diff or commit against each part and say **met** or **open**.
>    What the commit says about itself, in its message or comments, is a claim
>    to check, not evidence.
> 3. For each claim the amendment states, run a check that observes it — a
>    test that asserts the stated symptom, or a reproduction — and give the
>    command and result. A test that does not assert the symptom does not count.
>
> Return: each part as met or open with its evidence, the checks you ran, and
> anything the diff does that the amendment does not name.
