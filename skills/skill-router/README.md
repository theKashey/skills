# Skill Router

Skill Router picks which skills fit a task, before work starts, and says when
none match. It reads every `SKILL.md` in the skill folders around the work
location, listed or parked outside the listing, builds an extended skill table,
ranks the table for one task brief, and hands the agent a short answer: read
this first, or choose from these few, or nothing matches. It runs on the Python
standard library, needs no key or network, and writes nothing.

## The problem

Agents choose skills from a listing of names and descriptions, and that
listing has a budget: a small, fixed share of the context window. When the
listing outgrows it, harnesses drop or shorten descriptions. Either way, once a project carries a
hundred or more skills, the words a skill needs to be picked are the first to
go. A skill nobody picks never builds the usage that would keep its
description.

Making descriptions longer does not fix this, and neither does making them
shorter. The rule that separates two similar skills is usually in the
description itself: what the skill does, when it applies, and what it is not
for. Those are the words a shortened listing cuts first, and the router reads
them in full. A boundary that takes more cases than a description can hold
moves into the body as a pair of lists — use me when, don't use me when —
where no listing reads it. Even with perfect descriptions, a long list of
options that all say "use me" makes the choice itself worse.

The way out is the one tool search took for MCP: keep most skills out of the
listing, for example in `.agents/available-skills`, and let a router bring back
only what this task needs. Skill Router is that router, and nothing more.

## Who it serves

- **The agent at task start.** It gets one clear pick, or up to eight short
  cards to choose from, each with what the skill is for, the line of its text
  that matched the task, and the boundary that might rule it out, instead of
  scanning a hundred descriptions. The agent
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
   body, headings, and the rest of the body text, including tables and code,
   without its don't-use lines and sections. Nothing else in the skill folder
   is read, so a file a harness or team happens to keep there cannot change a
   route. Skill files are never edited; the table is the router's private
   view, and `table --format json` prints all of it but the body text.
3. **Lexical rank.** BM25 over the skill card: name, use-when, description,
   headings. The rest of the body is a second, lower-weighted document with its
   own word rarity: authors put the commands, file names, and package names a
   task mentions there, not in the card. A body word found in more than a
   fifth of the library's bodies (and in more than five) does not count as
   evidence. Adjacent words in one clause also count as a pair, so "feature
   gate" separates two skills that share "feature" and "gate" only apart.
   Identifiers such as `featureGate` or `parseJSON` count as the whole word and
   as its parts, so a task that names a code symbol meets prose that describes
   it. Each part is a word of its own in every rule below, so one identifier
   can be more than one distinctive word.
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
   the start of each skill's description, a matched use-when line when it
   adds something, the body line that best matches the task's distinctive
   words, short lines favoured (`matched:`), when one shares at least two, and
   one boundary line, either the matched don't-use line or the description's
   own "not for" part. That is the usual case; word
   matching rarely separates the owner from its near neighbours, and the agent
   reading short cards does. Cards are kept short so the list can be wide:
   at about the same cost, a deciding model found the owner more often in
   more, shorter cards than in fewer, fuller ones. The list is sized by how
   close the scores are: every card scoring at least half the top, at least
   two when two remain, at most eight. A clear leader comes with one
   neighbour; a flat field shows more. A skill too thin to route on, resting
   on one distinctive word, may take a remaining card after every
   better-supported one: the agent is choosing anyway, and one word is enough
   to be worth a look but not a pick. The cards never include skills set aside
   by a boundary.
6. **Abstain.** With no candidate left, the verdict is `ABSTAIN`. A task can
   need no skill, and saying so is a result, not a failure. `ABSTAIN` means
   that no skill shares enough words with the brief, not that no skill could
   apply: a process skill whose triggers describe the situation in other words
   abstains too, and an agent that already knows such a skill should still use
   it.
7. **The agent decides; a second stage is optional.** The calling agent
   reading the cards is the judge for a `CHOOSE` list. A team can also plug in
   any local command to reorder the candidates when the lexical stage lacks
   one clear pick. It sees each candidate's use-when and don't-use lines. Its
   order replaces the lexical score but not the boundaries. A failure or
   timeout falls back to the lexical result.

## Where it is strong and where it is not

Lexical routing works when the task and the skill share words, which is the
usual case when a task names a product, a tool, or an artifact and a skill is
about that thing. On a separate, much larger library of product skills,
routed on the skill files alone, scoring the body as well as the card puts the owner first and on the
cards more often than the card alone: the body finds owners whose tasks use words
the card lacks, and also lists the near-miss skill more often. Almost every
query ends as a short list; a clear single pick is rare. When the owner is
missing from the cards, the list usually already holds several skills without
it. Most of those are pairs of skills whose texts overlap; `eval -v` lists
them as collisions, which tells the library owner which skills to separate,
merge, or split. The body also makes the router abstain less often, so a large
library rarely says "nothing matches" to a task written for it.

Process skills are the hard case. Their triggers describe a
situation, such as "inherited work spanning several moves", while real tasks
describe events, such as "picking up Dana's investigation". Word matching
cannot see that link. On carry-the-load and helix, in a small library of 11
general-purpose skills, the owning skill came first for 5 of 18 positive
queries, was listed for 11, and was kept out for 17 of 20 non-trigger queries
(`eval --skills <library> -v`); the card alone gave 3, 5, and 19.

Those numbers grade the list, not the choice made from it. On the larger
library, a capable but fast model (Claude Haiku) chose from the cards, with
only the decision rules in `SKILL.md`. It put the owner first and loaded it
about as often as the same model reading the whole catalog of descriptions,
and kept the near-miss skill out about as often. It loaded a wrong extra skill
less often than from the catalog, for a small fraction of the catalog's
tokens. Choosing from cards scored on the card alone found and loaded the
owner less often, though it kept the near-miss skill out slightly more often:
the body text is what closes the gap. On the 11-skill library the owner came first for 73%
of trigger queries against 48% from card-only scoring, with the near-miss
skill kept out for every non-trigger query in both; there, a model reading all
11 descriptions still does better, because process skills rarely reach the
cards.

How often does routing need meaning rather than words? On the larger library,
BM25 alone settles some trigger queries. Most have the owner among the top ten
candidates, but not clearly first: that is judgment among a few cards, which
the agent supplies. A few have the owner outside the top ten, where only
reading meaning would find it; in the 11-skill library, the same gap shows up
as process skills whose tasks share no scoring word with them at all.

The agent can close part of that gap before routing, the way a model writes a
query for a tool search: the task in a few words, then synonyms and the other
names the same thing goes by, from its own vocabulary, without seeing any
skill. A fast model (Claude Haiku) wrote such queries for a sample of the
larger library's trigger queries. Against the raw task, the owner moved into first
place, and onto the cards, more often than it moved out, with slightly fewer
cards and near-miss listings. A one- to three-sentence prose brief did no
better: it sometimes put the owner first less often, with more cards and more
near-miss listings, because whole sentences add words that score for
neighbours. These findings grade the list only; the choice from cards built on
expanded queries, and the 11-skill library, were not measured.

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
- It does not ship a model. The calling agent decides among the cards. The
  optional second stage is a contract, so a team can plug
  in whatever runs locally for them.

## Tradeoffs

- **Parked skills lose their slash command.** A skill outside the listing
  cannot be invoked by name, and it is found only when the agent asks.
  Skill Router itself stays in the listing, and its description asks for a
  lookup at task start.
- **No enrichment pass.** The table uses only what the skill author wrote.
  Some routers have a model write extra keywords for each skill; that would
  need a model at build time, and the keywords would go stale. A skill that
  routes badly here needs a sharper statement, in its description, of what it
  does or when it applies, and that fix also helps every other harness. When
  its boundary does not fit in a description, the rest goes into `Use when`
  and `Do not use` lists at the top of the body, under their own headings or
  label lines. Adding to each card a few words that its own tasks use, and
  the card lacked, moved the owner first a little more often. It also let the
  skill reach a few more non-trigger queries, so the words have to describe
  the work, not just repeat the tasks.
- **A wider list.** `CHOOSE` lists up to eight short cards rather than five
  full ones, so the owner is on the list more often. The near-miss skill is
  listed more often too; that is safe only because the agent, not the list,
  decides what to load.
- **No routing on test queries.** Matching a task against a skill's shipped
  trigger queries finds more owners, but it rewards a skill for its test set
  rather than its own words, reads files whose format each harness defines
  differently, and makes `eval` grade the router on its own answer key.
- **Body text widens the net.** Reading the whole body finds owners the card
  misses, and lists the near-miss skill more often: fewer non-trigger queries
  are kept off the cards. The `matched:` line lets the agent
  see that a skill only names the same thing, and in the check above the
  agent kept the near-miss skill out about as often as it did from a whole
  catalog. A library whose bodies repeat each other's commands and file
  names pays more for this.
- **Rebuild on every call.** A call over about a hundred skills takes a
  fraction of a second on a laptop with warm disk caches, and reading and
  tokenizing the bodies is most of it. A cache could save only that, so it
  would add a stale-state bug for little saving.
- **Fixed weights.** The field weights, the body weight, and the thresholds
  were tuned on one larger library and checked on a small one. `eval` exists
  so a team can check them against its own library before trusting them.

## Rejected shortcuts

- **A hosted model for every prompt.** It is accurate enough, but it needs
  credentials many developers cannot share, and each call takes seconds.
- **Full-text search alone.** It is fast and deterministic, but it cannot
  express "don't use me for this", and that is the rule that separates
  near-identical skills.
- **Embeddings.** A small sentence-embedding model found the owner less often
  than BM25. Mixed with BM25, it added a little to the top-ten list,
  at the cost of a large machine-learning dependency. Its similarity score was
  the same for tasks that need a skill and tasks that only share its topic, so
  it cannot make the choice either.
- **A small local model as the judge.** Asked to choose from the cards, a 4B
  base model almost never answered none, and a 4B instruction-tuned one
  answered none but picked the owner no better than BM25. Having a model
  rewrite the task into skill-description words did not help on the larger
  library.
- **Expanding the task with the top skills' words.** Feeding the first
  results' distinctive words back into the query amplifies the first guess: the
  owner was listed for fewer trigger queries.
- **Hard enforcement.** Blocking edits until a routed skill loads produces
  workarounds when the route is wrong. Being wrong on a recommendation costs
  one line.
