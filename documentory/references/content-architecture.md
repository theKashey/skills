# Content architecture

Use this reference when planning a README, restructuring documentation, or building public documentation-site navigation.

## Reader paths

Start with the reader's question, not the repository's folders. Diátaxis names
content modes; it does not require separate files, folders, or navigation.

| Reader need | Diátaxis form | A useful success condition |
| --- | --- | --- |
| Decide whether the library is relevant | README or explanation | Understand the problem, audience, scope, and first next step. |
| Learn a capability | Tutorial | Reach a visible working result by following steps. |
| Solve a known problem | How-to | Complete the task with stated prerequisites and expected result. |
| Find an exact fact | Reference | Locate a precise answer quickly without reading a narrative. |
| Understand a design | Explanation | Understand the mental model, trade-off, and boundary. |

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

## README structure

Keep the README as an orientation and first-success document:

1. Why this library exists: reader problem, intended user, outcome, scope, and non-goals.
2. Installation and compatibility.
3. Smallest honest first success.
4. Primary concepts needed to adapt the example.
5. Essential boundaries or security assumptions.
6. Clear links to existing deeper material as applicable. If none exists, keep essential content in the README and report any worthwhile split as a proposal.

When deeper surfaces already exist, avoid duplicating their exhaustive detail in
the README. When the README is the only public documentation, completeness
takes precedence; organize necessary reference, procedure, and explanation
under clear sections.

## Opening and scan path

Treat the opening as a decision surface, not mandatory sales copy. In plain,
current terms, let the intended reader identify the problem, supported outcome,
scope, and first next step. State a meaningful distinction from alternatives
only when it matters to that decision and can be verified.

Put evidence beside evaluative or comparative claims. Include the conditions
needed to interpret a benchmark, size, compatibility, or security claim;
otherwise replace the adjective with the observable behavior it was meant to
describe.

Check the scan path: a reader who sees the opening, headings, and descriptive
links should still be able to determine relevance and find first success or the
needed detail. This test does not prescribe badges, bold text, horizontal rules,
a table of contents, or a fixed section order.

Validate installation and first success from a clean supported environment when
feasible. Do not silently depend on repository-local caches, global tools,
credentials, generated files, or maintainer knowledge. If clean-start validation
is not feasible, state what remained untested.

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
