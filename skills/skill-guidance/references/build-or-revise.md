# Advise a skill design

Assess whether a proposed or existing skill owns a distinct unresolved agent
choice and whether its package exposes the smallest procedure that selects the
supported move and proves completion. Return advice and evidence to the
host-provided skill creator; do not edit the target package.

## Completion contract

Finish with one evidence-backed recommendation—`No-op`, `Amend`, `Create
reference`, `Create skill`, `Split or merge`, or
`Needs-human-decision`—plus the applicable validation result for any existing
candidate. The report must identify the justified owner, admitted obligations,
the evidence-backed shape and relevant capability neighbourhood, route stopping
conditions, and any activation guidance, support prose, duplicated territory,
or drafting residue that the host creator should address.

## 1. Freeze the capability

Record:

- the recurring failure or unresolved choice that makes a skill necessary;
- the user-visible or agent-visible outcome;
- the observable impact expected when the agent chooses differently;
- representative tasks, including one unseen case when rationale should
  generalize;
- the open-world choices and observed or plausible wrong defaults;
- the exact [Agent Instruction Law](../LAWS.md) identifier and title that
  materially constrain each target-skill choice, with their supporting
  evidence;
- intended users, target harnesses, and invocation boundary;
- authorized files and mutation scope;
- observable success, failure, and premature-completion signals.

Use repository evidence and representative runs for current behavior. Keep
intended policy separate from observed behavior. Stop for authority when the
preferred choice cannot be established safely.

## 2. Identify the shape and recommend the canonical owner

A skill's shape is not one kind. Record only the independent dimensions that
change its activation, execution, composition, completion, or validation:

| Dimension | Record |
| --- | --- |
| **Reason** | Recurring failure or unresolved choice, affected agent, intended outcome, and observable completion. |
| **Governed capability and responsibility** | Choices, defaults, guarantees, boundaries, failure modes, and task or deliverable aspect the skill owns or intentionally exposes. Documentation, testing strategy, verification, and coordination are examples, not an allowed-types list. |
| **Operating form** | A single decision, routed or sequenced workflow, advisory review, verification gate, deterministic transformation, artifact production, or another evidenced intervention form. This is an open set. |
| **Runtime and package form** | Self-contained instructions, conditionally routed references, script-backed mechanics, assets or templates, or a justified combination. |
| **Capability relations** | The route-specific breadth, aspect, coordination, consumption, or guarantee edges to other evidenced owners or providers. |

Documentation and workflow are different dimensions: documentation describes a
governed responsibility and its completion claim, while workflow describes how
an intervention selects, sequences, and stops work. They may coexist in one
skill. Likewise, package form follows delivery needs and does not establish
semantic breadth or expertise.

Classify relations per capability and route; never assign one permanent shape
label to the whole skill:

| Relation | Establish it when | Preserve this boundary |
| --- | --- | --- |
| **Broader/default owner** | It owns the choice before a narrower condition and the default outside that condition. `Generalist` describes only this edge. | A narrower route does not change its normal case. |
| **Specialist/refinement owner** | A named condition selects a narrower capability on the same decision axis. | It owns only the conditional delta. |
| **Orthogonal/aspect owner** | It owns a separately testable choice or completion claim contributing to the same deliverable. | Neither aspect selects the other's internal procedure. |
| **Coordinator/composer** | It owns selection, sequence, interfaces, and aggregate stopping conditions across capabilities. | It does not inherit contributors' internal selection logic. |
| **Consumer** | It uses another capability's result. | Relevance to the result does not confer authority over its production. |
| **Guarantee provider** | An abstraction, executable gate, role, or system supplies verified behavior. | A supplied guarantee is not automatically a skill or semantic owner. |

Build only the relevant capability neighbourhood. Start from the target's owned
choices, required inputs, produced outcomes, delegated aspects, and duplicated
procedures. Names, folders, catalogs, descriptions, links, and topic overlap may
identify candidate counterparts; establish an ownership edge only from both
inspected capability contracts or an explicit user, product, or repository
decision. Record each material edge as:

```text
counterpart → governed choice or result → relation and direction
→ named condition or scope → interface and completion boundary
→ contract or decision evidence → runtime availability and isolation disposition
```

When a counterpart cannot be established, record the owner as unknown. Narrow
the contract, keep indispensable mechanics inside the standalone package, or
return `Needs-human-decision`; do not invent a skill, delegation, or dependency.

Apply the admission questions from `SKILL.md`, then recommend:

- `No-op` when existing context or enforcement already resolves the choice.
- `Amend` when an existing skill owns the missing decision.
- `Create reference` when only one branch of an existing skill needs the
  material.
- `Create skill` when the capability has distinct expertise, independent
  invocation, and a material behavioral delta.
- `Split or merge` when current boundaries hide a required route or duplicate
  one owner.

Keep the recommendation within the user's authorized mutation scope. The host
skill creator owns package mechanics and any file changes. If authority is
missing, return `Needs-human-decision` instead of designing around it.

Use this testing case as an ownership probe: a unit-testing skill owns strategy
selection as the broader/default owner; a Jest-mocking specialist owns
Jest-specific mock choices after that route is selected; dependency injection
owns the orthogonal construction and substitution aspect, not Jest mock or
mock-type selection; and an adjacent backend skill consumes the testing result
without selecting the testing strategy.

## 3. Assess invocation and disclosure

Recommend model discovery only when an agent or another skill must reach the
capability without a user naming it. Otherwise recommend explicit invocation
and avoid permanent description load.

Check that all skill-level activation conditions are in the frontmatter
description, every-run choices and invariants are inline, and branch-specific
procedures sit behind a pointer whose wording names the condition that requires
the material. Treat the pointer as behavioral: if must-have guidance loads
unreliably, recommend sharpening the condition before recommending inline
guidance.

Trace representative activated flows through every transitively required
reference. Judge a split by what a flow leaves unloaded, not by the size of
`SKILL.md`: when every relevant flow still reads the extracted material, do not
claim progressive disclosure, and recommend the nearest every-run owner unless
a separate ownership constraint justifies the file boundary.

A reference may point to narrower references when explicit child conditions let
other subflows avoid them and the split improves clarity or signal-to-noise. If
serial discovery through a nested route would materially delay work, recommend
listing the complete journey in the main `SKILL.md`, marking required and
conditional steps so independent reads can be planned together. Treat line
count as a signal, not a placement rule. Split by invocation when a branch needs
independent discovery. Split by sequence only after a sharper completion
criterion fails to prevent observed premature completion.

## 4. Review the runtime contract

Check the frontmatter description against the activation boundary contract in
the parent `SKILL.md`. Recommend omitting capability summaries, implementation
details, resources, benefits, reasons, and output promises unless a detail
distinguishes activation. Skill-level "when to use" and "when not to use"
guidance belongs outside the body.

The body should open at the first post-trigger decision or action, use
imperative language for actions and declarative language for execution facts
and decision criteria, and preserve conditions that select an internal route
after activation.

For every procedure, check:

1. State its internal branch condition and authorized scope.
2. Apply each named [Agent Instruction Law](../LAWS.md) that constrains its
   decisions, then check every remaining Law whose condition arises; naming a
   Law is not an exemption from the rest.
3. Put warnings immediately before the action they govern.
4. End each meaningful step with a checkable completion condition.
5. Use an example only when it resolves ambiguity left by the decision laws.

Recommend removing explanations, excuses, defenses, anticipated objections,
authoring help, and design history from the body and runtime references. Retain
a verified causal rationale beside an instruction only when it materially
improves compliance, choice transfer, or the outcome on an unseen case.

Durable reasons about the governed capability, its rejected alternatives,
reader-relevant boundaries, and concrete component ownership belong in
`README.md`. Authoring and review history, generic surface-selection
rationale, and framework provenance belong in the handoff. Recommend against
publishing claims such as “this README explains,” “this skill follows,” or
“this documentation uses Diátaxis” merely because they are true of the build.
A framework belongs in the final artifact only when its distinction changes the
reader's choice or is part of the governed subject or contract. The README must
remain outside the runtime dependency graph.

A maintainer README is generated on the user's request and then to the parent
reader contract: it opens with the skill's name, what it provides, and why a
reader would use it; a missing README is not a defect.
The recurring failure, affected agent or reader, intended observable impact,
evaluation boundary, and responsibility boundary should precede runtime
architecture or authoring mechanics. Relationships to other skills require
both package contracts or an explicit product decision and never create a
runtime dependency.

## 5. Form the recommendation and validation record

Apply
[Law II — Spend the instruction budget](../LAWS.md#law-ii--spend-the-instruction-budget)
sentence by sentence: if deletion changes no invocation, choice, scope,
execution, or completion, recommend deleting the sentence. Leave each surviving
meaning with one canonical owner.

Classify every retained prose unit as description trigger, runtime execution,
behavior-improving causal rationale, or README support. Identify anything
without a valid surface for the host creator to move or delete.

Keep the law-alignment record in the advisory report. Use the exact law
identifier and title so the host creator can act on a precise violation.
Recommend a named law in the target runtime only when its title and local
consequence directly select an agent action; never recommend a bare framework
list or cross-skill runtime dependency.

Apply
[Law VIII — Keep every claim falsifiable](../LAWS.md#law-viii--keep-every-claim-falsifiable)
and
[Law VII — Enforce or delete mechanical rules](../LAWS.md#law-vii--enforce-or-delete-mechanical-rules)
to every retained repository-specific claim.

Apply the validation selected by the parent router to an existing candidate.
When no candidate exists, specify the checks the host skill creator must run.
Structural validity and clean isolated comparisons are regression evidence, not
evidence that the skill changes the intended choice under accumulated-context
stress.
