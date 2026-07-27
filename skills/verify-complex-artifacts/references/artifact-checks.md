# Artifact checks

Select checks by artifact family and contract risk. This is a routing matrix,
not a universal checklist. Repository-native checks and explicit requirements
take precedence.

- [Cross-cutting damage signatures](#cross-cutting-damage-signatures)
- [Cross-artifact checks](#cross-artifact-checks)
- [Code, packages, and services](#code-packages-and-services)
- [Websites and interactive interfaces](#websites-and-interactive-interfaces)
- [Documentation and text deliverables](#documentation-and-text-deliverables)
- [Slide decks](#slide-decks)
- [Spreadsheets](#spreadsheets)
- [PDFs and editable office documents](#pdfs-and-editable-office-documents)
- [Diagrams, images, and visual assets](#diagrams-images-and-visual-assets)
- [Data and configuration bundles](#data-and-configuration-bundles)

## Cross-cutting damage signatures

Scan the complete consumer-visible candidate, not only the changed region. A
signature is a diagnostic lead, not an automatic verdict. Cite the target
evidence, run the adversarial check, and route the affected property to the
named gate.

| Signature | Observable damage | Adversarial check | Owning gate |
| --- | --- | --- | --- |
| **Proof leakage** (prompt or instruction leakage) | The artifact echoes the request, addresses the producer or user, narrates what was added, or embeds claims that it complied, verified, or passed. These are proofs of work rather than part of the delivered subject. | Search consumer-visible text, labels, comments, metadata, and generated assets for request phrases, instruction vocabulary, validation claims, agent language, and producer-to-user address. Preserve only a required audit record or durable operator process. | Isolated output-context review; factual review for required provenance records. |
| **Implementation-time recording** | The artifact preserves a momentary checkout, branch, rollout, access, or work-in-progress state instead of the authorized state expected when the iteration completes. The recording may be accurate when written but false or irrelevant at handoff. | State the intended completed contract independently of the observed implementation, then reconcile every temporal claim, caveat, placeholder, and omission against it. Search for future promises and temporary-state language, but also challenge neutral present-tense claims supported only by an in-flight implementation. | Factual and cross-artifact gates; isolated output-context review for consumer-visible process residue. |
| **Pink-elephant amplification** | A point emphasized during iteration becomes disproportionately repeated, detailed, styled, tested, or structurally dominant. The local repair creates a narrower artifact instead of restoring the whole. | Compare the focal material with sibling sections, paths, entities, and risks. Remove the repeated motif mentally and ask whether the remaining artifact still covers its contract. Require each recurrence and its prominence to serve a distinct consumer need. | Isolated output-context review for proportion and coherence; factual and consumer-surface review for displaced coverage. |
| **Offering and subject-order loss** | A surface makes the reader cross failure analysis or internal method before saying plainly what is offered and why; or it reaches methodology, workflow, taxonomy, or components without enough selection context to judge relevance and expected impact. | Inventory every independently selectable named subject. First ask an isolated reader to recover `name: what and why` from the document opening or compact catalog entry. Then, before internal method, ask them to recover the relevant situation or pressure, affected party or system, intended impact or changed decision, and boundary from a chooser or owning section. Require standalone subject pages and detailed owning sections to orient themselves locally. | Isolated output-context review; factual review for the truth of the stated problem and impact. |
| **Placement drift** (dizziness or laziness) | Correct material appears under the wrong owner, layer, heading, component, sheet, slide, branch, or end-of-file appendage because the producer changed the nearest visible location without understanding the full structure. | Read the complete containing artifact and its structural peers. Name the scope governed by the change and the narrowest canonical owner encountered by every affected consumer. Test the entry and navigation path to that owner. | Isolated output-context review for inferable locality; factual and consumer-surface review for ownership and reachability. |
| **Proxy completion** | The artifact satisfies the literal request, checklist, snapshot, metric, test, or visible example while missing the consumer outcome or damaging an unmeasured property. | Restate the outcome independently of the supplied proof, then exercise it from the consumer entry point. Add negative and invariant checks outside the optimized proxy. Treat altered tests, weakened criteria, and self-authored evidence as new candidate changes. | Factual, deterministic, and consumer-surface gates. |
| **Context neglect** | A requirement, exception, invariant, or dependency is omitted or contradicted because it was distant, structurally buried, or outside the producer's local view. | Reconcile every requirement and boundary against the final artifact by stable ID. Inspect middle sections, cross-references, negative constraints, and non-adjacent owners; search for contradictions and unaccounted exclusions. | Factual and cross-artifact gates. |
| **Confabulated support** | Plausible but invented facts, citations, paths, counts, test results, screenshots, rationale, or source attributions make the artifact appear grounded. Uncertainty may be silently converted into a confident claim. | Resolve each support item to an authoritative source or reproducible observation. Re-run claimed checks, open cited targets, and preserve explicit uncertainty where evidence does not decide. | Factual and deterministic gates. |
| **Uniformity collapse** | Distinct cases, voices, visual treatments, data classes, configurations, or failure modes are flattened into a repeated template or dominant pattern, erasing meaningful variation. | Compare representative siblings and boundary cases. Name every distinction the contract requires, then verify that content, behavior, and representation preserve it without cosmetic duplication. | Factual and consumer-surface gates; human acceptance for intentional style. |
| **Source contamination** | Prompt fragments, untrusted embedded instructions, examples, placeholders, secrets, local paths, or source-only annotations are followed or copied into the delivered artifact. | Separate instructions from source data before evaluation. Scan the bundle and rendered forms for source-only tokens and sensitive material; verify suspicious changes against authoritative requirements rather than the embedded text that suggested them. | Security and factual gates; isolated output-context review for visible residue. |
| **Collateral regression** | A focused improvement degrades an adjacent behavior, representation, mode, edge case, or previously correct region. The artifact becomes better on the optimized axis and worse overall. | Compare the frozen baseline with the candidate across neighboring paths and non-target invariants. Exercise unchanged modes and at least one counterexample to the focal improvement. | Deterministic, factual, and consumer-surface gates. |

## Cross-artifact checks

Apply these to every compound deliverable:

- inventory every primary, derived, embedded, linked, and packaged artifact;
- verify versions, names, paths, identifiers, and links agree across files;
- compare editable sources with exported or rendered forms;
- exercise the consumer entry point from a clean or stated starting state;
- verify examples, screenshots, charts, generated files, and documentation
  against their claimed sources;
- scan the delivery bundle for secrets, temporary files, draft markers, stale
  outputs, absolute local paths, and undeclared dependencies;
- confirm that regeneration is reproducible or record why it is not.
- inventory every consumer-visible named-subject relationship as source,
  relation, target, direction, modality, and condition; verify each edge
  against authoritative contracts for both endpoints or an explicit product
  decision, and report verified edges over total edges.

## Code, packages, and services

Deterministic candidates:

- format, parse, lint, typecheck, compile, unit, integration, and end-to-end
  checks;
- schema, migration, dependency, license, secret, and vulnerability checks;
- package-content inspection, clean install, public export inspection, and
  generated-file drift;
- assertions for important negative constraints and regression cases.

Consumer-surface candidates:

- invoke public commands, APIs, imports, routes, and error paths;
- test supported runtime or platform boundaries;
- compare configuration defaults, examples, generated clients, and observed
  behavior;
- inspect logs, permissions, cleanup, persistence, and rollback behavior where
  they are part of the contract.

## Websites and interactive interfaces

Deterministic candidates:

- production build, route generation, type and lint checks, link checks,
  automated accessibility rules, and browser tests;
- missing-asset, console-error, hydration, failed-request, and bundle checks.

Consumer-surface candidates:

- desktop and narrow viewport renders;
- keyboard-only navigation, focus order, labels, contrast, zoom, and reduced
  motion where applicable;
- loading, empty, error, validation, disabled, and success states;
- critical navigation, form, authentication, and persistence paths;
- visual comparison of materially distinct pages and states.

## Documentation and text deliverables

Deterministic candidates:

- parser or documentation build, link and anchor checks, code-fence checks,
  generated-reference drift, and example compilation or execution;
- inventory of public items, headings, references, and explicit exclusions.

Consumer-surface candidates:

- render the actual published or exported form;
- follow the primary reader path from its stated prerequisites;
- copy and run featured commands or examples unchanged;
- compare claims, defaults, errors, names, and links with authoritative
  sources;
- inspect tables, navigation, callouts, line wrapping, and code readability.

## Slide decks

Deterministic candidates:

- file open and export, slide count, aspect ratio, font availability, media and
  link resolution, and missing or off-slide object checks;
- chart data and embedded-source consistency.

Consumer-surface candidates:

- inspect a contact sheet and every full-size slide;
- check clipping, overflow, contrast, reading order, alignment, density, chart
  labels, footnotes, speaker notes, and transitions;
- verify that the narrative survives PDF export and presentation mode;
- compare claims and numbers with their sources.

## Spreadsheets

Deterministic candidates:

- file open, full recalculation, schema and sheet-name checks, formula-error
  scans, broken range or external-reference checks, and expected row or column
  counts;
- invariant, reconciliation, duplicate, missing-value, and outlier checks.

Consumer-surface candidates:

- inspect every sheet, frozen region, filter, validation, named range, chart,
  pivot, conditional format, print area, and protected input area in scope;
- trace representative formulas from source cells to summaries;
- test empty, zero, negative, maximum, and updated-input cases;
- compare displayed rounding, units, dates, and totals with underlying values.

## PDFs and editable office documents

Deterministic candidates:

- file parse and open, page or section count, font and image availability,
  link, bookmark, form-field, metadata, and extracted-text checks;
- round-trip or export checks between editable source and delivery format.

Consumer-surface candidates:

- inspect every page at normal zoom and representative print settings;
- check pagination, clipping, overflow, headers, footers, tables, figures,
  reading order, selectable text, links, forms, and accessibility tags;
- compare the delivered export with its editable source and required template.

## Diagrams, images, and visual assets

Deterministic candidates:

- source parse, export, dimensions, color profile, transparency, embedded font,
  link, node, and edge checks;
- expected labels, identifiers, legends, and alternative descriptions.

Consumer-surface candidates:

- inspect at target size, high zoom, low resolution, light or dark background,
  and intended crop;
- check legibility, overlaps, edge direction, grouping, hierarchy, contrast,
  annotations, and correspondence with the governed system or data;
- verify that textual or accessible equivalents preserve critical meaning.

## Data and configuration bundles

Deterministic candidates:

- parse, schema, encoding, checksum, uniqueness, referential integrity,
  allowed-value, ordering, completeness, and secret scans;
- expected counts, distributions, reconciliations, and transformation
  reproducibility.

Consumer-surface candidates:

- import with the actual consumer or a faithful harness;
- check defaults, overrides, precedence, version compatibility, unknown fields,
  malformed records, partial updates, and rollback behavior;
- trace representative records through every transformation and summary;
- verify that sample data and configuration agree with the shipped schema.
