# Mind Mapper

Mind Mapper keeps one durable planning map that links an outcome to the work
that might move it, the result of that work, and the one decision that follows.
It exists for inherited or uncertain work where tickets and commit history show
activity but not why a move matters or what evidence should change course.

The map deliberately keeps implementation detail last. It starts with the
outcome, proof, boundary, contribution branches, and a bounded move; code is
inspected only after those choices make an implementation question worth asking.
This is a planning stance, not an architecture framework or a ban on technical
investigation.

## What it preserves

- A move must link to a branch and outcome, or remain an explicit orphan rather
  than acquiring invented lineage.
- A result is appended beside its original readback. It can disconfirm a move
  without erasing the history that made the next decision understandable.
- A retry is a new move, not a rewritten old one. This prevents repeated work
  from looking like a new experiment.
- The map carries one selected next move or block, not a second task queue.

## Persistence and boundary

Mind Mapper requires an explicitly configured durable planning surface. The
configuration names its reference, its representation of the map semantics, and
the available read/write authority. It may use a local artifact, shared system,
or network integration; the skill does not choose among them or offer a default.
Without configuration, it asks the user to configure the map surface instead of
storing state in a transcript.

Mind Mapper does not prove an outcome is valuable, a branch is causal, or an
implementation is correct. It does not select or mutate a local file, ticket,
project-management service, or network integration without configuration and
authority, and it does not replace a routine task with a planning ritual.
