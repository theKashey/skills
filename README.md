# Agent Skills

Five standalone skills for evidence-led agent work: orient uncertain
situations, map wider goals into accountable work, author trustworthy
documentation or agent skills, and gate compound artifacts before they cross a
trust boundary.

Use them when an AI coding agent must choose a justified next move under
incomplete information, preserve the contribution path from implementation to
a wider outcome, keep a reader-facing contract true to the system, encode a
recurring agent decision, or decide whether a finished bundle is ready to hand
off. The packages share an operating model—separate observation from
interpretation, prefer the narrowest supported move, make completion observable,
and report uncertainty explicitly—but they do not depend on or invoke one
another.

## Choose the right skill

| Need | Skill | Supported result | Boundary |
| --- | --- | --- | --- |
| The next action depends on whether causality is clear, analyzable, emergent, unstable, or unknown. | [Read the Terrain](skills/read-the-terrain/SKILL.md) | One bounded, evidence-producing move with expected and disconfirming readbacks. | Problem alignment and orientation do not establish that a candidate works or covers its requirements. |
| A wider-goal map must be built from an epic or reconstructed from existing work, then scanned for where it should extend before implementation inspection. | [Mind Mapper](skills/mind-mapper/SKILL.md) | One living graph with outward epic-to-result branches, inward history and backlinks, an extension frontier of open or weak locations, and an action frontier of ready moves. | Scientific readbacks maintain completed branches. Neither backlinks nor positive effects prove causal explanation, safe generalization, move sufficiency, implementation correctness, or permission to read or change code. |
| Documentation, examples, public contracts, or code-local rationale must agree with verified implementation facts and reader context. | [Documentory](skills/documentory/SKILL.md) | Current documentation with explicit coverage, evidence, boundaries, and remaining risks. | Its domain gate does not verify the non-documentation parts of a mixed deliverable. |
| A skill must change the right agent choice, stay independently installable, and justify its recurring context cost. | [Skill Guidance](skills/skill-guidance/SKILL.md) | The smallest decision map with explicit routing, completion, isolation, and behavioral-validation status. | Structural validity alone does not prove that agent behavior changed. |
| A user or acceptance owner requests integrated readiness, or a finished artifact spans multiple files, representations, or consumer views before a trust boundary. | [Verify Complex Artifacts](skills/verify-complex-artifacts/SKILL.md) | A gate record that keeps factual review, deterministic checks, consumer-surface evidence, isolated output-context review, and human acceptance distinct. | It does not author the artifact or decide product strategy. |

## Use the skills together

Composition is conditional, not a pipeline every task must run:

1. **Map wider work when lineage is at risk.** Mind Mapper builds from an
   outcome-level epic or reconstructs relevant history into the same graph,
   then exposes its extension and action frontiers before code inspection.
2. **Orient a selected uncertain branch.** Read the Terrain selects one
   regime-appropriate move and defines the signal that will confirm, disconfirm,
   or renew it.
3. **Produce through the applicable lane.** Use Documentory for documentation
   work and Skill Guidance for skill work. Other artifact types keep their own
   authoring workflow.
4. **Gate when the user or acceptance owner requests integrated readiness, or
   when a compound candidate approaches a trust boundary and no single
   deterministic check can establish readiness.** Verify Complex Artifacts
   freezes the contract and bundle, checks the consumer surface, and returns
   `PASS`, `BLOCK`, `NEEDS-HUMAN-DECISION`, or `UNVALIDATED`.
5. **Renew from the readback.** A failed gate or changed signal returns to
   orientation; external evidence, not the number of completed procedures,
   closes the loop.

The user or named acceptance owner decides whether a discretionary transition
needs an integrated gate. A request for one narrow property, such as syntax,
links, formulas, or tests, stays with the repository-native check unless an
integrated readiness decision is also requested. When no acceptance owner is
named, default to the integrated gate for a compound candidate before handoff,
merge, publication, deployment, or acceptance whenever one deterministic check
cannot establish readiness.

When Mind Mapper coordinates wider work, treat every applicable skill in this
repository as a candidate attack-angle capability. Attach it to an indicator
only when its supported result contributes there; never turn the skill list
into a mandatory pipeline.

Building a multi-file skill package is one task that may use all five: Mind
Mapper links the wider outcome to indicators and tasks before implementation
inspection; Read the Terrain can orient a selected uncertain branch; Skill
Guidance owns agent behavior and package isolation; Documentory owns prose and
reader paths; and Verify Complex Artifacts gates the finished bundle. Their
checks answer different questions—problem alignment, contribution lineage,
domain correctness, and compound-artifact coherence. Do not treat a verdict as
evidence for a different question; the active workflow determines which gates
are required.

The suite currently supplies authoring workflows for documentation and agent
skills, not a universal producer for code, websites, data, design, deployment,
or product requirements. Verify Complex Artifacts can gate those deliverables
only after their native workflow has produced a candidate and an authoritative
contract exists.

## Install

From a checkout, list the five discoverable skills without installing them:

```bash
npx skills add . --list
```

Choose skills and supported agents interactively:

```bash
npx skills add .
```

Install the complete suite to every detected agent without prompts:

```bash
npx skills add . --all
```

Install one skill by its slug, optionally targeting one agent:

```bash
npx skills add . --skill read-the-terrain --agent codex
```

The same commands accept `theKashey/skills` instead of `.` when the environment
has access to the GitHub repository. See the
[skills CLI supported-agent list](https://github.com/vercel-labs/skills#supported-agents)
for current client slugs and install locations. Explicit skill-invocation syntax
varies by client.

## Try the complete loop

In a client that recognizes explicit `$name` invocation, a multi-file skill
request provides a concrete path through all five capabilities:

```text
Use $mind-mapper to build or reconstruct the wider goal graph, locate its open
extension points, and expose the ready action frontier before inspecting
implementation. Use $read-the-terrain on a selected branch when its causal
regime is uncertain and choose one bounded, evidence-producing move. If a skill
is justified, use $skill-guidance to build or revise it as an independently
installable decision map. Use $documentory for its README, references,
examples, and reader paths. After the package is finished, use
$verify-complex-artifacts to gate the delivered bundle before handoff. Keep
each verdict separate and report any remaining uncertainty.
```

The result should expose the next move and readback, the skill's changed choice
and completion condition, documentation that matches the finished package, and
a final trust-boundary status. A simple documentation edit, a narrow test run,
or a clear operational response should use only the relevant skill or
repository-native check.

## Capability details

### Read the Terrain

Read the Terrain combines a compact terrain card, causal-regime selection,
recognition-primed mental simulation, isolated problem checks, and an OODA
readback. It distinguishes problem opacity from execution opacity: the former
needs a reader who reconstructs the candidate's apparent purpose, while the
latter needs a signal that separates competing transition stories.

```text
Use $read-the-terrain to classify this situation and choose one bounded,
evidence-producing move with expected and disconfirming readbacks.
```

The skill closes only when external evidence reaches the stated aim. Read the
[runtime decision map](skills/read-the-terrain/SKILL.md).

### Mind Mapper

Mind Mapper is a methodology for building a new contribution graph or
reconstructing one from existing history, then locating where it can extend.
Its outward mind map decomposes one outcome-level epic into observable
indicator bones, hypotheses, smaller moves, and results. Its inward fishbone
trace restores the backlinks from existing work to that same goal. The
extension frontier exposes missing or weak graph locations; the action frontier
shows ready moves. Frozen readbacks update completed branches without rewriting
history; they maintain the map rather than define it. Code inspection stays
closed until the graph is ready.

```text
Use $mind-mapper to build or reconstruct the living graph for this initiative.
Define the epic; map its indicator bones, hypotheses, moves, results, and
backlinks; and orient the graph behind, present, and forward. Mark incomplete
nodes and open edges, select the extension and action frontiers, and count the
known remaining moves. Use frozen readbacks to maintain completed branches.
Do not inspect code until the graph is ready.
```

The skill defines graph semantics and procedure without prescribing a tracker,
specification format, file, or diagram tool. Read the
[runtime mind-map methodology](skills/mind-mapper/SKILL.md).

### Documentory

Documentory maps verified code, types, tests, defaults, errors, and artifacts
to the README, reference, example, or code-local rationale that owns them. It
uses reader questions and governed scope to improve the existing documentation
topology without forcing a new site or folder tree.

```text
Use $documentory to audit this package README against its public exports,
configuration defaults, errors, tests, and examples. Do not edit files. Report
evidence, gaps, justified exclusions, and remaining risks.
```

It does not invent behavior, rationale, compatibility, or performance claims.
Read the [runtime documentation workflow](skills/documentory/SKILL.md).

### Skill Guidance

Skill Guidance treats a skill as a verified decision map, not a collection of
relevant advice. It chooses among no-op, amendment, reference, new skill, or
split; keeps every runtime dependency inside the package; and separates
structural checks from representative behavior and fresh output-context review.

```text
Use $skill-guidance to decide whether this recurring agent failure belongs in a
new skill, an amendment, a reference, a deterministic gate, or no runtime
instruction. Implement only the admitted choice and prove its completion.
```

The package includes a standalone Python validator for skill structure and
isolation. Read the [runtime skill-authoring workflow](skills/skill-guidance/SKILL.md).

### Verify Complex Artifacts

Verify Complex Artifacts runs after generation when tests alone cannot
establish readiness across files, representations, or consumer views. It
freezes the trust boundary, inventories the bundle, runs factual and
deterministic gates, exercises the consumer surface, and gives a fresh reviewer
only the final target and neutral output-context rules.

```text
Use $verify-complex-artifacts to gate this finished release bundle before
handoff. Keep factual review, deterministic checks, consumer-surface evidence,
isolated output-context review, and human acceptance distinct.
```

The isolated review establishes semantic coherence, not external factual truth
or requirement coverage. Read the
[runtime verification workflow](skills/verify-complex-artifacts/SKILL.md).

## Package and repository contract

The packages follow the [Agent Skills](https://agentskills.io/) format.
Compatible agents discover a skill from its name and description, load
`SKILL.md` when the task matches, and load branch-specific resources only when
the active procedure points to them.

Each `skills/<name>/` directory is an independent distribution unit with a
required `SKILL.md` and the repository's `LICENSE`. A package may also include:

- `references/` — branch-specific guidance loaded when needed
- `scripts/` — executable helpers for deterministic work
- `assets/` — templates or other output resources

Repository validation checks every package in place and after copying it
without its siblings. It also checks that every standalone copy retains the
repository license:

```bash
python3 scripts/validate_skills.py
```

This proves structure and runtime isolation, not behavioral effectiveness.
Behavioral changes still require representative clean-context evaluation and
the completion gate defined by the active skill.

## License

[MIT](LICENSE) © 2026 Anton Korzunov.
