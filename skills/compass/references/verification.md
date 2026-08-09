# Verification Procedures

Formal checks that must pass before ratifying a root or advancing L0, L1, L2, L3, or Phase F. Run these as a mandatory gate — not optional polish. This file is the canonical owner of every completion checklist; other files point here rather than restating the items. Levels and phases with no section below carry no gate beyond their exit conditions in [`exploration.md`](exploration.md) and [`growth-and-drift.md`](growth-and-drift.md).

---

## First: move the mechanizable checks out of this file

**An agent ticking its own checkbox is self-certification, and roughly a dozen items below do not need judgment at all.** They are decidable by a script, they go stale silently, and the moment they live in a checklist they are only as reliable as the attention of whoever last ran it. Install them in the host's own test suite during Phase B, so they fail a build rather than waiting for a review:

| Decidable by a script | Owning checklist item |
|---|---|
| every `compass:` address resolves to a chart document | §Coordinate Verification → Correctness |
| every path named in a `## Implementation coordinates` section exists on disk | §Coordinate Verification → Staleness |
| every block folder appears in its root's `CONTAINERS.md`, and every listed block has a folder | §L2 |
| every relative link and heading anchor inside the chart resolves | §Markdown and Navigation |
| every zoom-chain document carries a Mermaid fence | §Markdown and Navigation |
| no forbidden filename (`SCOPE.md`, `CONTEXT.md`, `BLOCK.md`, `COMPONENT.md`) exists under the chart root | §Markdown and Navigation |

```python
# chart_check.py — decidable chart invariants. Adapt the two constants; run it in CI.
import pathlib, re, sys
CHART = pathlib.Path(".compass")          # the declared chart root
SRC_SUFFIXES = {".py", ".ts", ".tsx", ".go", ".rs", ".java", ".rb"}

fail, seen = [], {"addresses": 0, "links": 0, "coordinates": 0, "blocks": 0, "diagrams": 0}
# every line, not just the first: a marker legitimately sits under a comment, a licence
# header or an import block, and a file may carry a second coordinate for another root
addr_re = re.compile(r"^\s*(?:#|//|--)\s*compass:\s*(\S+)", re.M)
anchors = lambda t: {re.sub(r"[^a-z0-9 -]", "", h.lower()).replace(" ", "-")
                     for h in re.findall(r"^#{1,6} (.+)$", t, re.M)}

def doc_for(address):                      # root | root.block | root.block.component
    return CHART.joinpath(*address.split(".")) / "README.md"

for p in pathlib.Path(".").rglob("*"):
    # any dotted directory: .git, .venv, and — the one that bites — a nested git worktree,
    # which otherwise counts every marker in the repository twice
    if p.is_dir() or any(x.startswith(".") for x in p.parts[:-1]): continue
    if "node_modules" in p.parts or p.suffix not in SRC_SUFFIXES: continue
    for address in addr_re.findall(p.read_text(errors="ignore")):
        seen["addresses"] += 1
        if not doc_for(address).exists():
            fail.append(f"{p}: compass: {address} resolves to nothing")

for root in (d for d in CHART.iterdir() if d.is_dir() and d.name != "externals"):
    containers = root / "CONTAINERS.md"
    if not containers.exists(): continue
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
        elif anchor and anchor not in anchors(target.read_text()):
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
        # written as `{3} on purpose — a literal triple backtick would close this code block
        if not re.search(r"^`{3}\s*mermaid", body, re.M):
            fail.append(f"{md}: no mermaid diagram")

for name in ("SCOPE.md", "CONTEXT.md", "BLOCK.md", "COMPONENT.md"):
    for p in CHART.rglob(name): fail.append(f"{p}: identity documents are README.md")

print("\n".join(fail) or "chart: clean — " + ", ".join(f"{v} {k}" for k, v in seen.items()))
sys.exit(1 if fail else 0)
```

**Print the counts, and read them.** A check that scanned nothing exits zero exactly like a check that scanned everything — which is how a chart whose markers were all deleted keeps a green build. If `addresses` drops to 0 after Phase F, the script is passing because it stopped looking.

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
- [ ] The context list passes the Derivation Test (`SKILL.md` §The Derivation Test) — contexts mapping ~1:1 onto packages or onto the layer stack were read off the code, whatever their names now say
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
3. Any that fail → demote immediately (usually an L3 adapter; an internal implementation is L2, a shared helper L5); record the demotion in the compass's L2/L3 tier — name, used-by, and the fact about the dependency that puts it there, never the name of the test it failed — so it cannot be silently re-elevated
4. Re-run diagram checks after all demotions

---

## L2 Isolated Blocks Verification

Run before declaring Phase B complete.

- [ ] Every block has: name, responsibility (1 sentence), logical role, boundary statement, technology, implementation coordinates, communicates-with list
- [ ] Every block's **logical role** maps upward to a stable responsibility or phenomenon of the root, and is stated without naming a directory, package, or technology
- [ ] Every block survives the invariance test: its boundary still makes sense after a structure-only refactor
- [ ] No block exists only because a package, service, or deployable exists — implementation decomposition is not product decomposition
- [ ] No block was split or merged because deployment topology, framework, or repository layout changed
- [ ] **The block list passes the Derivation Test** (`SKILL.md` §The Derivation Test): laid beside the deployables, the packages, and the layers of the stack, it pairs off one-to-one with none of them. This is a check on the *set* — every member can pass the rewrite test while the cut was still read off topology
- [ ] **No residue block.** Every block name is one a practitioner would say out loud, unprompted. A category name (`*-intelligence`, `*-services`, `core`, `shared`, `common`) or a layer name (`foundation`, `platform`, `packages`) means the block was computed from what the other blocks did not absorb
- [ ] At least one block's implementation coordinates span more than one package, layer, or language — if every block maps to exactly one subtree, the cut is the file tree wearing semantic names
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
- [ ] Every coordinate-density observation — several coordinates in one folder, a file carrying two coordinates in one root, a file resisting every enclosing coordinate — carries a recorded disposition: *declutter* (with the move), *legitimate* (with what makes it so), or *debt* (with the independent cohesion or coupling evidence). An observation with no disposition is an unclosed lead; an observation dispositioned as debt on the coordinate pattern alone is an unearned verdict. Both fail this item

---

## Ownership Boundary Verification

Run over any chart document carrying nontrivial rationale, and over implementation documentation written near a coordinate. The contract is in [`ownership-boundary.md`](ownership-boundary.md).

- [ ] For each nontrivial reason in the chart: *would this reason survive a full implementation rewrite?* If no, it belongs with the code or its Context Docs owner — move it
- [ ] For each piece of implementation documentation that repeats chart semantics: *does Compass already canonically own this truth?* If yes, reduce it to the smallest local consequence plus a coordinate route
- [ ] No mechanism-specific Chesterton's Fence (queue semantics, retry placement, ordering guarantees, framework quirks) appears in L0–L2 prose
- [ ] No complete semantic explanation is reproduced at both a chart location and an implementation site

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

## Lead/Bleed Detection Checklist

Run at any time to detect level contamination. These are warning signs, not errors — each requires investigation.

| Signal | Likely cause | Action |
|--------|-------------|--------|
| L1 diagram has >1 node inside the boundary | Internal block leaked up | Remove internals, move to L2 |
| L1 external systems table has a vendor API or library | Implementation detail leaked up | Demote to L3 adapter |
| L1 external added right after a dependency was added | Manifest treated as admission evidence | Re-run both L1 tests against product reality |
| L1 external systems table has an adapter used by only one component | Adapter leaked up | Demote to L3 in that component |
| Block doc references a framework as a peer block | L5 infrastructure promoted | Demote to L5, remove block doc |
| A block's logical role can only be stated by naming a directory | Implementation structure became the identity | Restate semantically or merge the block away |
| A block split at the same time a service was extracted | Topology change mistaken for semantic change | Reclassify as remapping; restore the block |
| A root appeared alongside a new package or repository | Packaging mistaken for logical identity | Re-run root admission; retire if it fails |
| Component has 4+ external dependencies | Possible hidden block boundary or missing facade | Record justification; investigate split |
| File carries two coordinates within one root | Two logical participations, or unresolved chart ambiguity | Investigate and record which — do not split reflexively |
| File carries coordinates from different roots with no ratified second root | Agent invented a root | Remove the invented root |
| Block boundary statement is missing or >2 sentences | Boundary not understood | Clarify before proceeding |
| Component responsibility requires "and" | Component doing too much | Split candidate |
| Component diagram carries 6+ arrows | Too many relationships to hold at one level | Decompose candidate |
| Block communicates-with list exceeds 5 entries | Block doing too much | Record justification; investigate split |
| Siblings at one level describe wildly different breadths | Level not calibrated | Run level calibration |
| Chart prose explains a mechanism that a rewrite would delete | Implementation fence leaked into the chart | Move it to its Context Docs owner |

---

## Spot Check

Run periodically (after any significant code change, or at state 3 maintenance cadence).

1. Pick 5 random source files per block. For each: is it covered by a coordinate? Does that address exist in the chart? Can you navigate component → block → root in ≤2 hops?
2. Pick 3 random component documents — do their implementation coordinates still exist on disk? Classify every miss as remapping before touching anything semantic.
3. Pick 1 block document — does its communicates-with list match actual imports?
4. Pick 2 rules or invariants the chart records and check them against the product's current behaviour. This is the only check that finds a semantic change, and no structural comparison substitutes for it.
5. Pick 3 glossary terms — is each still the word humans use, and are the recorded aliases still the words in code?
6. Check `VIEWPORTS.md` — at most 3–4 active viewports, each still answering its named question with a diagram that describes reality. A chart that skipped L4 has no `VIEWPORTS.md` and no link to one; that passes.
7. Check document sizes against the level budgets in `SKILL.md` §Quick Reference: Levels — oversize means scope creep within the level; split the content down a level, don't raise the budget. L0 and L4 budgets are per unit (context, viewport): an oversize unit is doing too much — split or retire the unit, since there is no level below to push it into.

**If any check fails:** classify the finding using [`growth-and-drift.md`](growth-and-drift.md#classifying-disagreement) — semantic change, implementation remapping, or implementation violation — and respond per the priority order there. A finding repaired before it is classified is the failure this step exists to prevent.
