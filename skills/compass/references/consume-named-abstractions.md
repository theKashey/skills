# Consume named implementation abstractions

Use this path only when an existing `compass-abstraction: <slug>` marker or
definition affects the non-local task. This path interprets existing claims; it
does not add, change, or remove definitions or markers.

1. Confirm the trial is valid before interpreting a marker: the user opted in,
   the host usage hook points to the one nominated task, PR, or tracker record,
   the matching definition in `{chart-root}/ABSTRACTIONS.md` is unique, and the
   host test suite owns the installed chart check and its required fixtures. If
   any prerequisite is absent, classify the marker as an **orphan claim**,
   report its location, and stop this path. Do not interpret or reuse it.
2. Read the matching definition before interpreting the source marker.
3. Find declared instances with a hidden-aware exact-slug search, replacing
   only the example slug:

   ```sh
   rg -n --hidden '^[[:space:]]*(//|#|--)[[:space:]]*compass-abstraction:[[:space:]]+persisted-store-controller[[:space:]]*$' -g '!**/.git/**' -g '!**/node_modules/**' .
   ```

4. Reconcile the results with the source universe configured by the host chart
   check. Search results are declared occurrences only; absence is unknown and
   does not prove that code does not instantiate the abstraction.
5. Review the relevant owner against the definition's essential discriminator
   and nearest non-example. Marker resolution does not prove conformance.
6. Choose one task-local disposition: **reuse** the abstraction, implement
   something **materially distinct**, or **decline to name** the new code. Keep
   the local reason with the code or its Context Docs owner, never in
   `ABSTRACTIONS.md`.

If the definition, marker, or catalog needs to change, classify the need and
record it in the task's own PR, issue, or task record. That mutation belongs to
a separate Create task.
