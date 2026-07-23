# Contributing

Documentory improves when a change prevents a real documentation failure
without making every activation longer or more rigid.

## Before proposing a change

Check the current skill and its three references. Then identify:

- the documentation task or reader the change serves;
- the failure an agent currently permits;
- source, output, or a reproducible example that demonstrates the failure;
- why the smallest existing rule or procedure cannot already prevent it.

Open a focused issue for behavior changes that need agreement. Corrections with
clear evidence can go directly to a pull request.

## Make the change

- Keep the laws at the start of `documentory/SKILL.md`.
- Keep trigger conditions in the frontmatter description and procedures in the
  body.
- Preserve the distinction between current documentation, change history, and
  code-local rationale.
- Do not introduce a required documentation topology. Diátaxis remains a lens,
  and repository owners decide whether content is split.
- Put detailed guidance in the reference loaded by the relevant procedure.
- Remove prose whose deletion changes no likely agent decision.

Changes to examples or public-contract guidance should include a realistic
before-and-after case. Changes to code-local guidance should identify the
selective context and the plausible wrong edit the new rule prevents.

## Validate

Use Node.js 22.20 or newer for the distribution check:

```sh
npx --yes skills@1.5.20 add . --list
```

Confirm that exactly one skill named `documentory` is discovered. Pull request
CI also runs the official Agent Skills reference validator.

Review every changed Markdown link, code fence, cross-reference, and repeated
rule. If a validation cannot be run, state that in the pull request with the
remaining risk.

## Pull requests

Keep each pull request about one failure mode or one coherent capability.
Describe:

1. the observed failure;
2. the evidence or reproduction;
3. the behavioral change the skill should cause;
4. validation performed;
5. any intentional omission or compatibility risk.

By contributing, you agree that your contribution is licensed under the
repository's MIT License.
