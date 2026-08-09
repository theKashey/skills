# Roots, Blocks, Levels, and Documentation Formats

File placement is fixed by the canonical layout in `SKILL.md` §File Layout (directory-as-zoom under the project's declared chart root). This reference defines the *contents* of those files.

Every semantic entity defined here must first pass the rewrite test in `SKILL.md` §The Rewrite Test, and every semantic boundary change must run the invariance test in §The Invariance Test. Those two gates are not restated below.

## Block Definition

A block is any architectural unit with identity, boundary, and interface. Blocks exist at every level:

```
L0  block = bounded context, aggregate
L1  block = actor, external system
L2  block = isolated block (app, module, subsystem, database)
L3  block = component (service, repository, gateway)
```

Not everything is a block. Infrastructure, utilities, and shared helpers are the ground (L5). Forcing block identity onto shared code creates false boundaries.

---

## Roots

A **root** is a stable logical starting point from which *where am I?* has a useful independent answer. The five-part admission test and the rebuild-from-scratch challenge live in `SKILL.md` §Scope and Roots. This section covers what roots look like in practice.

Roots do not correspond to repositories, deployables, services, folders, or C4 systems. Nothing about a package boundary, a separate service, or a second language creates a root; only independent logical identity does.

### Valid multi-root cases

**Two products in one monorepo** — unrelated logical systems sharing a repository:

```text
COMPASS
├── Customer Product
└── Merchant Product
```

**A substantial domain inside larger product scaffolding** — the domain is a block of the product *and* a root in its own right:

```text
Product
└── Payments
```

may coexist with:

```text
Payments
├── Authorisation
├── Capture
├── Refunds
└── Reconciliation
```

**A top-level or "secret sauce" domain** surrounded by ordinary scaffolding:

```text
Product
├── Accounts
├── Admin
├── Billing
└── Ranking Engine
```

may expose an independent root:

```text
Ranking Engine
├── Candidates
├── Eligibility
├── Ranking
└── Feedback
```

### Overlap is expected

The last two cases overlap deliberately: the same logical material appears as an interior block of one root and as the whole of another. That is what multi-coordinate attribution records — the same code carries `compass: product.payments` and `compass: payments.authorisation.card-routing`, and both are true. Overlap is not duplication to be resolved; it is two useful orientations over one system.

Roots do not need to agree with each other on naming, levels, or boundaries. The registry connects them.

### Root lifecycle

- **Proposing.** An agent may propose a root, with the five admission answers and evidence from product or domain reality. It writes nothing until a human ratifies.
- **Ratifying.** A human ratifies; the root gets a row in `COMPASS.md` and a `{root}/` directory. Who ratified it, and when, belong to the commit that added the row.
- **Retiring.** A root that no longer earns independent orientation is retired by a human, and its row is removed — that it once existed is the commit history's job, and the ratification gate is what stops a retired root from coming back silently. (A demoted dependency keeps its row for exactly the missing half of that guard: nothing gates re-elevation but the record.) Its coordinates are remapped, not deleted in place.

---

## BEM Principle (Block–Element–Modifier)

A block describes only itself. A parent defines why it uses a block. Relationship context never lives in the block's self-document — it lives in the consumer.

---

## Markdown Conventions

### Semantic fields are Markdown structure

Every semantic field is a heading. Sets are lists, homogeneous collections are tables, navigation is links, diagrams are Mermaid. Never encode a field as prose punctuation:

```markdown
<!-- wrong: the schema is invisible to the Markdown AST -->
Responsibility — computes the price a customer will be charged
Boundary — does not take payment

<!-- right -->
## Responsibility

Computes the price a customer will be charged.

## Boundary

Does not take payment.
```

An agent reading a chart document should recover its schema from the heading structure, not from parsing dashes out of sentences.

**Where a bold-labelled bullet is admissible.** `- **name** — note` is correct when the bullets are *instances of one kind* and the bold text is an instance's name: a list of dependencies, actors, or communicating blocks. It is wrong when the bullets are *distinct named fields* of one entity — that is the pseudo-field form wearing a list marker, and it hides the schema exactly the same way. Fields become headings however deeply they nest.

### Cross-references are Markdown links

**All cross-references in chart docs MUST use markdown links — never plain backtick names.** A plain backtick name is a dead end; a link is a hop, and it makes the docs navigable by humans and agents without grep.

- `CONTAINERS.md` block table entries → link to `{block}/README.md`
- Block "Communicates with" entries → link to a sibling `../other-block/README.md` or `../other-block/{component}/README.md`
- Component "Depends on" / "Used by" entries → link to `../../other-block/README.md` or a sibling `../other-component/README.md`
- Component "Bounded context" entry → link to that context's heading in `DOMAIN.md`
- Glossary "Bounded context" entry → link to that context's heading in `DOMAIN.md`
- `VIEWPORTS.md` participant names → link where possible

```markdown
## Communicates with

- → [`api-client`](../api-client/README.md) — `getSystemStatus()` every 5s for live backend connection state
- → [`design-system`](../design-system/README.md) — `PageBoundary`, layout primitives
- ← [`billing-core`](../billing-core/README.md) — receives `InvoiceIssued` via the order event stream
```

Every entry above is written from a block document, so every hop is one level (`../sibling/`). From a component document the same sibling block is two levels up (`../../other-block/README.md`) — count from the document you are writing in, not from the example.

**Rule:** If you cannot form a relative link because the target doesn't exist yet, write the name in backticks and add `<!-- TODO: link when created -->` — do not leave it as plain text.

### Semantic rendering

When a term defined in the root's `GLOSSARY.md` is used semantically in chart prose, render it in **bold**:

```markdown
A **Matter** contains **Documents** and may produce **Findings**.
```

Bold marks *this word carries its glossary meaning here*. Never bold filenames, paths, source identifiers, code, or Mermaid syntax — those take backticks, links, or code fences.

---

## `{chart-root}/README.md` Template

The first chart file written (Phase 0), and the first one a reader opens. It answers *where am I?* for the chart as a whole.

```markdown
# {chart name}

## Scope

One sentence: what is the system this chart covers.

## Roots

| Root | What it is | Chart |
|---|---|---|
| {name} | {one sentence} | [{name}/](./{name}/README.md) |

## Out of scope

What a reader might expect here but must not look for.

## Navigating

Registry: [COMPASS.md](./COMPASS.md). Every architectural directory's
identity document is its `README.md`.
```

---

## Compass Registry Template

`COMPASS.md` is tiered — roots in one table, external systems in a second, named dependencies that are not external systems in a third — so a demotion stays recorded and nothing gets silently re-elevated:

```markdown
# Compass

## Roots

| Root | What it is | The orientation it gives |
|---|---|---|
| [{name}](./{name}/) | {one sentence} | {the independent answer it gives to *where am I*} |

## External systems

| Name | Owner | Scope boundary | Shared domain terms | Their chart |
|---|---|---|---|---|
| [{name}](externals/{name}.md) | {who — point into a live ownership source where one exists} | {one sentence: what is inside} | {terms} | {link to its own chart root, or —} |

## Named dependencies that are not external systems

| Name | Used by | Why it is not one |
|---|---|---|
| {name} | {component address} | {the fact about the dependency — not the name of the test it failed} |
```

**Ratification is a gate on the work, not a column in the artifact.** A root still requires a human before an agent writes it, and that requirement is stated where it governs behaviour: the boundaries in `SKILL.md`, and the state-0 checkpoint in `references/growth-and-drift.md`. It does not belong in `COMPASS.md`, because who approved a boundary and when is a fact about the chart's production rather than about the system. The same reasoning excludes three fields a registry attracts:

- **`Registry owner:`** — a page-ownership line answers no question a reader of the chart has, and it is a field nobody ever changes.
- **`Ratified by` / `Status`** — provenance and lifecycle metadata. A retired root is removed from the table; that it once existed is the commit history's job.
- **Headings naming the method** — *"human-ratified logical roots of orientation"*, *"every external here passed both L1 tests"*. A chart that explains the procedure it was built by teaches every reader that the artifact is about its own production. State the fact about the subject: what a root is, and why a thing is outside the boundary.

Give the reason a dependency is not an external system in terms of the dependency — *"an engine for a model we deploy"*, *"nobody who works with this system would name it as a tool they use"* — rather than as a test name. The tests are how **you** decide; the reason is what the **reader** needs.

For an external, the Name cell links to this chart's `externals/{name}.md`; `Their chart` links to the entry's own chart root if it publishes one — a different destination.

---

## L0 — Domain Model

**Format:** Prose markdown under semantic headings. No code. Context map in mermaid is acceptable.

**Contains:** Bounded contexts with their ubiquitous language. Aggregates and value objects per context. Invariants per aggregate. Context map with relationship types (upstream/downstream, shared kernel, ACL, customer/supplier, conformist). Domain events crossing context boundaries. This is Domain-Driven Design's strategic vocabulary (Evans), unmodified — recruit that prior; compass adds nothing to it.

**Does not contain:** Technology, code paths, database schemas, API shapes, implementation coordinates.

**Written by:** Agent, from human-taught domain knowledge and product/domain evidence. The agent scans the codebase for candidates and presents them as falsifiable claims; the human confirms, corrects, or redraws boundaries; the agent writes the document. Code proposes; product and domain reality ratify.

**Revision trigger:** New bounded context emerges, two contexts merge, or ubiquitous language shifts — a semantic change, never a repository reorganization. Human initiates.

Each bounded context is a `##` heading inside `DOMAIN.md` — the link target for component and glossary entries. Under it, concepts are `####` headings beneath one `### Concepts` container, and their fields are `#####`; neither contexts nor concepts get separate files.

### DOMAIN.md format

```markdown
# Domain — {root}

## {Bounded Context}

### What it is

One or two sentences, domain language only.

### Concepts

#### {Concept}

##### What it is

One or two sentences.

##### Invariants

What must always be true.

##### Lifecycle

States it moves through, if an entity.

##### Composed of

Value objects and entities within.

##### Domain events

What it publishes when things happen.

### Relationships

- → [{Other Context}](#other-context) — {upstream/downstream, ACL, shared kernel, …}

## Context map

Mermaid context map (optional).
```

No technology. No storage. No code paths.

---

## GLOSSARY.md Format

`{root}/GLOSSARY.md` is the canonical owner of that root's ubiquitous language. Every local product or domain term used architecturally must appear here. Implementation terminology belongs here only when humans genuinely use it as part of the domain — otherwise it is recorded as an alias.

One `##` heading per term, the term itself in bold:

```markdown
# Glossary — {root}

## **Matter**

### Meaning

A unit of legal work handled for a client.

### Bounded context

[**Matter Management**](./DOMAIN.md#matter-management)

### Product appearance

Appears as a matter in the matter list and workspace.

### Implementation aliases

`Case`, `MatterRecord`
```

**Context-specific meaning.** Do not force globally unique definitions. When the same word means different things in different bounded contexts, give the term one `##` heading with one `### Meaning` / `### Bounded context` pair per context, each labelled — the collision is a fact about the domain, and hiding it behind one blended definition loses it.

**Implementation aliases** record where code and product disagree. The product or domain term is canonical; the code term is the alias, never the reverse. When the difference is discovered during exploration, record it rather than resolving it silently:

```text
Product/domain language: **Workspace**
Implementation language: `Tenant`

Canonical Compass language: **Workspace**
Implementation alias: `Tenant`
```

---

## L1 — System Context

**Format:** Mermaid context diagram + brief prose per actor.

**Contains:** The root as one box. 2–5 actors (human-defined). External systems admitted by the two L1 tests. Relationships with verb labels. Each external system links to its own documentation stack if one exists.

L1 describes a recognizable interaction surface, not a dependency inventory. Actors are the people, organisations, and roles humans would name when asked who uses this; external systems are the things they would name as tools and services they possess. A dependency manifest is evidence about mechanism, never an L1 admission.

### `{root}/README.md` format (L1)

```markdown
# {Root}

## Scope

One sentence: what this root is.

## Diagram

Mermaid: the root as one box, actors, L1 externals, labelled edges.

## Actors

- **{Actor}** — one line: who they are and what they get out of the system

## External systems

| System | What crosses the boundary |
|---|---|
| [{name}](../externals/{name}.md) | {data or action} |

## Inside this root

- [Domain](./DOMAIN.md) — bounded contexts and context map
- [Glossary](./GLOSSARY.md) — ubiquitous language
- [Blocks](./CONTAINERS.md) — how the root is decomposed
- [Viewports](./VIEWPORTS.md) — cross-cutting flows (omit this line until
  VIEWPORTS.md exists; L4 may be skipped)
```

The external systems table is what the L1 external-system checks run over.

### Level Promotion Criteria

Use these tests before assigning anything to a level. Default down when uncertain.

**To be a root:** the five-part admission test in `SKILL.md` §Scope and Roots, all five, with a human ratification.

**To appear at L1 (external system):**
- Both L1 tests pass — User-Possession and Control Boundary (defined in `SKILL.md` §L1 Abstraction Guardrails, checked via the L1 checklist in [`verification.md`](verification.md))
- It has an identity independent of this system (it exists without you)
- The root's value proposition explicitly includes integrating with or serving it

**To appear at L2 (isolated block):**
- It is internal to the system boundary
- It owns a persistent logical responsibility that maps upward to a stable responsibility or phenomenon of the root
- Its identity survives a structure-only refactor (invariance test)
- It could be replaced or redesigned without changing the L1 context diagram

**To appear at L3 (component):**
- It is a logical module within one L2 block
- It maps to code paths
- It is not user-visible as a top-level service

**Default rule:** when unsure, go one level down — an unsure external → L3 adapter (externals never get block documents); an unsure internal L2 candidate → L3. Promote only with explicit justification.

**Contrast examples (same entity, different scopes — level assignment is relative to scope):**
- **Issue tracker** → **L1** when building a plugin *inside* that tracker (it's the platform); **L3 adapter** when the system only files tickets incidentally via an internal gateway
- **Local database file** → **L1** when the user owns it, can back it up, inspect it, migrate it (it outlives the process); the *engine* (SQLite, Postgres) that reads it is always **L3**
- **ML runtime** → **L1** for an ML platform product the user subscribes to; **L3** when it's the internal inference mechanism the system uses to compute outputs

Before adding any node to the L1 external systems table, run the external system checks in [`verification.md`](verification.md) §L1 System Context Verification — every item must pass.

### External system doc format

`externals/{name}.md` for an L1 external; the same fields embedded in the adapter's own document for a demoted one.

```markdown
# {Name}

Must match the compass entry.

## What it is

Its nature, not what it does for you.

## Good at

The grain it works with.

## Bad at

The grain it fights.

## How it breaks

Actual failure modes.

## How you talk to it

Protocol, interface.

## Their chart

Link to this system's own chart, if it publishes one.
```

---

## L2 — Isolated Blocks

**Format:** Mermaid flowchart + block documents.

**Contains:** Major isolated parts within the root's boundary. External systems (referenced). Technology choices per block. Communication between blocks.

Each isolated block gets a block document; external systems never do — an L1 external is documented in `externals/{name}.md`, and a demoted external inside the adapter that uses it. Consumer relationships documented in the consuming block.

**Written by:** Agent proposes from structural evidence and product/domain reality. Human confirms.

**A block's identity is semantic; its technology and code paths are coordinates.** Implementation decomposition is not product decomposition: decomposing one block into several services, merging two services, or replacing a framework changes coordinates only. A block splits or merges when its *logical responsibility* splits or merges.

### CONTAINERS.md format (L2 overview)

```markdown
# Blocks — {root}

## Decomposition

One sentence: how the root is decomposed and why along this seam.

## Blocks

| Block | Responsibility |
|---|---|
| [{name}](./{name}/README.md) | {one sentence} |

## Diagram

Mermaid: every block and what crosses each boundary (the wiring).
```

The block table and the diagram show the same set — a block present in one and missing from the other is drift.

### `{block}/README.md` format (L2 self-doc)

```markdown
# {Block}

## Responsibility

What this block owns.

## Logical role

Which stable responsibility or phenomenon of the root this block realizes —
stated without reference to source topology.

## Boundary

What it does NOT do.

## Technology

Language, framework, runtime. Coordinate detail: expected to change.

## Implementation coordinates

Filesystem subtree(s) this block currently occupies, e.g.
`Sources/Billing/`, `src/components/timeline/`. May be several, across
packages or services. Coordinate detail: expected to change.

## Communicates with

- → [`{block}`](../{block}/README.md) — {protocol, what crosses}
- ← [`{block}`](../{block}/README.md) — {protocol, what crosses}

## Uses

One `###` per block this block depends on, with Why / What I need from it /
What would make me leave — see §Consumer Relationship. Outbound (`→`)
communications need an entry here; inbound ones belong to the caller.

## Components

| Component | Responsibility |
|---|---|
| [{name}](./{name}/README.md) | {one sentence} |
| `{subtree}` | L5 — {what it is: formatter, logger, config loader, generic UI, shared types} |

## Diagram

Mermaid: the block's components and what crosses its boundary.
```

Implementation coordinates are the agent's entry point. An agent reading a block document should be able to reach code without searching — and should read a changed subtree as a remapping, not as evidence the block is wrong.

---

## L3 — Components

**Format:** Mermaid flowchart per block + component documents.

**Contains:** Logical modules within one isolated block. Dependencies between components. Mapping to code paths. Leaks, debt, and boundary violations (honest). Color-coded diagrams (red=leak, yellow=debt).

Each L3 component must reference which L0 bounded context it serves. If a component serves two contexts, that's a finding. Bounded contexts have no address — addresses run from the root down — so a component names its context by that context's heading in `DOMAIN.md` and links to it.

L3 is the coordinate layer: it is expected to move, split, and be renamed as the implementation changes, and doing so is not a semantic event.

**Written by:** Agent, validated by human. Use dependency tooling (not file reading) to discover actual relationships. When unavailable, import scanning (grep, build adjacency list manually).

### `{component}/README.md` format (L3)

```markdown
# {Component}

«service» | «entity» | «repository» | «handler» | «gateway» | «factory»

## Responsibility

One sentence. If you need two, the module does too much.

## Bounded context

[{Context}](../../DOMAIN.md#context) — exactly one. Two contexts is a
finding, not a longer section.

## Inputs and outputs

What crosses the boundary.

## Depends on

- [`{name}`](../{name}/README.md) — {what it relies on}

## Used by

- [`{name}`](../{name}/README.md) — {what it provides}

## Boundary

What it does NOT do.

## Implementation coordinates

Directories, key files, entry functions — e.g. `OrderService.swift`,
`InvoiceRepository.save()`, `Sources/Billing/Pipeline/`.

## Diagram

Mermaid: who calls it and what it calls.
```

Implementation coordinates are the agent's grep targets. An agent reading a component document should be able to open the right file without scanning the codebase.

---

## L4 — Viewports

L3 answers "what exists." L4 answers "how does it work across boundaries."

### Viewport types

**Runtime** — internals of one execution environment in isolation. Create when a block's L3 components alone don't convey how they work together.

**Domain** — one aggregate traced across all blocks. Horizontal cut. Shows different projections, reveals misalignments. Create when a shared kernel concept has meaningfully different representations in different blocks.

**Boundary** — contract between two isolated blocks. What crosses, in what shape, through what mechanism. The first viewport type to create when L4 is warranted: every communicating pair is a candidate, within the 3–4 cap — the skip rule still wins for small, loosely coupled systems.

**Lifecycle** — data from creation to consumption. Diagonal cut. Create when debugging requires understanding a full data path.

### VIEWPORTS.md format (L4)

All of a root's viewports live in one `VIEWPORTS.md`, one `##` per viewport, named for its question. The 3–4 cap counts those headings.

```markdown
# Viewports — {root}

## {question the viewport answers}

Type: runtime | domain | boundary | lifecycle

### Question

The concrete question that justified this viewport.

### Participants

- [`{component}`](./{block}/{component}/README.md) — {its part in the flow}

### Diagram

Mermaid. Sequence for runtime and lifecycle; the shape that fits the cut for
domain and boundary.

### Seams

Concrete types, serialization functions, bridging types, and the entry point on
the receiving side, at each place the data shape changes.
```

A viewport whose `### Question` is missing has no reason to exist — retire it rather than backfilling a question to match the diagram.

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

## L5 — The Floor

Formatters, loggers, config loaders, generic UI components, shared type definitions. Compass does not describe them: they carry no logical responsibility, so there is nothing for a semantic chart to say. Whether and how they are documented for a code reader belongs to Context Docs, not here.

The one thing Compass needs from the floor is a closable coordinate gate. A subtree recorded in its block's component table as `L5 — {what it is}` is exempt from coordinates; the naming is what stops the exemption from becoming a hatch that swallows un-attributed components.

---

## Consumer Relationship

When block A uses block B, the relationship is documented in A, never in B. It lives under `## Uses` in A's `README.md`, one `###` per block used:

```markdown
## Uses

### [{BlockName}](../{block}/README.md)

#### Why

The decision, the tradeoff.

#### What I need from it

Specific capabilities relied upon.

#### What would make me leave

Conditions for replacement.
```

`## Communicates with` records *that* A and B talk and what crosses; `## Uses` records *why* A accepted the dependency and what would end it. A block that lists a communication with no matching `## Uses` entry has recorded the wire and lost the decision — the L2 gate checks for this.

The "why" recorded here is a logical dependency reason and belongs to Compass. A reason that would disappear if the same product were reimplemented belongs to Context Docs instead — see [`ownership-boundary.md`](ownership-boundary.md).
