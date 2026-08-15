# Quality and maintenance

Non-inline documentation can look complete while stale contracts, broken reader
paths, or copied remote mechanics remain. Use this full reference for an audit,
release, work spanning multiple non-inline surfaces, or a material risk that
needs the detailed scorecard. Routine single-surface completion uses [Review
documentation at wrap-up](review-documentation-at-wrap-up.md) instead. An
explicit non-inline audit or review is itself the final task. This reference
never applies to line, block, or file comments.

- [Audit documentation](#audit-documentation)
- [Evidence scorecard](#evidence-scorecard)
- [Audit questions](#audit-questions)
- [Change triggers](#change-triggers)
- [End-state exit gate](review-documentation-at-wrap-up.md#end-state-exit-gate)
- [Release and drift review](#release-and-drift-review)

## Audit documentation

Use this workflow only at final work wrap-up or release, or when the user
explicitly requests a non-inline documentation audit, review, or maintenance
plan. That request is itself the final documentation task.

1. State the audit mode, boundary, and evidence horizon before collecting
   evidence. Audit current product documentation against the authorized
   completed product and distribution contract. Exclude any proposition that
   an ordinary publish, tag, deploy, propagation, or rollout operation could
   change without a product or distribution-contract decision, regardless of
   its source; do not report it as a defect, risk, caveat, prerequisite, route,
   or untested assumption. Inspect current delivery state only when the user
   explicitly makes that state the subject. Treat an explicit enduring
   source-only decision as product truth, and audit historical claims against
   durable historical evidence. For a change-set audit, inventory every changed
   public item and affected non-inline surface. For a completeness audit,
   inventory every stable public item and relevant non-inline surface in scope.
   When the distribution contract names external consumers, also inventory
   each material external consumer with their entry path and delivered
   context.
   Establish canonical facts, examples, and repository-native verification
   commands. Exclude line, block, and file comments; exported-symbol JSDoc
   remains a public-contract surface.
2. Read the [locality ladder](locality-ladder.md) only when documentation
   existence, ownership, governed scope, or placement is unresolved. Read
   [content architecture](content-architecture.md) only when a story,
   surface-role, scan-path, or multi-reader alignment question is live. When the
   audit questions the reader, goal, subject, or surface, read
   [casting](casting.md), honor its outcome, and report it before judging story
   coherence. When the scope includes a public contract, configuration
   reference, public JSDoc or TSDoc, or an example, also read [public contracts,
   JSDoc, and examples](api-jsdoc-examples.md).
3. Apply the [evidence scorecard](#evidence-scorecard) only to the gates in the
   stated scope. Distinguish a present-contract defect from missing change
   history; do not recommend the same prose in both places.
4. Report evidence and counts by surface, intentional exclusions, untested
   assumptions, and remaining risks. Do not infer completeness from tone,
   length, or a generic readability score.
5. Do not edit during a review-only request. If changes are separately
   authorized, route each defect through its authoring workflow, then re-run
   only the affected scorecard gates. This full scorecard owns terminal
   completion; do not invoke the compact wrap-up guide afterward.

## Evidence scorecard

Report documentation quality with evidence and counts.

| Gate | Pass condition |
| --- | --- |
| Currentness | At wrap-up, checked evidence shows no contradiction between the documented finished state and the completed exports, types, defaults, routes, tests, or supported versions in scope. |
| Casting validity | When the reader, goal, subject, or surface was new or challenged, the recorded casting outcome is supported by entrant, context, decision-right, trust-boundary, and intervention evidence. A non-`PROCEED` outcome was followed instead of being drafted around; a persisted class predicts a material content choice and is not merely a skill, package, page, task, workflow phase, or job title. Any service priority cites an observation source and window or is explicitly labeled as an unmeasured expectation; lower-frequency classes retain a reachable route. |
| Entry relevance | The document opens with the reader-relevant entry need defined in the reader entry and scan path section of `content-architecture.md` while keeping the governed subject inferable. Every compact chooser or catalog entry names the subject, what it provides, and why the reader would choose it before mechanism. |
| Selection context and impact | Before methodology, workflow, taxonomy, or components, the intended reader can infer the relevant situation or pressure, affected party or system, observable impact or changed decision, and boundary. A chooser may own this context for compact catalog entries; a standalone subject page and a detailed owning section orient themselves locally. |
| Public-contract coverage | Every stable public export, option, route, command, and relevant error in the stated audit scope is accounted for by a discoverable canonical source or has an explicit justified exclusion; prose fills only material semantic gaps. |
| Relationship coverage | Within the stated audit scope, every consumer-visible assertion connecting named subjects that a reader could act on—capability, compatibility, dependency, causation, ordering, or ownership claims—is inventoried by source, relation, target, direction, modality, and condition, then verified against authoritative contracts for both endpoints or an explicit product decision. Record the bound applied and its exclusions. Internal coherence, co-location, and repeated prose are not evidence. |
| Minimum sufficient explanation | Each unit in scope gives its intended reader the relevance, behavior, evidence, and boundaries needed to act or decide safely; do not force irrelevant detail into a low-risk entry. Every retained explanation names the wrong turn, repeated investigation, or unsafe continuation it prevents, and survives subtraction of the cast reader's assumed priors, another subject's speciality, and verified delegated guarantees under [prior and speciality admission](content-architecture.md#prior-and-speciality-admission). When nothing survives that subtraction, deletion or `No document` is the passing result. |
| Surface necessity | The surface passes the [locality ladder's existence and ownership gates](locality-ladder.md#pass-the-existence-and-ownership-gates). |
| Claim evidence | Evaluative or comparative claims have adjacent, interpretable evidence and measurement conditions; otherwise they state observable behavior without unsupported adjectives. |
| Remote-truth stability | Non-inline prose that depends on another owner preserves a stable contract or causal edge and its local consequence; it does not narrate remote mechanics that can change independently. |
| Scan-path usability | On a human-facing entry surface, inspection of the rendered or actual delivered form shows semantically meaningful [focus and attention anchors](content-architecture.md#focus-and-attention-management) that make the primary subject, path, and necessary boundary perceptible before secondary detail without relying on decoration. For a public website presentation page, a browser visitor can identify the intended context, supported outcome, and first verified action; any boundary needed to avoid a likely false expectation appears before it matters. For a public documentation home, a reader can find the relevant topic or exact fact without a product-presentation detour. For a README, the named technical reader can identify the governed scope, boundary, and route for their task without marketing posture. |
| Locality fit | Each fact remains with its established owner. When ownership is unresolved, the ladder supports a placement proposal at the narrowest governed scope visible to affected readers; it does not justify displacing another owner or creating a parallel record. |
| Topology fit | For each material external consumer named by the authorized distribution contract, the entry path delivers or directly routes the orientation, contract, and boundaries that consumer needs; no surface assumes ancestor context its external consumer does not receive. Individually correct documents do not pass this gate while a consumer path fails. |
| Entry-point validity | Commands, links, paths, prerequisites, and assumed context work from the documented starting state; any additional access or knowledge is explicit. |
| Reader-path usability | A representative intended reader can complete the documented outcome from the stated starting state without undocumented setup, unsafe inference, or a required condition or warning that arrives after the action it governs; any untested assumptions are explicit. |
| Level fit | Guided, Balanced, or Compressed matches the stated reader and is applied only to what admission kept; explanatory detail is neither withheld from a reader who needs it nor repeated for one who does not. Substituting one cast for another changes terminology, scaffolding, ordering, examples, and compression only: verified facts, guarantees, and required safety boundaries stay identical under both. |
| Example integrity | Every fenced example is runnable and validated, illustrative and syntax-checked, partial with stated omissions, or explicitly pseudocode. |
| Authorial intent and story coherence | Different reader questions remain distinguishable. The finished surface keeps the primary class and episode's reader goal distinct from the established authorial goal and expresses one evidence-backed through-line, intended reader change, proof, boundary, and completion route. Every major section advances that change, supplies necessary proof or boundary, or serves a materially distinct routed goal; incompatible intents are not blended into a committee story. When a task-local contract governed the change, the finished surface agrees with it. |
| Progressive disclosure | Each surface orients its named reader at its governed scope; detailed facts remain with their established owner and are reached through contextual links when that route is available to the reader. |
| Navigation health | Links resolve; docs build where supported; essential pages are not orphaned; facts needed to act are not available only through a visual. |
| Publishable end state | Non-inline documentation represents the completed result and requires no cleanup operation to remove draft scaffolding, temporary caveats, or promises of future completion. |

Record evidence capable of falsifying qualitative judgments. Use a task-local
table such as:

| Surface | Role and governed scope | Reader path tested | Contract coverage | Examples and links | Open risks |
| --- | --- | --- | ---: | --- | --- |
| Runtime reference | Package or module reference | Integrator finds a default and failure mode | 12 of 12 | 2 examples, 8 links | None |

For the judgment-heavy gates, record the observation:

- **Casting validity:** casting outcome, observed entrant and entry context,
  controlled decision, authority or trust boundary, rejected or merged
  candidates, frequency evidence or unmeasured expectation, direct/deeper
  disposition, and the evidence that supports or would overturn the result.
- **Locality fit:** governed scope, chosen owner, and the plausible competing
  scope.
- **Topology fit:** each material external consumer, their entry point,
  delivered context, and the route by which orientation reaches them.
- **Minimum sufficient explanation:** for each retained explanation, the wrong
  turn, repeated investigation, or unsafe continuation it prevents; for each
  intentional omission, whether visible context, an assumed prior, a verified
  delegated guarantee, or out-of-speciality ownership justifies it.
- **Level fit:** named reader, that reader's assumed priors, one detail
  deliberately included or removed for them, and one verified fact or safety
  boundary that stayed identical when the cast was substituted.
- **Reader path:** starting state, task attempted, and observed result.
- **Scan-path usability:** actual delivered view inspected, primary subject,
  path, and boundary located, and the semantic anchors that exposed them.
- **Progressive disclosure:** canonical detail owner and the route used to
  reach it.
- **Entry relevance:** the reader-relevant entry need served by the opening;
  for each independently selectable catalog subject, also record its name,
  capability, selection value, and entry location.
- **Selection context and impact:** one row per subject with its situation or
  pressure, affected party or system, intended impact or changed decision,
  boundary, and selection-context location.
- **Authorial intent and story coherence:** primary class, proven modifier and
  task-local episode, reader goal, established authorial goal, intended reader
  change, through-line, proof, boundary, completion route, and major sections
  accounted for over total.
- **Relationship coverage:** verified edges over total edges, authoritative
  evidence for both endpoints or the explicit product decision, and every
  exclusion.
- **Remote-truth stability:** remote owner, stable contract or causal edge,
  local consequence, and the implementation detail deliberately omitted.

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
5. Is this fact duplicated elsewhere, and which established owner already holds it?
6. What source evidence verifies it? For an evaluative or comparative claim, is the evidence adjacent and are its conditions clear?
7. Which established owner holds this fact? If ownership is unresolved, which
   governed scope best fits a placement proposal, and would the current surface
   duplicate or displace another owner?
8. What material named-reader gap justifies this surface, and which wrong turn,
   repeated investigation, or unsafe continuation does each retained
   explanation prevent? If readable code, types, tests, metadata, local
   context, an existing canonical surface, the cast reader's assumed priors, a
   verified delegated guarantee, or another subject's speciality already covers
   it, should no addition—or a deletion—be the result?
9. Can the project-defined reader—or the explicit task reader when no durable
   cast exists—find the purpose, primary path, and next detail appropriate to
   their available context and decision?
10. In the authorized completed delivery, where does the intended reader
    encounter this document, and which context, paths, credentials, tools, or
    prerequisites does that contract provide? Omit transient delivery-state
    propositions from the answer and report regardless of where they were
    observed, unless current delivery is the explicit audit subject.
11. If the primary reader path changed, was it checked from its stated starting state, and which assumptions remain untested?
12. For a procedure, does the heading state the task and does each step give one meaningful action after its necessary location, condition, and warning? For a tutorial, can the reader see its meaningful checkpoints?
13. Could this state enter its intended review, merge, or publication without editing away a temporary caveat, placeholder, draft marker, or promise about what will happen later?
14. What does the entering reader need to care about before mechanism? Does the
    opening lead with that reader-relevant entry need while keeping the
    governed subject inferable?
15. Which independently selectable named subjects have their own entry point?
    Does each compact catalog entry provide `name: what and why`? After that
    entry and before internal method or parts, can the reader recover the
    relevant situation or pressure, affected party, intended impact or decision,
    and boundary from its chooser or owning section? Does every standalone
    subject page orient itself locally?
16. Which statements connect two named subjects in a way a reader could act
    on? For each such directed, reciprocal, shared-property, conditional, or
    negative edge in the stated scope, what authoritative contract for both
    endpoints or explicit product decision establishes it?
17. Which non-inline statements describe behavior owned elsewhere? Would each
    remain true if that implementation changed without changing its contract,
    and does the statement preserve a material consequence here rather than
    remote mechanics?
18. For a new, challenged, or substantially reworked reader-facing surface,
    what casting outcome did the entrant, available context, controlled
    decision, authority or trust boundary, and intervention evidence support?
    Did the work follow a result that changed the reader, goal, surface,
    subject, or need for a document, or did it preserve the original brief by
    force?
19. Which explicit decision establishes why the document speaks and what should
    change for its primary class in this episode? Do the opening, every major
    section, proof and limits, and completion route advance that through-line or
    route a materially different goal without competing with it?

Flag bare verbs such as supports, handles, claims, configure, use, secure, or works when nearby text does not supply behavior, condition, and boundary.

## Change triggers

Require a documentation-impact decision when a change affects:

- public exports, type shapes, configuration, defaults, CLI commands, routes, or response/error contracts;
- installation, supported runtimes or versions, generated API inputs, or docs-site navigation;
- security, authorization, persistence, lifecycle, compatibility, or migration behavior;
- example programs or documentation build tooling.

Require a topology review—casting with the post-decision consumer set, not
merely a prose update—when an authorized product or distribution decision
makes an internal component externally consumable, starts or stops independent
distribution, adds a CLI, API, SDK, or generated-docs surface as a direct
external entry point, points a product surface straight at a subsystem, stops
delivering source context with the artifact, or creates a new external
compatibility or operational obligation. Ordinary implementation changes that
preserve the existing consumers and distribution model do not fire this
trigger; neither does registry, tag, or deployment state without a decision.

Also reconsider the canonical surface or its pointer when evidence shows
repeated support questions, failed onboarding or copy-paste paths, search
misses, or documented reader confusion. Do not accumulate an unstructured FAQ
instead of repairing the owned documentation.

Choose one result and record the evidence:

- update current docs;
- update changelog or migration docs;
- update public JSDoc or code-local rationale;
- no user-facing documentation impact.

Record each affected non-inline surface during the work so final coverage does
not depend on reconstructing the change from memory.

## Release and drift review

At release cadence:

1. Compare the public export and configuration inventory with reference coverage.
2. Revalidate each changed primary reader path from its stated starting state,
   including a public-website action, documentation navigation or reference
   lookup, technical integration, maintenance, operation, or recovery as
   applicable. Record untested assumptions.
3. Run repository-native docs builds, link checks, type checks, doctests, or example tests.
4. Search current documentation for legacy names and historical wording that should be in migration material.
5. Re-check that public defaults, errors, supported versions, and security boundaries match source.
6. Re-check non-inline statements about another owner against the stable
   contract they depend on; remove narration of remote mechanics.
7. Apply the [end-state exit
   gate](review-documentation-at-wrap-up.md#end-state-exit-gate) before
   declaring the documentation releasable.

Prefer generated inventory or repository-native documentation tooling. Introduce a maintained API map only if coverage cannot otherwise be derived, because every additional index is another drift risk.

Add custom automation only after repeated use shows that a mechanical check
cannot otherwise be performed reliably.
