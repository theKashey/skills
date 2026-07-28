# Mind Mapper

Mind Mapper gives agents one living planning graph that connects an outcome to
its contributing indicators, hypotheses, bounded moves, observed results, and
unresolved relationships. It exists because commit histories, tickets, and
specifications often flatten work into a list even when the real problem
contains dependencies, independent contribution paths, and fragments whose
connection is not yet known.

Its goal is to keep planning, inherited history, and readback in the same
evidence-bearing graph. That gives an agent a durable way to preserve
uncertainty, trace each prospective action back to an outcome, and choose the
smallest consequential extension before implementation details narrow the
problem.

## Work from context to action

Mind Mapper uses a scale ladder to keep different planning problems from
collapsing into one task tree:

- A product or body of work is a mind map of jobs, outcomes, evidence,
  constraints, history, and unresolved cross-cutting relationships.
- A job is a fishbone: several distinct directions may progress in parallel,
  but all directions named by its completion contract are required.
- A unit of work is linear only where one step or move truly requires or
  unlocks another.

An agent descends this ladder to make a broad problem actionable and ascends it
when a task has lost its reason or a job has lost product context. The ladder
selects the working view; labeled edges still distinguish contribution,
dependency, evidence, and association so layout cannot manufacture order or
causality.

## Principles and boundaries

- The map is a graph of accountable contribution, not a flat task list:
  prospective work needs a path back to the epic, while unrecoverable history
  remains an explicit gap rather than invented lineage.
- Keep the product, job, and unit levels distinct while labeling contribution,
  dependency, evidence, and association explicitly.
- Outward planning and inward reconstruction describe the same graph. Results
  update hypotheses and frontiers instead of becoming a separate experiment or
  status narrative.
- The code gate keeps the **what** and **why** ahead of the **how**. Before it
  opens, define the outcome, evidence, contribution paths, and bounded moves
  without letting code, tools, or architecture narrow the problem prematurely.
  Opening the gate means that reasoning is ready to guide implementation
  inspection for one selected move, within the scope the user already
  authorized; it does not create permission to inspect or change a repository.
- A frozen readback makes a move informative even when it disconfirms the
  hypothesis. The map owns its extension frontier, but derives the selected
  next move from current evidence and work state instead of becoming another
  task queue.

Mind Mapper is not an OKR framework, goal system, or project-management
process. Its links organize an investigation; they do not prove causality,
priority, value, or implementation correctness.
