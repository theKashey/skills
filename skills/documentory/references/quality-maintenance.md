# Quality and maintenance

Use this reference for documentation audits, PR review, release preparation, and ongoing maintenance.

## Evidence scorecard

Report documentation quality with evidence and counts.

| Gate | Pass condition |
| --- | --- |
| Currentness | No known contradiction with current exports, types, defaults, routes, tests, or supported versions. |
| Public-contract coverage | Every changed public export, option, route, command, and relevant error is documented in an authorized existing surface or has an explicit justified exclusion. |
| Minimum sufficient explanation | Each changed unit gives its intended reader the relevance, behavior, evidence, and boundaries needed to act or decide safely; do not force irrelevant detail into a low-risk entry. |
| Claim evidence | Evaluative or comparative claims have adjacent, interpretable evidence and measurement conditions; otherwise they state observable behavior without unsupported adjectives. |
| Scan-path usability | A reader scanning the opening, headings, and descriptive links can identify relevance, scope, the first-success route, and the next useful detail without relying on decorative formatting. |
| Entry-point validity | Commands, links, paths, and prerequisites work from where the intended reader encounters the documentation; consumer instructions do not silently assume a checkout, unpublished files, or maintainer access. |
| Reader-path usability | A representative intended reader can complete the documented first-success or task path from a clean supported environment without undocumented setup or unsafe inference; any untested assumptions are explicit. |
| Level fit | Guided, Balanced, or Compressed matches the stated reader; explanatory detail is neither withheld from a reader who needs it nor repeated for one who does not. |
| Example integrity | Every fenced example is runnable and validated, illustrative and syntax-checked, partial with stated omissions, or explicitly pseudocode. |
| Intent clarity | Different reader questions remain distinguishable within the existing structure; mixed intent may be reported as an optional split candidate. |
| Progressive disclosure | README provides orientation and first success; detail follows contextual links to existing material or clear in-page sections rather than unexplained link dumps or forced new pages. |
| Context resilience | A maintainer seeing only the changed symbol, nearby lines, and search matches can identify the non-local purpose, invariant, ownership boundary, or prohibited simplification required for a safe change. |
| Comment discipline | New code-local documentation preserves public semantics hidden by the signature or non-obvious why and why-not; none narrates mechanically recoverable behavior. |
| Navigation health | Links resolve; docs build where supported; essential pages are not orphaned. |

Use a task-local table such as:

| Surface | Public items covered | Examples validated | Links checked | Open risks |
| --- | ---: | ---: | ---: | --- |
| Runtime reference | 12 of 12 | 2 of 2 | 8 of 8 | None |

Do not replace this with word counts, generic readability scores, or a claim that documentation looks good.

Coverage means a discoverable canonical owner, not an independent paragraph or
file for every symbol. Group straightforward related types when that preserves
findability and safe use.

The absence of a documentation build or snippet harness does not pass the
example gate. Treat it as a visible risk: classify unsupported samples
conservatively and recommend the smallest repository-native check that would
validate the featured path.

## Audit questions

Ask for every changed section:

1. What does the reader need to know before this statement or snippet?
2. Does the text describe the present contract, a historical change, or implementation rationale? Is it in the right kind of content and an authorized existing surface?
3. Can the reader infer a capability, security property, or ownership boundary that is not actually guaranteed?
4. Does a code block prove a claim only after surrounding prose explains its role?
5. Is this fact duplicated elsewhere, and which location is canonical?
6. What source evidence verifies it? For an evaluative or comparative claim, is the evidence adjacent and are its conditions clear?
7. On a landing page, can a scanning reader determine relevance, scope, the first-success route, and the next detail without reading every paragraph?
8. From where does the intended reader encounter this document, and do its commands, links, paths, credentials, or prerequisites assume access available only to a maintainer?
9. If setup or first success changed, was it checked from that entry point in a clean supported environment, and which assumptions remain untested?
10. For code-local prose, which fact would disappear if the reader saw only the changed symbol and search matches, and what plausible wrong edit does it prevent?

Flag bare verbs such as supports, handles, claims, configure, use, secure, or works when nearby text does not supply behavior, condition, and boundary.

## Change triggers

Require a documentation-impact decision when a change affects:

- public exports, type shapes, configuration, defaults, CLI commands, routes, or response/error contracts;
- installation, supported runtimes or versions, generated API inputs, or docs-site navigation;
- security, authorization, persistence, lifecycle, compatibility, or migration behavior;
- example programs or documentation build tooling.

Choose one result and record the evidence:

- update current docs;
- update changelog or migration docs;
- update JSDoc or code-local rationale;
- no user-facing documentation impact.

## Release and drift review

At release cadence:

1. Compare the public export and configuration inventory with reference coverage.
2. Revalidate the README first-success path and featured examples from a clean supported environment when feasible; record any untested assumptions.
3. Run repository-native docs builds, link checks, type checks, doctests, or example tests.
4. Search current documentation for legacy names and historical wording that should be in migration material.
5. Re-check that public defaults, errors, supported versions, and security boundaries match source.

Prefer generated inventory or repository-native documentation tooling. Introduce a maintained API map only if coverage cannot otherwise be derived, because every additional index is another drift risk.
