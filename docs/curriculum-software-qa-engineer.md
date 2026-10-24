# Learning curriculum: Software QA Engineer

Engineer maintainable automated checks around a small application's risks.

[Home](../README.md) / [Curricula](curricula.md) / [Software, interfaces and embedded systems](professions-software.md#roles-in-this-group)

**Target profile:** [Software QA Engineer](professions-software.md#software-qa-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic Python and JavaScript
- Ability to run a small web app
- Git basics

**What you will produce:** A deterministic test suite with separated checks, fixtures and failure diagnostics.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Model quality risks](#stage-1)
2. [Implement deterministic checks](#stage-2)
3. [Automate a browser workflow](#stage-3)
4. [Deliver the test-engineering mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Model quality risks

**Learn:**

- Test boundaries
- Risk priorities
- Observable behavior

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Cypress Real World App](https://github.com/cypress-io/cypress-realworld-app) — intermediate in this topic; free access. [Details](area-testing.md#resource-cypress-real-world-app).

**Practise:** Inspect the demo and identify a critical flow and the lower-level rules it depends on.

**Advance when:** Justify a unit, integration or browser check for each selected behavior.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Implement deterministic checks

**Learn:**

- Fixtures
- Assertions
- Isolation

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).

**Practise:** Test a small calculation with controlled input and a regression case.

**Advance when:** Detect an intentional wrong result and pass after correcting it.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Automate a browser workflow

**Learn:**

- Locators
- User-visible assertions
- Failure artifacts

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Playwright - Getting Started](https://github.com/microsoft/playwright) — intermediate in this topic; free access. [Details](area-testing.md#resource-playwright-getting-started).

**Practise:** Automate a local flow and capture diagnostics when an expected element is absent.

**Advance when:** Repeat with fresh fixture state and produce a useful failure for a deliberately broken step.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver the test-engineering mini-project

**Learn:**

- Suite organization
- Flaky-test investigation
- Reproducible execution

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).
- [Playwright - Getting Started](https://github.com/microsoft/playwright) — intermediate in this topic; free access. [Details](area-testing.md#resource-playwright-getting-started).

**Practise:** Deliver unit and browser checks with setup notes, isolated data and one investigated intermittent failure.

**Advance when:** Report repeated-run results and explain the observed cause rather than merely adding retries.

## After this recipe

Study continuous integration and nonfunctional testing next; passing automation does not prove coverage of every quality risk.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Software Engineering Body of Knowledge](profession-references.md#reference-swebok)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-software.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
