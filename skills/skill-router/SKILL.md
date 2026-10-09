---
name: skill-router
description: Picks which local skills fit a task, listed or parked, or abstains, with an offline router. Use at task start and on each new surface when a project has many or parked skills; not for writing, editing, or auditing skills.
---

# Skill Router

Ask the library which skills this task needs before work starts. The router
reads every `SKILL.md` around the work location, ranks them for one task brief,
and returns one clear pick, a short list to choose from, or `ABSTAIN`.
It runs locally with the Python standard library, needs no key or network, and
writes nothing.

## Locate the library

Pass `--from <file or folder you are working in>`. The router collects every
`.<tool>/skills` and `.<tool>/available-skills` folder (`.agents`, `.claude`,
`.cursor`, and so on) in that folder and each folder above it, up to the home
folder, and the home folder's own. When two folders hold the same skill name,
the one nearest the work location wins. Folders below the work location are not
read, so start from the package you are changing, not the repository root.

Add `--skills <dir>` for a library outside that path, such as one the user or
project configured; it is searched first, and `--skills` alone skips discovery.
Skills inside nested folders are found too.

## Route one task

1. Write a one- to three-sentence brief: the change, the surfaces it touches,
   and any named product, tool, or file. The user's raw message is often too
   short or too chatty to route.
2. Run the router; it prints absolute `load:` paths:

   ```bash
   python3 <this-skill-dir>/scripts/skill_router.py route --from <work location> "<brief>"
   ```

   If it exits with `no SKILL.md found`, no library was found there or a
   `--skills` path is wrong; report that instead of treating it as `ABSTAIN`.

   Add `--json` when another tool consumes the result.
3. Act on the verdict:
   - `ROUTE`: read the `read first` skill's `SKILL.md` at its `load:` path and
     follow it. Read an `also relevant` skill only when its `because:` line
     applies to this task. Treat every `mind the boundary:` line as a reason
     that skill may not fit.
   - `CHOOSE`: no skill clearly leads. The closer the scores, the more cards
     (two to five). Read the cards (what each skill is
     about, why it matched, the boundary that may rule it out) and decide: load
     one, several, or none. Load a skill only when its card describes this
     task; a listed card is a candidate, not a recommendation.
   - `ABSTAIN`: proceed without a library skill. Small work stays small.
   - `set aside`: do not load these. The line says why: its don't-use boundary
     matched, only generic words matched, or it scored well behind the first
     pick or did not fit in the list.
4. Route again when the work reaches a new surface: a new module, owner,
   product, or risk. The router keeps no memory between calls, so pass
   `--seen name,name` with the skills whose cards or `SKILL.md` are already in
   your context. They are still ranked, so their place in the answer stays
   true, but the router prints only their name, score, and the lines about this
   task. Leave out any skill whose card you no longer have, for example after
   context compaction.

The answer is a recommendation, not a gate. If a loaded skill turns out not to
apply, drop it and say so; do not stretch the task to fit the skill.

## Inspect or measure

- `python3 <this-skill-dir>/scripts/skill_router.py table --from <work location>` prints the
  extended skill table: use-when and don't-use lines pulled from each
  description and body. Routing reads nothing else.
- `python3 <this-skill-dir>/scripts/skill_router.py eval --from <work location> -v` replays every
  skill's shipped `evals/eval_queries.jsonl` against the router. The queries
  only measure routing; they never steer it. The output lists the skill pairs
  that take each other's queries, then every miss.

## Add a second stage

The lexical stage matches shared words. It is reliable when a task names the
skill's domain, such as a product, tool, or file type. It is weak for process
skills whose triggers describe a situation. To add a local model or any other
scorer, pass `--rerank "<command>"` or set `SKILL_ROUTER_RERANK`. Read
[the rerank contract](references/rerank-contract.md) before writing or wiring
that command.
