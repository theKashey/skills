# Maintaining Documentory

This is the module-level technical README for `documentory`. The repository
root README is a public landing surface; [SKILL.md](SKILL.md) is the runtime
entry point. This file helps maintainers change the module without
reconstructing its design from runtime instructions and references.

It is not part of the runtime route. Keep it focused on module ownership,
current decisions, and maintenance—not on repeating agent instructions.

- [Technical role](#technical-role)
- [Architecture and ownership](#architecture-and-ownership)
- [Deliberate reading order](#deliberate-reading-order)
- [Current design decisions](#current-design-decisions)
- [Boundaries](#boundaries)
- [Changing the skill](#changing-the-skill)
- [Validation](#validation)
- [Influences](#influences)

## Technical role

Documentory turns verified implementation facts into documentation a particular
reader can use safely. It directs an agent to identify the reader and surface,
place each fact with its canonical owner, expose hidden constraints, and verify
that the finished documentation agrees with the finished code.

It is deliberately AI-aware at code level. A maintainer or coding agent may
see only a symbol, nearby lines, and search matches. Code-local prose therefore
preserves non-local rationale and constraints rather than narrating visible
mechanics.

## Architecture and ownership

| File | Owns | Change it when |
| --- | --- | --- |
| [SKILL.md](SKILL.md) | Universal laws, request routes, procedures, and completion criteria. | A change affects every invocation or execution order. |
| [content architecture](references/content-architecture.md) | Reader paths, README roles, procedure structure, and progressive disclosure. | A change affects documentation surfaces or reader journeys. |
| [locality ladder](references/locality-ladder.md) | Scope vocabulary for placing facts from a line comment to top-level documentation. | A change affects where a fact belongs. |
| [API, JSDoc, and examples](references/api-jsdoc-examples.md) | Public contracts, JSDoc/TSDoc, code-local rationale, and examples. | A change affects API semantics, snippets, or code comments. |
| [quality and maintenance](references/quality-maintenance.md) | Audit evidence, change triggers, drift checks, and the end-state exit gate. | A change affects how documentation quality is assessed or maintained. |
| This README | Maintainer intent, file ownership, decisions, and validation. | A change affects how the module is understood or maintained. |

Keep each behavior in one canonical owner. Link to it from other files rather
than restating it with slightly different wording.

## Deliberate reading order

The runtime path is ordered deliberately:

1. Read the laws that constrain every result.
2. Choose one primary request route.
3. Follow that procedure.
4. Load only the reference named for the decision at hand.
5. Verify the completed path.

Universal laws come first. After that, the active procedure comes before its
branch-specific doctrine. Keep references decision-triggered and broad
checklists inside the route they govern.

## Current design decisions

- **Start with why at the governing scope.** A public landing establishes
  relevance; an internal README explains responsibility and boundaries; a code
  comment preserves a non-local reason. The why must add a fact that raw code
  cannot safely provide at that rung.
- **Diátaxis is a reader-question lens, not an enforced file tree.** It informs
  content mode and separation while the existing documentation topology remains
  authoritative. See [Diátaxis](https://diataxis.fr/).
- **Locality is governed scope, not filesystem shape.** One README may be a
  landing page, package manual, or folder note; classify its reader and
  responsibility before choosing its posture.
- **Public landings and internal READMEs have different jobs.** The former make
  a verified case for relevance and first success; the latter explain system
  responsibility, technical boundaries, and internal entry points.
- **A map is not a transcript; mark reefs, not cliffs.** Select relationships,
  invisible behavior, and constraints a reader cannot recover locally instead
  of narrating implementation that is already visible.
- **A Chesterton's fence is an island of uncertainty.** Detect and expose an
  unknown reason for code; document verified rationale or an accepted `TODO` or
  `FIXME`, never an invented explanation. It does not direct a code decision.
- **Current documentation describes the finished state.** Historical change
  belongs in changelogs and migration material. An explicit `TODO` or `FIXME`
  is the only accepted visible gap.
- **Balanced detail is the default.** Guided and Compressed are reader-specific
  choices; they do not change the truth of the contract.

The public-landing decision test turns these principles into a choice-ready
opening without prescribing a feature list, badge set, or fixed section order.

## Boundaries

Documentory guides documentation work. It does not decide product behavior,
preserve or remove code, invent facts, or authorize a documentation
restructure. It may report a placement gap or propose a split; the user decides
whether to create or move a surface.

The module is deliberately portable: runtime instructions and direct references
are its only integration surface. Installation belongs to the repository's
public README. Add a client-specific integration artifact, executable helper,
or new documentation surface only when a real operating requirement and its
owner are explicit.

## Changing the skill

Start from an observed failure: a task artifact, audit finding, wrong route, or
forward test. State the behavior to change and its completion signal before
adding prose.

1. Identify the affected invocation branch and its canonical owner.
2. Put universal execution rules in [SKILL.md](SKILL.md); put branch-specific
   doctrine in the directly linked reference; keep maintainer rationale here.
3. Keep the frontmatter description about when the skill should trigger. Change
   it only when the invocation boundary changes.
4. Prefer a small, positive instruction with a checkable completion condition.
   Remove duplicated, stale, or no-op wording while editing.
5. Keep references one hop from `SKILL.md` and make their loading condition
   explicit.
6. For a behavioral, routing, or new-branch change, forward-test the affected
   route with a fresh agent and a raw task artifact. Do not disclose the
   intended rule, diagnosis, or expected answer.

This README records the current design, not a change log. Git history records
superseded decisions.

## Validation

For a meaningful change:

1. Run an available Agent Skills validator and check headings, links, and
   route-to-reference pointers.
2. From the repository root, confirm discovery:

   ```sh
   npx skills add . --list
   ```

3. Forward-test the affected route with realistic source facts and review for
   invented claims, wrong routing, duplicated doctrine, skipped completion
   criteria, or unsupported documentation changes.
4. Run `git diff --check` and report any validation that was unavailable.

The change is complete when its canonical source, discovered or installed skill,
and applicable forward-test behavior agree—or when the remaining uncertainty is
explicit.

## Influences

- [Diátaxis](https://diataxis.fr/) supplies the reader-question vocabulary.
- Start-with-why, map-not-territory, Chesterton's-fence, and reef metaphors
  keep attention on purpose, invisible constraints, and uncertainty rather
  than prose volume.
- [Writing Great Skills](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md)
  is a maintenance lens: keep runtime instructions lean, give each behavior one
  owner, and prove a material change with a fresh forward test.
