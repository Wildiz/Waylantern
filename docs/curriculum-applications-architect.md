# Learning curriculum: Applications Architect

An editorial portfolio exercise focused on application boundaries, duplicated responsibilities and incremental change.

[Home](../README.md) / [Curricula](curricula.md) / [Architecture and systems design](professions-architecture.md#roles-in-this-group)

**Target profile:** [Applications Architect](professions-architecture.md#applications-architect)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Have maintained or integrated multiple applications and can describe their dependencies.
- Understand API contracts and basic deployment constraints.
- Can separate a proposed target landscape from an existing implementation.

**What you will produce:** A fictional application portfolio map, responsibility matrix and phased consolidation proposal with acceptance conditions.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Map applications and the capabilities they expose](#stage-1)
2. [Identify duplicated and misplaced responsibilities](#stage-2)
3. [Design a manageable transition](#stage-3)
4. [Deliver an application-portfolio mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Map applications and the capabilities they expose

**Learn:**

- Application context
- Ownership
- External dependencies

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).

**Practise:** Document a fictional organisation's enrolment, billing and reporting applications, their users, owners and external interfaces.

**Advance when:** The inventory shows where each user action begins and which application owns its authoritative record.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Identify duplicated and misplaced responsibilities

**Learn:**

- Application boundaries
- Coupling
- Shared data

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [System Design (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design) — intermediate in this topic; free access. [Details](area-architecture.md#resource-karan-system-design).

**Practise:** Find a case where enrolment and billing both maintain a learner address, compare central ownership with duplicated copies and document the effect on updates and failures.

**Advance when:** The comparison names a benefit and failure mode for each option and does not recommend microservices merely because multiple applications exist.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Design a manageable transition

**Learn:**

- Interface changes
- Coexistence
- Reversal conditions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).
- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).

**Practise:** Plan how one application becomes the address owner while the others continue operating; define sample old and new interface payloads and a reversible switch-over condition.

**Advance when:** The transition identifies affected consumers, a compatibility check and what would trigger a return to the previous arrangement.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver an application-portfolio mini-project

**Learn:**

- Target landscape
- Responsibility traceability
- Change review

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).

**Practise:** Present current and proposed landscapes, the address-ownership decision and three example user journeys showing how the proposal changes dependencies.

**Advance when:** A reviewer can trace all three journeys and distinguish a justified consolidation from an unsupported organisation-wide redesign.

## After this recipe

Test the proposed boundaries with application owners and real change constraints; this fictional portfolio does not replace experience maintaining an organisation's estate.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)
- [Software Engineering Body of Knowledge](profession-references.md#reference-swebok)

[Back to roles in this group](professions-architecture.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
