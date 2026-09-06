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

When package mechanics changed, take the parent
[isolation-gate result](../SKILL.md#enforce-package-isolation) as prerequisite
evidence; otherwise it does not bear on the delta. Do not repeat its checks
here. Verify:

- every retained obligation satisfies the parent admission contract;
- each named [Agent Instruction Law](../LAWS.md) uses the exact identifier and
  title, has a target-skill choice and supporting evidence, and does not claim
  that unnamed Laws no longer apply;
- every claimed shape dimension is supported by the skill's reason, governed
  capability and responsibility, operating form, runtime or package form, or
  material capability relations; no permanent type label substitutes for that
  evidence;
- broader/default and specialist/refinement are classified on the same decision
  axis with a named condition; the specialist changes only its conditional
  delta and a normal-case change is made in the broader owner;
- documentation and workflow are treated as independent dimensions, and every
  orthogonal owner, coordinator, and consumer retains its own selection logic
  and completion claim;
- every material capability edge records its direction, condition or scope,
  interface and completion boundary, evidence from both inspected contracts or
  an explicit decision, and runtime-availability or isolation disposition; a
  missing counterpart remains unknown rather than becoming an invented owner;
- package form is earned by the task rather than copied from a taxonomy, and
  every ownership handoff passes the parent
  [isolation check](../SKILL.md#enforce-package-isolation);
- every repository-specific claim satisfies
  [Law VIII — Keep every claim falsifiable](../LAWS.md#law-viii--keep-every-claim-falsifiable);
- the description meets the parent activation boundary contract and covers
  every intended activation;
- the body and runtime references begin after activation and contain only
  execution content or behavior-improving causal rationale;
- README support and design reasons are not required by any runtime route;
- a maintainer README, when present or requested, meets the parent reader
  contract in `SKILL.md`;
- each route satisfies the parent locality, ownership, and conditional-pointer
  contracts;
- each representative activated flow is traced from the main `SKILL.md` through
  its transitive references, recording mandatory loads, conditional loads and
  their conditions, serial discovery depth, and each file's size from the
  validator's runtime flow report; every split satisfies the splitting clause
  of [Law II — Spend the instruction budget](../LAWS.md#law-ii--spend-the-instruction-budget);
- the completed package satisfies the parent reader contract and has a
  publishable end state.

Record the exact evidence and property it establishes.

## 3. Observe representative behavior

Use independent clean-context runs when behavior depends on instruction
interpretation. Give each observer only the inputs available in real use.
Compare the candidate and relevant baseline against the same frozen task.
Treat these runs as routing, interpretation, and preservation checks. They do
not establish behavior under accumulated-context stress unless the frozen task
actually retains the competing context, plausible wrong default, and target
harness conditions that create that pressure.

Assess:

1. correct invocation and internal route;
2. intended choice at the ambiguous fork;
3. generalization to an unseen case when rationale should transfer;
4. distinction between user intent, current behavior, and mechanical facts;
5. authorized scope and avoidance of unrelated ritual;
6. satisfaction of the checkable completion criterion;
7. decision reliability and total reading, retrieval, and execution cost,
   including recurring context and traversal latency, with the loaded flow's
   size for candidate and baseline taken from the validator's runtime flow
   report rather than estimated; a context saving does not justify a material
   loss in the intended choice or completion behavior.

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
