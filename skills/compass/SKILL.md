---
name: compass
description: Use when creating or consuming a Compass semantic architecture chart for non-local work; not for reader-facing docs, local code-only work, or implementation instructions.
---

# Compass

## Shared contract

Compass describes the logical system, not the repository that currently
implements it. Use it for non-local work that crosses a boundary, changes a
rule, adds a party, or asks whether something belongs. Building a new
capability is non-local even when it lands in one file. For a one-file fix,
rename, or line-specific bug, read the code instead.

Read the chart root declared by the host project's agent instructions before
using either flow. If none is declared, ask the user to configure one; never
invent a chart location.

Repository structure and executable code are evidence, not sole authority over
semantic identity. A `compass: <address>` coordinate locates implementation in
the chart; it does not define the semantic boundary. When chart and code
disagree, classify the finding as semantic change, implementation remapping, or
implementation violation before deciding what should change.

For inherited coordinates, the addressed document's `## Implementation
coordinates` records `carrier-path` covers `subtree-path/`, using backticked
repository-relative paths. The carrier must be an existing source file inside
that subtree and contain the document's address; only that address gains the
declared scope. Without that declaration a marker covers
only its file; a filename such as `index.ts` implies no scope. Resolve each
root independently: a file's explicit addresses for that root override inherited
ones; otherwise use the deepest declared covering subtree. Multiple carriers
at that subtree must agree on the address set for that root. Missing carriers
or conflicting declarations are remapping findings, not permission to guess.

## Choose exactly one flow

Select one flow before loading any reference. Do not combine the flows in one
task.

- **Create** — the task establishes or changes Compass-owned state: chart files,
  semantic entities, coordinates, viewports, lexicon rows, the host usage
  hook or installed checks, or named-abstraction definitions and claims. Maintenance, remapping,
  retirement, and completion verification are Create work. Read
  [references/create.md](references/create.md). Do not load the Consume guide.
- **Consume** — the task reads and applies an existing chart without changing
  Compass-owned or Compass-installed state. Read
  [references/consume.md](references/consume.md). Do not load Create references.

If Consume reveals missing, stale, or disputed chart content, classify it and
record it where the task's own evidence lives — the PR, issue, or task record —
then stop the Compass flow. That record is the task's, not Compass-owned state,
so writing there is not a Create action. A finding that exists only in the
conversation has no owner and is lost with the turn. Changing it is a separate
Create task with its own authority and checks. If a task requests both
outcomes, separate them into distinct tasks; never drift from Consume into
Create.
