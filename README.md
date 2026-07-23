# Documentory

Documentation should help a reader make a correct decision without making them
excavate the repository—or wade through prose that merely repeats the code.

Documentory is an [Agent Skill](https://agentskills.io/) for creating,
revising, and auditing documentation for open-source libraries. It keeps
current documentation about present behavior, moves historical change into
release material, and reserves code comments for non-obvious rationale that a
maintainer or coding agent would otherwise miss.

## What it covers

- README files and documentation sites
- tutorials, how-to guides, explanations, and reference material
- public APIs, configuration, JSDoc, and TSDoc
- runnable, illustrative, partial, and pseudocode examples
- file-, block-, and line-level rationale comments
- changelogs, migration guides, release checks, and documentation audits

Documentory uses Diátaxis to distinguish reader needs, not to prescribe files
or folders. It works within the documentation structure a repository already
owns and proposes a split only when the user should decide whether its benefit
justifies the maintenance cost.

## Install

The [`skills` CLI](https://github.com/vercel-labs/skills) can discover and
install Documentory for supported coding agents:

```sh
npx skills add theKashey/skills --skill documentory
```

To make it available globally to Codex without an interactive prompt:

```sh
npx skills add theKashey/skills --skill documentory --global --agent codex --yes
```

From a local clone, replace `theKashey/skills` with the path to the repository:

```sh
npx skills add . --skill documentory
```

Restart or begin a new agent session if the client does not reload installed
skills automatically.

## Use

Ask the agent to use `$documentory`, or make a documentation request that
matches the skill description. For example:

```text
Use $documentory to audit this package README against its public exports,
configuration, tests, and examples. Report defects without editing files.
```

```text
Use $documentory to document this public option. Keep the existing README
structure and use balanced detail.
```

```text
Use $documentory to review comments around this function. Preserve only the
non-local rationale that prevents a plausible wrong change.
```

The default documentation level is **Balanced**. Choose **Guided** when the
reader needs a friendly primary path, or **Compressed** when a known expert
audience needs only the irreducible contract and boundary.

## Package layout

```text
documentory/
├── SKILL.md
├── LICENSE.txt
├── agents/
│   └── openai.yaml
└── references/
    ├── api-jsdoc-examples.md
    ├── content-architecture.md
    └── quality-maintenance.md
```

`SKILL.md` contains the laws, request routing, and procedures. Each reference
is loaded only when its procedure needs the extra detail, so unrelated doctrine
does not consume the agent's working context.

## Validate a change

Check that distribution tooling can discover the skill:

```sh
npx --yes skills@1.5.20 add . --list
```

Pull requests also validate `documentory/` against the official Agent Skills
reference implementation and repeat the distribution discovery check on an
isolated runner.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the evidence expected with changes.
Security-sensitive behavior should follow [SECURITY.md](SECURITY.md).

## License

Documentory is available under the [MIT License](LICENSE).
