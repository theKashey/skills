# Output-context review

Review whether a finished artifact explains and represents itself coherently
without relying on the producer's private interpretation. This gate detects
missing context and unjustified production-process residue; it does not verify
external facts, requirements, tests, or source evidence.

- [Isolated and unbiased context](#isolated-and-unbiased-context)
- [Pass rules](#pass-rules)
- [Verdict format](#verdict-format)
- [Fresh-review protocol](#fresh-review-protocol)

## Isolated and unbiased context

Create a fresh reviewer with no inherited drafting or verification context.
Give it exactly two durable artifacts:

1. The final review target. Prefer the complete delivered artifact. A diff is
   sufficient only when it retains enough final-state context to assess the
   changed material and its opening or primary entry surface.
2. This review-rules artifact, unchanged.

For a compound deliverable, the final target may be the delivered bundle. Do
not add a producer-authored explanation, manifest, or review wrapper unless it
is genuinely part of the deliverable.

Supply no task summary, scope statement, producer interpretation, consumer or
reader profile, artifact role, layer or rung, semantic classification, source
facts, validation output, process declaration, producer rationale, prior
review, expected verdict, or intended fix. The reviewer must not consult other
sources. It infers context from the target itself and cites target evidence in
its verdict.

## Pass rules

Before applying the rules, infer the target's subject, artifact role and layer,
consumer or reader, task, classification, and process determination. An
unsupported inference is a block, not a request for producer interpretation.

Return `PASS` only when every applicable rule passes with no unclassified
ambiguity:

1. **Subject before artifact.** The opening or primary entry surface establishes
   the governed subject's purpose, responsibility, outcome, contract, or
   boundary before explaining production, file, tool, or review mechanics.
2. **Durable consumer value.** Each material unit advances the inferred
   consumer's contract, rationale, task, durable operating process, explicitly
   historical record, or necessary navigation.
3. **Finished-artifact focus.** The target represents its subject and completed
   state. Creation, drafting, validation, tooling, agent, instruction, and
   review details remain outside it unless the durable process itself qualifies
   under rule 5.
4. **Inferable context and coherence.** From the target alone, the reviewer can
   cite a coherent subject, role, layer or rung when applicable, consumer or
   reader, and task. The parts agree about that context and do not require a
   producer explanation to belong together.
5. **Durable-process exception.** Process content fails unless the target
   itself establishes an enduring operator, trigger, action, result or decision
   boundary, scope, and owner. A narrative of the session that produced or
   verified the artifact never qualifies.

For prose or labeled visual surfaces, apply two adversarial checks:

- **Deletion:** remove artifact labels, paths, and phrases such as “this file,”
  “this deck,” or “this report.” If no useful claim about the governed subject
  remains, the target fails.
- **Substitution:** replace the subject with a sibling unit. If the opening or
  primary entry surface remains equally true, it is generic artifact or process
  language rather than subject orientation.

Apply the rules to the artifact's actual consumer-visible forms. For changed
source code, inspect added comments, public documentation, examples,
reader-visible strings, test descriptions, and documentation-like identifiers;
do not demand document-shaped prose from implementation code.

## Verdict format

Return:

```text
Status: PASS | BLOCK | NEEDS-HUMAN-DECISION | UNVALIDATED
Inferred context: subject, artifact role and layer, consumer or reader, task, classification, with target evidence
Process determination: absent | qualifies | fails | indeterminate, with target evidence
Rule results: rules 1–5, with target locations
Blockers: location, broken rule, consumer impact, minimal repair direction
Review boundary: external factual correctness, requirements, coverage, source truth, and deterministic checks not assessed
```

Use `BLOCK` for a known rule violation or an inference that depends on producer
interpretation. Use `NEEDS-HUMAN-DECISION` only for artifact scope,
classification, or strategic intent that the target leaves genuinely
ambiguous. Use `UNVALIDATED` when the target, a required consumer-visible form,
or an isolated reviewer is unavailable.

This gate's `PASS` means the target is semantically coherent in its own context
and free of unjustified process residue. It does not establish factual
correctness, contract coverage, cross-artifact truth, or deterministic-check
results; those remain separate gates.

## Fresh-review protocol

1. Finish the candidate and run factual, deterministic, and consumer-surface
   checks. Keep their inputs, outputs, and conclusions outside this gate.
2. Start a fresh isolated reviewer with no inherited context.
3. Give it exactly the final target and this rules artifact. It reviews only;
   it does not edit, rewrite, or consult other sources.
4. Require the verdict format above.
5. On `BLOCK`, repair in the production context, rerun invalidated checks, and
   use a new isolated reviewer.
6. Give the new reviewer no prior verdict, repair narrative, expected outcome,
   or other producer interpretation.
7. When no isolated reviewer can run, record `UNVALIDATED`; never call that a
   pass or a publish-ready result.
8. Keep the verdict in the handoff, not in the delivered artifact, unless the
   review record is itself an explicitly requested deliverable.
