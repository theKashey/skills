# Documentory

Documentory creates, revises, and audits technical documentation so a named
technical reader can orient, decide, and act safely as the underlying system
changes.

Technically accurate documentation still fails when that reader cannot identify
a subject's purpose, the decision it supports, its boundary, or the surface that
owns the deeper truth. Documentory makes documentation a reliable decision
surface rather than an implementation transcript.

It provides the principles and procedures for establishing reader need, placing
verified facts at their canonical documentation layer, explaining relevant
purpose and boundaries, and checking the finished result against the completed
system.

- [Why Documentory exists](#why-documentory-exists)
- [Technical role](#technical-role)
- [Architecture and ownership](#architecture-and-ownership)
- [Principles and design rationale](#principles-and-design-rationale)
- [Boundaries](#boundaries)

## Why Documentory exists

Documentation may not exist at all. When it does, technically accurate prose can
still fail because a reader cannot tell why its subject matters, what should
change for them, or where deeper truth belongs.

Documentory closes that full lifecycle gap. It introduces purpose, relevance,
observable behavior, and boundaries before internal method, places deeper facts
at the lowest surface that owns them, checks the finished reader path against
the finished system, and keeps the result maintainable as that system changes.

## Technical role

The module covers the complete documentation cycle. It first decides whether a
material reader gap justifies documentation, then defines what and why should
be documented before deciding how much detail to expose. It directs an agent to
identify the reader and subject, establish the problem and intended impact at
each independently entered unit, place each deeper fact with its canonical
owner, expose hidden constraints, and verify that the finished documentation
agrees with the finished code.

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

Keep each behavior in one canonical owner. Link to it from other files rather
than restating it with slightly different wording.

## Principles and design rationale

The skill's durable principles are:

- **Start from the reader's needed decision.** Documentation earns its place
  only when a named reader has a material gap; technical accuracy alone is not
  enough.
- **Orient before mechanism.** State purpose, relevant effect, and boundary at
  the subject's owning scope before internal method or detail.
- **Keep truth local and canonical.** Put a fact at the lowest stable surface
  that governs every decision it affects, then link rather than duplicate.
- **Prefer a map to a transcript.** Preserve non-obvious constraints,
  interactions, and rationale that the reader cannot safely infer; omit visible
  mechanics and unneeded surface area.
- **Treat documentation as a completed-system claim.** Verify it against the
  finished code and artifacts, and exercise representative reader paths to
  expose context gaps.

The package separates runtime decisions from their maintenance rationale. The
[locality ladder](references/locality-ladder.md) owns the reader-context model;
[content architecture](references/content-architecture.md) owns reader paths
and document roles; [API, JSDoc, and examples](references/api-jsdoc-examples.md)
owns public-contract and code-local detail; and [quality and
maintenance](references/quality-maintenance.md) owns verification and drift
checks.

This split prevents a routine documentation task from carrying unrelated
contract, code-comment, or maintenance doctrine. It also keeps technical
READMEs, public documentation homes, and product presentation pages distinct
because they serve different readers and entry contexts. Diátaxis supplies a
reader-question vocabulary, not a required file tree.

## Boundaries

Documentory guides documentation work. It does not decide product behavior,
preserve or remove code, invent facts, or authorize a documentation
restructure. It may report a placement gap or propose a split; the user decides
whether to create or move a surface.
