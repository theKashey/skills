# Screaming Reefs

Screaming Reefs makes codebases reveal the constraints that matter. It turns a
verified documented reef into locally visible terrain—names, types, APIs,
ownership boundaries, or filesystem topology—so humans and coding agents can
act safely without reconstructing remote context.

## Why it exists

Important constraints often survive only because a comment, README, or agent
instruction explains them. That prose protects the decision, but it can be
missed in selective context, duplicated away from its owner, or allowed to
drift as the repository changes. Screaming Reefs treats the explanation as
evidence for making the constraint visible where the decision is made.

The fence comes first. The verified constraint and its consequence remain
protected while the repository is reshaped. Explanatory prose is removed only
when code, types, APIs, boundaries, or topology carry the same meaning. A reef
whose significance is irreducibly non-local remains documented.

## Technical role

Screaming Reefs owns explicitly authorized repository context refactoring. Its
subject is the relationship between a documented constraint and the structure
that should expose it. The intended result is not prettier code or fewer
comments; it is a safer local decision surface with an observable, bounded
change in the repository.

Typical visible owners include:

| Constraint becomes visible as | When it is the right owner |
| --- | --- |
| Domain names and vocabulary | Readers need to recognize a concept or responsibility. |
| Types, states, invariants, or constructors | An invalid state or unsafe transition should be constrained by the model. |
| APIs, exports, routes, or capability boundaries | Callers need a contract that cannot be recovered from a warning. |
| Module, package, or ownership boundaries | Responsibility must be local instead of inferred from organizational memory. |
| Filesystem topology | Discovery or selective context depends on where the truth lives. |

The smallest stable owner wins. Broad architecture changes, unrelated cleanup,
and comment deletion without structural equivalence are outside the capability.

## Relationship to Documentory

Documentory preserves hidden reasons that the current code cannot express.
Screaming Reefs uses those verified explanations as evidence for an explicitly
authorized code or repository change. Documentory may identify a clarity
opportunity, but it does not independently authorize mutation. Screaming Reefs
owns that transformation; after it, only the irreducibly non-local reef stays
with documentation.

The packages are independent. Screaming Reefs carries the fence-first and
evidence-first rules needed to act safely on its own, whether or not the
companion documentation capability is present.

## Boundaries

Screaming Reefs does not invent a reason for an unexplained fence, decide a
product or ownership policy, silently widen the mutation scope, or claim that
local structure proves behavior. It preserves existing meaning by default and
stops when authority, evidence, contract compatibility, or local readback is
unresolved.

The finished repository should let the affected reader answer the constrained
decision from the relevant local context, while any remaining non-local reason
is still available at its canonical documentation surface.
