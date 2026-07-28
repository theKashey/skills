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

Spawn a fresh review subagent with no inherited drafting or verification
context. Give it exactly two durable artifacts:

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

Before applying the rules, infer the target's subject, consumer or system,
intended task or effect, and process determination where the target exposes
them. Inventory independently selectable named subjects only when the artifact
presents them. An inference needed by an applicable rule but unsupported by the
target is a block, not a request for producer interpretation.

Return `PASS` only when every applicable rule passes with no unclassified
ambiguity:

1. **Artifact-appropriate orientation.** A prose or labeled visual surface
   states its governed subject or collection and consumer value before detailed
   mechanism. Every compact catalog entry names what its subject provides and
   why the consumer would choose it. For code, spreadsheets, decks, and other
   non-document artifacts, inspect the actual entry surface for the equivalent
   purpose, task, or effect; do not require document-shaped prose.
2. **Durable consumer value.** Each material unit advances the inferred
   consumer's contract, rationale, task, durable operating process, explicitly
   historical record, or necessary navigation. A statement that merely names
   the artifact, its format, its placement, or its intended maintenance use
   does not advance the governed subject: the consumer can already infer that
   from the artifact's location and form. A concrete component map, ownership
   boundary, or framework distinction passes when it changes the consumer's
   next choice; a bare framework declaration or construction account does not.
3. **Finished-artifact focus.** The target represents its subject and completed
   state, not an implementation-time recording that awaits another in-scope
   edit. Creation, drafting, validation, tooling, agent, instruction, and review
   details remain outside it unless the durable process itself qualifies under
   rule 5. A supported transitional product state may pass only when the target
   establishes it as part of the enduring contract.
4. **Inferable context and coherence.** From the target alone, the reviewer can
   cite a coherent subject, consumer or system, and task or effect where those
   are material to use. The parts agree about that context and do not require a
   producer explanation to belong together.
5. **Durable-process exception.** Process content fails unless the target
   itself establishes an enduring operator, trigger, action, result or decision
   boundary, scope, and owner. A narrative of the session that produced or
   verified the artifact never qualifies.
6. **Proportion and placement integrity.** The target contains no proof leakage
   that echoes instructions or claims compliance, no focal point whose
   repetition or prominence overwhelms sibling consumer needs, and no material
   placed at a structurally convenient but semantically wrong owner. Treat
   “this README,” “this module,” “this document,” or equivalent generic
   assertions of the artifact's own purpose, placement, or maintenance role as
   proof leakage. A concrete component map or ownership boundary passes when
   it changes the consumer's next choice. Repeated emphasis and unusual
   placement pass only when the target itself establishes their distinct
   consumer value and governed scope.

For prose or labeled visual surfaces, apply two adversarial checks to the
opening, each compact subject offer, and the owning section when one exists:

- **Deletion:** remove artifact labels, paths, and phrases such as “this file,”
  “this deck,” or “this report.” A remaining generic claim that the artifact
  helps someone understand, change, use, or maintain the governed subject also
  fails: it restates the artifact's placement rather than a fact about that
  subject. Retain a concrete framework distinction or component map only when
  it selects a different consumer action or understanding.
- **Substitution:** replace the subject with a sibling unit. If the opening or
  primary entry surface remains equally true, it is generic artifact or process
  language rather than subject orientation.

Apply the rules to the artifact's actual consumer-visible forms. For changed
source code, inspect added comments, public documentation, examples,
reader-visible strings, test descriptions, and documentation-like identifiers;
do not demand document-shaped prose from implementation code.

For an artifact that presents independently selectable named subjects, report
one row for each:

```text
Subject results: subject | what is offered | why choose it | offer location | situation or pressure | affected consumer or system | intended impact or changed decision | boundary | selection-context location | PASS or BLOCK
```

Judge whether relationship direction, modality, conditions, placement, and
internal consistency are clear, but do not infer that an internally coherent
relationship is true. The factual gate must verify each consumer-visible edge
against authoritative contracts for both endpoints or an explicit product
decision.

## Verdict format

Return:

```text
Status: PASS | BLOCK | NEEDS-HUMAN-DECISION | UNVALIDATED
Inferred context: subject, consumer or system, task or effect, with target evidence
Subject results: one row per independently selectable named subject, when applicable
Process determination: absent | qualifies | fails | indeterminate, with target evidence
Rule results: rules 1–6, with target locations
Blockers: location, broken rule, consumer impact, minimal repair direction
Review boundary: external factual correctness, requirements, coverage, source truth, and deterministic checks not assessed
```

Use `BLOCK` for a known rule violation or an inference that depends on producer
interpretation. Use `NEEDS-HUMAN-DECISION` only for artifact scope,
classification, or strategic intent that the target leaves genuinely
ambiguous. Use `UNVALIDATED` when the target, a required consumer-visible form,
or a review subagent is unavailable.

This gate's `PASS` means the target is semantically coherent in its own context
and free of unjustified process residue. It does not establish factual
correctness, contract coverage, cross-artifact truth, or deterministic-check
results; those remain separate gates.

## Fresh-review protocol

1. Finish the candidate and run factual, deterministic, and consumer-surface
   checks. Keep their inputs, outputs, and conclusions outside this gate.
2. Spawn a fresh review subagent with no inherited context.
3. Give it exactly the final target and this rules artifact. It reviews only;
   it does not edit, rewrite, or consult other sources.
4. Require the verdict format above.
5. On `BLOCK`, repair in the production context, rerun invalidated checks, and
   use a new review subagent.
6. Give the new reviewer no prior verdict, repair narrative, expected outcome,
   or other producer interpretation.
7. When no review subagent can run, record `UNVALIDATED`; never call that a
   pass or a publish-ready result.
8. Keep the verdict in the handoff, not in the delivered artifact, unless the
   review record is itself an explicitly requested deliverable.
