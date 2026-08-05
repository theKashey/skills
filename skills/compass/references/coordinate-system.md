# Coordinate System: Addresses, Attribution, and Domain Controllers

The coordinate system gives every piece of code an address in the architecture — the wiring between documentation and codebase that makes the architecture navigable, not just describable.

## Addresses

Names are unique within their parent:

```
L1 names are globally unique        (one "webshop" in the compass)
L2 names are unique within their L1 (one "order-core" in webshop)
L3 names are unique within their L2 (one "billing-gateway" in order-core)
```

Address: dot-separated path from L1 down:

```
webshop.order-core.billing-gateway
webshop.storefront.checkout
partner-portal.api-core.account-sync
```

Unambiguous without context. An agent or human reading `webshop.order-core.billing-gateway` anywhere knows exactly what it refers to.

---

## Attribution

Attribution connects code to its address via a comment:

```swift
// compass: webshop.order-core.billing-gateway
```

```typescript
// compass: webshop.storefront.checkout
```

The `//` above is "a comment" — write the marker in the host language's own comment syntax (`# compass:` in Python, `-- compass:` in SQL). The marker body is always `compass: <address>`, so search for it without a comment prefix:

```
grep -r "compass: webshop.order-core"   # every file in the order core block
```

---

## Gravity

Attribution wants to bubble up. Annotate at the coarsest level that's still true:

```
Package level     // compass: webshop.order-core
  applies to everything below unless overridden

Folder level      // compass: webshop.order-core.billing-gateway
  overrides package for this subtree

File level        // compass: webshop.order-core.pricing-engine
  overrides folder for this specific file
```

Treat these as laws:
- Attribution bubbles up.
- Prefer one attribution that covers the whole subtree.
- Use file-level attribution only when the file is an imposter or when no sound folder/package attribution can be established.
- Folder/package attribution is enough when all files in that subtree belong to the same primitive; exclude tests when they do not belong to that primitive.

A folder or package attribution is carried by that level's domain controller (below). A folder with no controller has nowhere to host one: if the enclosing attribution is still accurate for it, the folder needs nothing; if it is not, the folder's files take the file-level exception.

Gravity is a refactoring signal:
- Folder with 3 different attributions → pressure to reorganize (structure ≠ architecture).
- Single file with 2 attributions → pressure to split (serves two masters).

Ideal state: every folder uniform, attribution at folder/package level, individual file annotations rare (boundary exceptions only). Gap between current and ideal = structural debt map.

---

## Domain Controllers

Each level wants a wiring point — a real code file that composes and re-exports, making the architecture visible in the code itself. Follows the Abstraction Layered Architecture (ALA) pattern.

**L1 controller:** Top-level file composing L2 blocks. The app's main entry point, root router, composition root. Shows which blocks exist and how they connect.

**L2 controller:** One per block, composing L3 components. The block's public interface. Imports components, wires dependencies, exports what the block offers.

**L3 controller:** One per component, composing internals. The component's entry point. Imports classes, functions, types.

Domain controllers:
- Contain no logic. If they gain conditionals, feature flags, or branching → the level is too complex.
- Are the first file an agent reads when entering a level.
- Carry the level's attribution:

```swift
// compass: webshop.order-core
// Domain controller for the order core block.

import BillingGateway
import PricingEngine
import InvoiceRepository
import OrderEvents
```

---

## Single Attribution Principle

Every file wants exactly one attribution per stack — the architectural equivalent of single responsibility.

When a file has two attributions from the same stack:

1. The file does two things → split it.
2. The file is a boundary file (bridge, adapter, ACL) → attribute to whichever side owns the contract.
3. The file is infrastructure → remove attribution (L5).

Two attributions from the same stack is a refactoring signal. It can persist for months — it doesn't demand immediate action — but it maintains the pressure.

---

## Dual-Stack Limit

A file carries at most two attribution comments from two **different** stacks.

- **Top stack:** widest scope, typically product-wide.
- **Scoped stack:** a human-created subproduct lens. Independent view, not a child of top.

```
// compass: acme-platform.payments.stripe-gateway
// compass: checkout-flow.payment-step.stripe-adapter
```

Dual-stack attribution is exceptional, not normal.
- Humans decide whether a second stack exists.
- Agents do not create parallel stacks; they only honor an existing lens.
- The second stack is valid only when it forms an objectively sound C4 construct — its L1 is complex enough to deserve its own stack.
- The usual shape is `product` + `subproduct` or `application` + `service`.
- A human-created lens is registered in the compass's lens tier: its L1 root gets a row naming the declaring human as Owner. A second root with no lens row is an invented stack — remove it.

The two stacks don't need to agree on naming, levels, or boundaries. The compass connects them.

**Distinguishing same-stack from cross-stack:** Check whether the two addresses share the same L1 root.
- Same root = same stack = refactoring signal (split the file).
- Different roots = different stacks = allowed only as the bounded human-decided exception above.

Other stacks can exist in documentation but don't get code comments. Two is the persistence limit, not the analysis limit.

---

## Attribution Validation (Anti-Drift)

Attribution comments are code. Validate:

- Does the address correspond to a real node in the docs?
- Does the file's directory match the expected code path for that node?
- Has the node been renamed or removed since the comment was written?
- Are there files with no attribution that should have one?
- Are there attributions pointing to nodes that no longer exist?

This is the sealing mechanism (Phase F of growth pattern). Attribution wires code to docs. Validation scripts check the wiring. But the wiring is only useful after architecture stabilizes — premature attribution locks in wrong boundaries.
