---
name: verify-complex-artifacts
description: Use for a final verification, review, QA pass, or readiness gate on a finished multi-file artifact before handoff, merge, publication, deployment, or delivery; not for one routine check.
---

# Verify Complex Artifacts

Gate a finished candidate between generation and its next trust boundary.
Separate factual and deterministic evidence from an isolated output-context
review so the producer cannot explain the artifact into passing.

## Point at the problem

After a gate establishes a defect, name the matching [Sin](SINS.md) in the gate
record: `sin → observed evidence → countermeasure → invalidated gate`. Naming
the mechanism gives the repair a target; it does not turn a plausible mechanism
into proof of cause or completion.

## Laws

1. **Gate the candidate, not the conversation.** Verify the final files,
   renders, behaviors, and consumer entry points. Do not pass an artifact from a
   producer's summary, confidence, or remembered tool output.
2. **Expect gaps; refine from evidence.** Iterative and model-assisted
   production predictably leaves omissions, misplaced emphasis, private-context
   assumptions, and locally coherent relationships. Treat the gate as a way to
   expose and repair those gaps, not as a ceremony for confirming the
   producer's result. Preserve every unresolved gap in the verdict.
3. **Freeze the end-state factual boundary.** Name the candidate revision,
   artifact manifest, governing sources, intended consumer, next transition,
   and authorized state expected when the iteration completes before checking.
   Treat the observed implementation-time state as progress evidence, not as
   the acceptance contract. Keep that producer interpretation outside the
   isolated output-context review. A repair creates a new revision and
   invalidates affected results.
4. **Keep gate classes distinct.** Deterministic quality checks establish
   machine-testable facts. Factual review checks requirements and source truth.
   Consumer-surface inspection establishes what the consumer actually sees,
   runs, and can reach. Isolated output-context review checks inferable
   context, semantic coherence, and process residue. Human acceptance resolves
   subjective or strategic fit. One class cannot substitute for another.
   Security checks belong to the deterministic and factual classes; there is
   no separate security gate.
5. **Verify through the consumer surface.** Parse source, but also open, render,
   run, import, install, print, navigate, or recalculate the artifact from the
   entry point its consumer receives.
6. **Turn prohibitions into checks.** Convert important “must not” constraints
   into a linter, schema, assertion, search, permission boundary, or explicit
   adversarial review item whenever possible.
7. **Do not self-certify output-context integrity.** The producing context may
   run factual and deterministic checks, but a fresh review subagent with no
   drafting history must perform the output-context gate.
8. **Enforce an unbiased review boundary.** Give the reviewer exactly the final
   target and neutral durable review rules. Give it no producer interpretation,
   consumer or reader profile, artifact role or layer, source facts,
   validation output, process declaration, expected verdict, intended repair,
   or prior review. It must infer context from the artifact and cite that
   evidence in its verdict.
9. **Fail visibly.** A skipped required check, unavailable consumer view, or
   unavailable review subagent is `UNVALIDATED`, not a pass. A known
   violation is `BLOCK`.
10. **Repair by revision.** If edits are authorized, repair the production
   artifact outside the review session, regenerate derived outputs, rerun every
   invalidated check, and use a fresh review subagent.
11. **Reserve acceptance for judgment.** Ask a human about product direction,
    taste, brand, risk ownership, or an ambiguous contract. Do not ask a human
    to compensate for failed syntax, broken links, missing requirements, or
    other checkable defects.
12. **Diagnose damage, not polish.** Scan the whole candidate for cross-cutting
    damage signatures before accepting local improvements or passing checks.
    Treat each signature as a lead and prove or dismiss it through the gate
    class capable of observing the affected property.

## Select the post-trigger route

After activation, choose the smallest route that covers the trust transition:

| Activated verification need | Route |
| --- | --- |
| A complex artifact already exists and must be ready for handoff, merge, publication, deployment, or delivery | Run the complete gate |
| Create or change an artifact and verify it | Finish the relevant generation workflow, freeze its candidate, then run the complete gate as a separate phase |
| Review only, audit, or assess readiness | Run the gates and report; do not edit |
| Verify one explicit property such as syntax, links, formulas, or tests | Run the repository-native check; add the complete gate only when an integrated readiness decision is requested |
| Decide whether the result is desirable, on-brand, or strategically correct | Run applicable quality and review gates first, then request human acceptance |

Use the supplied domain contract as gate input. Do not copy a domain-specific
authoring workflow into the gate.

## Run the complete gate

### 1. Define the trust boundary

Record:

- the exact candidate revision and every artifact in scope;
- the next transition and the consumer or system receiving it;
- authoritative requirements, schemas, source facts, policies, and explicit
  user decisions, including the state expected when the current iteration is
  complete;
- critical failure modes and irreversible or high-impact consequences;
- whether repairs are authorized and who owns final acceptance.

Separate completed-state requirements from observations of the current
implementation, then separate verified requirements from assumptions. If the
intended completed state, scope, or strategic intent cannot be inferred safely,
return `NEEDS-HUMAN-DECISION`; do not promote the implementation-time state into
the contract.

### 2. Build the artifact manifest

Inventory primary files, generated or derived files, cross-file references,
consumer entry points, and required views. Include enough identity to detect a
stale check: revision, path, version, checksum, or an equivalent stable marker.

Read [artifact checks](references/artifact-checks.md), apply its cross-cutting
damage-signature scan, and select only the applicable artifact families. Add
contract-specific checks before running generic ones.

For a compound deliverable, state cross-artifact invariants such as:

- a README command matches the packaged executable;
- a chart agrees with its source table;
- a PDF export matches the editable document;
- screenshots reflect the shipped interface;
- schemas, examples, generated clients, and runtime defaults agree.

Inventory every material consumer-visible assertion connecting named subjects
as `source, relation, target, direction, modality, condition`. Material means
an edge a consumer could act on: a capability, compatibility, dependency,
causation, ordering, or ownership claim within the frozen scope. Record the
bound applied and its exclusions. Verify each inventoried edge against
authoritative contracts for both endpoints or an explicit product decision.
Repeated prose, co-location, valid links, and internal coherence are not
evidence for a relationship.

### 3. Freeze the factual verification plan

Create a concise verification plan before running checks. It must identify:

- candidate and manifest;
- consumer, transition, and authoritative sources;
- requirement and invariant IDs, minting short stable IDs when the request
  supplies none;
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

For every plausible damage signature, record the target evidence and run the
adversarial check named in the reference. Route proof leakage, disproportionate
attention, and placement drift through the isolated output-context review as
well as any factual gate they trigger. Do not clear a signature because the
change is requested, locally correct, or covered by a passing proxy check.

Check requirements, authoritative source facts, and cross-artifact invariants
here. Account for every in-scope requirement or record an explicit exclusion.
Account separately for every named-subject relationship edge in the manifest's
recorded bound or return `BLOCK`, `UNVALIDATED`, or `NEEDS-HUMAN-DECISION`
according to the missing evidence or authority.
These checks may use domain skills, source repositories, specifications,
schemas, and validation output; none of that evidence enters the isolated
output-context review.

Reconcile the candidate with the authorized state at the end of the iteration,
not merely with a checkout, branch, rollout, or artifact observed while work is
in flight. A consumer-visible record of that intermediate state is `BLOCK` when
it stands in for the completed contract, even if it was accurate when recorded.
A transitional state passes only when the finished product deliberately
supports it as part of its enduring contract.

Run prerequisite checks before expensive or judgment-heavy checks. Stop the
transition on a failed required check. If repair is authorized, fix the
candidate and restart from the earliest invalidated gate; otherwise report
`BLOCK`.

Apply the named sin's countermeasure to the repair plan, then rerun every
invalidated gate. The owning gate still proves whether the defect is repaired.

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

Spawn a fresh review subagent with no inherited generation context. Give it
exactly:

1. the final review target; and
2. [output-context review](references/output-context-review.md), unchanged.

Prefer the complete final artifact. Use a diff only when it retains enough
final-state context to assess the changed material and its opening or primary
entry surface. For a compound artifact, provide the delivered bundle itself;
do not add a producer-authored wrapper or manifest solely for review.

Supply no task summary, scope statement, artifact classification, consumer or
reader description, role or layer, source facts, validation summary,
process declaration, producer rationale, prior review, expected verdict, or
intended fix. The reviewer must not consult other sources; when the harness
supports tool restriction, limit its tools to reading the supplied target. It
reviews only; it does not edit or rewrite the artifact.

Require it to infer the subject, consumer or system, task or effect, and process
status from the target where those are material, and cite target evidence. When
the target presents independently selectable named subjects, require the
reviewer's per-subject result row, as specified in the review rules, for each.
Do not require a documentation-style
offer from code, spreadsheets, or other artifacts whose consumer surface
establishes purpose differently. This gate's `PASS` means the output is semantically coherent
in its own context and free of unjustified process residue. It does not
establish external factual correctness, requirement coverage, cross-artifact
truth, or deterministic-check results.

### 7. Resolve the verdict

Use exactly one gate status:

- `PASS`: every required factual, deterministic, and consumer-surface check
  passed, the fresh output-context review subagent passed, and acceptance passed or
  was not required.
- `BLOCK`: a known defect, contradiction, failed required check, or unmet
  contract remains.
- `NEEDS-HUMAN-DECISION`: only a subjective, strategic, ownership, or genuinely
  ambiguous contract decision prevents completion.
- `UNVALIDATED`: a required tool, view, source, environment, or review
  subagent was unavailable.

On `BLOCK`, repair only when authorized. Create a new candidate revision,
rerun invalidated checks, and use a new review subagent that receives no
prior verdict or repair narrative.

### 8. Produce the gate record

Report:

- candidate revision, manifest, consumer, and trust transition;
- contract sources and assumptions;
- named-subject relationship edges, authoritative evidence, exclusions, and
  verified-over-total count;
- deterministic checks with commands, results, and counts;
- damage signatures tested, evidence observed, and gate disposition;
- consumer surfaces and critical paths observed;
- isolated output-context review subagent status and inferred context;
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
4. every plausible cross-cutting damage signature was tested through its
   owning gate rather than dismissed from producer intent;
5. every material consumer-visible named-subject relationship in the recorded
   bound was inventoried and verified against both endpoint contracts or an
   explicit product decision;
6. primary consumer paths and materially distinct views were exercised;
7. a fresh output-context review subagent inferred context from only the
   target and neutral rules and returned a valid verdict;
8. required human acceptance is recorded;
9. the handoff distinguishes `PASS`, `BLOCK`, `NEEDS-HUMAN-DECISION`, and
   `UNVALIDATED` without softening them.
