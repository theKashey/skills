# Blocks, Levels, and Documentation Formats

File placement is fixed by the canonical layout in `SKILL.md` §File Layout (directory-as-zoom under the project's declared chart root). This reference defines the *contents* of those files.

## Block Definition

A block is any architectural unit with identity, boundary, and interface. Blocks exist at every level:

```
L0  block = bounded context, aggregate
L1  block = actor, external system
L2  block = isolated block (app, module, subsystem, database)
L3  block = component (service, repository, gateway)
```

Not everything is a block. Infrastructure, utilities, and shared helpers are the ground (L5). Forcing block identity onto shared code creates false boundaries.

## BEM Principle (Block–Element–Modifier)

A block describes only itself. A parent defines why it uses a block. Relationship context never lives in the block's self-document — it lives in the consumer.

---

## SCOPE.md Template

The first chart file written (Phase 0), and the first one a reader opens.

```
Scope — one sentence: what is the system
Systems — the L1 folder(s) under this chart root, linked; normally one
Out of scope — what a reader might expect here but must not look for
```

---

## Compass Registry Template

`COMPASS.md` is tiered — true L1 entries in one table, demoted L2/L3 externals in a second, human-declared lens roots in a third — so a demotion stays recorded, nothing gets silently re-elevated, and every second stack has a named owner:

```markdown
# Compass

## Systems and L1 externals — every external here passed both L1 tests
| Name | Owner | Scope boundary | Shared domain terms | Stack |
|---|---|---|---|---|
| [{name}](externals/{name}.md) | {who} | {one sentence: what is inside} | {terms} | {link to its own chart root, or —} |

For an external, the Name cell links to this chart's `externals/{name}.md`; for a system in scope, to its `{system}/CONTEXT.md`. `Stack` links to the entry's own chart root if it publishes one — a different destination.

## Touched externals (L2/L3 tier) — named here, documented in the adapter that uses them
| Name | Used by | Why not L1 |
|---|---|---|
| {name} | {component address} | {which L1 test it fails} |

## Lenses — human-declared second stacks
| Name | Owner | Why a separate stack |
|---|---|---|
| {lens-root} | {the human who declared it} | {what makes its L1 sound} |
```

---

## L0 — Domain Model

**Format:** Prose markdown. No code. Context map in mermaid is acceptable.

**Contains:** Bounded contexts with ubiquitous language. Aggregates and value objects per context. Invariants per aggregate. Context map with relationship types (upstream/downstream, shared kernel, ACL, customer/supplier, conformist). Domain events crossing context boundaries. This is Domain-Driven Design's strategic vocabulary (Evans), unmodified — recruit that prior; compass adds nothing to it.

**Does not contain:** Technology, code paths, database schemas, API shapes.

**Written by:** Agent, from human-taught domain knowledge. Agent scans codebase, identifies candidate bounded contexts from naming patterns, import clusters, and data flow, presents as falsifiable claims. Human confirms, corrects, or redraws boundaries; the agent writes the document.

**Revision trigger:** New bounded context emerges, two contexts merge, or ubiquitous language shifts. Human initiates.

Each bounded context is a `##` heading inside `DOMAIN.md` — the link target for `COMPONENT.md` bounded-context entries. Concepts are subsections within their context; neither contexts nor concepts get separate files.

### L0 domain concept doc format

```
Name
What it is — one or two sentences, domain language only
Invariants — what must always be true
Lifecycle — states it moves through (if entity)
Composed of — value objects and entities within
Domain events — what it publishes when things happen
```

No technology. No storage. No code paths.

---

## L1 — System Context

**Format:** Mermaid context diagram + brief prose per actor.

**Contains:** The system as one box. 2–5 actors (human-defined). External systems (discovered from dependencies, named per compass). Relationships with verb labels. Each external system links to its own documentation stack if one exists.

### CONTEXT.md format

```
Scope — the one-sentence scope, restated from SCOPE.md
Diagram — mermaid: the system as one box, actors, L1 externals, labelled edges
Actors — one line of prose per actor (2–5, human-defined)
External systems table — one row per L1 external: name linked to
  ../externals/{name}.md, what crosses the boundary
```

The external systems table is what the L1 external-system checks run over.

### Level Promotion Criteria

Use these tests before assigning anything to a level. Default down when uncertain.

**To appear at L1 (external system):**
- Both L1 tests pass — User-Possession and Control Boundary (defined in `SKILL.md` §L1 Abstraction Guardrails, checked via the L1 checklist in [`verification.md`](verification.md))
- It has an identity independent of this system (it exists without you)
- The system's value proposition explicitly includes integrating with or serving it

**To appear at L2 (isolated block):**
- It is internal to the system boundary
- It owns a persistent responsibility and a code root directory
- It could be replaced or redesigned without changing the L1 context diagram

**To appear at L3 (component):**
- It is a logical module within one L2 block
- It maps directly to code paths
- It is not user-visible as a top-level service

**Default rule:** when unsure, go one level down — an unsure external → L3 adapter (externals never get block documents); an unsure internal L2 candidate → L3. Promote only with explicit justification.

**Contrast examples (same entity, different scopes — level assignment is relative to scope):**
- **Issue tracker** → **L1** when building a plugin *inside* that tracker (it's the platform); **L3 adapter** when the system only files tickets incidentally via an internal gateway
- **Local database file** → **L1** when the user owns it, can back it up, inspect it, migrate it (it outlives the process); the *engine* (SQLite, Postgres) that reads it is always **L3**
- **ML runtime** → **L1** for an ML platform product the user subscribes to; **L3** when it's the internal inference mechanism the system uses to compute outputs

Before adding any node to the L1 external systems table, run the external system checks in [`verification.md`](verification.md) §L1 System Context Verification — every item must pass.

### External system doc format (L1 doc, or embedded in the demoted external's adapter)

```
Name — must match the compass entry
What it is — its nature, not what it does for you
Good at — the grain it works with
Bad at — the grain it fights
How it breaks — actual failure modes
How you talk to it — protocol, interface
Their stack — link to this system's own L0-L4 documentation (if it exists)
```

---

## Markdown Link Convention

**All cross-references in chart docs MUST use markdown links — never plain backtick names.**

This applies to every level:
- `CONTAINERS.md` container table entries → link to `{container}/BLOCK.md`
- `BLOCK.md` communicates-with entries → link to sibling `../other-container/BLOCK.md` or `../other-container/{component}/COMPONENT.md`
- `COMPONENT.md` depends-on / used-by entries → link to `../../other-container/BLOCK.md` or sibling `../other-component/COMPONENT.md`
- `COMPONENT.md` bounded-context entry → link to that context's heading in `DOMAIN.md`
- `VIEWPORTS.md` participant names → link where possible

**Why:** Markdown links make the docs navigable by humans and agents without grep. A plain backtick name is a dead end; a link is a hop.

**Format examples:**

```markdown
## Communicates-with

- → [`api-client`](../api-client/BLOCK.md) — `getSystemStatus()` every 5s for live backend connection state
- → [`design-system`](../design-system/BLOCK.md) — `PageBoundary`, layout primitives
- ← [`billing-core`](../../order-core/billing-core/BLOCK.md) — receives `InvoiceIssued` via the order event stream
```

```markdown
## Depends-on

- [`event-bus`](../event-bus/COMPONENT.md) — Event routing
- [`pricing-engine`](../../pricing-engine/BLOCK.md) — `PriceQuote` protocol
```

**Rule:** If you cannot form a relative link because the target doesn't exist yet, write the name in backticks and add `<!-- TODO: link when created -->` — do not leave it as plain text.

---

## L2 — Isolated Blocks

**Format:** Mermaid flowchart + block documents.

**Contains:** Major isolated parts within the system boundary. External systems (referenced). Technology choices per block. Communication between blocks.

Each isolated block gets a block document; external systems never do — an L1 external is documented in `externals/{name}.md`, and a demoted external inside the adapter that uses it. Consumer relationships documented in the consuming block.

**Written by:** Agent proposes from project structure. Human confirms.

### CONTAINERS.md format (L2 overview)

```
Purpose — one sentence: how the system is decomposed and why along this seam
Container table — one row per container: name linked to its BLOCK.md,
  responsibility (one sentence)
Diagram — mermaid: every container and what crosses each boundary (the wiring)
```

The container table and the diagram show the same set — a container present in one and missing from the other is drift.

### L2 isolated block doc format

```
Name
Responsibility — what this block owns
Root — filesystem subtree (e.g. Sources/Billing/, src/components/timeline/)
Technology — language, framework, runtime
Boundary — what it does NOT do
Communicates with — other blocks, protocol, direction
Components — table of the block's L3 components, each linked to its
  COMPONENT.md, plus any subtree recorded as L5 infrastructure — not attributed
Diagram — mermaid: the block's components and what crosses its boundary
```

Root is the agent's entry point. An agent reading an L2 document should be able to map the block to a directory without searching.

---

## L3 — Components

**Format:** Mermaid flowchart per block + component documents.

**Contains:** Logical modules within one isolated block. Dependencies between components. Mapping to code paths. Leaks, debt, and boundary violations (honest). Color-coded diagrams (red=leak, yellow=debt).

Each L3 component must reference which L0 bounded context it serves. If a component serves two contexts, that's a finding. Bounded contexts have no address — addresses run from L1 down — so a component names its context by that context's heading in `DOMAIN.md` and links to it.

**Written by:** Agent, validated by human. Use dependency tooling (not file reading) to discover actual relationships. When unavailable, import scanning (grep, build adjacency list manually).

### L3 component doc format

```
Name
«stereotype» — service, entity, repository, handler, gateway, factory
Responsibility — one sentence; if you need two, the module does too much
Bounded context — the one L0 context this component serves, linked to its
  heading in DOMAIN.md; two contexts is a finding, not a longer field
Inputs / Outputs — what crosses the boundary
Depends on — other blocks
Used by — what consumes this block
Boundary — what it does NOT do
Code paths — directories, key files, entry functions
  `e.g. OrderService.swift, InvoiceRepository.save(),
  Sources/Billing/Pipeline/`
Diagram — mermaid: who calls it and what it calls
```

Code paths are the agent's grep targets. An agent reading an L3 document should be able to open the right file without scanning the codebase.

---

## L4 — Viewports

L3 answers "what exists." L4 answers "how does it work across boundaries."

### Viewport types

**Runtime** — internals of one execution environment in isolation. Create when a block's L3 components alone don't convey how they work together.

**Domain** — one aggregate traced across all blocks. Horizontal cut. Shows different projections, reveals misalignments. Create when a shared kernel concept has meaningfully different representations in different blocks.

**Boundary** — contract between two isolated blocks. What crosses, in what shape, through what mechanism. The first viewport type to create when L4 is warranted: every communicating pair is a candidate, within the 3–4 cap — the skip rule still wins for small, loosely coupled systems.

**Lifecycle** — data from creation to consumption. Diagonal cut. Create when debugging requires understanding a full data path.

### Creating a viewport

1. Start with a question. No question = no viewport.
2. Trace the path through L3 documents. Note participants, order, interfaces.
3. Draw focused mermaid diagram. Annotate data shapes where they change.
4. Document seams: concrete types, serialization functions, bridging types, entry points on receiving side.
5. Name for the question: `order-lifecycle` not `frontend-backend-database-flow`.

### Using a viewport

1. Identify which viewport covers your change.
2. Read current path.
3. Do the work.
4. Check: does the viewport still describe reality?
5. If not, update the viewport.

### Limits

3–4 active viewports max. Skip L4 if L3 is small, clear, and loosely coupled.

---

## L5 — Infrastructure / Shared Code

Not documented at architecture level. Acknowledged in the enclosing block's `BLOCK.md` component table as "infrastructure — not attributed", which is what makes the L5 exemption in the Phase F gate explicit.

These are the floor: formatters, loggers, config loaders, generic UI components, shared type definitions. If infrastructure becomes complex enough to need docs, promote to L3.

---

## Shared Kernel

The shared kernel is **domain concepts**, not infrastructure. Not the database schema, not the API contract, not the wire format.

**Contains:** Named concepts with plain-language definitions. Invariants that hold regardless of implementation. Which bounded contexts share each concept.

**Does not contain:** Types, structs, interfaces. Database columns or schemas. API shapes or wire formats. Code paths.

Each side produces its own **projection** of the kernel. The backend projects a domain concept into a class or struct, the frontend into a view model type, and persistence into tables or documents. All valid, all different, all derived from the same kernel concept.

Validation: type checking, tests, and annotation-based tooling — not document cross-references.

---

## Consumer Relationship

When block A uses block B, the relationship is documented in A, never in B.

```
Uses: <BlockName>
  Why — the decision, the tradeoff
  What I need from it — specific capabilities relied upon
  What would make me leave — conditions for replacement
```
