# Content architecture

Content architecture gives each reader a clear path to a decision or task
without forcing a new filesystem topology.

Use this reference when planning a README, restructuring documentation, or
building public documentation-site navigation.

- [Reader paths](#reader-paths)
- [Detail level](#detail-level)
- [Procedure paths](#procedure-paths)
- [README roles](#classify-the-readme)
- [Landing decision test](#landing-decision-test)
- [Reader entry point](#reader-entry-point)
- [Opening and scan path](#opening-and-scan-path)
- [Progressive disclosure](#progressive-disclosure)
- [Explain-before-code pattern](#explain-before-code-pattern)
- [Meaningful visuals](#meaningful-visuals)
- [Separation tests](#separation-tests)

## Reader paths

Start with the reader's question, not the repository's folders. Diátaxis names
content modes; it does not require separate files, folders, or navigation.

| Reader need | Diátaxis mode | Likely surface | A useful success condition |
| --- | --- | --- | --- |
| Decide whether a project or published package is relevant | Explanation | Landing page | Understand the problem, audience, scope, and first next step. |
| Understand an internal unit's role | Explanation | Technical overview | Identify responsibility, boundary, interactions, and the next source or validation path. |
| Learn a capability | Tutorial | Tutorial or guided README section | Reach a visible working result by following steps. |
| Solve a known problem | How-to | How-to page or procedural README section | Complete the task with stated prerequisites and expected result. |
| Find an exact fact | Reference | API, configuration, or in-page reference | Locate a precise answer quickly without reading a narrative. |
| Understand a design | Explanation | Concept or architecture section | Understand the mental model, trade-off, and boundary. |

Apply these modes within the documentation surfaces the repository already
uses. If the README is the only surface, keep the necessary modes as clear
README sections. Do not create or move pages unless the user requested a new
structure or explicitly accepts a proposed split.

## Detail level

Choose Guided, Balanced, or Compressed for the intended reader before writing.

| Level | Include | Avoid |
| --- | --- | --- |
| Guided | A short mental model, defined unfamiliar terms, explicit prerequisites, one primary path, and expected results. | Background history, multiple equivalent paths, and line-by-line code narration. |
| Balanced | The reader outcome, non-obvious choices, important boundaries, and contextual links. | Repeating the reference contract or assuming specialist knowledge without evidence. |
| Compressed | The exact answer, required conditions, meaningful boundary, and a descriptive link to detail. | Introductions, examples, or explanations the named expert audience can safely infer. |

Do not use Compressed to hide a failure mode, security condition, required setup, or public API contract. Do not use Guided to make every page a tutorial. Keep code samples copyable at every level; change surrounding prose, not the amount of commentary inside the code.

## Procedure paths

Use a procedure only when a sentence, example, or link cannot carry the action
safely.

- A tutorial controls its starting conditions and follows one reproducible route
  to a visible result. State the expected result at meaningful checkpoints; defer
  variants.
- A how-to serves a reader who knows the goal. Name real prerequisites and
  branch only when a condition changes the action or recovery path.

For either, let the heading state the task. Put the location, condition, or
purpose before the action. Give each numbered step one meaningful action,
combining only trivial actions in the same context. Put required warnings or
decisions in the normal flow immediately before they matter.

## Classify the README

Read `locality-ladder.md` and classify the README by the scope it governs and
the reader it serves. The filename alone does not determine its role:

- A top-level open-source project, public site, or product README is a landing
  page for outsiders.
- A folder, internal package, or internal module README is a technical document
  for people working inside the containing system.
- An independently published package README may serve both roles. Keep its
  short external landing path distinct from its technical contract.

Do not apply the landing-page pattern to every README.

## Top-level landing README

Help an outsider decide whether to enter the project and reach first success:

1. Why the project exists: problem, intended audience, supported outcome,
   scope, and non-goals.
2. A concrete, verifiable reason to choose or explore it: observable behavior,
   a concise task-and-result, or a relevant comparison with its conditions.
3. Installation and compatibility from the outsider's actual entry point.
4. The smallest honest first success and expected result.
5. Essential concepts, boundaries, or security assumptions.
6. Clear routes to deeper technical material, contribution, support, and
   licensing as applicable.

This surface advertises by demonstrating relevance and usefulness. Keep package
mechanics in their technical owners instead of turning the landing page into a
monorepo manual.

## Landing decision test

Make the opening and scan path sufficient for an outsider to decide whether the
next action is worth taking:

1. Can I recognize my problem and intended environment or role here?
2. What supported outcome can I expect?
3. What verified behavior, task-and-result, or relevant comparison makes that
   credible?
4. What is the smallest next action from my actual environment?
5. If a likely false expectation exists, which relevant boundary should be
   visible before it matters?

This is a reader-decision check, not a fixed outline, badge set, or feature
inventory. Use the smallest verified evidence that lets the reader decide.

## Internal technical README

Help a maintainer or coding agent understand the governed folder, package, or
module without reconstructing the containing system:

1. Why the unit exists and its responsibility in the parent system.
2. What it owns, what it deliberately does not own, and its boundary with
   sibling units.
3. How it interacts with callers, dependencies, state, lifecycle, or host
   infrastructure.
4. Its entry points, configuration, failure behavior, local workflows, and
   validation commands when those facts belong at this scope.
5. Routes to source, tests, package reference, domain context, and broader
   architecture.

This surface is technical documentation. It may assume a checkout, internal
paths, and repository tooling when those are genuinely available to its reader.
Do not add project-level sales copy or external installation merely because the
file is named `README.md`.

## Dual-role package README

When a package is independently published, begin with the shortest external
landing path needed to establish relevance, installation, and first use. Then
make the technical package contract separately scannable. Do not let the
landing introduction displace required defaults, behavior, failures,
interactions, or boundaries.

When deeper surfaces already exist, avoid duplicating their exhaustive detail.
When a README is the only documentation at its rung, completeness takes
precedence; organize necessary reference, procedure, and explanation under
clear sections.

## Reader entry point

Model the reader at the surface where they first encounter the documentation.
Assume only context available at that rung.

For an external landing README, name an installation source the reader can
reach, such as a registry package, repository identifier, or URL. Use `.` only
after explicitly establishing a clone-and-enter-checkout workflow. For an
internal technical README, repository-local paths and commands may be the
correct primary path.

Check commands, links, paths, prerequisites, and first success from the stated
entry point. State additional authentication, source access, checkout state, or
tooling instead of relying on it silently.

## Opening and scan path

Treat a landing opening as a decision surface. In plain, current terms, let the
outsider identify the problem, supported outcome, scope, and first next step.
State a meaningful distinction from alternatives only when it matters to that
decision and can be verified.

Treat an internal technical opening as a boundary surface. Let the maintainer
identify the unit's responsibility, place in the containing system, owned
boundary, and first route to implementation or validation. Do not force a
marketing problem statement onto it.

Open every reader-facing surface with the governed subject's relevant purpose,
responsibility, outcome, contract, boundary, or rationale—not with the
artifact's label, placement, or production story. Keep drafting, validation,
tool, and review material in the work handoff. When a durable process is the
explicit reader subject, establish its operator, trigger, action, and decision
boundary before explaining the document mechanics.

State scope or a non-goal only when a reasonable reader might otherwise infer a
capability or ownership that is not promised. Do not add generic disclaimers.

Put evidence beside evaluative or comparative claims. Include the conditions
needed to interpret a benchmark, size, compatibility, or security claim;
otherwise replace the adjective with the observable behavior it was meant to
describe.

Check the scan path for the named reader and task. For example, a landing reader
should determine relevance and find first success; a maintainer should find
responsibility, boundary, and validation; an integrator should find contracts
and prerequisites; an operator should find state, failure, recovery, and
escalation paths. This test does not prescribe badges, bold text, horizontal
rules, a table of contents, or a fixed section order.

Make headings and link text identify their task, concept, or destination without
surrounding prose. Do not make visual position, such as "above" or "below", the
only way to locate content.

Validate the primary reader path from its stated starting state. For a landing
surface, use a clean supported environment. For an internal technical surface,
use the documented repository state and repository-native tooling. Do not
silently depend on unstated caches, global tools, credentials, generated files,
or maintainer knowledge. State what remained untested.

## Progressive disclosure

Give enough context before each link to answer why it applies. Move detail only
to an existing or authorized surface. Otherwise disclose it progressively in
the current document through headings and local navigation.

Use a canonical-owner rule within the existing documentation topology. The
terms below describe content modes and may refer to sections in one README:

- Put exact defaults, type shapes, error details, and exhaustive option facts in reference.
- Put task-specific setup and procedure in how-tos.
- Put concepts and trade-offs in explanations.
- Put only a short contextual summary plus a link in other surfaces.

Delete repeated prose if a reader can still determine purpose, behavior, and boundary. Add only the smallest missing explanation at the reader's present level.

## Explain-before-code pattern

Use prose before a non-trivial example to state:

- the reader outcome;
- prerequisites and assumed surrounding context;
- why the selected API or option belongs in this example.

Use prose after it to state:

- expected result;
- meaningful limit, ownership boundary, or failure case;
- next useful page.

Do not narrate every line inside a runnable sample. Preserve comments only when they carry a non-obvious rationale that remains true when the sample is copied elsewhere.

## Meaningful visuals

When a diagram, screenshot, or image carries a fact, state, decision, or
relationship needed to act, expose it in concise contextual alt text or nearby
prose. Do not make a contract, requirement, or necessary state visible only in
the visual.

## Separation tests

Apply these tests while reviewing:

- Tutorial: can a newcomer complete it without unexplained prior decisions?
- How-to: can an informed reader identify the goal, prerequisites, steps, and result?
- Reference: can a reader find the factual contract without a narrative detour?
- Explanation: does it answer a conceptual or design question rather than conceal procedural steps?

Flag a possible split when one page attempts to teach, prescribe, enumerate
facts, and justify architecture with no clear separation. Until the user
accepts restructuring, preserve the current files and improve separation with
headings and local navigation.
