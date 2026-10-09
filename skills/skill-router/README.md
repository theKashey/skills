# Skill Router

Skill Router picks which skills fit a task, before work starts, and says when
none do. It reads every `SKILL.md` in the skill folders around the work
location, listed or parked outside the listing, builds an extended skill table,
ranks the table for one task brief, and hands the agent a short answer: read
this first, or choose from these few, or nothing fits. It runs on the Python
standard library, needs no key or network, and writes nothing.

## The problem

Agents choose skills from a listing of names and descriptions, and that
listing has a budget: a small, fixed share of the context window. When the
listing outgrows it, harnesses drop or shorten descriptions. Either way, once a project carries a
hundred or more skills, the words a skill needs to be picked are the first to
go. A skill nobody picks never builds the usage that would keep its
description.

Making descriptions longer does not fix this, and neither does making them
shorter. The rule that separates two similar skills is usually a pair of
lists — use me when, don't use me when — and that pair lives in the skill
body, where no listing reads it. Even with perfect descriptions, a long list of
options that all say "use me" makes the choice itself worse.

The way out is the one tool search took for MCP: keep most skills out of the
listing, for example in `.agents/available-skills`, and let a router bring back
only what this task needs. Skill Router is that router, and nothing more.

## Who it serves

- **The agent at task start.** It gets one clear pick, or two to five short
  cards to choose from, each with the reason it matched and the boundary that
  might rule it out, instead of scanning a hundred descriptions. The agent
  makes the final choice; the router only narrows it.
- **The team that owns the library.** They can park skills without deleting
  them, and can see whether a parked skill would still be found.
- **Anyone deciding whether routing works.** `eval` replays each skill's
  shipped trigger and non-trigger queries, so the answer is a number, not a
  demo. The queries only measure the router; routing never reads them. A skill
  found only through its own test queries would pass its eval and still be
  invisible to every task its author did not foresee.

## How it decides

1. **Where it looks.** The agent passes its work location. The router reads the
   `.<tool>/skills` and `.<tool>/available-skills` folders there and in every
   folder above it, up to the home folder, and the home folder's own; the
   nearest copy of a name wins. A monorepo keeps skills next to the packages
   they serve, so the work location, not the repository root, decides which
   ones apply. Folders below it are not read: a sibling package's skills would
   only add near-duplicates. A skill reached twice through symlinks is read
   once.
2. **Extended table.** For each skill: the use part and the "not for" part of
   the description, `Use when` and `Do not use` sections and lines from the
   body, and headings. Nothing else in the skill folder is read, so a file a
   harness or team happens to keep there cannot change a route. Skill files are
   never edited; the table is the router's private view.
3. **Lexical rank.** BM25 over the skill card: name, use-when, description,
   headings. Adjacent words in one clause also count as a pair, so "feature
   gate" separates two skills that share "feature" and "gate" only apart.
   Identifiers such as `featureGate` or `parseJSON` count as the whole word and
   as its parts, so a task that names a code symbol meets prose that describes
   it.
4. **Boundaries.** Words shared with a skill's don't-use lines count against
   it; the matching line is shown as `mind the boundary`. The skill is set
   aside when that evidence reaches 60% of its use evidence, or when the match
   is too thin to route on. A match is too thin when it rests only on generic
   words, on words found on more than 35% of the library's skill cards
   (and on more than five), or on one distinctive word. In a library of
   a hundred skills, almost any short task shares one word with some skill.
   A task that repeats one "not for" phrase can
   still route to that skill if the rest of the task fits it; the boundary
   line is there so the agent can catch that.
5. **One pick or a short list.** One skill that scores at least twice the next
   one, with no boundary hit, is the pick. Otherwise the agent gets cards:
   what each skill is about, why it matched, and the description's own
   "not for" line when no boundary line matched. That is the usual case;
   word matching rarely separates the owner from its near neighbours, and the
   agent reading a few short cards does. The list is sized by how close the
   scores are: every card scoring at least 60% of the top, at least two, at most
   five. A clear leader comes with one neighbour; a flat field shows more. A
   skill too thin to route on, resting on one distinctive word, may take a
   remaining card after every better-supported one: the agent is choosing
   anyway, and one word is enough to be worth a look but not a pick. The cards
   never include skills set aside by a boundary.
6. **Abstain.** With no candidate left, the verdict is `ABSTAIN`. "No skill
   needed" is a result, not a failure.
7. **Optional second stage.** Any local command can reorder the candidates
   when the lexical stage lacks one clear pick. It sees each candidate's
   use-when and don't-use lines. Its order replaces the lexical score but not
   the boundaries. A failure or timeout falls back to the lexical result.

## Where it is strong and where it is not

Lexical routing works when the task and the skill share words, which is the
usual case when a task names a product, a tool, or an artifact and a skill is
about that thing. On a 102-skill product monorepo library that ships 2,245
trigger and non-trigger queries, routed on the skill files alone, the owning
skill came first for 54% of trigger queries, was among the cards for 75%, and
was kept off them for 78% of non-trigger queries, with 2.7 cards per query on
average. Almost every query ends as a short list; a clear single pick is rare.
Changing the weights moves those numbers by under a point; word matching has
reached its limit there. A third of the misses already show five cards without
the owner: its own files do not use the words its tasks use. Most of the
rest are pairs of skills whose descriptions overlap; `eval -v` lists them as
collisions, which tells the library owner which descriptions to separate. Short
trivial tasks are the remaining weak spot at that size: half or more still
reach some skill on one or two shared words.

Process skills are the hard case. Their triggers describe a
situation, such as "inherited work spanning several moves", while real tasks
describe events, such as "picking up Dana's investigation". Word matching
cannot see that link. On carry-the-load and helix, with the whole repository
loaded, the owning skill came first for 3 of 18 positive queries, was listed
for 5, and was kept out for 19 of 20 non-trigger queries
(`eval --skills skills -v`).

That gap is what the second stage is for. A separate experiment with two small
local models found that neither beat BM25 when asked to choose the owner from a
list. One model did help when asked about each candidate on its own, and its
mistakes were not BM25's mistakes. The rerank contract asks for that shape.

## Boundaries

- It routes. It does not plan the task, review the work, enforce that a skill
  was loaded, follow sub-agents, or learn from past sessions. Those choices
  belong to the harness or the team, not to a lookup.
- It is stateless. Every call reads the library afresh and remembers nothing.
  A router that remembers starts to author the library nobody agreed to. The
  agent says which skills it has already seen (`--seen`), and those come back
  as a name and the lines about this task. They are still ranked, not dropped:
  dropping a skill the agent knows hands its tasks to the next-closest skill,
  which then reads as the pick. Because the agent restates what it has seen on
  every call, a compacted context cannot leave the router out of date.
- It does not write, move, or delete skills. Deciding which skills to park is
  the library owner's decision.
- It does not ship a model. The second stage is a contract, so a team can plug
  in whatever runs locally for them.

## Tradeoffs

- **Parked skills lose their slash command.** A skill outside the listing
  cannot be invoked by name, and it is found only when the agent asks.
  Skill Router itself stays in the listing, and its description asks for a
  lookup at task start.
- **No enrichment pass.** The table uses only what the skill author wrote.
  Some routers have a model write extra keywords for each skill; that would
  need a model at build time, and the keywords would go stale. A skill that
  routes badly here needs better use-when lines, and that fix also helps every
  other harness.
- **No routing on test queries.** Matching a task against a skill's shipped
  trigger queries finds more owners, but it rewards a skill for its test set
  rather than its own words, reads files whose format each harness defines
  differently, and makes `eval` grade the router on its own answer key.
- **Rebuild on every call.** A call over about 100 skills takes about 80 ms on
  a laptop with warm disk caches, about 30 ms of it Python start-up. Starting
  from a package inside a large monorepo, with the home folder, that is about
  140 skills in about 100 ms. A cache could save only the reading and
  indexing, so it would add a stale-state bug for a few tens of milliseconds.
- **Fixed weights.** The field weights and thresholds were tuned on one
  product library of about 100 skills and checked on a small one. `eval` exists so a
  team can check them against its own library before trusting them.

## Rejected shortcuts

- **A hosted model for every prompt.** It is accurate enough, but it needs
  credentials many developers cannot share, and each call takes seconds.
- **Full-text search alone.** It is fast and deterministic, but it cannot
  express "don't use me for this", and that is the rule that separates
  near-identical skills.
- **Expanding the task with the top skills' words.** Feeding the first
  results' distinctive words back into the query amplifies the first guess: the
  owner was listed for 11 points fewer trigger queries.
- **Hard enforcement.** Blocking edits until a routed skill loads produces
  workarounds when the route is wrong. Being wrong on a recommendation costs
  one line.
