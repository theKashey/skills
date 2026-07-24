# Quality and maintenance

Quality and maintenance keep documentation trustworthy as code changes: claims
remain evidence-backed, reader paths stay usable, and drift becomes visible
before publication.

Use this reference for documentation audits, PR review, release preparation,
and ongoing maintenance.

- [Evidence scorecard](#evidence-scorecard)
- [Audit questions](#audit-questions)
- [Change triggers](#change-triggers)
- [Output-context review gate](#output-context-review-gate)
- [End-state exit gate](#end-state-exit-gate)
- [Release and drift review](#release-and-drift-review)

## Evidence scorecard

Report documentation quality with evidence and counts.

| Gate | Pass condition |
| --- | --- |
| Currentness | At exit, checked evidence shows no contradiction between the documented finished state and the completed exports, types, defaults, routes, tests, or supported versions in scope. |
| Public-contract coverage | Every stable public export, option, route, command, and relevant error in the stated audit scope is documented in an authorized existing surface or has an explicit justified exclusion. |
| Minimum sufficient explanation | Each unit in scope gives its intended reader the relevance, behavior, evidence, and boundaries needed to act or decide safely; do not force irrelevant detail into a low-risk entry. |
| Claim evidence | Evaluative or comparative claims have adjacent, interpretable evidence and measurement conditions; otherwise they state observable behavior without unsupported adjectives. |
| Scan-path usability | The named reader can identify the document's purpose, task or destination from headings and links, primary path, and next useful detail without relying on decorative formatting. For a public landing, an outsider can identify the problem and intended context, supported outcome, a concrete reason to believe it, and the first action; any boundary needed to avoid a likely false expectation appears before it matters. |
| Locality fit | Each fact has a canonical owner at the narrowest governed scope visible to affected readers; overlapping physical and logical roles are explicit rather than duplicated or forced apart. |
| Entry-point validity | Commands, links, paths, prerequisites, and assumed context work from the documented starting state; any additional access or knowledge is explicit. |
| Reader-path usability | A representative intended reader can complete the documented outcome from the stated starting state without undocumented setup, unsafe inference, or a required condition or warning that arrives after the action it governs; any untested assumptions are explicit. |
| Level fit | Guided, Balanced, or Compressed matches the stated reader; explanatory detail is neither withheld from a reader who needs it nor repeated for one who does not. |
| Example integrity | Every fenced example is runnable and validated, illustrative and syntax-checked, partial with stated omissions, or explicitly pseudocode. |
| Intent clarity | Different reader questions remain distinguishable within the existing structure; mixed intent may be reported as an optional split candidate. |
| Progressive disclosure | Each surface orients its named reader at its governed scope; detailed facts remain at their canonical owner and are reached through contextual links. |
| Context resilience | A maintainer seeing only the changed symbol, nearby lines, and search matches can identify the non-local purpose, invariant, ownership boundary, or prohibited simplification required for a safe change. |
| Comment discipline | New code-local documentation preserves public semantics hidden by the signature or non-obvious why and why-not; none narrates mechanically recoverable behavior. |
| Fence visibility | Every Chesterton's fence in scope has either a verified rationale at the governed decision or an explicit accepted `TODO` or `FIXME` recording that its rationale is unknown. |
| Navigation health | Links resolve; docs build where supported; essential pages are not orphaned; facts needed to act are not available only through a visual. |
| Publishable end state | Documentation and code represent the completed result and require no cleanup operation to remove draft scaffolding, temporary caveats, or promises of future completion. Any accepted gap is an explicit `TODO` or `FIXME` comment. |
| Output-context integrity | A fresh independent reviewer passes the output-context review for every changed artifact in scope. The artifact foregrounds its governed subject rather than its creation or review process; any declared process content is reader-relevant and authorized. A producer self-review or unavailable reviewer is `UNVALIDATED`, not a pass. |

Record evidence capable of falsifying qualitative judgments. Use a task-local
table such as:

| Surface | Role and rung | Reader path tested | Contract coverage | Examples and links | Open risks |
| --- | --- | --- | ---: | --- | --- |
| Runtime reference | Package reference, rung 5 | Integrator finds a default and failure mode | 12 of 12 | 2 examples, 8 links | None |

For the judgment-heavy gates, record the observation:

- **Locality fit:** governed scope, chosen owner, and the plausible competing
  rung.
- **Level fit:** named reader and one detail deliberately included or removed
  for that reader.
- **Reader path:** starting state, task attempted, and observed result.
- **Progressive disclosure:** canonical detail owner and the route used to
  reach it.
- **Context resilience:** the non-local fact and plausible wrong edit its
  absence would invite.
- **Output-context integrity:** semantic subject, artifact role, orientation
  window, reviewer verdict, declared process exception, and any exact repair.

Do not replace this with word counts, generic readability scores, or a claim that documentation looks good.

Coverage means a discoverable canonical owner, not an independent paragraph or
file for every symbol. Group straightforward related types when that preserves
findability and safe use.

A surface may route a category to its canonical owner. When a surface is the
canonical reference for a category, such as configuration, routes, or public
API, it accounts for every stable member in its stated scope or records an
explicit exclusion.

The absence of a documentation build or snippet harness does not pass the
example gate. Treat it as a visible risk: classify unsupported samples
conservatively and recommend the smallest repository-native check that would
validate the featured path.

## Audit questions

First state whether this is a change-set audit or a completeness audit. Ask for
every section and public item in that stated scope:

1. What does the reader need to know before this statement or snippet?
2. Does the text describe the present contract, a historical change, or implementation rationale? Is it in the right kind of content and an authorized existing surface?
3. Can the reader infer a capability, security property, or ownership boundary that is not actually guaranteed?
4. Does a code block prove a claim only after surrounding prose explains its role?
5. Is this fact duplicated elsewhere, and which location is canonical?
6. What source evidence verifies it? For an evaluative or comparative claim, is the evidence adjacent and are its conditions clear?
7. Which ladder rung contains everything this fact governs, and is the current surface serving that role rather than a broader or narrower one?
8. Can the named reader—outsider, maintainer, integrator, operator, administrator, support engineer, or end user—find the purpose, primary path, and next detail appropriate to their role?
9. From where does the intended reader encounter this document, and which context, paths, credentials, tools, or prerequisites are actually available there?
10. If the primary reader path changed, was it checked from its stated starting state, and which assumptions remain untested?
11. For a procedure, does the heading state the task and does each step give one meaningful action after its necessary location, condition, and warning? For a tutorial, can the reader see its meaningful checkpoints?
12. For code-local prose, which fact would disappear if the reader saw only the changed symbol and search matches, and what plausible wrong edit does it prevent?
13. Could this state enter its intended review, merge, or publication without editing away a temporary caveat, placeholder, draft marker, or promise about what will happen later?
14. Where is the reason for code's existence or present form unknown? What evidence supplies the missing rationale, or which explicit `TODO` or `FIXME` records the uncertainty?
15. What is the semantic subject, distinct from the artifact role? Does the
    orientation window establish that subject's reader-relevant purpose,
    responsibility, outcome, or boundary before document or production
    mechanics appear?

Flag bare verbs such as supports, handles, claims, configure, use, secure, or works when nearby text does not supply behavior, condition, and boundary.

## Change triggers

Require a documentation-impact decision when a change affects:

- public exports, type shapes, configuration, defaults, CLI commands, routes, or response/error contracts;
- installation, supported runtimes or versions, generated API inputs, or docs-site navigation;
- security, authorization, persistence, lifecycle, compatibility, or migration behavior;
- example programs or documentation build tooling.

Also reconsider the canonical surface or its pointer when evidence shows
repeated support questions, failed onboarding or copy-paste paths, search
misses, or documented reader confusion. Do not accumulate an unstructured FAQ
instead of repairing the owned documentation.

Choose one result and record the evidence:

- update current docs;
- update changelog or migration docs;
- update JSDoc or code-local rationale;
- no user-facing documentation impact.

## Output-context review gate

A changed artifact leaves its producing session as an **unvalidated output**.
Run this semantic review gate after applicable deterministic checks and before
calling the artifact complete. It complements source verification, tests,
example checks, links, and the end-state exit gate; it does not replace them.
The producing agent cannot pass this gate for its own artifact.

### Review packet

Create the reviewer without inherited drafting context. Give it only the final
artifact or changed diff and:

- the semantic subject, artifact role, rung, intended reader, and reader task;
- authoritative facts and completed deterministic validation relevant to the
  artifact;
- whether a durable process is explicitly the requested subject, plus its
  operator, trigger, action, result or decision boundary, scope, and owner;
- the pass rules below.

Do not provide the drafting conversation, producer rationale, prior review,
expected verdict, or intended fix. Those are process context, not evidence for
the reader artifact.

### Pass rules

The reviewer returns `PASS` only when every applicable rule passes with no
unclassified ambiguity:

1. **Subject before artifact.** In the orientation window—the title plus first
   substantive reader-facing prose, excluding navigation—the artifact explains
   the governed subject's reader-relevant purpose, responsibility, outcome,
   contract, boundary, or non-local rationale. For a technical module, package,
   or service, it makes a concrete verified claim about what the unit does or
   owns and names a relevant relationship, boundary, or constraint before
   explaining the README, file, skill, or authoring task.
2. **Durable reader value.** Each changed prose unit advances a current
   contract, verified rationale, durable operating procedure, explicitly
   historical record, or necessary navigation for the named reader.
3. **Finished-artifact focus.** The artifact represents the subject and its
   completed state. Creation, drafting, validation, tool, subagent, instruction,
   and review details remain in the gate record or work handoff unless the
   durable process itself is the declared reader subject.
4. **Verified and local.** Existing truth, locality, end-state, and example
   rules pass. Reader-facing evidence remains only when it helps the reader
   interpret a contract or decision at that rung.
5. **Declared process exception.** A process-oriented artifact identifies its
   enduring operator, trigger, action, result or decision boundary, scope, and
   owner. It may describe that durable process; it does not narrate the
   particular agent session that produced the artifact.

Apply two checks to the orientation window:

- **Deletion:** remove document labels, paths, and phrases such as “this
  README” or “this file.” If no useful claim about the governed subject remains,
  the artifact fails.
- **Substitution:** replace the subject with a sibling unit. If the opening
  remains equally true, it is generic artifact or process prose rather than
  subject orientation.

For changed source code, apply these rules to added comments, JSDoc/TSDoc,
examples, reader-visible strings, test descriptions, and documentation-like
identifiers. Do not force document-shaped prose into code. Repository-native
tests and a code-specific review remain responsible for implementation
correctness beyond this gate's scope.

### Fresh-review protocol

1. Finish the candidate and run applicable deterministic checks.
2. Spawn a fresh independent review subagent with no inherited drafting
   context. When the platform cannot create an isolated subagent, start an
   independent agent session with no inherited drafting context instead.
3. Give it the review packet. It reviews only; it does not edit or rewrite the
   artifact.
4. Require this result:

   ```text
   Status: PASS | BLOCK | NEEDS-HUMAN-DECISION | UNVALIDATED
   Classification: current | historical | rationale | declared process
   Rule results: rules 1–5, with evidence
   Blockers: location, broken rule, reader impact, minimal repair direction
   Unverified facts or classification decisions:
   ```

5. On `BLOCK`, repair from the evidence, rerun applicable checks, and use a
   new fresh reviewer. The producing agent cannot waive its own failed gate.
6. On `NEEDS-HUMAN-DECISION`, ask the user only to resolve artifact scope,
   classification, or strategic intent. Missing evidence remains a block.
7. When no independent reviewer can run, record `UNVALIDATED`; never call that
   a pass or publish-ready result.
8. Put the gate result in the work handoff, not in the finished reader artifact,
   unless the user explicitly requested a review record.

## End-state exit gate

Write current documentation as the contract expected when the requested work is
complete. It may temporarily lead the implementation while both are being
edited, but it must not claim completion until the final code, generated
artifacts, and documented behavior agree.

Reject a result that requires another edit merely to:

- replace future tense with the completed contract;
- remove notes about temporary repository, branch, rollout, or access state;
- delete draft labels, placeholders, commented-out scaffolding, or instructions
  to finish the work later;
- reveal content that was intentionally hidden during implementation.

An explicit `TODO` or `FIXME` comment may remain when it deliberately accepts a
gap. Keep it recognizable as debt and local to the affected code; do not turn
the gap into ordinary prose that makes incomplete behavior appear complete. For
an unresolved Chesterton's fence, this marker records missing knowledge; it is
not a rationale.

A supported transitional state in the finished product is not implementation
residue. Document it when it is part of the verified contract.

The end-state exit gate removes temporary-state residue. The output-context
review gate removes authoring and review residue. Pass both.

## Release and drift review

At release cadence:

1. Compare the public export and configuration inventory with reference coverage.
2. Revalidate each changed primary reader path from its stated starting state,
   including landing first success, integration, maintenance, operation, or
   recovery as applicable. Record untested assumptions.
3. Run repository-native docs builds, link checks, type checks, doctests, or example tests.
4. Search current documentation for legacy names and historical wording that should be in migration material.
5. Re-check that public defaults, errors, supported versions, and security boundaries match source.
6. Apply the end-state exit gate before declaring the documentation releasable.
7. Run the output-context review gate for every changed artifact and retain its
   result with the release evidence.

Prefer generated inventory or repository-native documentation tooling. Introduce a maintained API map only if coverage cannot otherwise be derived, because every additional index is another drift risk.
