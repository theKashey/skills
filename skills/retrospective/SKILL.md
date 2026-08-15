---
name: retrospective
description: Use when an existing solution claims to work and its problem, beneficiary, owner, priority, evidence, or consequential oddities need interrogation; not for contract gating, fixing bugs, forward design, or team-morale retrospectives.
---

# Retrospective

Cross-examine the solution, not its author. Determine what problem it actually
solves, whether that problem existed before the solution, why it outranks the
work it displaces, why each consequential oddity exists, and whether the
evidence earns the claim that it works.

Use this governing question:

> Why are **YOU** solving **THIS PROBLEM**, **HERE** and **NOW**, with **THIS
> SOLUTION**, in **THIS WAY**, **FOR WHOM**—and what makes you say it **WORKS**?

Treat each stressed phrase as a separate claim. A history can explain a choice
without justifying its continued existence.

## Hold the posture

- Treat “it works” as the opening claim, not as evidence or the conclusion.
- Be adversarial toward claims and fair toward people. Test ownership and
  reasoning without attributing motives.
- Freeze the candidate before proposing changes. Do not improve it while still
  reconstructing what it is trying to do.
- Separate observations, owner accounts, inferences, and evidence. Never
  silently promote one into another.
- Follow consequential oddities, not personal taste or unfamiliarity. A choice
  deserves scrutiny when it changes the outcome, boundary, owner, cost,
  reversibility, state, timing, dependency, or failure mode.
- Apply Chesterton’s Fence twice: recover why a choice appeared, then test
  whether that reason remains true.
- Continue until every consequential oddity is classified or explicitly
  unresolved. Do not stop at the first coherent story.

When the solution owner is available, conduct a dialogue. Ask one
high-information question at a time and let the answer select the next
question. Never open with a questionnaire.

## Freeze the case

Record the smallest case that preserves the dispute:

```text
Candidate: [exact artifact, version, behavior, or decision under review]
Claim: [what “works” is asserted to mean]
Beneficiary: [who should experience the improvement]
Observed effect: [what has actually been seen]
Boundary: [environment, scale, time, inputs, and exclusions]
Known constraints: [facts that allegedly shape the solution]
Evidence supplied: [tests, measurements, comparisons, incidents, or none]
Problem origin: [Pre-existing | Exposed | Candidate-created | Candidate-amplified | Unknown; evidence]
Displaced work: [one consequential problem competing for the same resources, or Unknown]
```

Preserve the owner’s wording for the Claim where possible. If a field is not
known, write `Unknown`; if inferred, label it `Hypothesis`. Do not derive the
problem statement from the vocabulary of the implementation.

## Reconstruct the problem backwards

Infer which problem would have to exist for this exact candidate to be a
reasonable response:

1. Name the present friction, risk, or missed outcome.
2. Name the beneficiary and the observable change they should experience.
3. Distinguish the selected problem from adjacent variants.
4. State the cost of leaving it unsolved.
5. State what completion would look like without referring to the candidate’s
   internal mechanics.
6. Name one consequential, evidenced problem competing for the same actor,
   time, budget, or attention. State why this problem outranks it, or record
   that its priority is unsupported.
7. Trace whether the friction predates the candidate, was merely exposed by it,
   or was created or amplified by the candidate or an enabling decision.

Compare that reconstruction with the claimed problem:

- **Aligned** — both select the same change, beneficiary, and boundary.
- **Misaligned** — the candidate optimizes a different problem, beneficiary,
  or boundary.
- **Unreadable** — the candidate or available account does not expose enough
  to decide.

When producer context is likely to anchor the inference, use an isolated
reader—a fresh subagent or new session—whose entire context is the frozen
candidate; do not simulate the reader inside the producing context. Give it
only the candidate and this neutral question:

```text
From the candidate alone, infer:
- What change is this candidate trying to produce?
- What present friction or risk makes that change worthwhile?
- What conditions must already be true for this approach to make sense?
- What would a recipient observe if the candidate had its intended effect?
- Which consequential choice is left implicit or unresolved?
```

Compare its reconstruction with the frozen case afterward. Do not give the
reader the rationale, source facts, or desired answer.

## Grind the problem claim

Do not stop when the selected problem becomes coherent or even real. Force two
comparisons before accepting that the work deserves to exist:

> What should you be solving instead—and why are you spending attention here?

Compare the selected problem with one concrete, consequential problem competing
for the same owner or resources. Require evidence that distinguishes their
impact, urgency, reach, or reversibility. Do not invent a backlog of speculative
alternatives. If choosing between them requires strategy or risk authority,
surface the tradeoff and return `NEEDS-HUMAN-DECISION`.

> Did this candidate create the problem it now congratulates itself for solving?

Trace the shortest causal chain across the candidate boundary. Ask what was
observed before the candidate, what disappears if it is removed, and which
workarounds exist only because of its prerequisites or earlier decisions.
Distinguish a problem the candidate **created**, **amplified**, or merely
**exposed**. Suspicion is not causation: require a timeline, comparison, removal
test, or other discriminating observation.

A self-created problem does not automatically refute the candidate. It may be
the justified cost of a more valuable capability. Test the net outcome instead
of treating every induced dependency as failure. When either comparison is
consequential, record `Problem selection` or `Problem genealogy` as a row in the
existing decision ledger and classify it with the existing statuses.

## Inventory consequential oddities

Scan the whole candidate before choosing the first challenge. Include choices
such as:

- a bespoke abstraction, extra layer, indirection, or duplicated state;
- a manual responsibility that could belong to a system, another role, or a
  different boundary;
- asymmetric treatment of apparently equivalent cases;
- a retry, fallback, cache, queue, timeout, feature flag, exception, or
  hard-coded path;
- a global, privileged, irreversible, or unusually coupled action;
- complexity justified by hypothetical future use;
- a metric or test that proves internal activity but not beneficiary-visible
  effect;
- a convention, dependency, or inherited constraint used as its own rationale.

Include domain-specific anomalies that carry the same consequences. Omit
ordinary mechanics whose alternatives would not change the verdict.

Trace dependencies between oddities. An upstream choice that exists only to
support another unexplained choice is not independent evidence for either.

## Interrogate the stressed words

Use the lenses adaptively. Ask next about the lens whose plausible answers would
most change the reconstructed problem, decision ledger, or verdict.

| Lens | Challenge |
| --- | --- |
| **WHY** | What observable problem requires action? What happens if nothing is done? Why does that consequence matter? |
| **YOU / WE** | Who is the beneficiary, implementer, operator, payer, and decision owner? Why does this responsibility belong to this actor or layer? |
| **THIS PROBLEM** | Which variant is selected? Is it a cause, symptom, proxy, or adjacent problem? What is deliberately outside the boundary? |
| **HERE / NOW** | Which environmental, scale, timing, regulatory, or organizational conditions make the choice valid? When do they expire? |
| **THIS SOLUTION** | Which alternatives were genuinely available? Which constraint or evidence selected this one? Is the candidate searching for a problem? |
| **THIS WAY** | What job does each odd decision perform? Is it compelled, a supported tradeoff, inherited, or accidental? What else now exists only because of it? |
| **FOR WHOM** | Who experiences the benefit, and who absorbs the complexity, delay, risk, operation, or displaced work? |
| **WORKS** | What external observation distinguishes success from activity? Within which boundary, at what cost, against which baseline, and what would disconfirm it? |

Do not let `we` hide several actors with different incentives or obligations.
Do not let `this` slide between the problem, candidate, mechanism, and outcome.

## Challenge one decision at a time

Start with the highest-consequence oddity carrying the weakest rationale. Use
only as many of these follow-ups as the decision requires:

1. What observation caused this decision to exist?
2. What breaks, worsens, or becomes impossible without it?
3. Which alternatives were live, and what ruled each one out?
4. Which current constraint compels the choice, and who owns that constraint?
5. What evidence shows the rationale is still true now?
6. Which cost or responsibility does the choice move elsewhere?
7. What observation would falsify the rationale?

Reject an answer as incomplete when it merely:

- restates the implementation;
- names a framework, vendor, convention, or historical decision;
- substitutes preference for a requirement;
- claims success without a boundary, comparison, or observable outcome;
- invokes future-proofing without a committed future condition;
- invokes risk without its consequence and applicable boundary; or
- explains how the choice arose but not why it should remain.

Do not run “five whys” mechanically. Stop when the decision reaches an observed
problem and current constraint, or when the remaining link is an unsupported
assertion that can be tested.

Maintain this ledger as the interrogation proceeds:

| Decision or oddity | Claimed job | Evidence | Assumption and counterfactual | Cost or displaced responsibility | Status |
| --- | --- | --- | --- | --- | --- |

Use one status:

- **Supported** — current evidence connects the choice to the claimed outcome.
- **Conditional** — justified only while named conditions remain true.
- **Inherited** — origin is known; present necessity is not.
- **Accidental** — no deliberate rationale exists, though consequences may.
- **Obsolete** — the selecting problem or constraint no longer exists.
- **Misaligned** — the choice serves a different problem or beneficiary.
- **Unresolved** — plausible accounts remain and predict different conclusions.

An explanation is not evidence. A surviving hypothesis is not yet a cause.

## Produce a discriminating readback

When testimony and existing artifacts cannot classify a consequential choice,
stop debating and select one bounded evidence-producing move:

```text
Question: [the exact unresolved claim]
Move: [one comparison, trace, query, replay, removal test, or isolated read]
Expected signal: [observation predicted if the rationale holds]
Disconfirming signal: [observation that counts against it]
Safety: [maximum scope, reversibility, or containment]
Review point: [time, attempt, state transition, or measurement]
```

Choose a move whose possible outcomes divide the plausible accounts. Reject a
probe when every outcome leaves the verdict unchanged. Do not turn the move
into a rewrite or roadmap. Retrospective selects the question, bounded move,
and signals that would divide the accounts; it does not execute the move or
infer causality from the proposed probe. When installed, Read the Terrain owns
execution. Update the ledger from the result; more activity without a
discriminating signal is not progress.

Return `BLOCK` when the same consequential question survives two inconclusive
moves or requires unavailable evidence. Return `NEEDS-HUMAN-DECISION` when
resolving it requires authority, intent, or a tradeoff only the decision owner
can supply.

## Deliver the retrospective

Keep the report proportional to the candidate. Include:

```text
Claim under review
Actual problem reconstructed
Problem alignment: Aligned | Misaligned | Unreadable
Decision ledger
What is genuinely necessary
What is conditional, inherited, accidental, obsolete, or misaligned
Hidden contracts and displaced costs
Claim verdict and evidence boundary
Smallest unresolved question or next evidence-producing move
```

Use one claim verdict:

- **SUPPORTED** — beneficiary-visible evidence supports the claim inside an
  explicit boundary.
- **CONDITIONALLY SUPPORTED** — it works only under named conditions or costs
  omitted by the original claim.
- **MISALIGNED** — it works at something other than the problem claimed.
- **UNPROVEN** — it may work, but available evidence cannot distinguish success
  from activity, coincidence, or an untested account.
- **REFUTED** — observed evidence contradicts the defined claim.
- **BLOCK** — required evidence is unavailable or bounded moves remain
  inconclusive.
- **NEEDS-HUMAN-DECISION** — evidence exposes an intent or tradeoff choice that
  only the authorized owner can make.

Do not recommend replacement architecture merely because the existing one is
strange. First establish which decisions survive, which fail, and which question
would change the conclusion. If the user then asks for a redesign, carry forward
the supported constraints and discard unsupported rationales.
