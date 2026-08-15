# Retrospective

Retrospective helps an evaluator challenge an existing solution, including one
produced by an AI agent, that is presented as done or working. It reviews the
problem–beneficiary–outcome claim, not implementation quality in isolation.

A coherent artifact can still solve the wrong problem, promote an unsupported
assumption into a problem, create the friction it then repairs, solve a real
but lower-priority problem, or prove only that its own mechanism runs.
Retrospective reconstructs what problem would make the candidate reasonable,
then asks whether that problem exists, matters, belongs to this team, layer, or
system, and changed for the intended beneficiary.

## Why it exists

When an AI agent produces the implementation and its explanation in the same
context, every unusual choice becomes easy to defend in terms of the artifact
around it. The explanation can therefore become a closed proof: the solution
justifies the decisions, and those decisions are offered as proof that the
solution was necessary.

Five mismatches survive that proof:

- **Problem substitution:** the candidate improves a tractable neighbor of the
  requested outcome, then reports the original problem as solved.
- **Problem invention:** the candidate treats an assumption, convention, or
  suspicious-looking metric as harm without establishing that anyone needs it
  changed.
- **Problem manufacture:** the candidate or one of its enabling decisions
  creates or amplifies the friction that is then presented as evidence that
  more work is necessary.
- **Priority displacement:** the candidate solves a real problem but provides
  no reason it should consume the owner, time, budget, or attention needed by a
  more consequential problem.
- **Completion substitution:** the mechanism runs, a test passes, or a metric
  moves, but the intended beneficiary does not experience the promised change.

All five can produce polished code, green tests, and a persuasive completion
summary. The missing evidence is not visible from implementation quality alone.

## How false completion presents

These hypothetical examples illustrate recurring mismatch patterns; they are
not claims about observed incidents.

| Requested outcome | AI claim | What it actually established | Missing challenge |
| --- | --- | --- | --- |
| Reduce support tickets about incorrect invoice totals. | “Fixed invoices by making the invoice page 40% faster.” | Rendering became faster; total correctness and ticket volume were not tested. | Why would rendering latency cause incorrect totals? |
| Reduce database load. | “Added a cache, so the database problem is solved.” | A local benchmark emitted fewer queries; no capacity, latency, or cost problem was established. | What observed harm makes the current query load a problem? |
| Improve regression protection. | “Raised line coverage from 71% to 90%.” | More lines execute under tests that assert mocked calls; detection of meaningful regressions is unknown. | Which previously plausible failure can the new tests now detect? |
| Keep client and server schemas consistent. | “Added a second validator in the frontend.” | The client rejects some invalid input; it also becomes another schema owner that can drift. | Why is the frontend responsible for a contract already owned by the server? |
| Deliver a usable export. | “The CSV generator passes every test.” | The service can write correct bytes; the intended user still cannot retrieve the file under their permissions. | What does the beneficiary observe when the export succeeds? |
| Reduce failed customer checkouts this week. | “Fixed a genuine 200 ms delay in internal admin search.” | A real latency problem was solved, but no evidence shows it should have displaced investigation of failed payments. | What higher-consequence problem competed for the same day, and why did this one outrank it? |
| Speed up account lookup. | “Added cache reconciliation, so stale reads are solved.” | The reconciliation mitigates stale reads introduced by the new cache; whether the speedup justifies the added correctness and operational costs is unknown. | Did stale reads exist before the cache, and what remains if the cache is removed? |

The point is not that each implementation choice is bad. The claim fails when
its evidence establishes a different change from the one being reported.

## What changes

Retrospective makes the candidate and its exact “works” claim stable before
discussion can improve either one. It reconstructs the problem backwards
without borrowing the implementation's vocabulary, follows every consequential
oddity to its current evidence, and separates owner accounts from observations
and hypotheses.

It then refuses to treat “real problem” as equivalent to “right problem.” It
compares the work with one evidenced competing problem and traces whether the
selected friction predates the candidate, was exposed by it, or exists because
of it. This extra pressure prevents a mechanism from laundering its own costs
into a new justification for itself.

When explanation cannot settle a consequential choice, the skill asks for one
bounded readback whose expected and disconfirming outcomes would change the
verdict. It can therefore finish with support, a named condition, misalignment,
refutation, or an explicit unresolved boundary instead of a smoother rationale.

## Boundaries and tradeoffs

- Retrospective starts from an existing candidate and completion claim. It does
  not replace forward design, routine bug fixing, or a team-morale retrospective.
- “Strange” means consequential to outcome, ownership, cost, reversibility,
  state, timing, dependency, or failure. Unfamiliar style alone earns no ritual.
- The result does not prove implementation correctness, security, product
  desirability, or requirement coverage beyond the evidence actually examined.
- Added scrutiny has a cost. Use it where a wrong completion claim could preserve
  unnecessary complexity, move responsibility, or close the wrong problem.
- A blocked or owner-dependent verdict is a valid result. The skill does not
  invent evidence or authority to produce closure.
- Identifying displaced work does not authorize the evaluator to choose the
  next roadmap item. Strategic priority remains with its decision owner.
- A candidate-created problem is not automatically disqualifying. The relevant
  question is whether the capability's net outcome justifies the induced cost.

The skill deliberately rejects a generic questionnaire, mechanical “five whys,”
and immediate redesign. A fixed checklist spends attention on low-value choices;
an early rewrite destroys evidence about why the present candidate exists. The
interrogation instead follows the next question whose possible answers would
most change the verdict.

The second-order consequence is that some working mechanisms will survive while
their original story does not. Preserve a mechanism only within the boundary
its evidence supports; do not let operational success silently promote it into
proof that the selected problem was real or worth solving.

## How it relates to the suite

Retrospective interrogates the completion claim upstream of a readiness gate:
Verify Complex Artifacts checks a finished artifact against a frozen contract,
while Retrospective asks whether that claim selects a real, current, rightly
prioritized problem. Read the Terrain owns one bounded evidence-producing move
inside live work; Retrospective owns the full interrogation of a finished
claim, and when Read the Terrain is installed it can execute the discriminating
readback this skill selects. A `REFUTED` or `MISALIGNED` verdict can seed
Helix's epitaphs so a retired story does not return under a new name.

These are external compositions of separately installed skills, not runtime
dependencies; the package completes alone. One maintenance invariant follows
from the overlap: the isolated-reader question block in
[`SKILL.md`](SKILL.md) is a deliberate verbatim duplicate of Read the
Terrain's neutral second-order question, and read-the-terrain remains its
canonical owner. Keep the two blocks identical when either changes, or record
a deliberate divergence; an accidental paraphrase between them is a defect.

## Runtime contract

[`SKILL.md`](SKILL.md) is the package's only runtime entry point; it contains
the executable interrogation, decision ledger, bounded readback, and terminal
verdicts. The rationale above is maintainer support and is not required to run
the skill.
