# Staying Put

The load card in [SKILL.md](SKILL.md) fixes where the increment stands; these
moorings govern the executor between the freeze and the readback, when mid-flow
discoveries, failures, and improvement ideas pull against the frozen scope.

Load this file when an intended mutating action is not plainly covered by the
frozen Increment's maximum scope, or when a completion report is about to omit
a deferral, a side repair, or work already mutated before the freeze. Each
mooring names a **Drift** — the
observable pull off the frozen position — and a **Hold** — the move that
keeps the increment where it was frozen. A drift acted on is a violation of the
mooring, not a judgment call. The moorings restate no other package's rules
and borrow no other package's names; where a mooring meets a rule that lives
in SKILL.md, it points there instead of restating it.

## 1. The card is the ground

Once frozen, the load card outranks every idea that arrives after it. Evidence
that contradicts a frozen field is not an idea: it takes a door in mooring 6,
never a self-authorized rewrite.

**Drift:** A mid-flow insight starts steering — the increment quietly grows a
second goal, or the frozen Misfire is re-argued because the work now looks
safer than it did.

**Hold:** Check the intended action against the frozen Increment's maximum
scope before mutating anything. An action the card does not cover needs a new
decision, not a better justification.

## 2. Discovery is not scope

Finding a problem is evidence; it is not authorization to fix it here.

**Drift:** An off-scope defect gets repaired inline "while the file is open,"
and the diff now answers two questions.

**Hold:** Apply the side-track rule in [SKILL.md](SKILL.md); it decides
between a bounded in-place repair, a delegated brief, a deferral, and a
terminal status. A side repair shares the diff, so report it against its own
boundary — that is what keeps the increment's scope answerable to one
question.

## 3. Improvement is not scope either

The Drift of virtue: cleanups, renames, and refactors feel free because they
are good.

**Drift:** The diff contains changes made after the freeze whose absence
would not have failed the readback.

**Hold:** Strip the improvement from the increment and record it as a
deferral. Its worth is not the question; its membership in the frozen scope
is. Improvement already in the diff before the freeze is reported under
mooring 5, not stripped.

## 4. Failure does not widen scope

A failed readback is information about this increment, not a mandate for a
larger one.

**Drift:** After a disconfirming readback, the repair attempt touches paths
the frozen scope never included, because "the real problem turned out to be
bigger."

**Hold:** Repair within the frozen scope, or — when the cause sits outside it
— treat it as mooring 2's case and apply the side-track rule, or exit through
a terminal status and let the next increment be sized to what was learned.
Bigger-than-expected is a finding, not an amendment.

## 5. Nothing leaves silently

The completion report is the only exit, and it must account for both kinds of
silence.

**Drift:** Work appears in the diff that neither the frozen scope nor a
reported exception covers, or work set aside vanishes without a deferral line
— the report and the actual change disagree.

**Hold:** Before reporting, reconcile the diff against the frozen scope plus
what [SKILL.md](SKILL.md) authorized outside it — a reported side repair, or
reported work already mutated before the freeze — and reconcile the deferral
list against what was set aside: side problems and stripped improvements
alike. A report that matches both is the definition of having stayed put.

## 6. The statuses are the only doors

When staying put becomes impossible, leave through a terminal status, not
through improvisation.

**Drift:** Blocked or ambiguous work continues anyway — the executor invents
an interpretation, widens authority, or keeps mutating past a stop condition
because stopping feels like failure.

**Hold:** `BLOCK` and `NEEDS-HUMAN-DECISION` exist so that stopping in place
is always available and always cheap. Taking a door is staying put; forcing a
window is not.
