# Validate changed choices

Test whether the skill changes the intended decision and completion behavior,
not merely whether it loads, parses, or repeats supplied facts.

## Completion contract

Finish with `PASS`, `BLOCK`, `NEEDS-HUMAN-DECISION`, or `UNVALIDATED`, supported
by mechanical results and representative behavior. A missing required source,
environment, clean observer, or check is `UNVALIDATED`, never an inferred pass.

## 1. Freeze the evaluation

Before observing a run, record:

- candidate revision, target harness, and executing model: the named floor, as
  for routing;
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
6. satisfaction of the checkable completion criterion; a pass that relied on
   a critical input the skill never elicited, but the user or task happened to
   supply, is not evidence of its process—recommend an eliciting step;
7. decision reliability and total reading, retrieval, and execution cost,
   including recurring context and traversal latency, with the loaded flow's
   size for candidate and baseline taken from the validator's runtime flow
   report rather than estimated; a context saving does not justify a material
   loss in the intended choice or completion behavior.

Reference loading, tool use, produced files, and literal instruction compliance
are evidence only when they contribute to the frozen outcome.

### Check description routing

Reword a description only for an observed or reproduced misroute, frozen as a
prompt, or a named activation-contract violation; a contract repair still leaves
routing `UNVALIDATED` until this check runs. Freeze the co-installed description
set plus `none`, and the evaluator model: the floor, the least capable model the
skill must support, as the maintainer or consumer names it. A result transfers
to neither another set nor another model; without a named floor, routing is
`UNVALIDATED`. A floor change is a reason to rerun, and a prompt it loses is the
measured misroute that permits rewording. The target's
`evals/eval_queries.jsonl` is its must-not-lose baseline: one object per line
with `query`, `should_trigger`, and an optional `note`, speaking only for the
target and naming no other skill. Recommend appended lines to the host skill
creator; only a frozen observed misroute or a fresh author adds one, never the
proposer after seeing results. When the target has no such file, recommend
creating it from this check's prompts. A fresh author who is not the proposer
writes the prompts: positives as user requests and as post-inspection task
states; near-misses owned by a co-installed skill that carry the target's
trigger words; and routine tasks, or tasks with an artifact merely in view, that
no contract claims. Each evaluator sees only the whole frozen set plus `none`
and one `query`, never its `note`, and returns up to three ranked candidates
with scores, marking which it would load; run each query three times. The proposer neither
evaluates nor revises prompts after results. Classify the target per query:

| Target across runs | `should_trigger: true` | `should_trigger: false` |
| --- | --- | --- |
| Sole winner in every run | Go | Overtrigger |
| Among winners in any run, or sole winner in only some runs | Grey | Overtrigger |
| Not a winner in any run, including when `none` wins | Loser | Go |

Scores support the ranking; they set no threshold. The candidate passes only
when every query is a go. A loser means sharpening the target's own *what* or
*when*. Grey means the same when the inspected contracts show distinct scopes;
when more than one claims the prompt, report `NEEDS-HUMAN-DECISION` with a
[Law X](../LAWS.md#law-x--restructure-overlap-do-not-reword-it) recommendation
to rescope the competitors instead of rewording. Report `BLOCK` for any other
query that is not a go, and always when the candidate turns a baseline go into
any other cell.

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
