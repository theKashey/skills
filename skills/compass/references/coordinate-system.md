# Coordinate System: Addresses, Coordinates, and Validation

Implementation coordinates are the wiring between the semantic chart and today's code. They make the architecture navigable from a source file and a source file locatable from the architecture. They are the *replaceable* half of the model: coordinates change whenever the implementation moves, and that is normal operation, not damage.

## Addresses

An address names a place in the semantic chart. Names are unique within their parent:

```
Root names are unique within the chart   (one "webshop" in the compass)
Block names are unique within their root (one "order-core" in webshop)
Component names are unique within block  (one "billing-gateway" in order-core)
```

Address: dot-separated path from the root down:

```
webshop.order-core.billing-gateway
webshop.storefront.checkout
partner-portal.api-core.account-sync
```

Unambiguous without context. An agent or human reading `webshop.order-core.billing-gateway` anywhere knows exactly which place it refers to.

An address is a place, not a file. Two different files may sit at one address; one file may sit at addresses in two different roots. Neither fact is a defect.

---

## Coordinates

A coordinate connects code to an address via a comment:

```swift
// compass: webshop.order-core.billing-gateway
```

```typescript
// compass: checkout.payment.authorisation
```

**What a coordinate means:**

> The logic implemented here participates in this Compass location.

**What it does not mean:**

> This source file defines the semantic boundary.

Treat these comments like coordinates on a map. Coordinates may change while the place remains the same — a package move rewrites the coordinate and leaves the semantics untouched.

The `//` above is "a comment" — write the marker in the host language's own comment syntax (`# compass:` in Python, `-- compass:` in SQL). The marker body is always `compass: <address>`, so search for it without a comment prefix:

```
grep -r "compass: webshop.order-core"   # every file participating in the order core block
```

---

## Gravity

Coordinates want to bubble up. Annotate at the coarsest level that's still accurate:

```
Package level     // compass: webshop.order-core
  applies to everything below unless overridden

Folder level      // compass: webshop.order-core.billing-gateway
  overrides package for this subtree

File level        // compass: webshop.order-core.pricing-engine
  overrides folder for this specific file
```

Treat these as laws:
- Coordinates bubble up.
- Prefer one coordinate that accurately covers the whole subtree.
- Use file-level coordinates only when the file's address differs from the enclosing one.
- Folder/package coordinates are enough when everything in that subtree participates in the same place; exclude tests when they do not.

A folder needs no coordinate of its own when the enclosing one is still accurate for it; when it is not, the folder's files take the file-level exception.

### Coordinate density points; it does not sentence

Where coordinates refuse to bubble up, physical grouping and logical grouping disagree at that spot. That is real information and worth acting on — it is the cheapest standing signal the method produces, and it usually points toward decluttering:

| Observation | What it suggests looking at | Healthy outcome when it holds up |
|---|---|---|
| A folder's files carry three different coordinates | Whether one file is simply filed in the wrong place | Move the stray file to the subtree that shares its address — the coordinate then bubbles up on its own |
| A file carries two coordinates within one root | Whether it does two jobs, or bridges two places | Split a file that does two jobs; keep and name a genuine bridge |
| A file resists every enclosing coordinate | Whether it belongs to the floor | Recognize it as L5 and drop the coordinate |

Follow the lead, and prefer the move that makes the coordinate coarser **when the code is better for it**. Decluttering toward coarse attribution is a good default direction of travel.

What it must never become is a verdict or an obligation:

- The signal is a prior toward looking, not proof. Independent cohesion or coupling evidence decides — a module that changes for unrelated reasons, a boundary crossed on every change, a dependency cycle. Record that evidence, not the coordinate count, as the reason.
- None of these is by itself a defect. A semantic phenomenon may legitimately span frontend, API, workers, storage, several packages, and several services; one technical module may legitimately participate in several phenomena; two ratified roots may both claim the same file.
- `repository topology != semantic topology` is the normal condition of a real system, not a backlog. Compass maps that relationship. It never requires maintainers to reshape the implementation until it resembles the chart, and a non-uniform folder is not by itself a debt entry.
- **Do not manufacture a source boundary solely to make a coordinate coarse.** Coarse attribution is worth reaching for when it also improves the code, and worth nothing when it only tidies the marker.

The gate that keeps both halves honest: a density observation may open an investigation, and only cohesion or coupling evidence may close one as debt.

---

## Where a Folder-Level Coordinate Lives

Where the implementation already has a composition root — an entry point, a root router, a barrel that imports and re-exports a level's parts — that file is the natural carrier for the folder's coordinate, and the first file an agent reads on entering the level.

```swift
// compass: webshop.order-core
// Composition root for the order core block.

import BillingGateway
import PricingEngine
import InvoiceRepository
```

**Do not create one to satisfy Compass.** Where no such file exists, use folder or file coordinates; a missing composition root is an implementation style, not a chart finding.

---

## Multiple Coordinates

The same executable code may have several legitimate orientations:

```ts
// compass: commerce.checkout.payment
// compass: payments.authorisation.card-routing
```

Both may be true. There is no universal maximum; prefer the smallest useful set that keeps navigation honest.

**Multiple coordinates trigger verification, not refactoring.** The question to answer is:

> Are these genuinely independent logical orientations?

- **Across roots** (different first segments) — usually yes. Two ratified roots each have a valid claim on the same code; that is what multi-root overlap looks like in the source. Confirm both roots are registered in `COMPASS.md` and ratified; an unratified second root is an invented stack — remove it.
- **Within one root** (same first segment) — investigate. A boundary file, bridge, or anti-corruption layer legitimately participates in two places, and the honest answer is to keep both or attribute to the side that owns the contract. Two coordinates because nobody could decide is a signal to resolve the ambiguity in the chart, not an order to split the file.
- **Infrastructure** — if the code turns out to be L5, remove the coordinates entirely.

Other orientations can exist in documentation without appearing in code comments. The set of coordinates on a file is a navigation choice, not the analysis limit.

---

## Coordinate Validation (Remapping, Not Repair)

Coordinates are code. Validate:

- Does the address correspond to a real place in the chart?
- Does the file's location still match the coordinates recorded for that place?
- Has the place been renamed or removed since the comment was written?
- Are there files with no coordinate that should have one?
- Are there coordinates pointing to places that no longer exist?

**A failure here is a remapping problem by default.** A moved package, a renamed directory, or an extracted service makes coordinates stale; it does not make the semantic chart wrong. Update the coordinates and the block's `## Implementation coordinates` section, and leave L0–L2 identity alone unless the *logical* system changed — the classification in [`growth-and-drift.md`](growth-and-drift.md#classifying-disagreement) decides which case you are in.

The exception is an address that no longer exists in the chart at all: that is either a semantic change nobody recorded or a coordinate written against a place that was never ratified. Investigate rather than deleting the comment.

This is the sealing mechanism (Phase F of the growth pattern). Coordinates wire code to the chart; validation checks the wiring. But the wiring is only useful after semantic boundaries stabilize — premature sealing multiplies the cost of correcting a boundary that was wrong.
