# Create and maintain named implementation abstractions

This is an opt-in experiment for implementation-design concepts that are too
local to enter semantic Compass but useful enough to recognize across non-local
work. A named abstraction may disappear under a full implementation rewrite.
It is coordinate-layer vocabulary, not L0–L4 architecture, a component
stereotype, a feature taxonomy, or a graph of the codebase.

The mechanism has two owners:

- `{chart-root}/ABSTRACTIONS.md` owns what each admitted name means.
- A `compass-abstraction: <slug>` source comment claims that one stable
  declaration is an instance.

Nothing owns an occurrence list. Exact marker search supplies the declared
incidence when needed.

## When to load this procedure

Load it only when one of these conditions holds:

1. The user explicitly asks to start or change the named-abstraction trial.
2. Create work encounters an existing `compass-abstraction:` marker that must
   be validated, changed, or removed.
3. Create work exposes a candidate whose admission would change a concrete
   navigation, implementation, or comparison decision.

Do not create a catalog in anticipation of future use, scan routine local work
for possible names, or turn repeated code shapes into candidates by default.
Before starting, require the user to nominate and authorize one existing task,
PR, or tracker record as the trial-evidence owner. Do not invent a new file or
service for this purpose. The nominated record owns the frozen task, the
trigger that ends the trial, admission evidence, before/after decision,
observations, and maintenance findings. If no such owner is available, do not
create `ABSTRACTIONS.md` or a marker; report the blocked trial.

The trial ends by its own rule, recorded in the nominated record before the
first definition as part of writing that record: the user sets one trigger an
agent can check from the record alone — a calendar date, a count of recorded
observations, or a named event. Starting a trial without one violates this
section, and the gate fails until it is recorded. The five conditions in
§Maintenance and falsification are unactionable without a moment at which
they are read, and an experiment nobody is scheduled to judge becomes
permanent by inertia.

In the same host agent-instruction block that declares the chart root, add one
durable routing line after the user approves it:

```markdown
Named-abstraction trial evidence: {existing task, PR, or tracker URL or stable ID} — before building a new capability, scan {chart-root}/ABSTRACTIONS.md
```

This pointer is not a second evidence owner. It lets every later activation
find the sole record without putting trial history in the chart, and it is the
only host line that routes to the catalog: the trial-agnostic hook never names
`ABSTRACTIONS.md`, so an agent must be told here that it exists. Add or update
it before the first definition or marker; read it whenever this procedure
loads and follow it to the record's trigger before admitting or changing
anything; remove it when the trial is removed or separately ratified.

The host's test suite must also own an installed, adapted copy of the chart
check in [`verification.md`](verification.md#first-the-mechanizable-checks-belong-to-the-hosts-test-suite)
before the first definition or marker. Record its exact repository-native
command and its valid, invalid-slug, missing-definition,
malformed-spacing-or-multiline, unsupported-form, and hidden-source fixture
commands in the nominated trial record, together with the one fixture path
that the checker and the raw-hit audit exclude (`verification.md` §First). Installing the check, starting the
trial, writing its record, and adding or changing source markers are ask-first
actions. A manual checkbox is not a fallback for trial source claims.

If a marker is encountered without user opt-in, a unique definition, a valid
host-usage-hook pointer to the nominated evidence owner, or that installed
check, classify it as an **orphan claim**. Do not interpret or reuse it. Report
its location and ask whether to remove it or complete the trial setup; never
create the missing state silently.

## Admission gate

Admit a name only when all five statements are true:

1. **Independent meaning.** Its definition can be stated without current file
   paths, symbols, features, or a list of instances.
2. **Sharp boundary.** One essential discriminator separates it from a named
   nearest non-example.
3. **Decision effect.** Recognizing it changes a specific navigation,
   implementation, or comparison decision. Record the before/after decision in
   the nominated trial record; "interesting" or "repeated" is insufficient.
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

This experiment does not change the existing L3 `stereotype` field. A
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
relationships, trial history, or occurrence counts.

## Source claim

Write the fixed marker body using one of the trial's supported line-comment
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

At trial start, configure the chart check's `SRC_SUFFIXES` to include every
source technology allowed to carry a marker. Do not use another comment form or
marker-bearing suffix until the checker supports it and its fixtures pass.
Before trusting the checker's occurrence count, run a repository-wide literal
search and reconcile every raw hit with the configured source universe and the
reported count:

```sh
# Raw audit: reconcile every result; replace {fixture-path} and {checker-file} from the trial record.
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

## Maintenance and falsification

Change a central definition only when the concept's meaning changes. Moving or
renaming an owner requires no catalog edit; move the marker with the owner.
Remove or replace a marker when review shows that its declaration no longer
meets the discriminator. Do not repair stale claims by adding an occurrence
list to the catalog.

Keep the frozen task, before/after decisions, navigation observations, and
marker maintenance findings in the nominated trial record outside the chart.
Consume tasks append their observation lines there
(`consume-named-abstractions.md` step 7).
This package defines the experiment's mechanics; it does not establish that the
experiment works. Treat the approach as failing—and remove the catalog and
markers with user approval—if names stay feature-flavoured or trivial, markers
create confident classification errors, the useful view requires lists or
graphs, maintenance routinely goes stale, or the names do not change concrete
task decisions.

Freeze the filename, schema, marker literal, and trigger for the duration of
one trial; do not tune them around each task. The decision point is the
trigger the record set at start. The Create activation that finds it reached —
this procedure loading, or the gate running — reads the record against the
five conditions above before any other trial action. A record holding no
observation in which a name changed a decision meets the last condition:
absence of evidence is failing, never grounds to extend. Failing, the
activation removes the catalog, the markers, and the pointer line with user
approval, as above, and writes the verdict to the record. Not failing, it
writes the verdict with a new user-set trigger, so a new bounded run begins
under the same frozen syntax, and presents ratifying permanent
vocabulary as the separate package decision it cannot take. A Consume task
that finds the trigger reached says so in its observation line and in the
task's own record; the reading is Create work. Trial use alone does not make
this syntax part of Compass's settled chart format.

Run the [optional gate](verification.md#named-abstraction-verification-optional)
whenever a definition or marker changes. A green mechanical result proves only
definition shape, slug uniqueness, and marker resolution; conformance,
completeness, and usefulness remain unproven.
