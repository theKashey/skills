# Artifact checks

Select checks by artifact family and contract risk. This is a routing matrix,
not a universal checklist. Repository-native checks and explicit requirements
take precedence.

- [Cross-artifact checks](#cross-artifact-checks)
- [Code, packages, and services](#code-packages-and-services)
- [Websites and interactive interfaces](#websites-and-interactive-interfaces)
- [Documentation and text deliverables](#documentation-and-text-deliverables)
- [Slide decks](#slide-decks)
- [Spreadsheets](#spreadsheets)
- [PDFs and editable office documents](#pdfs-and-editable-office-documents)
- [Diagrams, images, and visual assets](#diagrams-images-and-visual-assets)
- [Data and configuration bundles](#data-and-configuration-bundles)

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
