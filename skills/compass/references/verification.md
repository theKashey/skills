# Verification Procedures

Formal checks that must pass before ratifying a root, advancing L0, L1, L2, L3
(including the blind semantic read), or Phase F, or changing a named
abstraction. Run the applicable checks as a mandatory gate — not optional
polish. Each completion checklist
below is canonical; other procedures point to the applicable section rather
than restating its items. Levels and phases with no section below carry no gate
beyond their exit conditions in [`exploration.md`](exploration.md) and
[`growth-and-drift.md`](growth-and-drift.md).

---

## First: the mechanizable checks belong to the host's test suite

**An agent ticking its own checkbox is self-certification, and the items the table below maps need no judgment at all.** Install them in the host's own test suite during Phase B, so they fail a build rather than waiting for a review. Installing the check is ask-first (`create.md` §Boundaries). A checklist row marked *script-owned* is a green run of the installed check and nothing else; while the check is not yet installed, and after a recorded decline (§L2), that row is run by hand like every other. Once installed, require a passing suite with valid, dangling, malformed, hidden-source, and unsupported-form/suffix coordinate fixtures, plus scope-carrier, exclusion, and template-heading fixtures; `tests/test_chart_check.py` in the Compass package is the reference suite. A green run covers only the mapped properties. The installed copy is frozen at install time: every Create task compares it with this fence, and a difference is Phase E work (`growth-and-drift.md` §Phase E), ask-first. Template-shape failures are prefixed `template:` and route to the format trigger there; every other failure routes to §Classifying Disagreement.

The manual fallback does not apply to named-abstraction claims: a claim exists
to be resolved, and nothing resolves it before the check. Before the first
definition or source claim, the host test suite must own an installed, adapted
checker and repository-native fixtures for a valid claim, an invalid slug, a
missing definition, malformed spacing or a multiline claim, an unsupported
form, and a supported marker in a hidden source directory; the suite is the
only record of that command and those fixtures. Those fixtures are files
containing deliberately invalid marker literals, so they live under the one
path the checker's `FIXTURES` names, and the checker and the raw-hit audit
exclude that path and the checker's own file, and no other source path — the
`.git`, `node_modules`, `.venv`, and nested-worktree exclusions stand. Without
that exclusion the required fixtures are themselves unmatched hits and the gate
cannot pass.

| Decidable by a script | Owning checklist item |
|---|---|
| every `compass:` address resolves to a chart document | §Coordinate Verification → Correctness |
| every declared scope names an existing carrier inside the subtree, with the addressed marker, and same-root carriers at that subtree agree | §Coordinate Verification → Coverage |
| every supported `compass-abstraction:` marker in the configured source universe is valid and resolves to exactly one definition with the required headings | §Named Abstraction Verification |
| every path-shaped coordinate in a `## Implementation coordinates` section — backticked, containing `/`, no placeholder — exists on disk | §Coordinate Verification → Staleness |
| every block folder appears in its root's `CONTAINERS.md`, and every listed block has a folder | §L2 |
| every relative link and heading anchor inside the chart resolves | §Markdown and Navigation |
| every zoom-chain document carries a Mermaid fence | §Markdown and Navigation |
| every block and component `README.md` carries the headings its template requires | §L2, §L3 |
| every outbound (`→`) communicates-with entry names a block with a `###` entry under `## Uses` | §L2 |
| every block `README.md` carries a component table | §L2 |
| every viewport in `VIEWPORTS.md` carries `### Type`, `### Question`, `### Participants`, `### Diagram`, and `### Seams`, and its type is `runtime`, `domain`, `boundary`, or `lifecycle` | §Markdown and Navigation |
| no forbidden filename (`SCOPE.md`, `CONTEXT.md`, `BLOCK.md`, `COMPONENT.md`) exists under the chart root | §Markdown and Navigation |
| every lexicon row is in tool order, unique per root, bridges a lexical gap, resolves its address or scope, and keeps every code stem in some identifier; every `### Lexicon` link names a row whose first speech form is the heading; no glossary carries `### Implementation aliases` — `compass_lex.py check`, a separate installed check | §Lexicon Verification |

````python
# chart_check.py — decidable chart invariants. Adapt CHART, SRC_SUFFIXES, FIXTURES, and MINIMUM; run it in CI.
import os, pathlib, re, sys
CHART = pathlib.Path(".compass")          # the declared chart root
ABSTRACTIONS = CHART / "ABSTRACTIONS.md"
FIXTURES = pathlib.Path("tests/fixtures/compass")  # the one path the checker and the raw-hit audit exclude
SELF = pathlib.Path(__file__).resolve()
# Both marker kinds use this source universe. Raw hits outside it fail.
SRC_SUFFIXES = {".py", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".go", ".rs",
                ".java", ".rb", ".swift", ".sql"}

fail, seen = [], {"addresses": 0, "abstraction_definitions": 0,
                  "abstraction_markers": 0, "links": 0, "coordinates": 0,
                  "blocks": 0, "diagrams": 0}
raw_marker_re = re.compile(r"compass(?:-abstraction)?:")
marker_re = re.compile(
    r"^[ \t]*(?:#|//|--)[ \t]*(compass(?:-abstraction)?):[ \t]+([^\r\n]*?)[ \t]*$", re.M)
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
source_addresses = {}
for current, dirs, files in os.walk("."):
    base = pathlib.Path(current)
    dirs[:] = [name for name in dirs if name not in {".git", "node_modules", ".venv"}
               and (base / name).resolve() != FIXTURES.resolve()
               and not (base / name / ".git").exists()]
    for name in files:
        p = base / name
        if p.resolve() == SELF or not p.is_file(): continue
        source = p.read_text(errors="ignore")
        raw_hits = raw_marker_re.findall(source)
        if not raw_hits: continue
        # Markdown examples are documentation, not source claims.
        if p.suffix.lower() == ".md": continue
        if p.suffix not in SRC_SUFFIXES:
            fail.append(f"{p}: marker outside SRC_SUFFIXES"); continue
        claims = marker_re.findall(source)
        if len(claims) != len(raw_hits):
            fail.append(f"{p}: unsupported or malformed marker literal")
        for kind, value in claims:
            if kind == "compass":
                seen["addresses"] += 1
                source_addresses.setdefault(p.resolve(), set()).add(value)
                if not re.fullmatch(r"[^./\\\s]+(?:\.[^./\\\s]+){0,2}", value):
                    fail.append(f"{p}: invalid compass address '{value}'")
                elif not doc_for(value).is_file():
                    fail.append(f"{p}: compass: {value} resolves to nothing")
            else:
                seen["abstraction_markers"] += 1
                if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value):
                    fail.append(f"{p}: invalid compass-abstraction slug '{value}'")
                elif definition_slugs.count(value) != 1:
                    fail.append(f"{p}: compass-abstraction: {value} does not resolve exactly once")

for root in (d for d in CHART.iterdir() if d.is_dir() and d.name != "externals"):
    containers = root / "CONTAINERS.md"
    if not containers.exists():
        fail.append(f"{root.name}: no CONTAINERS.md"); continue
    listed = set(re.findall(r"\]\(\./([^/)]+)/README\.md\)", containers.read_text()))
    dirs = {d.name for d in root.iterdir() if d.is_dir()}
    seen["blocks"] += len(dirs)
    for miss in dirs - listed: fail.append(f"{root.name}: block '{miss}' is not in CONTAINERS.md")
    for miss in listed - dirs: fail.append(f"{root.name}: CONTAINERS.md lists '{miss}', no folder")

scopes = {}
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
    coordinate_text = section.group(1) if section else ""
    declarations = re.findall(r"`([^`]+)` covers `([^`]+)`", coordinate_text)
    if len(declarations) != len(re.findall(r"`[^`]+` covers", coordinate_text)):
        fail.append(f"{md}: malformed carrier/subtree declaration")
    for carrier, subtree in declarations:
        address = ".".join(md.parent.relative_to(CHART).parts)
        carrier_path, scope_path = pathlib.Path(carrier), pathlib.Path(subtree)
        if (md.name != "README.md" or not address or not subtree.endswith("/") or carrier_path.is_absolute()
                or scope_path.is_absolute() or ".." in carrier_path.parts or ".." in scope_path.parts):
            fail.append(f"{md}: scope needs an addressed README and repository-relative paths"); continue
        if not scope_path.is_dir() or scope_path.resolve() not in carrier_path.resolve().parents:
            fail.append(f"{md}: carrier {carrier} is not inside subtree {subtree}")
        if address not in source_addresses.get(carrier_path.resolve(), set()):
            fail.append(f"{md}: carrier {carrier} lacks compass: {address}")
        key = (scope_path.resolve(), address.split(".")[0])
        scopes.setdefault(key, {}).setdefault(carrier_path.resolve(), set()).add(address)
    # the five zoom-chain kinds each require a diagram
    zoom = md.name in ("CONTAINERS.md", "VIEWPORTS.md") or (
        md.name == "README.md" and md.parent != CHART)
    if zoom:
        seen["diagrams"] += 1
        if not re.search(r"^ {0,3}```\s*mermaid", body, re.M):
            fail.append(f"{md}: no mermaid diagram")
    # template headings (blocks-and-levels.md): depth below CHART says which README this is
    depth = len(md.relative_to(CHART).parts) - 1 if md.name == "README.md" else 0
    h2 = re.findall(r"^## (.+?)\s*$", body, re.M)
    # `template:` failures are document-shape failures: rewrite to the current template (Phase E), never classify
    older = "written to an earlier Compass template"
    prose_stereotype = depth == 3 and re.search(r"^«[^»]+»", body.split("\n## ", 1)[0], re.M)
    if prose_stereotype:
        fail.append(f"{md}: template: {older} — stereotype is a prose line, now ## Stereotype")
    for heading in {2: ["Responsibility", "Logical role", "Boundary", "Technology",
                        "Implementation coordinates", "Communicates with", "Uses",
                        "Components", "Diagram"],
                    3: ["Stereotype", "Responsibility", "Bounded context", "Inputs and outputs", "Depends on",
                        "Used by", "Boundary", "Implementation coordinates", "Diagram"]}.get(depth, []):
        if heading not in h2 and not (heading == "Stereotype" and prose_stereotype):
            fail.append(f"{md}: template: missing ## {heading}")
    if depth == 2:                         # the wire (→) needs its decision (### under ## Uses)
        part = lambda name: (re.search(rf"^## {name}\n(.*?)(?=^## |\Z)", body, re.S | re.M) or [None, ""])[1]
        decided = set(re.findall(r"^### \[[^\]]+\]\(\.\./([^/)]+)/", part("Uses"), re.M))
        for target in re.findall(r"^\s*-\s*→.*?\]\(\.\./([^/)]+)/", part("Communicates with"), re.M):
            if target not in decided: fail.append(f"{md}: template: → {target} has no ### entry under ## Uses")
        if not re.search(r"^\|.*\|\s*$", part("Components"), re.M):
            fail.append(f"{md}: template: no component table")
    if md.name == "VIEWPORTS.md":         # one ## per viewport, each with its ### sections and one legal type
        for title, text in re.findall(r"^## (.+?)\s*\n(.*?)(?=^## |\Z)", body, re.S | re.M):
            h3 = re.findall(r"^### (.+?)\s*$", text, re.M)
            prose_type = "Type" not in h3 and re.search(r"^Type:", text, re.M)
            if prose_type:
                fail.append(f"{md}: template: viewport '{title}' {older} — type is a prose line, now ### Type")
            for heading in ["Type", "Question", "Participants", "Diagram", "Seams"]:
                if heading not in h3 and not (heading == "Type" and prose_type):
                    fail.append(f"{md}: template: viewport '{title}' missing ### {heading}")
            value = re.search(r"^### Type\s*\n(.*?)(?=^### |\Z)", text, re.S | re.M)
            kind = (value.group(1).split() or [""])[0] if value else ""
            if "Type" in h3 and kind not in ("runtime", "domain", "boundary", "lifecycle"):
                fail.append(f"{md}: template: viewport '{title}' type '{kind}' is not runtime, domain, boundary, or lifecycle")

for (subtree, root), carriers in scopes.items():
    if len({frozenset(addresses) for addresses in carriers.values()}) > 1:
        fail.append(f"{subtree}: conflicting carrier scopes for root {root}")

for name in ("SCOPE.md", "CONTEXT.md", "BLOCK.md", "COMPONENT.md"):
    for p in CHART.rglob(name): fail.append(f"{p}: identity documents are README.md")

# Commit the minimum beside this command. Chart-side counts take the count at the last passing
# run and move only in the diff that changes the chart. Source-side counts (addresses,
# abstraction_markers) take 1 once Phase F has sealed anything or a marker has claimed anything:
# they guard against a scan that stopped looking, not against a declutter that bubbles up.
MINIMUM = {"blocks": 0, "diagrams": 0, "links": 0, "coordinates": 0, "abstraction_definitions": 0,
           "addresses": 0, "abstraction_markers": 0}
for k, minimum in MINIMUM.items():
    if seen[k] < minimum:
        fail.append(f"{k}: {seen[k]} scanned, minimum is {minimum} — the check stopped looking")
if fail:  # route each failure kind, not only report it
    template, other = (any(": template: " in f for f in fail), any(": template: " not in f for f in fail))
    if template:
        fail.append("A `template:` failure is a document written to an earlier or incomplete Compass "
                    "template: rewrite it to the current template, ask-first (growth-and-drift.md "
                    "§Phase E); its semantics stand and there is nothing to classify.")
    if other:
        fail.append("Classify each other failure before repairing it: Compass Create, growth-and-drift.md "
                    "§Classifying Disagreement. A coordinate that resolves to nothing is investigated "
                    "rather than deleting the comment.")
print("\n".join(fail) or "chart: clean — " + ", ".join(f"{v} {k}" for k, v in seen.items()))
sys.exit(1 if fail else 0)
````

**Print the counts, and assert them.** A check that scanned nothing exits zero exactly like a check that scanned everything — which is how a chart whose markers were all deleted keeps a green build. If `addresses` drops to 0 after Phase F, the script is passing because it stopped looking. A printed count nobody reads is a checkbox with extra steps, so `MINIMUM` is committed beside the command. Chart-side counts take the count at the last passing run and move only in the diff that changes the chart; `addresses` and `abstraction_markers` take 1 once anything is sealed or claimed, because they legitimately fall when a declutter bubbles a coordinate up. Changing a minimum is a chart-check change and is ask-first like installing it (`create.md` §Boundaries). Dropping below a minimum is a build failure, not a warning.

For named abstractions, read `abstraction_definitions` and
`abstraction_markers` the same way. Zero markers means the checker proves
nothing about adoption or coverage; it does not mean no implementation uses the
concept.

Both marker kinds share the configured suffix set and exclusions: `.git`,
`node_modules`, `.venv`, nested worktrees, the one fixture directory, and the
checker itself. Other hidden directories remain included. The checker rejects
raw marker literals that it cannot parse or whose suffix is not configured;
Markdown examples are documentation, not claims. Before trusting its count,
run this raw-hit audit from the repository root and reconcile every result
with that universe, including documentation and excluded trees:

```sh
rg -n --hidden -e 'compass:' -e 'compass-abstraction:' -g '!**/.git/**' -g '!**/node_modules/**' -g '!{fixture-path}/**' -g '!{checker-file}' .
```

An unmatched raw hit in any source file fails the gate — whether the file's suffix is outside the configured set or the marker's form is one the checker does not parse; a documentation example is reconciled, not failed.
A source claim outside `SRC_SUFFIXES`, using a comment form other than `//`,
`#`, or `--`, or missing from its marker count is such a hit. Extend
the checker and its fixtures before permitting that form; never silently narrow
"every marker" to what the current regex happened to see.

**What a passing run does and does not establish.** It establishes only the mechanical properties in the table, within the configured universe. It does not establish complete coordinate coverage, valid semantic relationships, correct boundaries, product-rule conformance, or useful names. Those are the rest of this file, and they stay judgment. Never report a green script as verification of the chart.

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
- [ ] The context list passes the Derivation Test (`create.md` §The Derivation Test): any one-to-one match with packages or layers was investigated, and domain evidence justifies the decomposition independently of topology; the task record holds the disposition
- [ ] `GLOSSARY.md` exists and covers every term used architecturally anywhere in this root's chart
- [ ] Terminology is consistent across `DOMAIN.md`, block documents, and component documents — one concept, one word
- [ ] Where product and code names differ, the product term is canonical; a code form that identifier-split search cannot reach is a candidate in the task record for the lexicon admission task (§Lexicon Verification), and a reachable one is recorded nowhere. No glossary carries the form itself
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
- [ ] Outside the selected logical root's boundary; another product may share this repository or team and still be external to this root
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

Run before declaring Phase B complete, and re-run the hook rows after Phase E updates the hook (`growth-and-drift.md` §Phase E).

- [ ] Every block has: name, responsibility (1 sentence), logical role, boundary statement, technology, implementation coordinates, communicates-with list — heading presence is script-owned (§First); the checkbox covers the content
- [ ] Every block's **logical role** maps upward to a stable responsibility or phenomenon of the root, and is stated without naming a directory, package, or technology
- [ ] Every block survives the invariance test: its boundary still makes sense after a structure-only refactor
- [ ] No block exists only because a package, service, or deployable exists — implementation decomposition is not product decomposition
- [ ] No block was split or merged because deployment topology, framework, or repository layout changed
- [ ] **The block list passes the Derivation Test** (`create.md` §The Derivation Test): any one-to-one match with deployables, packages, layers, or subtrees was investigated. A repository shaped around ratified domain boundaries is legitimate; a cut justified only by topology is redrawn from domain evidence. Record the evidence and disposition in the task record
- [ ] **No residue block.** Each block owns a coherent, human-recognized responsibility. Category or layer names (`core`, `shared`, `platform`, and similar) prompted investigation, not automatic rejection; no block exists merely to hold what the others did not absorb
- [ ] Every external system referenced in L2 is either listed at L1 (passed eligibility) or explicitly marked as "L3 adapter" in the block doc
- [ ] Each block meets L2's semantic admission criteria and sibling scale; a single-file or single-class implementation neither establishes nor disqualifies a block
- [ ] No circular block dependencies (A → B → A)
- [ ] Every block boundary statement says what it does NOT do (missing boundary = incomplete), and is no longer than 2 sentences
- [ ] Every outbound (`→`) communicates-with entry has a matching `## Uses` entry in the same block, carrying why, relied capabilities, and replacement conditions — the wire without the decision is an incomplete block document; entry presence is script-owned (§First), the three answers are not
- [ ] No block's communicates-with list exceeds 5 entries without a recorded justification — the block is a candidate for doing too much
- [ ] Block diagram exists and reflects all communicates-with entries
- [ ] `CONTAINERS.md` exists, carries a wiring diagram, and lists every block folder
- [ ] The host's agent instructions carry the current [usage-hook template](agent-hook.md), with the installed Compass skill and declared chart-root paths substituted and human-approved — a chart no agent is routed to does not exist
- [ ] The hook says **when** to read the chart, not that it precedes all code work — an unconditional claim is disbelieved after the third one-line fix, and then it is skipped for the change that needed it
- [ ] The hook carries the template's non-local trigger, live search command, matched-section consultation, BM25 boundary, and local-work exclusion; equivalent host wording is allowed, but an older or incomplete contract fails until Phase E updates it, ask-first
- [ ] The chart check (§First) is installed in the host's test suite with `MINIMUM` set by the rule under its fence (§First), or the human's decline is recorded in the task's PR, issue, or task record — a Phase B closed with an all-zero minimum is green over a chart it never scanned
- [ ] Every block's component table is present (script-owned, §First)

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

- [ ] Every component has: stereotype, responsibility (1 sentence), bounded context, I/O, semantic dependencies, boundary, implementation coordinates — heading presence is script-owned (§First); the checkbox covers the content. Any reverse view links to consumer-owned entries or an identified generated/live source rather than maintaining another caller inventory
- [ ] No component names two L0 bounded contexts (if it does → boundary finding, flag it)
- [ ] Every implementation coordinate exists on disk (`grep` or `ls` to confirm)
- [ ] Every component is owned by exactly one block (it lives in one block folder); callers from other blocks are consumption, not ownership — 3+ consuming blocks is a shared-library smell: demote to L5 or split, or record why it stays
- [ ] No component's depends-on list reaches 4+ entries from different blocks or external systems without a recorded justification — that is boundary pressure: an integration hub, a missing facade, or a hidden block
- [ ] Mermaid diagram exists and projects the owning semantic relationship entries; machine-owned import/call incidence stays linked or generated
- [ ] Components are listed in their parent block's component table

---

## Coordinate Verification

Run before declaring Phase F complete on any block, and whenever the implementation is restructured. "Code file" means a source file written in one of the technologies the block declares. Files whose format carries no comment syntax (JSON, lockfiles) and generated files are out of scope — attribute the folder that holds them, not the file.

### Coverage
- [ ] Every code file in the block is **covered** by a coordinate — its own, or the nearest enclosing folder/package one — or is a test that does not participate in the place its enclosing coordinate names, or is recorded as L5 infrastructure in the block's component table
- [ ] Every L5 entry in the component table names what it is (formatter, logger, config loader, generic UI, shared types); a bare `L5` with no name is an un-attributed component wearing an exemption
- [ ] Every component documented in the block is named by at least one coordinate in code (chart → code); a block sealed only at block level leaves its components unwired
- [ ] Every inherited scope has a carrier/subtree declaration in the addressed document's implementation coordinates and resolves under `SKILL.md` §Shared contract; no coverage is inferred from a carrier's filename, and missing or conflicting carriers remain unresolved remapping findings

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
- [ ] Every coordinate-density observation — several coordinates in one folder, a file carrying two coordinates in one root, a file resisting every enclosing coordinate — names the observed Compass level and parent boundary, then carries a disposition in the task record: *declutter* (with the useful move), *legitimate* (with what makes it so and no required move), or *debt* (with independent cohesion or coupling evidence at that level and the healthier direction it suggests). An observation with no disposition is an unclosed lead; one that blends levels or calls the coordinate pattern itself debt is an unearned verdict. Both fail this item

---

## Ownership Boundary Verification

Run over any chart document carrying nontrivial rationale, and over implementation documentation written near a coordinate. The contract is in [`ownership-boundary.md`](ownership-boundary.md).

- [ ] For each nontrivial reason in the chart: *would this reason survive a full implementation rewrite?* If no, it belongs with the code or its Context Docs owner — move it
- [ ] For each piece of implementation documentation that repeats chart semantics: *does Compass already canonically own this truth?* If yes, reduce it to the smallest local consequence plus a coordinate route
- [ ] No mechanism-specific Chesterton's Fence (queue semantics, retry placement, ordering guarantees, framework quirks) appears in L0–L2 prose
- [ ] No complete semantic explanation is reproduced at both a chart location and an implementation site. When both a chart location and an implementation site carry the same reason, the rewrite test decides which keeps it: a reason that survives a full implementation rewrite stays in the chart; a reason that constrains only the current implementation stays with the code or its Context Docs owner.
- [ ] The chart retains semantic boundaries and current mappings; violation/debt findings, dispositions, and correctness status stay in task records, not chart prose or diagram verdict colors

---

## Named Abstraction Verification (Optional)

Run whenever `ABSTRACTIONS.md` or a `compass-abstraction:` marker exists. The
governing procedure is [`named-abstractions.md`](named-abstractions.md). A
marker without a unique definition or without the installed check is an orphan
claim (`named-abstractions.md` §Prerequisites) and fails this gate until the
user authorizes its removal or completes the missing setup; a catalog without
the installed check fails the same way.

- [ ] The host test suite owns the installed checker and runs passing valid, invalid-slug, missing-definition, malformed-spacing-or-multiline, unsupported-form, and hidden-source fixtures under the one path that the checker and the raw-hit audit exclude
- [ ] Every definition heading has a unique lowercase-hyphen slug and its required `Meaning`, `Essential discriminator`, and `Nearest non-example` sections
- [ ] The repository-wide raw-hit audit has no unsupported or uncounted source claim; every supported marker in the configured source universe resolves to exactly one definition
- [ ] Every marker is adjacent to a stable, authored declaration that owns the claimed instance — never a call site, generated file, barrel export, or convenience import
- [ ] Each marked owner conforms to the definition's discriminator and is not its nearest non-example; this is review evidence, not a script result
- [ ] Every admitted name changed a concrete navigation, implementation, or comparison decision, and the change that admitted it records the before/after decision; mere recurrence or resemblance did not qualify it
- [ ] `ABSTRACTIONS.md` contains no occurrence paths, feature mappings, `used-by` lists, edges, flows, or history
- [ ] Marker absence is treated as unknown, searches are reported as declared occurrences only, and no coverage or completeness claim is made
- [ ] No named abstraction reinterprets an L3 stereotype or changes any L0–L4 semantic entity

A green mechanical check establishes only definition shape, slug uniqueness,
and marker resolution. It does not establish that a marked owner conforms, that
all conforming code is marked, or that the abstraction is useful.

---

## Lexicon Verification (Optional)

Run whenever `{chart-root}/LEXICON.jsonl` or a `### Lexicon` section exists.
The governing procedure is [`lexicon.md`](lexicon.md). The check is
`compass_lex.py check`, invoked from the host test suite by the skill path
beside the chart check and not folded into it (`lexicon.md` §The installed
check); a lexicon without the installed check is unproven from the next rename
onward.

- [ ] The host test suite runs `python3 {compass-skill}/scripts/compass_lex.py --chart-root … --repo-root … check` and it exits 0
- [ ] Every row's admission is a Create task of its own whose record holds the candidate it came from; a row with no such record is retired
- [ ] Every glossary term with a lexicon row links it with `### Lexicon`; the heading being that row's first speech form is the script's to prove
- [ ] No `note` carries meaning — a note that restates the glossary is the glossary's, and the row loses it
- [ ] A `where` row points outside the repository and nothing inside it, and its code stems are optional; a row for something the repository holds uses `chart` or `scope`

A green check proves the file's shape and that every stem still occurs in
source. It does not prove a form is what people actually say; Spot Check
step 5 does.

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
- [ ] `VIEWPORTS.md`, where it exists, carries one `##` per viewport named for its question, each with its five `###` sections and a `### Type` naming one of the four viewport types (section presence and type value are script-owned, §First), and every root README linking to it has one to link to

---

## Blind Semantic Read

Run when the L3 checklist passes (Phase C), before calling the level done, and again after any later phase that touched more than one document. Every other checklist in this file measures the container — headings, links, coordinates, symmetry — and all of them pass on a chart that is well-formed and untrue. This one reads the arguments.

The reader is blind: a fresh agent context holding only `{chart-root}` and this list — no authoring session, no exploration scratchpad, no code. An author re-reading their own chart is not a blind read; the author sees what was meant. When no such context can be launched, stop there and report, as with any missing checkpoint. Record every finding in the task's own record and classify it (`growth-and-drift.md` §Classifying Disagreement) before changing anything. A contradiction between two chart pages has no code side to classify against: the page that owns the claim (`create.md` §Quick Reference: Levels, *Kind decides*) keeps it, the other page is reduced to a link, and a correction that changes what a ratified level says goes back through that level's checklist.

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
3. Pick 1 block document — do current imports, events, or other interactions realize its semantic communicates-with relationships? Investigate disagreement; a semantic edge need not be an import edge.
4. Pick 2 rules or invariants the chart records and check them against the product's current behaviour. This is the only check that finds a semantic change, and no structural comparison substitutes for it.
5. Pick 3 glossary terms — is each still the word humans use, and does `compass_lex.py resolve` with that word still land on the row it links to?
6. Check `VIEWPORTS.md` — at most 3–4 active viewports, each still answering its named question with a diagram that describes reality. A chart that skipped L4 has no `VIEWPORTS.md` and no link to one; that passes.
7. Check document sizes against the level budgets in `create.md` §Quick Reference: Levels — oversize means scope creep within the level; split the content down a level, don't raise the budget. L0 and L4 budgets are per unit (context, viewport): an oversize unit is doing too much — split or retire the unit, since there is no level below to push it into.

**If any check fails:** classify the finding using [`growth-and-drift.md`](growth-and-drift.md#classifying-disagreement) — semantic change, implementation remapping, or implementation violation — and respond per the priority order there. A finding repaired before it is classified is the failure this step exists to prevent.
