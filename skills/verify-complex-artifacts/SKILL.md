---
name: verify-complex-artifacts
description: Verify complex generated artifacts after authoring and before handoff, publication, merge, deployment, or acceptance. Use for post-generation verification of complex artifacts or artefacts, isolated and unbiased output-context review, release or readiness gates, independent QA, and create-or-change requests that explicitly require a final gate for compound outputs such as code changes, websites, documents, slide decks, spreadsheets, PDFs, diagrams, data or configuration bundles, and multi-file deliverables. Use especially when tests alone cannot establish visual, structural, cross-file, contextual, or requirement correctness. Run after the generation workflow has produced a candidate; do not use as the primary authoring workflow or for a narrow single-check request.
---

# Verify Complex Artifacts

Gate a finished candidate between generation and its next trust boundary.
Separate factual and deterministic evidence from an isolated output-context
review so the producer cannot explain the artifact into passing.

## Laws

1. **Gate the candidate, not the conversation.** Verify the final files,
   renders, behaviors, and consumer entry points. Do not pass an artifact from a
   producer's summary, confidence, or remembered tool output.
2. **Freeze the factual boundary.** Name the candidate revision, artifact
   manifest, governing sources, intended consumer, and next transition before
   checking. Keep that producer interpretation outside the isolated
   output-context review. A repair creates a new revision and invalidates
   affected results.
3. **Keep gate classes distinct.** Deterministic quality checks establish
   machine-testable facts. Factual review checks requirements and source truth.
   Isolated output-context review checks inferable context, semantic coherence,
   and process residue. Human acceptance resolves subjective or strategic fit.
   One class cannot substitute for another.
4. **Verify through the consumer surface.** Parse source, but also open, render,
   run, import, install, print, navigate, or recalculate the artifact from the
   entry point its consumer receives.
5. **Turn prohibitions into checks.** Convert important “must not” constraints
   into a linter, schema, assertion, search, permission boundary, or explicit
   adversarial review item whenever possible.
6. **Do not self-certify output-context integrity.** The producing context may
   run factual and deterministic checks, but a fresh isolated reviewer with no
   drafting history must perform the output-context gate.
7. **Enforce an unbiased review boundary.** Give the reviewer exactly the final
   target and neutral durable review rules. Give it no producer interpretation,
   consumer or reader profile, artifact role, layer or rung, source facts,
   validation output, process declaration, expected verdict, intended repair,
   or prior review. It must infer context from the artifact and cite that
   evidence in its verdict.
8. **Fail visibly.** A skipped required check, unavailable consumer view, or
   unavailable independent reviewer is `UNVALIDATED`, not a pass. A known
   violation is `BLOCK`.
9. **Repair by revision.** If edits are authorized, repair the production
   artifact outside the review session, regenerate derived outputs, rerun every
   invalidated check, and use a fresh reviewer.
10. **Reserve acceptance for judgment.** Ask a human about product direction,
    taste, brand, risk ownership, or an ambiguous contract. Do not ask a human
    to compensate for failed syntax, broken links, missing requirements, or
    other checkable defects.

## Route the request

Choose the smallest route that covers the requested trust transition:

| Request | Route |
| --- | --- |
| A complex artifact already exists and must be ready for handoff, merge, publication, deployment, or delivery | Run the complete gate |
| Create or change an artifact and verify it | Finish the relevant generation workflow, freeze its candidate, then run this skill as a separate phase |
| Review only, audit, or assess readiness | Run the gates and report; do not edit |
| Verify one explicit property such as syntax, links, formulas, or tests | Run the repository-native check; use this skill only if an integrated readiness decision is also requested |
| Decide whether the result is desirable, on-brand, or strategically correct | Run applicable quality and review gates first, then request human acceptance |

This skill owns the post-generation gate, not the domain-specific authoring
method. A producing skill may define what a correct document, site, code
change, or data product means; keep that domain contract as an input rather
than copying its workflow here.

## Run the complete gate

### 1. Define the trust boundary

Record:

- the exact candidate revision and every artifact in scope;
- the next transition and the consumer or system receiving it;
- authoritative requirements, schemas, source facts, policies, and explicit
  user decisions;
- critical failure modes and irreversible or high-impact consequences;
- whether repairs are authorized and who owns final acceptance.

Separate verified requirements from assumptions. If scope or strategic intent
cannot be inferred safely, return `NEEDS-HUMAN-DECISION`; do not invent a
contract.

### 2. Build the artifact manifest

Inventory primary files, generated or derived files, cross-file references,
consumer entry points, and required views. Include enough identity to detect a
stale check: revision, path, version, checksum, or an equivalent stable marker.

Read [artifact checks](references/artifact-checks.md) and select only the
applicable artifact families. Add contract-specific checks before running
generic ones.

For a compound deliverable, state cross-artifact invariants such as:

- a README command matches the packaged executable;
- a chart agrees with its source table;
- a PDF export matches the editable document;
- screenshots reflect the shipped interface;
- schemas, examples, generated clients, and runtime defaults agree.

### 3. Freeze the factual verification plan

Create a concise verification plan before running checks. It must identify:

- candidate and manifest;
- consumer, transition, and authoritative sources;
- requirement and invariant IDs;
- required factual, deterministic, and consumer-surface checks;
- severity and pass rules;
- acceptance questions and decision owners.

Do not change the contract merely to make the candidate pass. A legitimate
plan or contract change is a new gate revision and must remain visible in the
handoff. This plan is producer context: never include it in the isolated
output-context review.

### 4. Run factual and deterministic gates

Prefer repository-native validators, builds, tests, linters, schema checks,
exporters, and inspectors. Capture the command or tool, candidate revision,
scope, result, and material counts.

Check requirements, authoritative source facts, and cross-artifact invariants
here. Account for every in-scope requirement or record an explicit exclusion.
These checks may use domain skills, source repositories, specifications,
schemas, and validation output; none of that evidence enters the isolated
output-context review.

Run prerequisite checks before expensive or judgment-heavy checks. Stop the
transition on a failed required check. If repair is authorized, fix the
candidate and restart from the earliest invalidated gate; otherwise report
`BLOCK`.

A command exiting successfully proves only the property it actually checks.
Do not relabel a build as semantic, visual, security, or requirement
verification.

### 5. Inspect consumer surfaces

Exercise the artifact from its declared starting state:

1. Open or execute each primary entry point.
2. Inspect every materially distinct representation or mode.
3. Traverse the critical reader, user, operator, or importer path.
4. Check boundaries, error states, empty or extreme cases, and cross-artifact
   links.
5. Record what was observed and which views or environments were unavailable.

Use rendered evidence for layout and visual claims. Use runtime or imported
evidence for behavioral claims. Source inspection alone does not pass these
checks.

### 6. Run the isolated output-context review

Start a fresh reviewer or isolated agent session with no inherited generation
context. Give it exactly:

1. the final review target; and
2. [output-context review](references/output-context-review.md), unchanged.

Prefer the complete final artifact. Use a diff only when it retains enough
final-state context to assess the changed material and its opening or primary
entry surface. For a compound artifact, provide the delivered bundle itself;
do not add a producer-authored wrapper or manifest solely for review.

Supply no task summary, scope statement, artifact classification, consumer or
reader description, role, layer or rung, source facts, validation summary,
process declaration, producer rationale, prior review, expected verdict, or
intended fix. The reviewer must not consult other sources. It reviews only; it
does not edit or rewrite the artifact.

Require it to infer the subject, artifact role and layer, consumer or reader,
task, classification, and process status from the target and cite target
evidence. This gate's `PASS` means the output is semantically coherent in its
own context and free of unjustified process residue. It does not establish
external factual correctness, requirement coverage, cross-artifact truth, or
deterministic-check results.

### 7. Resolve the verdict

Use exactly one gate status:

- `PASS`: every required factual, deterministic, and consumer-surface check
  passed, the fresh output-context reviewer passed, and acceptance passed or
  was not required.
- `BLOCK`: a known defect, contradiction, failed required check, or unmet
  contract remains.
- `NEEDS-HUMAN-DECISION`: only a subjective, strategic, ownership, or genuinely
  ambiguous contract decision prevents completion.
- `UNVALIDATED`: a required tool, view, source, environment, or independent
  reviewer was unavailable.

On `BLOCK`, repair only when authorized. Create a new candidate revision,
rerun invalidated checks, and use a new independent reviewer who receives no
prior verdict or repair narrative.

### 8. Produce the gate record

Report:

- candidate revision, manifest, consumer, and trust transition;
- contract sources and assumptions;
- deterministic checks with commands, results, and counts;
- consumer surfaces and critical paths observed;
- isolated output-context reviewer status and inferred context;
- human acceptance result or exact decision needed;
- exclusions, unavailable checks, residual risks, and final gate status.

Keep the gate record outside the delivered artifact unless that record is
itself an explicitly requested deliverable. Never add production-process
commentary merely to prove that verification occurred.

## Completion conditions

Declare the post-generation gate complete only when:

1. the manifest accounts for every artifact and derived representation in
   scope;
2. the factual verification plan accounts for every requirement and
   cross-artifact invariant;
3. applicable factual and deterministic checks ran against the reported
   candidate revision;
4. primary consumer paths and materially distinct views were exercised;
5. a fresh isolated output-context reviewer inferred context from only the
   target and neutral rules and returned a valid verdict;
6. required human acceptance is recorded;
7. the handoff distinguishes `PASS`, `BLOCK`, `NEEDS-HUMAN-DECISION`, and
   `UNVALIDATED` without softening them.
