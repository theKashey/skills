# Lean development

This reference expands the compact doctrine statement in the package README
("Lean governs flow"). The README statement is the binding definition; this file explains why the discipline works and how it maps to
AI-assisted software development. It is maintainer and reader support, never a
runtime dependency: the runtime rules derived from it already live in
[SKILL.md](../SKILL.md).

## What it is

Lean is the Toyota-derived production discipline, generalized by Womack and
Jones into five commitments — specify value from the recipient's side, map the
value stream, make value flow, let demand pull the work, pursue perfection —
and carried into software by the Poppendiecks: eliminate waste, amplify
learning, decide as late as responsibility allows, deliver fast, empower the
team, build quality in, and optimize the whole system rather than one
station.

Its central objects are:

- **Value** — an effect the recipient can observe, defined by them, not by the
  producer's effort.
- **Value stream** — every step between request and delivered, verified value,
  including the waits between steps.
- **Flow** — value moving through that stream without piling up between
  stations.
- **Pull** — a station takes on work only when the downstream station can
  absorb its output.
- **Quality at the source** — the station that can first observe a defect
  stops and fixes it there, instead of shipping it to inspection.
- **Kaizen** — each cycle improves the stream itself, not just its output.

## Why it works

- **Small batches shorten feedback.** The cost of a defect grows with the time
  between creating and detecting it, because the producing context decays and
  later changes stack on top of the flaw. A small batch reaches verification
  while its cause is still legible.
- **Bounded work-in-progress bounds lead time.** By Little's law, average lead
  time is work-in-progress divided by throughput. Every additional open,
  unverified piece of work delays all of them and multiplies the states a
  failure could have come from.
- **Pull prevents inventory.** Work produced ahead of downstream capacity is
  inventory: it decays, hides defects, and demands storage and re-orientation.
  Producing only what the next verification step can absorb keeps every
  artifact fresh when it is judged.
- **Stopping at the source is cheaper than inspecting at the end.** The
  context that produced a defect is the cheapest place to understand it; a
  defect found at final inspection must be re-diagnosed from scratch.
- **Improving the stream compounds.** Fixing one output helps once; removing
  the queue or defect source that produced it helps every later cycle.

## How it maps to AI-assisted software development

The unit of flow is a **verified engineering increment** — not a token, a
file, a model response, or a merged diff. That translation drives everything
else:

- **Generation is not the constraint; verification is.** A model produces
  candidate changes faster than any reviewer, test suite, or deploy pipeline
  can absorb them. Optimizing generation volume therefore manufactures
  inventory: unverified diffs, open branches, and unread output piling up in
  front of the real bottleneck. Lead time to a *verified* outcome is the
  measure that resists this.
- **Unverified work is inventory with a decay rate.** An unreviewed diff loses
  value as the branch drifts and as the context that produced it is evicted or
  summarized away. Agent work decays faster than human work because the
  producing context is routinely discarded.
- **One increment in flight per context is the working WIP limit.** Several
  concurrent edits in one context confound the readback: when verification
  fails, the failure could belong to any of them. The limit is per executing
  context, not a ban on a second context working a separately bounded problem.
- **Context is capacity, so pull applies to it.** Loading files, tools, and
  abstractions in advance fills a bounded attention budget with material the
  current constraint never demanded. Pull context when the increment needs it.
- **Quality at the source means the earliest owner runs the check.** A type, a
  test, or a lint rule at the point of change beats a final review pass, and
  an executed observation beats a prediction of one.
- **Kaizen is the learning harvest.** A cycle that only ships output leaves
  the next cycle equally likely to fail; a cycle that moves a learned
  constraint into code, a gate, or the narrowest instruction owner improves
  the stream.

## What Lean is not

Lean is not thinness, minimal token use, or deleted code; the README records
the *berezhlivoe proizvodstvo* reading — careful stewardship of value,
capacity, attention, and material. Nor is Lean a diagnosis discipline: it
governs flow once an outcome is selected, and choosing the outcome or finding
an unknown cause is outside this skill's activation boundary.
