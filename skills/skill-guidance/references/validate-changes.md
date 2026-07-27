# Validate changed choices

Test whether the skill changes the intended decision and completion behavior,
not merely whether it loads, parses, or repeats supplied facts.

## Completion contract

Finish with `PASS`, `BLOCK`, `NEEDS-HUMAN-DECISION`, or `UNVALIDATED`, supported
by mechanical results and representative behavior. A missing required source,
environment, clean observer, or check is `UNVALIDATED`, never an inferred pass.

## 1. Freeze the evaluation

Before observing a run, record:

- candidate revision and target harness;
- representative task and supplied context;
- intended outcome and non-negotiable invariants;
- choice the skill must change and plausible default it must beat;
- allowed decisions, tools, files, and mutations;
- observable completion signal and failure conditions;
- relevant baseline: current skill, no skill, or both.

Do not revise the frozen contract merely to accommodate the candidate.

## 2. Validate the delta

When package mechanics changed, take the bundled structural and isolation
validator command from the parent `SKILL.md` as prerequisite evidence;
otherwise skip that gate. Do not repeat its checks here. Verify:

- every retained obligation satisfies the parent admission contract;
- each named [Agent Instruction Law](../LAWS.md) uses the exact identifier and
  title, has a target-skill choice and supporting evidence, and does not claim
  that unnamed Laws no longer apply;
- every repository-specific claim satisfies
  [Law VIII — Keep every claim falsifiable](../LAWS.md#law-viii--keep-every-claim-falsifiable);
- the description is one sentence of at most 240 characters, contains only a
  concrete situation and behavior trigger, and covers every intended
  activation;
- the body and runtime references begin after activation and contain only
  execution content or behavior-improving causal rationale;
- README support and design reasons are not required by any runtime route;
- an existing or authorized maintainer README first makes the skill's name,
  offering, and reader-relevant reason inferable, then makes the driving
  failure, affected agent or reader, intended impact, and boundary inferable
  before package architecture or methodology;
- each route satisfies the parent locality, ownership, and conditional-pointer
  contracts;
- the completed package satisfies the parent reader contract and has a
  publishable end state.

Record the exact evidence and property it establishes. Structural validity does
not establish semantic or behavioral correctness.

## 3. Observe representative behavior

Use independent clean-context runs when behavior depends on instruction
interpretation. Give each observer only the inputs available in real use.
Compare the candidate and relevant baseline against the same frozen task.

Assess:

1. correct invocation and internal route;
2. intended choice at the ambiguous fork;
3. generalization to an unseen case when rationale should transfer;
4. distinction between user intent, current behavior, and mechanical facts;
5. authorized scope and avoidance of unrelated ritual;
6. satisfaction of the checkable completion criterion;
7. reduction in traversal or decision work sufficient to justify recurring
   context and cognitive cost.

Reference loading, tool use, produced files, and literal instruction compliance
are evidence only when they contribute to the frozen outcome.

## 4. Decide and record

- `PASS` when the candidate preserves invariants and improves or matches the
  relevant baseline without material new burden.
- `BLOCK` for a known defect, contradiction, regression, or unmet criterion.
- `NEEDS-HUMAN-DECISION` only for unresolved policy, scope, ownership, or
  strategic judgment.
- `UNVALIDATED` when required authority or observation is unavailable.

Change one root cause at a time, rerun invalidated checks, and use a fresh
observer after a repair. Keep evaluation records in the handoff, not the
runtime skill.
