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
- A comment, docblock, or document lead over its content-line budget—15 for a
  file overview, 5 for a block, 10 for a docblock, a 15-line lead for a
  document—or one that gained a heading, a measurement, history, or an export's
  contract, moved that content to the surface that owns it and kept a one-line
  route, leaving the surface well under budget rather than shaved to it;
  nothing was copied, and no cause was dropped to fit. Overflow outside the
  change's scope, or bound for an owner the change cannot update, is named in
  the PR as unfinished work.

A host that wants a build gate writes it in its own linter, with these numbers
and the ladder's counting rules, keying any recorded debt by file and kind.

Verify that the rule, the cast, and each review check sit where the
repository's own instructions deliver them to the agents that write and review
changes, and that no host instruction routes rationale to a surface without a
budget—an instruction that sends "why" to the docstring with no limit defeats
every check above.
