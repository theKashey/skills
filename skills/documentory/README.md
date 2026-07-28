# Documentory

Documentory preserves verified explanations for fences: choices, constraints,
boundaries, relationships, and structures whose reason is not visible in the
code or system surface where a reader encounters them. It documents reefs, not
cliffs—the hidden why and consequence, not mechanics already in view.

Locality is how Documentory makes those explanations useful. It leaves each one
at the narrowest authorized surface a human reader or coding agent naturally
encounters before making the affected decision.

- [Why Documentory exists](#why-documentory-exists)
- [Technical role](#technical-role)
- [Architecture and ownership](#architecture-and-ownership)
- [Principles and design rationale](#principles-and-design-rationale)
- [Boundaries](#boundaries)

## Why Documentory exists

Code and system structure usually expose what happens. They often cannot expose
the non-local cause that makes a surprising choice, constraint, boundary, or
relationship necessary here. Without that causal edge, a maintainer or coding
agent can make a locally reasonable change that violates an invisible
requirement.

Fences appear differently across implementation levels:

- **Low-level code** is their usual home. Syntax exposes an operation but not
  the platform, representation, ordering, concurrency, ownership, or algorithmic
  constraint that makes an apparent alternative unsafe.
- **Business logic** can look foolish for no visible reason, but its domain
  names, conditions, and nearby policy more often make the reason recoverable.
  When they do, there is no fence to document.
- **Orchestration and system code** contain fences especially often. A lower
  implementation detail, parallel process, lifecycle transition, or event that
  happened earlier or will happen later can constrain a decision without
  appearing in its local source.

These are implementation abstraction levels, not documentation rungs. At every
level, the fence is the same shape: a cause not locally visible has a material
effect here. Document the causal edge and local consequence; keep remote
mechanics with their canonical owner.

Prose duplicates system truth and can decay independently from it. Prose about
a remote action is especially fragile because its owner can change without the
copy beside this decision changing. Prefer code, names, types, API shape, or
structure when they can make the constraint locally visible. When the
significance remains irreducibly non-local, retain only the stable causal edge
and its local consequence.

Documentation density is therefore a diagnostic signal, not proof of bad code.
It can reveal accidental opacity, essential concurrency or lifecycle
complexity, or a genuinely non-local influence. An explanation protects the
decision now and may expose an opportunity to make the constraint visible
later.

Documentory is also a filesystem-level context-engineering practice. Code and
domain structure should expose what they can—[“If your code-base doesn’t scream
its domain, AI will whisper
nonsense.”](https://asdlc.io/concepts/context-engineering/#references)—while
documentation supplies only the hidden reasons that remain. What is omitted
matters too: in evaluated repository-level context-file settings, [Gloaguen et
al. (2026)](https://arxiv.org/abs/2602.11988) found that agents generally
followed the instructions, explored and reasoned more, and incurred higher
inference cost without significantly improved task performance. Unnecessary
instruction is therefore active context, not neutral background.

Documentory closes that explanation gap across the full documentation
lifecycle. At broader surfaces, a fence may be hidden purpose, contract,
failure, interaction, or ownership boundary. At code level, it is the verified
non-local cause that makes a locally selectable, apparently reasonable
alternative unsafe. Documentory leaves that explanation with its canonical
owner and omits facts the reader can already recover.

## Technical role

Fence discovery and explanation is the organizing decision across the complete
documentation cycle. The module first decides whether a material, non-visible
reason affects a reader's decision, then establishes that reason from evidence
and chooses its canonical owner. Locality determines where the explanation
belongs; progressive disclosure determines how much of it the reader needs.

A fence is a present choice, constraint, boundary, relationship, or structure
whose reason is not locally visible. Its reef is the material hidden cause and
consequence that can make an apparently reasonable action unsafe. A cliff is
meaning already visible and safely recoverable from local context. A
Chesterton's Fence is a fence whose reason remains unresolved. Documentory
investigates that uncertainty; it records only a verified explanation or an
explicit accepted `TODO` or `FIXME`, never an invented rationale.

A coding agent may enter through a task, diff, README, public contract, symbol,
or search match without tacit organizational memory. The same selective-context
problem affects human readers. At code level, Documentory preserves
evidence-backed causes that rule out a locally reasonable alternative. It does
not narrate visible mechanics, inevitable effects, or remote behavior that has
no material consequence for the decision here.

Source evidence supports documentation while it is authored, but documentation
review and deterministic completion checks happen once at wrap-up. Line, block,
and file comments are admitted and written from evidence but never enter
documentation review; exported-symbol JSDoc remains a public contract.

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

- **Document fences; preserve reefs, not cliffs.** Keep the verified reason and
  consequence that code or the current surface does not reveal; omit visible
  mechanics.
- **Investigate Chesterton's Fences.** Recover the reason from evidence or mark
  accepted uncertainty explicitly; never manufacture rationale.
- **Orient before mechanism.** State purpose, relevant effect, and boundary at
  the subject's owning scope before internal method or detail.
- **Keep truth local and canonical.** Put a fact at the lowest stable surface
  that governs every decision it affects, then link rather than duplicate.
- **Prefer a map to a transcript.** Preserve non-obvious constraints,
  interactions, and rationale that protect a real decision the reader cannot
  safely infer; omit visible or inevitable mechanics, callee-owned behavior,
  and unneeded surface area.
- **Use explanations as clarity signals.** Protect an invisible constraint
  first, then notice when code, types, an API, or structure could expose it
  directly. Keep the explanation when the significance remains non-local; do
  not treat every documented fence as a mandatory refactor.
- **Treat documentation as a completed-system claim.** At wrap-up, verify it
  against the finished code and artifacts, and exercise representative reader
  paths to expose context gaps. Do not review line, block, or file comments.

The package separates runtime decisions from their maintenance rationale. The
[locality ladder](references/locality-ladder.md) owns the reader-context model;
[content architecture](references/content-architecture.md) owns reader paths
and document roles; [API, JSDoc, and examples](references/api-jsdoc-examples.md)
owns public-contract and code-local detail; and [quality and
maintenance](references/quality-maintenance.md) owns verification and drift
checks at wrap-up.

This split prevents a routine documentation task from carrying unrelated
contract, code-comment, or maintenance doctrine. It also keeps technical
READMEs, public documentation homes, and product presentation pages distinct
because they serve different readers and entry contexts. Diátaxis supplies a
reader-question vocabulary, not a required file tree.

## Boundaries

Documentory guides documentation work. It does not independently decide product
behavior, preserve or remove code, invent facts, or authorize a documentation
restructure. It may report a code-clarity or placement opportunity, but acts on
code or topology only when that change is already authorized and in scope.
