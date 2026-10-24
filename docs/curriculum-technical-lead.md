# Learning curriculum: Technical Lead

An editorial collaboration exercise that combines technical direction, review and reproducible delivery without equating a title with seniority.

[Home](../README.md) / [Curricula](curricula.md) / [Architecture and systems design](professions-architecture.md#roles-in-this-group)

**Target profile:** [Technical Lead](professions-architecture.md#technical-lead)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Can implement, test and review changes in an existing codebase.
- Have collaborated through Git and can explain a technical choice to another developer.
- Can ask for feedback and distinguish technical leadership from people-management authority.

**What you will produce:** A small reviewed change with a clear plan, decision record, test evidence and handover notes; individual practice cannot demonstrate team-leadership competence by itself.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Frame a change so someone else can contribute](#stage-1)
2. [Make a decision that the team can challenge](#stage-2)
3. [Review behavior as well as the diff](#stage-3)
4. [Deliver a technical-direction mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Frame a change so someone else can contribute

**Learn:**

- Acceptance criteria
- Technical scope
- Implementation dependencies

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).

**Practise:** Choose a modest improvement in a Python practice project, describe its externally observable result and map the affected components before splitting work into two reviewable tasks.

**Advance when:** Each task has an acceptance example and the plan identifies the shared interface that must remain consistent.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Make a decision that the team can challenge

**Learn:**

- Alternatives
- Decision rationale
- Review questions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).

**Practise:** Record one contested implementation choice with its constraints, alternatives and consequences, then ask a collaborator to challenge it or label a solo review explicitly.

**Advance when:** The record includes an objection and a response based on the project's needs, not on the author's job title.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Review behavior as well as the diff

**Learn:**

- Pull requests
- Regression checks
- Reproduction steps

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [GitHub Skills: Introduction to GitHub](https://github.com/skills/introduction-to-github) — beginner in this topic; free access. [Details](area-software.md#resource-github-skills-introduction-to-github).
- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).

**Practise:** Implement the change on a branch in a separate practice repository, add a relevant Python test and prepare a pull request with reproduction steps; the GitHub exercise teaches mechanics, not a complete review methodology.

**Advance when:** A relevant deliberate mistake makes the test fail, and review notes identify behavior or maintainability evidence rather than merely confirming that the diff exists.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver a technical-direction mini-project

**Learn:**

- Handover
- Follow-up decisions
- Collaboration limits

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).

**Resource still needed:** The catalogue does not yet contain verified training for coaching, conflict resolution or inclusive technical leadership; ADR guidance only supports the decision-documentation part.

**Practise:** Package the plan, change, test evidence and review discussion, record one improvement from feedback and write handover instructions with the next technical risk to investigate.

**Advance when:** Another reader can reproduce the result and identify which decisions changed after review; solo work is not presented as evidence of leading a team.

## After this recipe

Practise planning, mentoring and disagreement resolution with a real team and experienced feedback; fill the explicit leadership-training gap instead of treating reading or pull-request mechanics as leadership qualification.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Software Engineering Body of Knowledge](profession-references.md#reference-swebok)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-architecture.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
