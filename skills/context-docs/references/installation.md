# Install Context Docs

Add this rule to the repository's agent instructions, through their
established owner:

> Use `context-docs` whenever a change creates or revises documentation,
> examples, code comments, or handoffs, including documentation a code change
> makes false.

Establish the project-owned reader cast Context Docs follows—by convention a
`CONTENT-PERSONAS.md` under the project's `.agents` or `.context-docs`
directory—as [casting](casting.md) describes; without one, Context Docs serves
only each task's explicit reader.

Add these review checks to the review file the root instructions point to; if
none is named, ask where they belong:

- Every added comment or documentation passage states a verified non-local
  cause and its local consequence, or a contract the reader needs; restated
  code, narrated diffs, and facts the reader already has are removed.
- No existing comment, documentation passage, or structure is changed or
  removed without its recovered reason; one whose reason stays unknown keeps
  its form, with the uncertainty recorded as a `TODO` or `FIXME` in code, never
  an invented rationale.
- A comment, docblock, or document lead over its content-line budget, or one
  that gained a heading, a measurement, history, or an export's contract,
  moved that content to the surface that owns it and kept a one-line route;
  nothing was copied, and no cause was dropped to fit. An exception carries
  its reason in the budget baseline.

The installed check covers code comments and docblocks; document leads have
only the review check above. Ask where the host keeps its own checks, copy
`scripts/comment_budget.py` there, and add one invocation to the host's test
or lint command:

```bash
python3 path/to/comment_budget.py src --baseline path/to/comment-budget.json
```

Write the baseline once from the current tree with `--write-baseline
--accept`, so a comment that grows past its budget fails a build instead of
waiting for review. The baseline records today's over-budget surfaces and
only shrinks; raising it needs `--accept` in a reviewed change, and a surface
that stays over budget on purpose carries a `reason`. The host sets other
limits in that baseline's `limits` when its defaults differ. Where the host's
instructions authorize moving overflow to an existing owner during a code
change, say so in the rule above; otherwise the agent returns a placement
proposal.

Verify that the rule, the cast, the check, and each review check sit where the
repository's own instructions deliver them to the agents that write and review
changes, and that no host instruction routes rationale to a surface without a
budget—an instruction that sends "why" to the docstring with no limit defeats
every check above.
