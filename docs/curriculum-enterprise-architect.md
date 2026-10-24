# Learning curriculum: Enterprise Architect

An editorial planning exercise for experienced practitioners, with explicit gaps where verified enterprise-specific learning resources are missing.

[Home](../README.md) / [Curricula](curricula.md) / [Architecture and systems design](professions-architecture.md#roles-in-this-group)

**Target profile:** [Enterprise Architect](professions-architecture.md#enterprise-architect)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Have worked with multiple organisational systems and their operational constraints.
- Can discuss stakeholder priorities and distinguish business capabilities from individual applications.
- Can document assumptions without presenting invented organisation data as evidence.

**What you will produce:** A fictional capability-to-system map and a reasoned transition proposal, suitable for discussion with an experienced practitioner rather than a claim of enterprise-architecture competence.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Map the business need before the technology estate](#stage-1)
2. [Describe system boundaries and cross-system dependencies](#stage-2)
3. [Plan an incremental transition](#stage-3)
4. [Present an enterprise-change mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Map the business need before the technology estate

**Learn:**

- Business capabilities
- Stakeholder priorities
- Current-state inventory

**Resource still needed:** The catalogue lacks a verified introductory enterprise-architecture resource teaching capability mapping and business-to-technology alignment.

**Practise:** For a fictional training organisation, list enrolment, teaching and billing capabilities, their owners and the systems supporting them; label every assumed fact.

**Advance when:** The map distinguishes a capability from an application and shows a responsible stakeholder for each capability.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Describe system boundaries and cross-system dependencies

**Learn:**

- System context
- External dependencies
- Quality constraints

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).

**Practise:** Use context and quality sections to document the enrolment system, its billing interface and a dependency that would disrupt teaching if unavailable.

**Advance when:** Readers can locate that dependency and explain its business impact; the template is used for documentation, not presented as an enterprise methodology.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Plan an incremental transition

**Learn:**

- Transition states
- Portfolio constraints
- Retirement criteria

**Resource still needed:** No verified resource in the catalogue currently teaches enterprise transition architectures, portfolio governance and capability-based migration planning.

**Practise:** Compare replacing the enrolment system at once with an incremental migration, identify two intermediate states and define evidence required before retiring the old system.

**Advance when:** Each transition has an owner, a dependency, an acceptance condition and a fallback; cost and timing estimates are clearly assumptions.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Present an enterprise-change mini-project

**Learn:**

- Decision rationale
- Exceptions
- Stakeholder review

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).

**Practise:** Assemble the maps and transition plan, use an ADR to record the preferred migration and obtain a critical review of one competing stakeholder priority.

**Advance when:** The proposal traces the choice to a business need, records an unresolved objection and states which operational evidence could reverse the decision.

## After this recipe

Fill the explicit enterprise-methodology gaps with verified learning material and supervised work across business and technical teams; document templates alone do not teach enterprise governance.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-architecture.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
