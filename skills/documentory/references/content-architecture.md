# Content architecture

Content architecture gives each reader a useful path to a task or decision without
forcing a new filesystem topology. It starts with reader context and governed
scope, not with a filename, repository visibility, or an assumed marketing role.

Use this reference when planning a README, restructuring documentation, or
building public documentation-site navigation.

- [Reader contexts](#reader-contexts)
- [Detail level](#detail-level)
- [Procedure paths](#procedure-paths)
- [Classify technical documents and public sites](#classify-technical-documents-and-public-sites)
- [Technical README roles](#technical-readme-roles)
- [Public documentation homes](#public-documentation-homes)
- [Public website presentation pages](#public-website-presentation-pages)
- [Reader entry and scan path](#reader-entry-and-scan-path)
- [Progressive disclosure](#progressive-disclosure)
- [Explain-before-code pattern](#explain-before-code-pattern)
- [Meaningful visuals](#meaningful-visuals)
- [Separation tests](#separation-tests)

## Reader contexts

Start with the reader's question, entry context, and task. Diátaxis names content
modes; it does not require separate files, folders, or navigation.

| Reader need | Diátaxis mode | Appropriate surface | Useful success condition |
| --- | --- | --- | --- |
| Orient in a repository, system, or documentation set | Explanation | Top-level technical README or documentation home | Identify purpose, scope, boundaries, and the technical route relevant to the reader's task. |
| Understand a package or module | Explanation and reference | Package or module README, API reference | Identify contract, integration conditions, and the next technical detail. |
| Work safely inside a repository area | Explanation | Folder overview | Identify ownership, conventions, boundary, and local validation. |
| Learn a capability | Tutorial | Tutorial or guided README section | Reach a visible working result by following one stated path. |
| Solve a known problem | How-to | How-to page or procedural README section | Complete the task with stated prerequisites and expected result. |
| Find an exact fact | Reference | API, configuration, or in-page reference | Locate a precise answer without a narrative detour. |
| Understand a design | Explanation | Concept or architecture section | Understand the mental model, trade-off, and boundary. |
| Evaluate or access a browser-based product | Presentation or product guidance | Public website page, not a README | Recognize the supported outcome and take a verified browser-native next action. |

Apply modes within the documentation surfaces the repository already uses. If a
README is the only surface, keep the necessary modes as clear technical README
sections. Do not create or move pages unless the user requested a new structure
or explicitly accepts a proposed split.

## Detail level

Choose Guided, Balanced, or Compressed for the intended reader before writing.

| Level | Include | Avoid |
| --- | --- | --- |
| Guided | A short mental model, defined unfamiliar terms, explicit prerequisites, one primary path, and expected results. | Background history, multiple equivalent paths, and line-by-line code narration. |
| Balanced | The reader outcome, non-obvious choices, important boundaries, and contextual links. | Repeating the reference contract or assuming specialist knowledge without evidence. |
| Compressed | The exact answer, required conditions, meaningful boundary, and a descriptive link to detail. | Introductions, examples, or explanations the named expert audience can safely infer. |

Do not use Compressed to hide a failure mode, security condition, required setup,
or public API contract. Do not use Guided to make every page a tutorial. Keep
code samples copyable at every level; change surrounding prose, not the amount
of commentary inside the code.

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

## Classify technical documents and public sites

Read locality-ladder.md. Classify every surface by its governed scope, reader,
available context, and task:

- A top-level repository or project README is technical orientation for the
  whole technical system or repository.
- A package README is technical orientation and contract for the package,
  whether it is internal or independently published.
- A folder or module README is technical orientation for the governed area.
- A public documentation home is navigation and orientation for readers already
  seeking documentation.
- A public website or product landing page is a separate presentation surface
  for browser visitors; it is not a README and is not implied by public source.

README is never an advertising landing page. Do not import landing-page section
order, persuasion goals, browser calls to action, or source-versus-browser
routing into a README. This does not ban verified technical commands,
installation instructions, or routes for the README's named reader. Public
access, root placement, a source host, and a license establish availability, not
the reader's task.

A document can host several technical modes when it is the authorized surface,
but its sections must remain scannable by role. Do not create a split just to
make the taxonomy tidy.

## Technical README roles

### Top-level repository or project README

Help a named technical reader orient in the whole repository or system. Do not
assume the reader is a prospective customer, a contributor, or an integrator;
derive the actual technical task from the request and verified context.

State only what that reader needs at top level:

1. What the project or system is for in technical terms, its scope, and important
   non-goals.
2. Its major components, boundaries, and any system-wide constraints that change
   a safe technical decision.
3. The technical audience or audiences served by the documented routes.
4. The verified route relevant to the task: using a published package, running
   the system, contributing, operating it, or finding deeper documentation.
5. Links to canonical package, domain, API, configuration, operation, and
   contribution material as applicable.

A source or package start belongs here only when it is the verified technical
task for the reader. It is an instruction, not a conversion call to action.
Do not add a generic source quickstart merely because source exists, and do not
turn this README into a product advertisement or a monorepo manual.

### Package README

Help an integrator or consumer use a bounded technical unit. Give its purpose,
supported contract, prerequisites, installation when verified and relevant,
smallest safe use, configuration, defaults, failures, compatibility boundaries,
and routes to deeper reference.

A published package can serve readers outside the repository without becoming a
landing page. It remains a technical contract. Keep marketing claims and
product-wide narrative outside it; keep exhaustive API detail with its canonical
reference owner.

### Folder, module, domain, and service README

Use the locality ladder's reader-context matrix. Explain responsibility,
ownership, boundary, interactions, and the technical route appropriate to that
scope. A folder-level reader may have a checkout; a package-level reader may not;
a service-level reader may need operational context. Do not borrow assumptions
from a broader or narrower rung.

## Public documentation homes

Help a reader who has already arrived to find documentation. Start with the
documentation subject, its available navigation, and a route to the relevant
tutorial, how-to, explanation, or reference. A public documentation home may be
browser-delivered, but that does not make it a product presentation page or
give it a conversion goal.

Validate that the reader can navigate to a relevant topic or locate an exact
fact from the stated entry. Keep product evaluation and browser-product actions
on a separately classified public website presentation page.

## Public website presentation pages

Use this route only for an actual public website or product page. Its browser
visitor may need a decision or verified web-native action, so it has a different
reader contract from every README.

Describe verified purpose, supported outcome, relevant limits, and the smallest
honest browser-native next step. Keep source secondary unless contribution or
self-hosting is a verified visitor task. If no browser action is verified, route
to neutral deeper material rather than inventing a call to action.

A public documentation home is not automatically a marketing page. Classify it
by whether its reader needs documentation navigation, technical reference, or a
product decision.

## Reader entry and scan path

Model the reader at the surface where they first encounter the documentation.
Assume only context genuinely available at that rung.

For a README, state the technical reader, task, and starting context before
giving a route. A repository checkout, package registry, command line, runtime,
credentials, or source access is available only when stated or verified. For a
public website presentation page, the primary route is browser-native. Do not
swap those contracts. For a public documentation home, the primary route is
documentation navigation or reference lookup, not a product conversion path.

Open every reader-facing surface with the governed subject's relevant purpose,
responsibility, outcome, contract, boundary, or rationale—not with the
artifact's label, placement, or production story.

A technical README opening should let its technical reader identify the governed
system or unit, scope, boundary, and the route that fits their task. A public
documentation home should let a documentation reader identify the subject and
next navigation route. A public website presentation opening may instead help a
browser visitor recognize a supported outcome and next action. This distinction
does not prescribe badges, a table of contents, visual position, or a fixed
section order.

Validate the primary reader path from its documented starting state. For a
README, validate its stated technical task rather than assuming installation or
a browser journey. For a public website presentation page, use a clean supported
browser entry with stated access. For a public documentation home, test the
documented navigation or reference path. For an internal technical surface, use
the documented repository state and repository-native tooling. Do not silently
depend on unstated caches, global tools, credentials, generated files, or
maintainer knowledge. State what remained untested.

## Progressive disclosure

Give enough context before each link to answer why it applies. Move detail only
to an existing or authorized surface. Otherwise disclose it progressively in the
current document through headings and local navigation.

Use a canonical-owner rule within the existing documentation topology. The
following modes may be sections in one README:

- Put exact defaults, type shapes, error details, and exhaustive option facts in reference.
- Put task-specific setup and procedure in how-tos.
- Put concepts and trade-offs in explanations.
- Put only a short contextual summary plus a link in other surfaces.

Delete repeated prose if a reader can still determine purpose, behavior, and
boundary. Add only the smallest missing explanation at the reader's present
level.

## Explain-before-code pattern

Use prose before a non-trivial example to state:

- the reader outcome;
- prerequisites and assumed surrounding context;
- why the selected API or option belongs in this example.

Use prose after it to state:

- expected result;
- meaningful limit, ownership boundary, or failure case;
- next useful page.

Do not narrate every line inside a runnable sample. Preserve comments only when
they carry a non-obvious rationale that remains true when the sample is copied
elsewhere.

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
- Technical README: can the named technical reader locate scope, boundary, and
  the route for their task without encountering marketing posture?
- Public documentation home: can a reader find the relevant topic or exact fact
  without a product-presentation detour?
- Public website presentation page: can a browser visitor find only a verified
  web-native path without source setup being made primary?

Flag a possible split when one page attempts to teach, prescribe, enumerate
facts, and justify architecture with no clear separation. Until the user accepts
restructuring, preserve the current files and improve separation with headings
and local navigation.
