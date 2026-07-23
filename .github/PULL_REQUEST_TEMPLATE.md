## Why

Which observed documentation failure does this change prevent?

## Evidence

Provide the prompt, output, source fact, or reproducible artifact that
demonstrates the failure.

## Behavioral change

What should an agent do differently after this change?

## Validation

- [ ] `npx --yes skills@1.5.20 add . --list` discovers only `documentory`
- [ ] Changed links, code fences, and relative references resolve
- [ ] New guidance loads only on the request path that needs it
- [ ] Repeated or superseded guidance was removed
- [ ] Remaining assumptions or untested behavior are stated below

## Remaining risk

What could not be verified, or what trade-off remains?
