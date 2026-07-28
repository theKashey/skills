# Build or revise a skill

Create or amend a skill only when it owns a distinct unresolved agent choice.
The finished package must expose the smallest procedure that selects the
supported move and proves completion.

## Completion contract

Finish when the capability has a justified owner, every retained obligation
passes admission, every route has a checkable stopping condition, the runtime
body and references contain no activation guidance, support prose, duplicated
territory, or drafting residue, and the required validation passes or has an
explicit non-pass status.

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

## 2. Choose the canonical owner

Apply the admission questions from `SKILL.md`, then select:

- `No-op` when existing context or enforcement already resolves the choice.
- `Amend` when an existing skill owns the missing decision.
- `Create reference` when only one branch of an existing skill needs the
  material.
- `Create skill` when the capability has distinct expertise, independent
  invocation, and a material behavioral delta.
- `Split or merge` when current boundaries hide a required route or duplicate
  one owner.

Continue only within the user's authorized mutation scope. When the selected
outcome requires package mechanics, create or edit files only inside the target
skill directory, then return here for unresolved runtime choices.

## 3. Design invocation and disclosure

Choose model discovery only when an agent or another skill must reach the
capability without a user naming it. Otherwise prefer explicit invocation and
avoid permanent description load.

Put all skill-level activation conditions in the frontmatter description.
Inline choices and invariants every activated run needs. Disclose branch-specific
procedures behind a pointer whose wording names the condition that requires the
material. Treat the pointer as behavioral: if must-have guidance loads
unreliably, sharpen the condition before moving the guidance inline.

Treat line count as a signal, not a placement rule. Split by invocation when a
branch needs independent discovery. Split by sequence only after a sharper
completion criterion fails to prevent observed premature completion.

## 4. Write the runtime contract

Write the frontmatter description as one activation sentence of at most 240
characters. Name the concrete situation and behavior that need the skill; do
not catalogue possible failures, artifact types, adjacent tools, or workflow
phases. Omit capability summaries, implementation details, resources,
benefits, reasons, and output promises unless a detail distinguishes the
activation. Keep all skill-level "when to use" and "when not to use" guidance
out of the body.

Open the body at the first post-trigger decision or action. Use imperative
language for actions and declarative language for execution facts and decision
criteria. Preserve conditions that select an internal route after activation;
they are execution logic, not skill triggers.

For every procedure:

1. State its internal branch condition and authorized scope.
2. Apply each named [Agent Instruction Law](../LAWS.md) that constrains its
   decisions, then check every remaining Law whose condition arises; naming a
   Law is not an exemption from the rest.
3. Put warnings immediately before the action they govern.
4. End each meaningful step with a checkable completion condition.
5. Use an example only when it resolves ambiguity left by the decision laws.

Remove explanations, excuses, defenses, anticipated objections, authoring help,
and design history from the body and runtime references. Keep a verified causal
rationale beside an instruction only when it materially improves compliance,
choice transfer, or the outcome on an unseen case.

Put durable reasons about the governed capability, its rejected alternatives,
reader-relevant boundaries, and concrete component ownership in `README.md`.
Keep authoring and review history, generic surface-selection rationale, and
framework provenance in the authoring record or handoff. Do not publish claims
such as “this README explains,” “this skill follows,” or “this documentation
uses Diátaxis” merely because they are true of the build. A framework belongs
in the final artifact when its distinction changes the reader's choice or it is
part of the reader's governed subject or contract. Keep the README outside the
runtime dependency graph: `SKILL.md` and its runtime references must execute
correctly without reading it.

When the package has an existing or authorized maintainer README, open with the
skill's name, what it provides, and why a reader would use it. Follow that
simple offer with the recurring failure, affected agent or reader, intended
observable impact, and boundary before describing runtime architecture or
authoring mechanics. State relationships to other skills only when both
package contracts or an explicit product decision establish them. A
relationship in maintainer prose never creates a runtime dependency.

## 5. Prune and verify the package

Apply
[Law II — Spend the instruction budget](../LAWS.md#law-ii--spend-the-instruction-budget)
sentence by sentence: if deletion changes no invocation, choice, scope,
execution, or completion, delete the sentence.
Leave each surviving meaning with one canonical owner.

Classify every retained prose unit as description trigger, runtime execution,
behavior-improving causal rationale, or README support. Move or delete anything
without a valid surface.

Keep the law-alignment record in the handoff. Use the exact law identifier and
title so a reviewer can cite a violated rule precisely. Add a named law to the
target runtime only when its title and local consequence directly select an
agent action; do not publish a bare list of frameworks or create a cross-skill
runtime dependency.

Apply
[Law VIII — Keep every claim falsifiable](../LAWS.md#law-viii--keep-every-claim-falsifiable)
and
[Law VII — Enforce or delete mechanical rules](../LAWS.md#law-vii--enforce-or-delete-mechanical-rules)
to every retained repository-specific claim.

Apply the validation selected by the parent router. Structural validity is not
evidence that the skill changes the intended choice.
