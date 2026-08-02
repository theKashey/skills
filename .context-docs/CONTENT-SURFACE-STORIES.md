# Content surface stories

These current evidence-backed surface contracts keep repository authors aligned
on which decision-rights class and episode each surface serves, why that surface
should speak, and the through-line its revisions must preserve. Select a class
and task-local episode from the [content-persona cast](CONTENT-PERSONAS.md), then
consult the row for the surface in scope; for root repository narrative work,
read the repository story first. Document types do not create reader classes.
Recast when the actual entrant or controlled decision conflicts with a row.

## Repository story

The repository's primary story is that producing more output is not the hard
part of AI-assisted engineering. Work becomes unsafe when its reason,
uncertainty, evidence, or non-local constraints disappear. Six independently
installable skills address different decision failures. A practitioner should
recognize the current problem, select the bounded skill that owns it, understand
what that skill does not prove, and install only what the project and agent
need. The activated agent then receives a standalone decision map that ends on
observable evidence rather than activity.

The [repository opening](../README.md#agent-skills), [problem
chooser](../README.md#choose-by-problem), [composition
map](../README.md#how-the-skills-support-each-other), and [installation
route](../README.md#install) establish that story.

## Surface stories

| Surface | Current primary class and episode | Authorial goal | Required through-line |
| --- | --- | --- | --- |
| Root `README.md` | **Evaluator** choosing a bounded intervention | Help a practitioner recognize their failure, select a bounded offering, understand its limits, and install deliberately. | AI-assisted work loses intent or evidence → six skills own different failures → choose by problem and boundary → install only what applies. |
| `skills/*/README.md` | **Evaluator** deciding fit, with an **Owner** route for durable rationale | Preserve why the skill exists, who is affected, what changes, important tradeoffs, and where responsibility stops. | Recurring failure → affected actor and stakes → intended observable effect → boundaries and rejected shortcuts → route to the runtime. |
| `skills/*/SKILL.md` | **Actor**, usually with selective context, executing the triggered task | Change the intended post-trigger choice and make completion observable without requiring repository context. | Active condition → bounded decision and action → evidence or readback → explicit completion or unresolved status. |
| Runtime branch reference | **Actor** resolving one conditional task episode | Resolve one conditional choice without taxing unrelated activations. | Branch condition → necessary method and rationale → checkable branch completion → return to the owning route. |
| Root `AGENTS.md` and validation tooling | **Owner** revising or reviewing the repository | Keep rationale, semantic scope, review independence, and standalone distribution intact through change. | Recover purpose → freeze preserve/change boundaries → edit at the owner → run deterministic and independent gates. |
