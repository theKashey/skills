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
| Scan-path usability | A landing reader can identify relevance and first success; an internal technical reader can identify responsibility, boundary, interactions, and validation without relying on decorative formatting. |
| Locality fit | Each fact lives at the lowest rung that contains everything it governs; top-level landing, internal technical, extracted contract, and code-local rationale roles are not conflated. |
| Entry-point validity | Commands, links, paths, prerequisites, and assumed context work from the documented starting state; any additional access or knowledge is explicit. |
| Reader-path usability | A representative intended reader can complete the documented outcome from the stated starting state without undocumented setup or unsafe inference; any untested assumptions are explicit. |
| Level fit | Guided, Balanced, or Compressed matches the stated reader; explanatory detail is neither withheld from a reader who needs it nor repeated for one who does not. |
| Example integrity | Every fenced example is runnable and validated, illustrative and syntax-checked, partial with stated omissions, or explicitly pseudocode. |
| Intent clarity | Different reader questions remain distinguishable within the existing structure; mixed intent may be reported as an optional split candidate. |
| Progressive disclosure | A top-level landing surface provides relevance and first success; each internal technical surface explains its own boundary; detailed facts remain at their canonical rung and are reached through contextual links. |
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
7. Which ladder rung contains everything this fact governs, and is the current surface serving that role rather than a broader or narrower one?
8. On a landing page, can an outsider determine relevance, scope, first success, and the next detail? In an internal technical README, can a maintainer determine responsibility, boundary, interactions, and validation?
9. From where does the intended reader encounter this document, and which context, paths, credentials, tools, or prerequisites are actually available there?
10. If the primary reader path changed, was it checked from its stated starting state, and which assumptions remain untested?
11. For code-local prose, which fact would disappear if the reader saw only the changed symbol and search matches, and what plausible wrong edit does it prevent?

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
2. Revalidate top-level landing first success and featured examples from an
   outsider's supported environment. For changed internal technical READMEs,
   revalidate their local entry points and workflows from the stated repository
   context. Record untested assumptions.
3. Run repository-native docs builds, link checks, type checks, doctests, or example tests.
4. Search current documentation for legacy names and historical wording that should be in migration material.
5. Re-check that public defaults, errors, supported versions, and security boundaries match source.

Prefer generated inventory or repository-native documentation tooling. Introduce a maintained API map only if coverage cannot otherwise be derived, because every additional index is another drift risk.
