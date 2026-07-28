---
name: mind-mapper
description: Use when planning or inherited work needs a persistent outcome-to-move map with one next decision; not for a routine task with clear scope and order.
---

# Mind Mapper

Keep a small, durable map from an outcome to the next bounded move. Work from
the outcome and uncertainty before implementation detail: the map explains why
work exists; it does not predict or prescribe how code must look.

## Configure the map surface

Before mapping, require an explicitly configured planning surface. The
configuration must name its durable reference, how it represents the map
semantics below, and the available read/write authority. It may be a local
artifact, shared system, or network integration, but Mind Mapper never selects
one.

If configuration is missing, return `NEEDS-HUMAN-DECISION` and ask the user to
configure the map surface. Do not propose a filename, project location, task
system, external service, MCP, or transcript as a fallback.

The configured surface must represent these semantics. Keep fields short and
leave an unknown explicit rather than inventing detail.

| Map semantic | Required content |
| --- | --- |
| Outcome | Intended change, proof, and boundary. |
| Branch | A distinct possible contribution, or `unknown`. |
| Move | Bounded action, linked branch, and expected plus disconfirming readback. |
| Result | Immutable observation linked to its move, effect, and next decision. |
| Open link | Orphan, unknown relationship, or blocked dependency. |
| Next | One move, map repair, block, or `none`. |

## Map before implementation

1. State one outcome, its proof, and its boundary. If materially different
   outcomes remain plausible, return `NEEDS-HUMAN-DECISION`.
2. Reconstruct supplied history as a result linked to its move and branch. Keep
   an unknown or orphan link when lineage cannot be recovered; never write a
   retrospective rationale just to complete the graph.
3. Add only the distinct branches that can change the outcome. A branch may
   progress independently, but it is not a mandatory sequence unless a real
   dependency is written in **Open links**.
4. Add one bounded move with a readback that could change the next decision.
   A move without a branch is an orphan: repair the link or leave it out.
5. Choose one entry for **Next**. The map is complete enough to use when this
   choice and its unresolved links are visible; do not expand it for ceremony.

Before inspecting code, confirm only this: the map names why the move matters,
what boundary it has, and what result would change the next decision. After the
user authorizes inspection, inspect only the implementation question needed by
that move. Code can refine a move; it does not redefine the outcome.

## Update from a result

Append a result; never rewrite the move's original readback. Keep observation
separate from interpretation, then choose the next map change.

| Result | Map action |
| --- | --- |
| Expected | Continue only within the observed boundary. |
| Disconfirming | Retire dependent work and select another branch or question. |
| Mixed | Preserve both signals; narrow or split the branch. |
| Inconclusive | Repair observation only when a different bounded move could decide something. |

A retry is a new move, never a rewrite of the old one. Add it only when a
changed condition, execution defect, or new observation can alter the next
decision. “Worked” means the recorded readback matched under its boundary, not
that the outcome is proved or the explanation is causal.

## Return

Return the configured map reference, the updated **Next** entry, and any
orphan, unknown, or authority block. A map with explicit uncertainty is usable; a task list
without outcome lineage is not a Mind Mapper result.
