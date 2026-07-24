# Agent Skills

Installable capabilities for AI coding agents. This repository currently ships
**Documentory**: a documentation skill for library and package maintainers who
need documentation to stay true when code changes.

## Documentory — documentation that survives contact with the code

Documentory guides an AI coding agent to keep a library's README, public
contract, configuration reference, examples, API docs, and code-local rationale
aligned with verified code. It directs the agent to check source, types, tests,
and artifacts before making claims; it does not turn a plausible guess into
documentation.

Use it when an option exists only in a configuration object, a public example
cannot be copied safely, a package README silently assumes a checkout, or a
strange guard has a reason that a selective code reader cannot see.

### What it changes

- **Current public contracts.** Inventory stable exports, options, defaults,
  errors, and boundaries; document them in an existing canonical surface or
  report a justified exclusion.
- **The right document at the right layer.** Distinguish a public landing README
  from an internal technical README, then place detail from line-level rationale
  through package, service, and top-level documentation without duplicating it.
- **Examples readers can trust.** Explain meaningful choices before code,
  classify samples honestly, and verify runnable examples unchanged where the
  repository supports it.
- **Rationale that survives selective context.** Preserve the non-obvious why
  and why-not that future maintainers and coding agents cannot recover from a
  local scan.
- **A review-ready exit.** Check reader paths, links, coverage, historical
  leakage, and remaining risk instead of declaring a pleasant-looking README
  complete.

It uses Diátaxis to identify the reader's question, not to force a new docs site
or a fixed folder structure. It works inside the documentation topology you
already have.

## Install

Install every skill in this repository:

```bash
npx skills add theKashey/skills
```

Install only Documentory:

```bash
npx skills add theKashey/skills --skill documentory
```

## First use

In clients that recognize `$documentory`, ask a compatible agent to audit a
package without changing it:

```text
Use $documentory to audit this package README against its public exports,
configuration defaults, error behavior, tests, and examples. Do not edit files.
Report the evidence, documentation gaps, justified exclusions, and remaining
risks.
```

The audit path inventories the public surface, identifies the canonical owner
for each important fact, validates examples and entry points from their stated
context where repository tooling permits, and records what remains untested. It
also separates a missing current contract from missing change history or
code-local rationale.

## Compatibility

Documentory has no API key, service, or executable dependency. Install it with
`npx skills` for Codex, Claude Code, Cursor, OpenCode, and other supported
agents. To target one explicitly:

```bash
npx skills add theKashey/skills --skill documentory --agent codex
```

See the [skills CLI supported-agent list](https://github.com/vercel-labs/skills#supported-agents)
for the current set. Explicit skill-invocation syntax varies by client.

## What it deliberately does not do

- Invent behavior, defaults, compatibility, performance claims, or rationale.
- Treat a changelog as current documentation, or current documentation as a
  record of the past.
- Force Diátaxis pages, a documentation-site redesign, or a new folder layout.
- Create or move documentation surfaces without the user's authorization.

Read the [Documentory skill](skills/documentory/SKILL.md) to inspect its rules,
procedures, references, and verification gates.

## About these skills

Skills follow the [Agent Skills](https://agentskills.io/) format. Compatible
agents use the skill description to decide when to load instructions, then load
the relevant supporting reference only when the task needs it.

Each skill lives under `skills/<skill-name>/` and contains a required
`SKILL.md` with metadata and agent instructions. It may also include:

- `scripts/` — executable helpers when deterministic work needs them
- `references/` — supporting guidance loaded only when needed
- `assets/` — templates or other output resources when needed

## License

[MIT](LICENSE) © 2026 Anton Korzunov.
