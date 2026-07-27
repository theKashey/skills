# Verify Complex Artifacts

Verify Complex Artifacts independently gates finished multi-file deliverables
before a handoff or trust transition, so hidden cross-file and
producer-context gaps become exact refinement signals instead of false
confidence.

## Why it exists

Model-assisted work is produced from selective context, so gaps are expected:
the result may be polished while its subject is unclear, one file may be
correct while the bundle contradicts it, or a focused revision may quietly
distort the whole. The producing model cannot reliably find those gaps by
explaining its own intent back to itself.

Verify Complex Artifacts exists to turn those expected blind spots into an
independent refinement signal before a complex deliverable crosses into
publication, merge, deployment, delivery, or acceptance. Its intended effect is
not a reassuring pass. It is an evidence-separated decision that either exposes
the exact gap to repair, records what could not be validated, asks for the
missing human judgment, or permits the frozen candidate to move forward.

Use this skill when no single deterministic check can establish that the
finished candidate is coherent across its requirements, files, representations,
and consumer paths. It is especially useful after iterative or model-assisted
work, where a locally successful change can conceal broader damage.

The producer may run factual and deterministic checks, but cannot certify the
artifact's subject or output-context integrity. A fresh review subagent must
reconstruct the problem, intended impact, boundary, and internal relationships
from the delivered target alone. Relationship truth is checked separately
against the contracts of both endpoints or an explicit product decision.

Do not add the complete gate to a request for one narrow property such as
syntax, links, formulas, or tests. Use the repository-native check for that
property unless an integrated readiness decision is also required. This skill
verifies a completed candidate; it does not replace the artifact's authoring
workflow or decide whether its product direction is desirable.

## Damage the gate looks for

These are diagnostic signatures, not claims about intent and not proof that
every generated artifact contains them. An observed signature directs the
reviewer to the factual, deterministic, consumer-surface, security, or isolated
review gate capable of deciding whether damage is present.

| Signature | What may be damaged |
| --- | --- |
| **Proof leakage** | The artifact repeats the request, addresses the producer or user, or claims it complied, verified, or passed instead of representing the delivered subject. |
| **Pink-elephant amplification** | Repeated attention makes one concern disproportionately dominant and displaces sibling requirements, paths, or risks. |
| **Placement drift** | Correct material is added under the nearest visible heading, component, sheet, slide, or branch instead of its semantic owner. |
| **Proxy completion** | A checklist, metric, snapshot, example, or test passes while the consumer outcome or an unmeasured invariant fails. |
| **Context neglect** | A distant or structurally buried requirement, exception, dependency, or boundary disappears or is contradicted. |
| **Confabulated support** | Invented facts, citations, paths, counts, screenshots, rationales, or test results make the artifact appear grounded. |
| **Uniformity collapse** | A dominant template flattens cases, modes, voices, data classes, or failure paths that need to remain distinct. |
| **Source contamination** | Prompt fragments, embedded instructions, examples, placeholders, secrets, or source-only annotations leak into the delivered result. |
| **Collateral regression** | Improving the focal case degrades an adjacent behavior, representation, mode, edge case, or previously correct region. |

The [damage-signature reference](references/artifact-checks.md#cross-cutting-damage-signatures)
defines the observable evidence, adversarial check, and owning gate for each
signature.

## Point at a discovered problem

When a gate has established a defect, name the matching [Sin in *The Sins of
the LLM*](SINS.md) as `sin → evidence → countermeasure → invalidated gate`.
The name gives the repair a target; it never replaces target evidence or the
gate that proves the repair.

## What the gate establishes

The skill freezes the candidate and its trust boundary, inventories the bundle,
checks requirements and machine-testable properties, exercises the actual
consumer surfaces, and sends only the finished target and neutral rules to a
fresh review subagent. It returns one explicit readiness status:

- `PASS` — every required gate passed;
- `BLOCK` — a known defect or unmet contract remains;
- `NEEDS-HUMAN-DECISION` — only a subjective, strategic, ownership, or
  genuinely ambiguous contract decision remains;
- `UNVALIDATED` — required evidence, tooling, consumer view, or independent
  review was unavailable.

A `PASS` is scoped to the frozen contract and candidate. The isolated review
establishes semantic coherence and absence of unjustified process residue; it
does not substitute for source truth, requirement coverage, deterministic
checks, security review, or human product acceptance.

The [runtime workflow](SKILL.md) owns the complete procedure. The
[isolated review rules](references/output-context-review.md) own the review
subagent boundary.
