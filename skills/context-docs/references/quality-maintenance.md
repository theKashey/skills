# Quality and maintenance

Non-inline documentation can look complete while stale contracts, broken reader
paths, or copied remote mechanics remain. Use this reference at final wrap-up
or release to decide from evidence whether the finished documentation is
publishable and to expose any remaining risk. An explicit non-inline
documentation audit or review is itself this final task. This reference never
applies to line, block, or file comments.

- [Evidence scorecard](#evidence-scorecard)
- [Audit questions](#audit-questions)
- [Change triggers](#change-triggers)
- [End-state exit gate](#end-state-exit-gate)
- [Release and drift review](#release-and-drift-review)

## Evidence scorecard

Report documentation quality with evidence and counts.

| Gate | Pass condition |
| --- | --- |
| Currentness | At wrap-up, checked evidence shows no contradiction between the documented finished state and the completed exports, types, defaults, routes, tests, or supported versions in scope. |
| Entry relevance | The document opens with the reader-relevant entry need defined in the reader entry and scan path section of `content-architecture.md` while keeping the governed subject inferable. Every compact chooser or catalog entry names the subject, what it provides, and why the reader would choose it before mechanism. |
| Selection context and impact | Before methodology, workflow, taxonomy, or components, the intended reader can infer the relevant situation or pressure, affected party or system, observable impact or changed decision, and boundary. A chooser may own this context for compact catalog entries; a standalone subject page and a detailed owning section orient themselves locally. |
| Public-contract coverage | Every stable public export, option, route, command, and relevant error in the stated audit scope is accounted for by a discoverable canonical source or has an explicit justified exclusion; prose fills only material semantic gaps. |
| Relationship coverage | Within the stated audit scope, every consumer-visible assertion connecting named subjects that a reader could act on—capability, compatibility, dependency, causation, ordering, or ownership claims—is inventoried by source, relation, target, direction, modality, and condition, then verified against authoritative contracts for both endpoints or an explicit product decision. Record the bound applied and its exclusions. Internal coherence, co-location, and repeated prose are not evidence. |
| Minimum sufficient explanation | Each unit in scope gives its intended reader the relevance, behavior, evidence, and boundaries needed to act or decide safely; do not force irrelevant detail into a low-risk entry. |
| Surface necessity | The surface passes the [locality ladder's existence gate](locality-ladder.md#existence-gate). |
| Claim evidence | Evaluative or comparative claims have adjacent, interpretable evidence and measurement conditions; otherwise they state observable behavior without unsupported adjectives. |
| Remote-truth stability | Non-inline prose that depends on another owner preserves a stable contract or causal edge and its local consequence; it does not narrate remote mechanics that can change independently. |
| Scan-path usability | The named reader can identify the document's purpose, task or destination from headings and links, primary path, and next useful detail without relying on decorative formatting. For a public website presentation page, a browser visitor can identify the intended context, supported outcome, and first verified action; any boundary needed to avoid a likely false expectation appears before it matters. For a public documentation home, a reader can find the relevant topic or exact fact without a product-presentation detour. For a README, the named technical reader can identify the governed scope, boundary, and route for their task without marketing posture. |
| Locality fit | Each fact has a canonical owner at the narrowest governed scope visible to affected readers; overlapping physical and logical roles are explicit rather than duplicated or forced apart. |
| Entry-point validity | Commands, links, paths, prerequisites, and assumed context work from the documented starting state; any additional access or knowledge is explicit. |
| Reader-path usability | A representative intended reader can complete the documented outcome from the stated starting state without undocumented setup, unsafe inference, or a required condition or warning that arrives after the action it governs; any untested assumptions are explicit. |
| Level fit | Guided, Balanced, or Compressed matches the stated reader; explanatory detail is neither withheld from a reader who needs it nor repeated for one who does not. |
| Example integrity | Every fenced example is runnable and validated, illustrative and syntax-checked, partial with stated omissions, or explicitly pseudocode. |
| Intent clarity | Different reader questions remain distinguishable within the existing structure; mixed intent may be reported as an optional split candidate. |
| Progressive disclosure | Each surface orients its named reader at its governed scope; detailed facts remain at their canonical owner and are reached through contextual links. |
| Navigation health | Links resolve; docs build where supported; essential pages are not orphaned; facts needed to act are not available only through a visual. |
| Publishable end state | Non-inline documentation represents the completed result and requires no cleanup operation to remove draft scaffolding, temporary caveats, or promises of future completion. |

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
- **Entry relevance:** the reader-relevant entry need served by the opening;
  for each independently selectable catalog subject, also record its name,
  capability, selection value, and entry location.
- **Selection context and impact:** one row per subject with its situation or
  pressure, affected party or system, intended impact or changed decision,
  boundary, and selection-context location.
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
5. Is this fact duplicated elsewhere, and which location is canonical?
6. What source evidence verifies it? For an evaluative or comparative claim, is the evidence adjacent and are its conditions clear?
7. Which ladder rung contains everything this fact governs, and is the current surface serving that role rather than a broader or narrower one?
8. What material named-reader gap justifies this surface? If readable code,
   types, tests, metadata, local context, or an existing canonical surface
   already covers it, should no addition—or a deletion—be the result?
9. Can the named reader—stranger, developer, coding agent, coder, maintainer,
   integrator, operator, administrator, support engineer, end user, or browser
   visitor—find the purpose, primary path, and next detail appropriate to their
   role?
10. From where does the intended reader encounter this document, and which context, paths, credentials, tools, or prerequisites are actually available there?
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
- update public JSDoc or other non-inline documentation;
- no user-facing documentation impact.

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

A supported transitional state in the finished product is not implementation
residue. Document it when it is part of the verified contract.

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
7. Apply the end-state exit gate before declaring the documentation releasable.

Prefer generated inventory or repository-native documentation tooling. Introduce a maintained API map only if coverage cannot otherwise be derived, because every additional index is another drift risk.
