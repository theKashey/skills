# Install Compass

The adopted rule is the usage hook in [agent-hook.md](agent-hook.md). It is
installed ask-first when Phase B closes, in the file that declares the chart
root ([growth-and-drift.md](growth-and-drift.md)), never before a chart
exists; a host with no chart starts at Phase 0. Install the chart check in
the host's test suite (`verification.md` §First) and, once a lexicon is
admitted, the lexicon check (`lexicon.md` §The installed check), both
ask-first, so drift fails a build instead of waiting for review.

Add these review checks, ask-first, to the review file the host's root
instructions point to; if none is named, ask where they belong:

- **Updated when needed.** A change that alters what the chart describes
  updates the chart through Create work, or records the disagreement,
  classified per `growth-and-drift.md` §Classifying Disagreement, in the PR or
  task record. A chart silently out of step with the code is the failure this
  catches.
- **Consulted when needed** (optional). Non-local work shows it consulted the
  chart, as the usage hook directs.

Verify the hook and chart check through their `verification.md` §L2 rows, the
lexicon check by a passing host suite, and that each review check sits where
the host's instructions deliver review guidance.
