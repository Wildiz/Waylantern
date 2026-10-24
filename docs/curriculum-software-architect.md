# Learning curriculum: Software Architect

An editorial practice sequence for turning quality requirements into boundaries and justified design decisions.

[Home](../README.md) / [Curricula](curricula.md) / [Architecture and systems design](professions-architecture.md#roles-in-this-group)

**Target profile:** [Software Architect](professions-architecture.md#software-architect)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Have built and debugged a small application with persistent data.
- Can use Git and write an automated test in the application's language.
- Can explain one maintenance problem encountered in an existing codebase.

**What you will produce:** A small application, architecture sketch, tested module boundary and decision records; this is practice, not proof of professional qualification.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Turn vague goals into observable requirements](#stage-1)
2. [Study one manageable decomposition](#stage-2)
3. [Implement a boundary and record the tradeoff](#stage-3)
4. [Deliver a reviewed architecture mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Turn vague goals into observable requirements

**Learn:**

- Stakeholders
- Quality goals
- System context

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).

**Practise:** Choose a local task tracker and write three functional requirements plus two observable quality scenarios, such as retaining tasks after a restart and rejecting an invalid update.

**Advance when:** Each scenario names a starting condition, an action and an expected result that another reader can check.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Study one manageable decomposition

**Learn:**

- Module boundaries
- Interfaces
- Dependency direction

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [500 Lines or Less](https://github.com/aosabook/500lines) — intermediate in this topic; free access. [Details](area-architecture.md#resource-500-lines-or-less).

**Practise:** Read one chapter in a language you know, trace an input through its modules and compare two possible boundaries for your tracker.

**Advance when:** Your diagram identifies responsibility and data passed at each boundary, and you can state a cost of your preferred decomposition.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Implement a boundary and record the tradeoff

**Learn:**

- Storage interfaces
- Architectural decisions
- Regression tests

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).
- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).

**Practise:** In a Python practice version, separate task rules from file persistence, test an invalid update and record why you chose that interface; pytest is only relevant to the Python version.

**Advance when:** A test fails when the rule is deliberately broken, passes after restoration, and storage code can change without rewriting that rule.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver a reviewed architecture mini-project

**Learn:**

- Architecture views
- Requirement traceability
- Change impact

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).
- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).

**Practise:** Package the tracker, run instructions, diagrams and two decision records; assess a new requirement for shared tasks and revise only the necessary boundaries.

**Advance when:** A reviewer can run the existing version and trace the proposed change to its requirements, affected modules and unresolved assumptions.

## After this recipe

Apply the same reasoning to a real team project under review; practise revisiting decisions after operational evidence rather than treating the documents as certification.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Software Engineering Body of Knowledge](profession-references.md#reference-swebok)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-architecture.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
