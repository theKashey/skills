# Documentation locality ladder

Use this reference to decide where documentation belongs and which context it
may assume.

- [Placement rule](#placement-rule)
- [Line-level comment](#1-line-level-comment)
- [Block-level comment](#2-block-level-comment)
- [File-level comment](#3-file-level-comment)
- [Folder-level documentation](#4-folder-level-documentation)
- [Package- or module-level documentation](#5-package--or-module-level-documentation)
- [Domain- or service-level documentation](#6-domain--or-service-level-documentation)
- [Top-level documentation](#7-top-level-documentation)
- [Movement tests](#movement-tests)

Locality answers **where a fact belongs**. Diátaxis answers **which reader
question it serves**. JSDoc or TSDoc extraction answers **which symbol
semantics must remain visible outside the implementation**. Do not treat
content mode or extractability as another locality rung.

## Placement rule

1. Identify the fact and every decision, task, or boundary it governs.
2. Choose the lowest rung whose surface is encountered by all affected readers.
3. If the fact governs sibling units, move it to their shared parent rung.
4. Keep the detailed fact in one canonical place. Higher rungs orient and link;
   lower rungs contain only the local consequence they must expose.
5. Choose by governed scope and reader role, not by filename alone. A
   `README.md` can be a folder note, an internal package manual, or a top-level
   landing page.
6. Do not create a missing surface without authorization. Report the placement
   gap and propose the smallest useful surface.

## 1. Line-level comment

**Governs:** one expression, argument, branch, return, or assignment.

Preserve the non-local constraint, rejected alternative, or consequence needed
at that exact decision. Omit mechanics already visible in the line. Move up
when the reason governs more than that decision.

## 2. Block-level comment

**Governs:** one contiguous guard, transformation, sequence, or algorithmic
block.

Explain an invariant across statements: ordering, atomicity, intentional
duplication, synchronization, or an unusual algorithm. Do not narrate the
statements. Move up when the invariant governs multiple blocks.

## 3. File-level comment

**Governs:** the file as a cohesive implementation unit.

Explain the file's responsibility, boundary, lifecycle, or non-obvious
relationship to another subsystem when declarations and imports cannot reveal
it reliably. Do not provide a declaration tour. Move up when the explanation
applies to sibling files.

## 4. Folder-level documentation

**Governs:** a coherent directory, subsystem slice, or implementation area.

Use the existing folder README or nearest authorized overview to explain why
the area exists, what it owns, how its parts are organized, shared conventions,
its boundary with sibling areas, and the local validation path. This is
technical documentation for people working in the repository; it may assume a
checkout when that is the real reader context. Do not turn it into a project
landing page.

## 5. Package- or module-level documentation

**Governs:** an independently imported, versioned, built, or reused unit.

For an internal package or module, explain its role in the containing system,
owned contract, entry points, dependencies, configuration, lifecycle, failure
behavior, and how other internal units use it. It is a technical document, not
an advertisement for the whole project.

When the unit is independently published, the same README may have two roles:
a short landing path for external consumers followed by the technical package
contract. Keep those roles distinguishable instead of applying either posture
to the entire document.

## 6. Domain- or service-level documentation

**Governs:** a business capability, deployable service, or collaboration among
multiple packages and modules.

Explain responsibility and ownership, boundaries, major flows, external and
internal contracts, dependencies, state and lifecycle, failure modes,
operational entry points, and where deeper technical detail lives. Do not
duplicate file or package mechanics.

## 7. Top-level documentation

**Governs:** the whole project, product, public documentation site, or
repository.

For an open-source project or public site, treat the top-level README or home
page as a landing page for outsiders. Make the verifiable case for relevance:
the problem, intended audience, supported outcome, meaningful distinction,
scope and non-goals, installation or first success, and routes to deeper
material. Advertise through demonstrated usefulness and evidence, not hype.

For an internal-only project, the same rung orients a newcomer to the whole
system rather than selling it publicly. In either case, keep internal package
mechanics below this rung and link to their canonical owners.

## Movement tests

- **Scope:** Does this fact govern a wider or narrower unit than its surface?
- **Visibility:** Will every affected reader naturally encounter this surface?
- **Role:** Is this a landing surface, technical boundary document, extracted
  contract, or local rationale?
- **Duplication:** Is repeated lower-level prose evidence that the fact belongs
  at their shared parent?
- **Deletion:** Can a higher-level repetition become a short orientation or
  link without losing safety or findability?
