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

Verify that the rule, the cast, and each check sit where the repository's own
instructions deliver them to the agents that write and review changes.
