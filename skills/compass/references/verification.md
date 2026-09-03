# Verification Procedures

Formal checks that must pass before ratifying a root, advancing L0, L1, L2, L3
(including the blind semantic read), or Phase F, or changing an opted-in named
abstraction. Run the applicable checks as a mandatory gate — not optional
polish. Each completion checklist
below is canonical; other procedures point to the applicable section rather
than restating its items. Levels and phases with no section below carry no gate
beyond their exit conditions in [`exploration.md`](exploration.md) and
[`growth-and-drift.md`](growth-and-drift.md).

---

## First: the mechanizable checks belong to the host's test suite

**An agent ticking its own checkbox is self-certification, and the items the table below maps need no judgment at all.** They are decidable by a script, they go stale silently, and the moment they live in a checklist they are only as reliable as the attention of whoever last ran it. Install them in the host's own test suite during Phase B, so they fail a build rather than waiting for a review. They keep their checklist rows all the same — installing the check is ask-first (`create.md` §Boundaries), and before it lands the rows are run by hand like everything else — but once the script is in CI, a green run is the only honest tick:

The manual fallback does not apply to the named-abstraction trial. Before its
first definition or source claim, the host test suite must own an installed,
adapted checker and repository-native fixtures for a valid claim, an invalid
slug, a missing definition, malformed spacing or a multiline claim, an
unsupported form, and a supported marker in a hidden source directory. Record
the exact commands in the nominated trial record. Those fixtures are files
containing deliberately invalid marker literals, so they live under one path the
trial record names, and the checker and the raw-hit audit exclude that path and
the checker's own file, and no other source path — the `.git`, `node_modules`,
`.venv`, and nested-worktree exclusions stand. Without that exclusion the
required fixtures are themselves unmatched hits and the gate cannot pass. The host usage hook that
declares the chart root must also carry the durable pointer to that record
specified in `named-abstractions.md`.

| Decidable by a script | Owning checklist item |
|---|---|
| every `compass:` address resolves to a chart document | §Coordinate Verification → Correctness |
| every supported `compass-abstraction:` marker in the configured source universe is valid and resolves to exactly one definition with the required headings | §Named Abstraction Verification |
| every path-shaped coordinate in a `## Implementation coordinates` section — backticked, containing `/`, no placeholder — exists on disk | §Coordinate Verification → Staleness |
| every block folder appears in its root's `CONTAINERS.md`, and every listed block has a folder | §L2 |
| every relative link and heading anchor inside the chart resolves | §Markdown and Navigation |
| every zoom-chain document carries a Mermaid fence | §Markdown and Navigation |
| no forbidden filename (`SCOPE.md`, `CONTEXT.md`, `BLOCK.md`, `COMPONENT.md`) exists under the chart root | §Markdown and Navigation |

````python
# chart_check.py — decidable chart invariants. Adapt CHART, SRC_SUFFIXES, FIXTURES, and MINIMUM; run it in CI.
import pathlib, re, sys
CHART = pathlib.Path(".compass")          # the declared chart root
ABSTRACTIONS = CHART / "ABSTRACTIONS.md"
FIXTURES = pathlib.Path("tests/fixtures/compass")  # the one fixture path the trial record names
SELF = pathlib.Path(__file__).resolve()
# Include every source suffix allowed to carry `//`, `#`, or `--` markers.
SRC_SUFFIXES = {".py", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".go", ".rs",
                ".java", ".rb", ".swift", ".sql"}

fail, seen = [], {"addresses": 0, "abstraction_definitions": 0,
                  "abstraction_markers": 0, "links": 0, "coordinates": 0,
                  "blocks": 0, "diagrams": 0}
# every line, not just the first: a marker legitimately sits under a comment, a licence
# header or an import block, and a file may carry a second coordinate for another root
addr_re = re.compile(r"^\s*(?:#|//|--)\s*compass:\s*(\S+)", re.M)
abstraction_claim_re = re.compile(
    r"^[ \t]*(?:#|//|--)[ \t]*compass-abstraction:[ \t]+(.*?)[ \t]*$", re.M)
anchors = lambda t: {re.sub(r"[^a-z0-9 -]", "", h.lower()).replace(" ", "-")
                     for h in re.findall(r"^#{1,6} (.+)$", t, re.M)}

def doc_for(address):                      # root | root.block | root.block.component
    return CHART.joinpath(*address.split(".")) / "README.md"

entries = []
if ABSTRACTIONS.exists():
    abstraction_body = ABSTRACTIONS.read_text()
    heading_count = len(re.findall(r"^## ", abstraction_body, re.M))
    entry_re = re.compile(
        r"^## [^\n]+ \(`([a-z0-9]+(?:-[a-z0-9]+)*)`\)[ \t]*\n(.*?)(?=^## |\Z)",
        re.M | re.S)
    entries = entry_re.findall(abstraction_body)
    seen["abstraction_definitions"] = len(entries)
    if not entries:
        fail.append(f"{ABSTRACTIONS}: no named abstraction definitions")
    if len(entries) != heading_count:
        fail.append(f"{ABSTRACTIONS}: every ## heading must be 'Name (`lowercase-slug`)'")
    slugs = [slug for slug, _ in entries]
    for slug in sorted({slug for slug in slugs if slugs.count(slug) > 1}):
        fail.append(f"{ABSTRACTIONS}: duplicate abstraction slug '{slug}'")
    for slug, section in entries:
        for heading in ("Meaning", "Essential discriminator", "Nearest non-example"):
            field = re.search(
                rf"^### {re.escape(heading)}[ \t]*\n(.*?)(?=^### |\Z)",
                section, re.M | re.S)
            if not field or not field.group(1).strip():
                fail.append(f"{ABSTRACTIONS}: '{slug}' lacks ### {heading}")

definition_slugs = [slug for slug, _ in entries]
for p in pathlib.Path(".").rglob("*"):
    # any dotted directory: .git, .venv, and — the one that bites — a nested git worktree,
    # which otherwise counts every marker in the repository twice
    if p.is_dir() or any(x.startswith(".") for x in p.parts[:-1]): continue
    if "node_modules" in p.parts or p.suffix not in SRC_SUFFIXES: continue
    source = p.read_text(errors="ignore")
    for address in addr_re.findall(source):
        seen["addresses"] += 1
        if not doc_for(address).exists():
            fail.append(f"{p}: compass: {address} resolves to nothing")

def inside_nested_worktree(p):
    return any(parent != pathlib.Path(".") and (parent / ".git").exists()
               for parent in p.parents)

for p in pathlib.Path(".").rglob("*"):
    # Unlike coordinate scanning, legitimate hidden source directories such as
    # .storybook remain in the named-abstraction universe.
    if p.is_dir() or ".git" in p.parts or "node_modules" in p.parts or ".venv" in p.parts:
        continue
    # the declared fixtures and this file spell invalid literals on purpose; nothing else is exempt
    if p.resolve() == SELF or FIXTURES in p.parents: continue
    if inside_nested_worktree(p) or p.suffix not in SRC_SUFFIXES: continue
    source = p.read_text(errors="ignore")
    for slug in abstraction_claim_re.findall(source):
        seen["abstraction_markers"] += 1
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            fail.append(f"{p}: invalid compass-abstraction slug '{slug}'")
        elif definition_slugs.count(slug) != 1:
            fail.append(f"{p}: compass-abstraction: {slug} does not resolve exactly once")

for root in (d for d in CHART.iterdir() if d.is_dir() and d.name != "externals"):
    containers = root / "CONTAINERS.md"
    if not containers.exists():
        fail.append(f"{root.name}: no CONTAINERS.md"); continue
    listed = set(re.findall(r"\]\(\./([^/)]+)/README\.md\)", containers.read_text()))
    dirs = {d.name for d in root.iterdir() if d.is_dir()}
    seen["blocks"] += len(dirs)
    for miss in dirs - listed: fail.append(f"{root.name}: block '{miss}' is not in CONTAINERS.md")
    for miss in listed - dirs: fail.append(f"{root.name}: CONTAINERS.md lists '{miss}', no folder")

for md in CHART.rglob("*.md"):
    body = md.read_text()
    for href in re.findall(r"\]\(([^)\s]+)\)", body):
        if href.startswith(("http", "mailto:")): continue
        path, _, anchor = href.partition("#")
        target = (md.parent / path) if path else md
        seen["links"] += 1
        if path and not target.exists(): fail.append(f"{md}: dead link {href}")
        elif anchor and not target.is_file():
            fail.append(f"{md}: anchor into a non-document {href}")
        elif anchor and anchor not in anchors(target.read_text(errors="ignore")):
            fail.append(f"{md}: dead anchor {href}")
    # coordinates only. A token with no separator is prose; one with a placeholder is a shape
    section = re.search(r"^## Implementation coordinates\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    for coord in re.findall(r"`([^`]+)`", section.group(1) if section else ""):
        if "/" not in coord or any(c in coord for c in "<>{}*"): continue
        seen["coordinates"] += 1
        if not pathlib.Path(coord).exists(): fail.append(f"{md}: coordinate {coord} not on disk")
    # the five zoom-chain kinds each require a diagram
    zoom = md.name in ("CONTAINERS.md", "VIEWPORTS.md") or (
        md.name == "README.md" and md.parent != CHART)
    if zoom:
        seen["diagrams"] += 1
        if not re.search(r"^ {0,3}```\s*mermaid", body, re.M):
            fail.append(f"{md}: no mermaid diagram")

for name in ("SCOPE.md", "CONTEXT.md", "BLOCK.md", "COMPONENT.md"):
    for p in CHART.rglob(name): fail.append(f"{p}: identity documents are README.md")

# Commit the minimum beside this command. Chart-side counts take the count at the last passing
# run and move only in the diff that changes the chart. Source-side counts (addresses,
# abstraction_markers) take 1 once Phase F has sealed anything or a trial has claimed anything:
# they guard against a scan that stopped looking, not against a declutter that bubbles up.
MINIMUM = {"blocks": 0, "diagrams": 0, "links": 0, "coordinates": 0, "abstraction_definitions": 0,
           "addresses": 0, "abstraction_markers": 0}
for k, minimum in MINIMUM.items():
    if seen[k] < minimum:
        fail.append(f"{k}: {seen[k]} scanned, minimum is {minimum} — the check stopped looking")
print("\n".join(fail) or "chart: clean — " + ", ".join(f"{v} {k}" for k, v in seen.items()))
sys.exit(1 if fail else 0)
````

**Print the counts, and assert them.** A check that scanned nothing exits zero exactly like a check that scanned everything — which is how a chart whose markers were all deleted keeps a green build. If `addresses` drops to 0 after Phase F, the script is passing because it stopped looking. A printed count nobody reads is a checkbox with extra steps, so `MINIMUM` is committed beside the command. Chart-side counts take the count at the last passing run and move only in the diff that changes the chart; `addresses` and `abstraction_markers` take 1 once anything is sealed or claimed, because they legitimately fall when a declutter bubbles a coordinate up. Changing a minimum is a chart-check change and is ask-first like installing it (`create.md` §Boundaries). Dropping below a minimum is a build failure, not a warning.

For an opted-in named-abstraction trial, read `abstraction_definitions` and
`abstraction_markers` the same way. Zero markers means the checker proves
nothing about adoption or coverage; it does not mean no implementation uses the
concept.

The configured suffix set is the checker's marker universe, not a discovery
claim. Before trusting its count, run this raw-hit audit from the repository
root and reconcile every result—including documentation examples and
unsupported source forms—with that universe:

```sh
rg -n --hidden -F 'compass-abstraction:' -g '!**/.git/**' -g '!**/node_modules/**' -g '!{fixture-path}/**' -g '!{checker-file}' .
```

An unmatched raw hit in any source file fails the gate — whether the file's suffix is outside the configured set or the marker's form is one the checker does not parse; a documentation example is reconciled, not failed.
A source claim outside `SRC_SUFFIXES`, using a comment form other than `//`,
`#`, or `--`, or missing from `abstraction_markers` is such a hit. Extend
the checker and its fixtures before permitting that form; never silently narrow
"every marker" to what the current regex happened to see.

**What a passing run does and does not establish.** It proves the chart is internally consistent and still points at real code. It proves nothing about whether the boundaries are right, whether a rule the chart records is the rule the product enforces, or whether a name is one a human would use. Those are the rest of this file, and they stay judgment. Never report a green script as verification of the chart.

---

## Root Verification

Run before a root is ratified and given a `{root}/` directory.

- [ ] A human ratified this root — in the conversation or the commit, never as a field in `COMPASS.md`
- [ ] Humans recognize it as a coherent area of reasoning or work — evidenced from product, domain, or human explanation, not from the file tree
- [ ] Its logical identity is stated without reference to source topology
- [ ] It survives the rewrite test: rebuilt in another language, framework, layout, and topology, humans would still say "I am working on X"
- [ ] It has meaningful internal responsibilities or phenomena — not a single concept wearing a root's costume
- [ ] Independent *where am I?* navigation is genuinely useful; the answer differs from what an existing root already gives
- [ ] It was **not** created because a package, service, deployable, repository, or language exists
- [ ] If it overlaps another root, the overlap is recorded and both orientations are justified

---

## L0 Domain Verification

Run before declaring Phase A complete.

- [ ] Bounded contexts are expressed semantically — responsibilities and phenomena, not modules, layers, or directories
- [ ] Every important concept maps to a human-recognizable phenomenon or rule in the product or domain, with the evidence named
- [ ] No mechanism visible only in code was promoted to a domain concept without a separate semantic justification
- [ ] `DOMAIN.md` contains no technology, code paths, schemas, API shapes, or implementation coordinates
- [ ] The context list passes the Derivation Test (`create.md` §The Derivation Test) — contexts mapping ~1:1 onto packages or onto the layer stack were read off the code, whatever their names now say
- [ ] `GLOSSARY.md` exists and covers every term used architecturally anywhere in this root's chart
- [ ] Terminology is consistent across `DOMAIN.md`, block documents, and component documents — one concept, one word
- [ ] Where product and code names differ, the product term is canonical and the code term is recorded as an implementation alias
- [ ] Context-specific meanings are recorded per context rather than blended into one definition
- [ ] Glossary terms used semantically in chart prose are bold; filenames, paths, identifiers, code, and Mermaid syntax are not

---

## L1 System Context Verification

Run before declaring Phase B complete. Every item must pass.

### Diagram checks (structural)
- [ ] **Single-box rule:** count system nodes inside the boundary — must be exactly **1** (the root)
- [ ] **No internals:** no block names, component names, or module names appear inside the boundary
- [ ] **No tech labels:** node labels contain no framework names, database names, protocol names, or API endpoint names
- [ ] **No internal edges:** all edges connect the root to external actors/systems — no edges between internals
- [ ] **All edges labelled:** every relationship has a verb label describing what crosses (data, action, event)

### Actor checks
- [ ] 2–5 actors are named, and each was supplied or confirmed by the human — never inferred from code alone
- [ ] Each actor is a person, organisation, or role, not a system
- [ ] Each actor corresponds to a recognizable interaction with the product or operation, not to an entry point in the code

### Document checks
- [ ] `{chart-root}/README.md` and `{root}/README.md` exist, and `{root}/README.md` carries a diagram
- [ ] Every L1 external system has an `externals/{name}.md` doc, linked from its `COMPASS.md` row

### External system checks (semantic)
For each node in the external systems table, confirm ALL:
- [ ] Passes User-Possession Test: *"Would the primary actor name this as a top-level tool/service they use?"*
- [ ] Passes Control Boundary Test: *"If this system stopped running, does this thing still exist and belong to the user/operator?"*
- [ ] Admitted from product or operator reality — **not** inferred from a dependency manifest, lockfile, or import
- [ ] Not implemented inside the system (no code root in this repo)
- [ ] You are naming the **product/service/store**, not an engine, SDK, API version, or client library
- [ ] Not a framework, library, runtime, or OS component (engines are never L1; the stores they serve may be)
- [ ] Would appear in a product description or user-facing documentation
- [ ] Has a compass entry (or local compass note) — created when it first passes these checks, so admissions and demotions both leave a record

### Meaning check
- [ ] The L1 picture agrees with how humans describe using and operating this system
- [ ] The L1 picture would remain true after a structure-only refactor — nothing in it depends on today's repository layout, packaging, or deployment shape

### Cut Loose Ends (after every L1 pass)
1. List every external system referenced anywhere in L1 and L2 docs
2. Apply the external system checklist to each
3. Any that fail → demote immediately (usually an L3 adapter; an internal implementation is L2, a shared helper L5); record the demotion in the registry's named-dependencies table — name, used-by, and the fact about the dependency that puts it there, never the name of the test it failed — so it cannot be silently re-elevated
4. Re-run diagram checks after all demotions

---

## L2 Isolated Blocks Verification

Run before declaring Phase B complete.

- [ ] Every block has: name, responsibility (1 sentence), logical role, boundary statement, technology, implementation coordinates, communicates-with list
- [ ] Every block's **logical role** maps upward to a stable responsibility or phenomenon of the root, and is stated without naming a directory, package, or technology
- [ ] Every block survives the invariance test: its boundary still makes sense after a structure-only refactor
- [ ] No block exists only because a package, service, or deployable exists — implementation decomposition is not product decomposition
- [ ] No block was split or merged because deployment topology, framework, or repository layout changed
- [ ] **The block list passes the Derivation Test** (`create.md` §The Derivation Test): laid beside the deployables, the packages, and the layers of the stack, it pairs off one-to-one with none of them. This is a check on the *set* — every member can pass the rewrite test while the cut was still read off topology
- [ ] **No residue block.** Every block name is one a practitioner would say out loud, unprompted. A category name (`*-intelligence`, `*-services`, `core`, `shared`, `common`) or a layer name (`foundation`, `platform`, `packages`) means the block was computed from what the other blocks did not absorb
- [ ] A block list where every block maps to exactly one subtree was investigated as a Derivation Test lead, and the disposition is recorded: a repository deliberately shaped around the ratified boundaries is *legitimate* (with what makes it so); a cut read off the file tree is *derived* (redraw from the domain). The pattern opens the question; only derivation evidence closes it
- [ ] Every external system referenced in L2 is either listed at L1 (passed eligibility) or explicitly marked as "L3 adapter" in the block doc
- [ ] No component is documented as a block (if it maps to a single file or a single class, it's L3)
- [ ] No circular block dependencies (A → B → A)
- [ ] Every block boundary statement says what it does NOT do (missing boundary = incomplete), and is no longer than 2 sentences
- [ ] Every outbound (`→`) communicates-with entry has a matching `## Uses` entry in the same block, carrying why, relied capabilities, and replacement conditions — the wire without the decision is an incomplete block document
- [ ] No block's communicates-with list exceeds 5 entries without a recorded justification — the block is a candidate for doing too much
- [ ] Block diagram exists and reflects all communicates-with entries
- [ ] `CONTAINERS.md` exists, carries a wiring diagram, and lists every block folder
- [ ] The host's agent instructions carry the usage hook (chart root + entry pattern), human-approved — a chart no agent is routed to does not exist
- [ ] The hook says **when** to read the chart, not that it precedes all code work — an unconditional claim is disbelieved after the third one-line fix, and then it is skipped for the change that needed it
- [ ] Every block's component table is present

---

## Level Calibration Verification

Run at each level after its documents exist, and again whenever a sibling set changes.

- [ ] Siblings under one parent sit at comparable **semantic scale** — comparable breadth of logical responsibility
- [ ] Every calibration finding cites semantic evidence; no finding rests on lines of code, file count, module count, or implementation complexity
- [ ] Any concept promoted for oversized scope passes the gate of its new level (and root admission, if promoted to a root)
- [ ] Any umbrella introduced to group fine-grained siblings has a glossary entry and human ratification, or is explicitly recorded as a grouping with no semantic claim
- [ ] Any sibling found unlike the rest has been re-levelled, not left in place with a note

---

## L3 Component Verification

Run before declaring Phase C complete.

- [ ] Every component has: stereotype, responsibility (1 sentence), bounded context, I/O, depends-on, used-by, boundary, implementation coordinates
- [ ] No component names two L0 bounded contexts (if it does → boundary finding, flag it)
- [ ] Every implementation coordinate exists on disk (`grep` or `ls` to confirm)
- [ ] Every component is owned by exactly one block (it lives in one block folder); callers from other blocks are consumption, not ownership — 3+ consuming blocks is a shared-library smell: demote to L5 or split, or record why it stays
- [ ] No component's depends-on list reaches 4+ entries from different blocks or external systems without a recorded justification — that is boundary pressure: an integration hub, a missing facade, or a hidden block
- [ ] Mermaid diagram exists and matches depends-on/used-by entries
- [ ] Components are listed in their parent block's component table

---

## Coordinate Verification

Run before declaring Phase F complete on any block, and whenever the implementation is restructured. "Code file" means a source file written in one of the technologies the block declares. Files whose format carries no comment syntax (JSON, lockfiles) and generated files are out of scope — attribute the folder that holds them, not the file.

### Coverage
- [ ] Every code file in the block is **covered** by a coordinate — its own, or the nearest enclosing folder/package one — or is a test that does not participate in the place its enclosing coordinate names, or is recorded as L5 infrastructure in the block's component table
- [ ] Every L5 entry in the component table names what it is (formatter, logger, config loader, generic UI, shared types); a bare `L5` with no name is an un-attributed component wearing an exemption
- [ ] Every component documented in the block is named by at least one coordinate in code (chart → code); a block sealed only at block level leaves its components unwired

### Correctness
- [ ] Every coordinate address exists as a place in the chart (`grep -r "compass:" {source root}` → validate each address; the marker is the comment body, so match it without a language-specific comment prefix)
- [ ] Every coordinate still locates today's implementation — the file or subtree carrying it genuinely participates in that place
- [ ] No file repeats the address its enclosing folder/package coordinate already gives it; a file-level coordinate is warranted only when its address differs
- [ ] No source boundary was created solely to make a coordinate coarse

### Multiple coordinates
- [ ] Every file carrying coordinates from **different roots** has both roots registered in `COMPASS.md` and ratified, and the two orientations are genuinely independent — an unratified second root is an invented stack; remove it
- [ ] Every file carrying two coordinates within **one root** has been investigated: it is a boundary, bridge, or ACL participating in two places, or the chart's ambiguity has been resolved. Record which — do not leave it unexamined
- [ ] No file was split, and no code was moved, solely to reduce a coordinate count

### Staleness
- [ ] Stale coordinates are classified as **implementation remapping** and repaired by updating coordinates — not by editing L0–L2 semantics
- [ ] A coordinate pointing to a place absent from the chart was investigated (unratified semantic change, or a marker written against a place that never existed) before the comment was deleted
- [ ] Every coordinate-density observation — several coordinates in one folder, a file carrying two coordinates in one root, a file resisting every enclosing coordinate — names the observed Compass level and parent boundary, then carries a recorded disposition: *declutter* (with the useful move), *legitimate* (with what makes it so and no required move), or *debt* (with independent cohesion or coupling evidence at that level and the healthier direction it suggests). An observation with no disposition is an unclosed lead; one that blends levels or calls the coordinate pattern itself debt is an unearned verdict. Both fail this item

---

## Ownership Boundary Verification

Run over any chart document carrying nontrivial rationale, and over implementation documentation written near a coordinate. The contract is in [`ownership-boundary.md`](ownership-boundary.md).

- [ ] For each nontrivial reason in the chart: *would this reason survive a full implementation rewrite?* If no, it belongs with the code or its Context Docs owner — move it
- [ ] For each piece of implementation documentation that repeats chart semantics: *does Compass already canonically own this truth?* If yes, reduce it to the smallest local consequence plus a coordinate route
- [ ] No mechanism-specific Chesterton's Fence (queue semantics, retry placement, ordering guarantees, framework quirks) appears in L0–L2 prose
- [ ] No complete semantic explanation is reproduced at both a chart location and an implementation site. When both a chart location and an implementation site carry the same reason, the rewrite test decides which keeps it: a reason that survives a full implementation rewrite stays in the chart; a reason that constrains only the current implementation stays with the code or its Context Docs owner.

---

## Named Abstraction Verification (Optional)

Run whenever `ABSTRACTIONS.md` or a `compass-abstraction:` marker exists,
including when no valid trial was configured. The governing procedure is
[`named-abstractions.md`](named-abstractions.md). An unconfigured catalog or
marker is an orphan claim and fails this gate until the user authorizes its
removal or completes every trial prerequisite.

- [ ] One existing task, PR, or tracker record is user-nominated and authorized as the sole owner of trial tasks, admission evidence, decisions, observations, and maintenance findings; the host usage hook carries the prescribed durable pointer to it
- [ ] The host test suite owns the installed checker and the nominated trial record names its exact command plus passing valid, invalid-slug, missing-definition, malformed-spacing-or-multiline, unsupported-form, and hidden-source fixture commands, and the one fixture path that the checker and the raw-hit audit exclude
- [ ] Every definition heading has a unique lowercase-hyphen slug and its required `Meaning`, `Essential discriminator`, and `Nearest non-example` sections
- [ ] The repository-wide raw-hit audit has no unsupported or uncounted source claim; every supported marker in the configured source universe resolves to exactly one definition
- [ ] Every marker is adjacent to a stable, authored declaration that owns the claimed instance — never a call site, generated file, barrel export, or convenience import
- [ ] Each marked owner conforms to the definition's discriminator and is not its nearest non-example; this is review evidence, not a script result
- [ ] The nominated trial record shows that every admitted name changed a concrete navigation, implementation, or comparison decision; mere recurrence or resemblance did not qualify it
- [ ] The nominated trial record states one trigger that ends the trial — a calendar date, a count of recorded observations, or a named event — and, once that trigger is reached, carries the verdict of the reading (`named-abstractions.md` §Maintenance and falsification); a missing trigger, or a reached trigger with no verdict, fails this gate
- [ ] `ABSTRACTIONS.md` contains no occurrence paths, feature mappings, `used-by` lists, edges, flows, or trial results
- [ ] Marker absence is treated as unknown, searches are reported as declared occurrences only, and no coverage or completeness claim is made
- [ ] The trial did not reinterpret L3 stereotypes or change any L0–L4 semantic entity

A green mechanical check establishes only definition shape, slug uniqueness,
and marker resolution. It does not establish that a marked owner conforms, that
all conforming code is marked, or that the abstraction is useful.

---

## Markdown and Navigation Verification

Run at each level, over every document written so far.

- [ ] Every architectural directory's identity document is its `README.md`
- [ ] No `SCOPE.md`, `CONTEXT.md`, `BLOCK.md`, or `COMPONENT.md` remains anywhere under the chart root
- [ ] Semantic fields are Markdown headings — no pseudo-fields encoded as `Field — value` prose lines
- [ ] Sets are lists, homogeneous collections are tables, diagrams are Mermaid
- [ ] Every cross-reference is a markdown link, not a plain backtick name (`<!-- TODO: link when created -->` is the only sanctioned placeholder)
- [ ] Every relative link resolves — including glossary → `DOMAIN.md` anchors and component → context anchors
- [ ] Opening each zoom-level directory on GitHub renders a landing page that answers *where am I?*
- [ ] Every zoom-chain document carries its required Mermaid diagram
- [ ] `VIEWPORTS.md`, where it exists, carries one `##` per viewport named for its question, and every root README linking to it has one to link to

---

## Blind Semantic Read

Run when the L3 checklist passes (Phase C), before calling the level done, and again after any later phase that touched more than one document. Every other checklist in this file measures the container — headings, links, coordinates, symmetry — and all of them pass on a chart that is well-formed and untrue. This one reads the arguments.

The reader is blind: a fresh agent context holding only `{chart-root}` and this list — no authoring session, no exploration scratchpad, no code. An author re-reading their own chart is not a blind read; the author sees what was meant. When no such context can be launched, stop there and report, as with any missing checkpoint. Record every finding in the task's own record and classify it (`growth-and-drift.md` §Classifying Disagreement) before changing anything. A contradiction between two chart pages has no code side to classify against: the page that owns the claim (`create.md` §Kind decides) keeps it, the other page is reduced to a link, and a correction that changes what a ratified level says goes back through that level's checklist.

- [ ] No glossary entry contradicts the document that defines its concept, and no term carries two meanings inside one bounded context
- [ ] No singular claim — *the one invariant*, *the only failure this system does not tolerate* — is made about more than one entity
- [ ] No argument is re-derived on more than one page: a recurring cross-cutting claim has one owning page, and every other page states the local fact and links to it
- [ ] L0's context map and L2's wiring diagram are not one diagram with renamed nodes: a block-to-block edge legitimately repeats in that block's own diagram, but a context-map relationship carried word-for-word into `CONTAINERS.md` means one level was read off the other instead of derived from the domain and the repository
- [ ] Every block `README.md` answers *why does this exist* on its own, without a second document needed to make it true
- [ ] The Derivation Test (`create.md` §The Derivation Test) holds on reading, not only on scanning: no block is a package wearing a domain name

---

## Lead/Bleed Detection Checklist

Run the shared warning-sign inventory in
[`structural-signals.md`](structural-signals.md). Each signal opens an
investigation; it is not a failed completion gate by itself.

---

## Spot Check

Run periodically (after any significant code change, or at state 3 maintenance cadence).

1. Pick 5 random source files per block. For each: is it covered by a coordinate? Does that address exist in the chart? Can you navigate component → block → root in ≤2 hops?
2. Pick 3 random component documents — do their implementation coordinates still exist on disk? Classify every miss as remapping before touching anything semantic.
3. Pick 1 block document — does its communicates-with list match actual imports?
4. Pick 2 rules or invariants the chart records and check them against the product's current behaviour. This is the only check that finds a semantic change, and no structural comparison substitutes for it.
5. Pick 3 glossary terms — is each still the word humans use, and are the recorded aliases still the words in code?
6. Check `VIEWPORTS.md` — at most 3–4 active viewports, each still answering its named question with a diagram that describes reality. A chart that skipped L4 has no `VIEWPORTS.md` and no link to one; that passes.
7. Check document sizes against the level budgets in `create.md` §Quick Reference: Levels — oversize means scope creep within the level; split the content down a level, don't raise the budget. L0 and L4 budgets are per unit (context, viewport): an oversize unit is doing too much — split or retire the unit, since there is no level below to push it into.

**If any check fails:** classify the finding using [`growth-and-drift.md`](growth-and-drift.md#classifying-disagreement) — semantic change, implementation remapping, or implementation violation — and respond per the priority order there. A finding repaired before it is classified is the failure this step exists to prevent.
