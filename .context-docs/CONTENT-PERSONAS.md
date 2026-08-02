# Content-persona cast for this repository

This repository publishes independently installable agent skills for bounded
decision failures. Its recurring documentation entrants need to evaluate an
intervention, act through it, or govern it safely. The repository cast is not a
universal audience model for projects that install a skill, and it must not
become a runtime dependency of any package.

## Casting verdict

`PROCEED` with three provisional decision-rights classes: **Evaluator**,
**Actor**, and **Owner**.

Do not create one class per skill: those profiles merely restate the offering,
while task, workflow phase, delivery mode, and repository surface belong below
the cast. Agent, Engineer, and Architect also do not currently form a sound
default taxonomy: agent is usually a delivery mode, while engineer and
architect describe overlapping roles or decision altitude. None yet predicts
three stable sibling reader classes for this repository.

## Goal scaffold

| Layer | Current evidence-backed answer |
| --- | --- |
| Project outcome | Keep AI-assisted engineering from losing the reason, uncertainty, evidence, or non-local constraint that makes work safe. |
| Subject promise | Six standalone skills address bounded decision failures; no skill owns the whole development lifecycle. |
| Authorial goal | Help an entrant recognize, use, or safely govern the smallest applicable intervention without overstating what it proves. |
| Evidence | The [repository story](CONTENT-SURFACE-STORIES.md#repository-story), [problem chooser](../README.md#choose-by-problem), package rationales, runtime contracts, and [repository governance](../AGENTS.md). |
| Non-fit | This cast does not establish downstream product audiences, market segments, contributor demand, or one reader per skill. |

## Select by the decision the entrant controls

| Content-persona class | Durable starting point and decision right | Generic reader goal | Observable success |
| --- | --- | --- | --- |
| **Evaluator** | A recurring failure or need is visible; the entrant can decide whether this repository or one bounded skill fits. | Choose the smallest relevant intervention and understand its promise, evidence requirement, and non-fit. | Select a justified route—or reject all routes—without treating a skill as proof of the final outcome. |
| **Actor** | An intervention has been selected; the entrant can perform the in-scope task but cannot silently expand its authority. | Make the intended decision or action, produce the required evidence, and stop with completion or an explicit unresolved gap. | The task reaches the skill's observable terminal condition without importing unrelated repository context. |
| **Owner** | The entrant can change, review, distribute, or accept risk for the repository or an individual skill. | Preserve or deliberately revise purpose, behavior, boundaries, compatibility, and standalone distribution. | The change survives scope, behavioral, isolation, and preservation evidence without losing its durable why. |

The same human or agent can move between classes when their decision right
changes. Select one primary class for a surface or major route; a secondary
class earns only a route to its established owner, not another complete story.

## Add only proven context

Use the task as an **episode**, not a new persona. Choosing among skills,
running Context Docs, probing uncertainty, reviewing an artifact, or revising a
skill are episodes under the class that controls the decision.

Use **selective context** as a modifier when the entrant receives only a task,
diff, symbol, search match, or installed skill package. It changes assumed
context, locality, and explicit boundaries; it does not create an “activated
agent” persona. Treat decision altitude in the same way if evidence shows it
changes density, proof, or route.

No subclass file is currently earned. Add a conditional detail under
`.context-docs/content-personas/` only when recurring evidence shows a content
delta that cannot remain compact here. The child must contain only the delta
from its parent. Never add one for a skill, surface, package, task, or workflow
stage.

## Form the task-local story

For the surface in scope, combine:

```text
primary class + proven modifier + current episode + reader goal
+ authorial goal + intended change + proof and boundary + completion route
```

Use the applicable current contract in
[CONTENT-SURFACE-STORIES.md](CONTENT-SURFACE-STORIES.md) only as evidence. If
the actual entrant, controlled decision, supported outcome, or reachable owner
conflicts with it, run the Context Docs
[casting procedure](../skills/context-docs/references/casting.md) and follow its
result—even when that means changing the reader, goal, surface, subject, or need
for a document.

## Confidence and recasting triggers

This cast is reconstructed from current repository content and governance, not
from interviews, analytics, support volume, or market research. Recast when a
recurring entrant cannot fit without distortion; two classes produce no
different content choice; a class starts mapping one-to-one to skills or pages;
or entry context, decision rights, trust boundaries, supported outcomes, or
authoring consequences change.
