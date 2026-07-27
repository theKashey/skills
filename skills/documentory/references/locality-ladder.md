# Documentation locality ladder

Place each fact where its reader encounters it before the governed decision.
Use the rungs as a scope vocabulary, not as a required folder tree, document
outline, or measure of importance.

- [Existence gate](#existence-gate)
- [Reader states](#reader-states)
- [Reader-context rule](#reader-context-rule)
- [Choose a rung](#choose-a-rung)
- [Reader-context matrix](#reader-context-matrix)
- [Overlapping rungs](#overlapping-rungs)
- [Three heuristics](#three-heuristics)
- [Movement tests](#movement-tests)

## Existence gate

First decide whether any documentation belongs. A reader state, package,
repository root, public source, or code location is not itself evidence of a
gap. Add or retain a surface only when a named reader needs a material fact for
a real decision and cannot safely recover it from readable code, types, tests,
package metadata, existing canonical documentation, or context they genuinely
have.

If no gap remains, add nothing. Clear code needs no comment; a package needs no
README; a public source repository needs neither a public documentation home nor
a presentation page. The ladder only selects the existing or authorized home of
a fact that has earned one.

## Reader states

Reader labels describe available context, not a rank or required audience. One
person or agent can hold several states, and a coding agent may be acting as a
developer, coder, integrator, or operator. None requires its own page, README,
or comment.

| Reader state | May already know | Needs before acting, if a gap exists |
| --- | --- | --- |
| **Stranger** | Only an entry point or name; their intent may be technical, product-facing, or exploratory. | Whether the subject is relevant and the safest next route, without assumed topology, credentials, or domain knowledge. |
| **Developer** | General development practice and a task, perhaps a checkout. | System or repository scope, boundaries, and the route relevant to that task. |
| **Integrator** | A package name, manifest, import, or API and an integration goal. | Supported contract, configuration, versions, failures, and compatibility boundary. |
| **Coder** | Target code, language, nearby tests, and a change goal. | Local ownership, hidden invariant, and validation route—not a system manual. |
| **Maintainer** | Ongoing ownership and some system or history context. | Durable why, lifecycle or compatibility consequence, and responsibility boundary. |
| **Coding agent** | A task, diff, selective source, or search matches, without tacit organizational memory. | Explicit non-local constraints and canonical context only where the local view cannot make a change safe. |
| **Operator or support engineer** | Runtime access and a service or recovery goal. | Health, lifecycle, failure recovery, escalation, and operational boundaries. |
| **End user** | A desired product outcome and product access. | How to achieve it, eligibility or limits, and recovery or support routes without source assumptions. |

## Reader-context rule

For every fact, establish five things before deciding its home:

1. **Reader:** who naturally encounters this surface while doing real work?
2. **Available context:** what code, system, task, access, and prior knowledge
   can that reader reasonably have at this point?
3. **Need:** which purpose, condition, boundary, or decision would remain
   unsafe or costly to reconstruct from that context?
4. **Scope:** what can this surface state truthfully without pretending to own a
   broader contract or duplicating a narrower one?
5. **Placement:** why must the reader see this fact here, before the governed
   decision, rather than only in a parent, sibling, or later document?

Write the missing fact, not a narration of what the reader can already see.
Broader rungs orient and route; narrower rungs preserve the local consequence.
Keep detailed content with one canonical owner.

### README boundary

**README.md** names a technical orientation document at the rung it serves. It
is never a marketing or advertising landing page. A repository README, package
README, and folder README differ because their technical readers, available
context, and tasks differ—not because one is more public.

A README is optional. A package, repository root, or public source does not
create a README task when its reader can safely act from readable code, types,
metadata, and existing canonical documentation.

A public website or product landing page is a separate presentation surface with
a browser visitor's reader contract. Classify it independently. Do not transfer
its promotional structure, browser-product conversion call to action, or
source-versus-browser routing into any README. Verified technical commands,
installation steps, and task routes remain appropriate in a README. Do not
infer a presentation surface from a public repository.

## Choose a rung

1. Pass the existence gate. If no material reader gap remains, add nothing.
2. Name the actual reader and the decision or task they are about to make.
3. List only context available at that encounter: nearby code, imported API,
   checkout, package metadata, system access, or public browser page.
4. Identify the invisible fact that changes a safe decision at that point.
5. Choose the narrowest surface that every affected reader naturally encounters
   before the decision.
6. State the fact in the form that rung can support: local rationale, technical
   boundary, contract, system map, or route. Link to the canonical owner for
   deeper detail.

Do not create a missing surface without authorization. Report the placement gap
and propose the smallest useful surface instead.

## Reader-context matrix

Each row is a candidate home for a qualifying gap, not an artifact checklist.
If no row is needed, add no surface.

| Candidate rung | Reader and likely context | What the reader needs now | What this rung can tell them | Why and how it belongs here |
| --- | --- | --- | --- | --- |
| **1. Line** | A maintainer or coding agent sees one expression, branch, argument, or assignment and nearby syntax. | The non-obvious reason this exact choice, exception, or value cannot be simplified safely. | A concise local constraint, rejected alternative, or consequence. | For a qualifying hidden fact, put the reason immediately before or beside the decision; otherwise add no comment. Do not narrate syntax, types, or names already visible. |
| **2. Block** | A reader sees one guard, transformation, loop, or sequence and understands its statements in isolation. | The invariant joining the statements: ordering, atomicity, ownership transfer, intentional duplication, synchronization, or algorithmic boundary. | The block-wide purpose and the condition that must survive edits within it. | For a qualifying block-wide fact, put one comment at the block boundary; move it up when it governs more than this block. |
| **3. File** | A reader has the declarations, imports, and implementation unit, but may not know the containing subsystem. | Why this file exists, what it owns, its lifecycle or non-local relationship, and where its responsibility stops. | The cohesive implementation responsibility and a boundary that declarations cannot reliably expose. | For a qualifying unit-wide gap, use a file header or local overview; do not turn it into a declaration tour or system manual. |
| **4. Folder** | A contributor has entered an implementation area and can see sibling names and paths, usually with a checkout. | The area's purpose, ownership, organization, shared conventions, boundary with neighboring areas, and local validation route. | A technical map of the area and how to work in it safely. | When an area-wide gap remains, use an existing folder README or authorized overview; do not make it describe the project as a whole. |
| **5. Package or module** | An integrator, maintainer, or internal consumer knows the package or module name and may have its manifest, import, or public API, but not its parent system. | The unit's purpose, public or internal contract, supported entry points, configuration, lifecycle, failures, dependencies, and compatibility boundaries. | The technical contract and integration conditions for this reusable unit. | A package README is optional: readable exports, types, metadata, or a canonical reference may already suffice. When a reader gap remains, it may include verified installation and use without becoming a product advertisement. |
| **6. Domain or service** | An engineer, operator, or collaborator works across several packages and knows the wider product area, but not every implementation detail. | Responsibility and ownership, major flows, cross-unit contracts, state, lifecycle, failures, operational entry points, and escalation boundaries. | A map of one capability or service and routes to the owning packages, APIs, and operations material. | When a cross-unit gap remains, keep mechanics in their canonical package or file owner; document the collaboration and boundary here. |
| **7. Top level** | A technical reader arrives at a repository, system, or documentation root with little or no topology knowledge. They may know the project's name and their own task, but not its internals. | What the system or repository is for, its scope and major boundaries, its technical audience, the relevant starting route, and where deeper detail lives. | A technical orientation: system map, supported technical entry points, global constraints, and routes for using, contributing to, operating, or learning the system. | When an existing or authorized top-level technical surface is needed, keep it broad and factual; do not duplicate package mechanics, infer a browser journey, or turn the README into an advertisement. |

The matrix is deliberately asymmetric: each higher rung can explain a wider
relationship, but must not overwrite the detailed contract of a lower owner.
Each lower rung can preserve a closer rationale, but must not reconstruct the
whole system.

### Public documentation home

A public documentation home, when one exists or is authorized, uses the
top-level orientation rung for a reader who arrived to find documentation, not
to evaluate a product. It may state the
documentation map, topic boundaries, and routes to tutorials, how-tos,
explanations, and reference. Validate that navigation or lookup path. Do not
give it a product-presentation posture merely because it is browser-delivered.

## Overlapping rungs

Physical layout and logical scope do not always align. A language module can be
a file, a package can be a folder, and a one-service repository can also be the
top-level system. One technical document may therefore contain sections serving
more than one rung.

Classify each section by reader and governed scope. Make different roles
scannable, keep one canonical owner for detail, and co-locate only when the
scopes genuinely coincide. Do not manufacture files or repeat prose merely to
make the ladder look physically nested.

## Three heuristics

### A map is not the territory

Source and runtime behavior are the territory and evidence. Documentation is a
selective map for a reader and task. Expose purpose, relationships, observable
contract, and boundaries that raw implementation does not give that reader; do
not transcribe implementation.

### Chesterton's fence

A Chesterton's fence is code whose reason for existing or present form is
unknown: an island of uncertainty.

Search history, callers, tests, runtime effects, and neighboring invariants for
the missing rationale. If evidence verifies it, document the non-local reason
at the rung where it governs a decision. If it remains unknown and the gap is
accepted, mark it with an explicit **TODO** or **FIXME**. Never invent rationale.

### Mark reefs, not cliffs

Document hazards hidden below the reader's normal view: non-obvious defaults,
failure modes, security or ownership boundaries, lifecycle coupling, and
cross-unit invariants. Do not mark cliffs already visible in code, types, names,
signatures, or the surrounding surface. Visibility changes by rung, so judge
from the reader context in the matrix.

## Movement tests

- **Reader:** Who encounters this before the governed decision, and what can
  they genuinely see or know there?
- **Existence:** Does a material fact remain unavailable from the reader's
  present context and existing canonical surfaces? If not, add nothing.
- **Need:** Which unsafe inference or expensive reconstruction does the fact
  prevent for that reader?
- **Scope:** Does the fact govern a wider or narrower unit than this surface?
- **Capability:** Is this surface asserting only a local rationale, technical
  boundary, contract, system map, or route that it can own?
- **Placement:** Would moving it leave an affected reader without the fact when
  they need it, or would keeping it duplicate the canonical owner?
- **README separation:** Has a technical README been kept separate from any
  public website presentation page and its visitor journey?
