# Agent Skills

A collection of skills for AI coding agents. Each skill packages instructions
and optional supporting resources. Compatible agents use the skill description
to decide when to load its instructions, then load referenced resources only
when the task needs them.

Skills follow the [Agent Skills](https://agentskills.io/) format.

## Available Skills

### documentory

Creates, revises, and audits documentation for open-source libraries and
packages.

**Use when:**

- Working on README files, documentation sites, tutorials, how-to guides,
  explanations, or reference material
- Documenting public APIs, configuration, examples, JSDoc, or TSDoc
- Preserving non-obvious rationale in file, block, function, or line comments
- Reviewing changelogs, migration guides, release documentation, or
  documentation maintenance

**What it covers:**

- Procedures for verifying current contracts against source, types, tests, and
  generated artifacts
- Diátaxis as a reader-needs lens without imposing files or folders
- Guided, Balanced, and Compressed explanation levels
- Public-contract inventory and evidence-based example classification
- Code-local rationale for context that selective readers and coding agents
  would otherwise miss

## Installation

From this repository's root, let the `skills` CLI discover the available
skills:

```bash
npx skills add .
```

Install only Documentory:

```bash
npx skills add . --skill documentory
```

These commands describe local installation from an existing checkout. This
README does not declare a public repository source.

## Usage

After installation, a compatible agent can select a skill by matching its
description to the task. Explicit invocation syntax depends on the client. In
clients that recognize `$documentory`, for example:

```text
Use $documentory to audit this package README against its public exports,
configuration, tests, and examples. Report defects without editing files.
```

## Skill Structure

Each skill lives under `skills/<skill-name>/` and contains:

- `SKILL.md` - Required metadata and agent instructions
- `agents/` - Optional client-facing metadata
- `scripts/` - Executable helpers, when the skill needs them
- `references/` - Supporting guidance loaded only when needed
- `assets/` - Templates or other output resources, when needed

### OpenAI metadata

Documentory includes
[`agents/openai.yaml`](skills/documentory/agents/openai.yaml), which OpenAI
documents as [optional skill metadata](https://learn.chatgpt.com/docs/build-skills#optional-metadata)
for the ChatGPT desktop skill UI. It supplies the display name, short
description, and starter prompt. It does not change the skill instructions,
declare tool dependencies, or override invocation policy. Clients that only
implement the portable Agent Skills format do not need this file.

## License

No repository-wide license has been selected.
