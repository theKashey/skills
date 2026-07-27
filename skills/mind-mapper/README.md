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

## Choose the shape that matches the relationship

Linear plans, classic fishbone diagrams, and classic mind maps are optional,
composable views of the graph, not required methods or phases:

- Use a sequence when one bounded move truly requires or unlocks another.
- Use parallel contribution branches when distinct aspects can make independent
  gains toward the same outcome. A fishbone is one useful way to render them.
- Use associative links when history, evidence, constraints, or possible moves
  are connected but their direction or role is still uncertain. A mind map can
  connect those fragments without claiming dependency or contribution.

For example, reducing onboarding failures may have independent instruction,
account-access, and recovery branches. Within account access, locating the
failures may unlock choosing an explanation, which may unlock a bounded pilot.
Old support tickets, an abandoned experiment, and an unexplained metric spike
can remain associated fragments until evidence gives them a supported role.
All three shapes belong in the same graph.

## Principles and boundaries

- The map is a graph of accountable contribution, not a flat task list:
  prospective work needs a path back to the epic, while unrecoverable history
  remains an explicit gap rather than invented lineage.
- Choose a shape per relationship, not once for the whole problem. Label
  contribution, dependency, evidence, and association explicitly so proximity
  or an arrow does not manufacture order or causality.
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
  hypothesis. The skill reports the extension frontier separately from the
  dependency-free action frontier so readiness is not mistaken for priority.

Mind Mapper is not an OKR framework, goal system, or project-management
process. Its links organize an investigation; they do not prove causality,
priority, value, or implementation correctness.
