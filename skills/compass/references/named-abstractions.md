# Create and maintain named implementation abstractions

Named abstractions are implementation-design concepts too local to enter
semantic Compass but useful enough to recognize across non-local work. A named
abstraction may disappear under a full implementation rewrite.
It is coordinate-layer vocabulary, not L0–L4 architecture, a component
stereotype, a feature taxonomy, or a graph of the codebase.

The mechanism has two owners:

- `{chart-root}/ABSTRACTIONS.md` owns what each admitted name means.
- A `compass-abstraction: <slug>` source comment claims that one stable
  declaration is an instance.

Nothing owns an occurrence list. Exact marker search supplies the declared
incidence when needed.

## Prerequisites

Do not create a catalog in anticipation of future use, scan routine local work
for possible names, or turn repeated code shapes into candidates by default.
The catalog exists from the first admitted name (§Definition schema) and no
sooner. The host [usage hook](agent-hook.md) sends every new capability through
chart search; when the catalog exists, that search can surface its definitions.

The host's test suite must own an installed, adapted copy of the chart check
in [`verification.md`](verification.md#first-the-mechanizable-checks-belong-to-the-hosts-test-suite)
before the first definition or marker, running its valid, invalid-slug,
missing-definition, malformed-spacing-or-multiline, unsupported-form, and
hidden-source fixtures under the one path that the checker and the raw-hit
audit exclude (`verification.md` §First). The suite is the only record of that
command and those fixtures. Installing the check, admitting or retiring a name,
and adding or changing source markers are ask-first actions (`create.md`
§Boundaries). A manual checkbox is not a fallback for a source claim
(`verification.md` §First).

If a marker is encountered without a unique definition or without that
installed check, classify it as an **orphan claim**. Do not interpret or reuse
it. Report its location and ask whether to remove it or complete the missing
setup; never create the missing state silently.

## Admission gate

Admit a name only when all five statements are true:

1. **Independent meaning.** Its definition can be stated without current file
   paths, symbols, features, or a list of instances.
2. **Sharp boundary.** One essential discriminator separates it from a named
   nearest non-example.
3. **Decision effect.** Recognizing it changes a specific navigation,
   implementation, or comparison decision. Record the before/after decision in
   the change that admits the name; "interesting" or "repeated" is insufficient.
4. **Refactor stability.** The meaning survives ordinary renames, moves,
   extraction, and structure-only refactors within the current implementation
   approach. It need not survive a full technology rewrite.
5. **Stable claim site.** Each declared instance has one authored declaration
   that owns it and can carry the marker without depending on a call site,
   barrel export, convenience import, or generated output.

Reject a candidate that is merely a framework primitive, a familiar design
pattern with no project-specific discriminator, a feature or domain noun, a
similarity cluster, or a group that becomes useful only after adding occurrence
lists, relationships, flows, or `used-by` data. Leave it unnamed rather than
weakening the gate.

A named abstraction does not change a component's existing `## Stereotype`. A
stereotype classifies a component's broad architectural role; a named
abstraction identifies a narrower project-specific implementation design.

## Definition schema

When the first name is admitted, create `{chart-root}/ABSTRACTIONS.md` with one
entry per concept:

```markdown
# Named Implementation Abstractions

## Persisted Store Controller (`persisted-store-controller`)

### Meaning

One concise definition that does not depend on today's paths or instances.

### Essential discriminator

The one property an owner must have to qualify.

### Nearest non-example

Name the closest misleading alternative and the property it lacks.

### Meaning-changing scope

Optional. Include only when a lifecycle or scope condition changes the meaning.
```

Use a human-readable heading and a unique lowercase-hyphen slug. `Meaning`,
`Essential discriminator`, and `Nearest non-example` are required.
`Meaning-changing scope` is optional; omit it when it adds no boundary. Do not
add paths, examples-by-location, feature mappings, owners, lifecycle status,
relationships, history, or occurrence counts.

## Source claim

Write the fixed marker body using one of the checker's supported line-comment
forms—`//`, `#`, or `--`—immediately above the stable declaration that owns the
instance:

```typescript
// compass-abstraction: persisted-store-controller
export function createPersistedStoreController() {
  // ...
}
```

```python
# compass-abstraction: persisted-store-controller
class PersistedStoreController:
    ...
```

Use one marker line per claim. If a declaration genuinely owns two admitted
concepts, use two adjacent marker lines; do not invent a compound slug. Never
mark generated output, call sites, imports, re-exports, or every member inside
an already marked owner.

Before the first marker, configure the chart check's `SRC_SUFFIXES` to include
every source technology allowed to carry a marker. Do not use another comment
form or marker-bearing suffix until the checker supports it and its fixtures
pass.
Before trusting the checker's occurrence count, run a repository-wide literal
search and reconcile every raw hit with the configured source universe and the
reported count:

```sh
# Raw audit: reconcile every result; replace {fixture-path} and {checker-file} with the installed checker's FIXTURES path and its own file.
rg -n --hidden -F 'compass-abstraction:' -g '!**/.git/**' -g '!**/node_modules/**' -g '!{fixture-path}/**' -g '!{checker-file}' .

# Exact declared incidence: replace only the example slug.
rg -n --hidden '^[[:space:]]*(//|#|--)[[:space:]]*compass-abstraction:[[:space:]]+persisted-store-controller[[:space:]]*$' -g '!**/.git/**' -g '!**/node_modules/**' .
```

An unmatched raw hit in any source file fails the gate — whether the file's suffix is outside the configured set or the marker's form is one the checker does not parse; a documentation example is reconciled, not failed.
The checker does not make an unconfigured source universe exhaustive.

The marker is an authored design claim, not proof of conformance. Its absence
is unknown, not evidence that the code does not instantiate the abstraction.
Search results contain declared occurrences only. Report them that way; never
claim coverage or completeness from marker search.

## Maintenance and retirement

Change a central definition only when the concept's meaning changes. Moving or
renaming an owner requires no catalog edit; move the marker with the owner.
Remove or replace a marker when review shows that its declaration no longer
meets the discriminator. Do not repair stale claims by adding an occurrence
list to the catalog.

Retire a name — remove its definition and every marker that claims it, with
user approval — when task records show that it stays feature-flavoured or
trivial, its markers create confident classification errors, a useful view of
it needs lists or graphs, its maintenance routinely goes stale, or it stops
changing concrete task decisions. A Consume task that finds a name misleading
records that as a definition finding in the task's own record
(`consume-named-abstractions.md`); the retirement is Create work that reads
those findings. An empty catalog fails the chart check, so retiring the last
name removes the file; the hook stays because it searches the chart that is
present rather than naming the optional catalog.

Never tune the filename, schema, or marker literal around a task or a chart.

Run the [optional gate](verification.md#named-abstraction-verification-optional)
whenever a definition or marker changes. A green mechanical result proves only
definition shape, slug uniqueness, and marker resolution; conformance,
completeness, and usefulness remain unproven.
