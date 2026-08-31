# Structural signals

Use these read-only signals to detect level contamination or a component or
block that may be doing too much. Each signal opens an investigation; it is not
an error or permission to change the chart.

| Signal | Likely cause | Investigation |
| --- | --- | --- |
| L1 diagram has more than one node inside the boundary | Internal block leaked up | Check whether the extra nodes belong at L2 |
| L1 external systems table has a vendor API or library | Implementation detail leaked up | Re-run both L1 tests against product reality |
| L1 external was added with a dependency | Manifest treated as admission evidence | Re-run both L1 tests against product reality |
| L1 external adapter is used by only one component | Adapter leaked up | Check whether it belongs at L3 in that component |
| Block document names a framework as a peer block | L5 infrastructure promoted | Check whether it belongs at L5 |
| Block logical role can be stated only by naming a directory | Implementation structure became identity | Restate the responsibility semantically; if that fails, report a merge lead |
| Block split alongside a service extraction | Topology change mistaken for semantic change | Classify whether semantics changed or only coordinates remapped |
| Root appeared alongside a package or repository | Packaging mistaken for logical identity | Re-run root admission |
| Component has four or more external dependencies | Hidden block boundary or missing facade | Record the lead and inspect coupling |
| Component is consumed by three or more blocks | Shared-library pressure | Check whether it belongs at L5, should split, or has a justified owner |
| File carries two coordinates within one root | Two logical participations or chart ambiguity | Investigate and record which; do not split reflexively |
| File carries coordinates from different roots without a ratified second root | Invented root | Report the unratified orientation |
| Block boundary is missing or exceeds two sentences | Boundary not understood | Clarify the unresolved boundary |
| Component responsibility requires "and" | Component may do too much | Inspect whether the responsibilities separate semantically |
| Component diagram carries six or more arrows | Too many relationships at one level | Inspect whether a decomposition is warranted |
| Block communicates-with list exceeds five entries | Block may do too much | Require justification and inspect whether it should split |
| Siblings describe wildly different breadths | Level not calibrated | Run level calibration |
| Chart prose explains a mechanism a rewrite would delete | Implementation fence leaked into the chart | Route the rationale to its Context Docs owner |
