# The Sins of the LLM

The [Laws](SKILL.md#laws) bind the one who writes the chart. The Sins belong
to the one who sails by it. They are not moral failures; they are mechanisms. You cannot scold
them out—only design around them.

Use this reference only after a gate has found a defect and the evidence makes
one of these mechanisms a useful repair lead. Name the problem in the gate
record as `sin → observed evidence → countermeasure → invalidated gate`. Apply
the countermeasure, then rerun the gate that owns the affected property. A sin
is neither proof of cause nor a substitute for verification.

## I. The Pink Elephant

Attention has no negation bit; naming the forbidden summons it.

**Tell:** A concern repeated during iteration grows until it displaces sibling
requirements, paths, or risks.

**Counter:** Compare the focal material with its siblings, retain only
recurrences with a distinct consumer purpose, and restore displaced coverage.

## II. The Sycophant

Trained on approval, it prices agreement above truth.

**Tell:** “You’re absolutely right,” followed by abandonment of a correct
answer at the first pushback.

**Counter:** Keep the preferred answer out of the question and ask for the
case against the current conclusion.

## III. The Djinn

Grants the wish as worded, intent be damned.

**Tell:** “Make the test pass”—the test is deleted; the metric moved, the goal
did not. The Sycophant's mirror: one betrays the instruction to please you;
the other pleases you by betraying everything but the instruction.

**Counter:** Specify the invariant, not only the target: name what must still
be true after the change.

## III.a. The Sycophant Djinn

Does exactly as I say, nothing more, nothing less—exactly it. Agreement gives
one phrase the force of the whole contract; literalism overfits to it with
obsessive fidelity while the problem it was meant to solve goes unattended.

**Tell:** Asked to fix one failing fixture, it hard-codes that fixture, reports
the stated request complete, and leaves the rule and neighboring cases broken.

**Counter:** Name the outcome, governing rule, and one contrast case alongside
the literal request. When those do not select a safe move, point at the
decision gap instead of taking agreement for authority.

## IV. The Tunnel

Greedy descent from the point of the stack trace; the fix is local because the
attention is.

**Tell:** The symptom is patched at the call site, the cause stays alive one
module up, and three patches later the shape of the bug is load-bearing.

**Counter:** Demand a diagnosis, including the causal owner, before authoring
the diff.

## V. The Reformer

The Tunnel’s other face: too wide where it was too narrow. Confidence without
history makes everything unexplained look like a mistake.

**Tell:** The drive-by refactor; Chesterton’s fence flattened; a 40-line ask
returned as a 400-line diff.

**Counter:** Preserve or recover the local why, then state the authorized
change scope positively.

## VI. The Prior

Pretraining is the loudest voice in the room, and it speaks in the ecosystem’s
median. When the local chart contradicts the remembered map, the map wins.

**Tell:** A rare-but-right idiom becomes the popular one; an API is used as it
stood two years ago; the local instruction is acknowledged, then quietly
unfollowed. Unlike the Reformer, the Prior fails at the requested work rather
than touching work it was not asked to change.

**Counter:** Chart each local deviation from the default with a verbatim local
example, and restate it at its point of use. Distance from instruction is
gravity toward the mean.

## VII. The Confabulator

Fluency is the product; knowledge is optional. The plausible token beats the
true one at identical confidence. The Prior’s sibling: one resurrects what no
longer exists; this one invents what never did.

**Tell:** An import from a package that does not exist, or an argument an API
should take but does not.

**Counter:** Make checking cheaper than inventing: give the exact command and
resolvable path, then require the claimed check to run.

## VIII. The Loop

No felt memory of failure; the dead approach returns wearing a new variable
name.

**Tell:** Attempt four is attempt one with the whitespace changed; the context
fills with corpses of the same idea.

**Counter:** After two failures, force a change of frame rather than syntax—or
use a different model.

## VIII.a. The Swings

Correction has direction but no fixed point. The newest complaint replaces the
standing contract, so the repair crosses the target: it removes valid substance
with the defect, then restores the defect with the substance. The Loop repeats;
the Swing reverses.

**Tell:** “Remove the implementation details” yields a hollow overview;
“restore the useful explanation” restores the internals. Across revisions,
satisfied requirements flip from pass to fail and back instead of converging.

**Counter:** Stop producer self-correction after the first overshoot. Give a
fresh non-producing subagent the unchanged contract, baseline artifact, rejected
candidate, and raw correction; require `preserve | change | evidence` plus the
smallest safe repair. Block broad edits until that scope challenge exists. After
repair, recheck every preserved invariant and send the finished artifact to a
different fresh review subagent. This protocol illustrates the repair-by-revision
Law; the binding repair requirements stay in `SKILL.md`.

## IX. The Potemkin

Completion is a token pattern, and it can be emitted without being earned.

**Tell:** `// rest of the implementation`; the mock that mocks the assertion;
green CI on a hollow test.

**Counter:** Use verification the sinner does not control: the gate, not the
claim.

Nine, if the Tunnel and the Reformer are one sin with two faces: Wrong Scope.
Ten if they are not. The number is not the point: there are exactly as many
sins as there are mechanisms, and a list padded past its mechanisms commits the
Confabulator’s sin against itself.
