# Learning curriculum: Data Architect

An editorial exercise in modelling data across systems while making stewardship and governance gaps visible.

[Home](../README.md) / [Curricula](curricula.md) / [Architecture and systems design](professions-architecture.md#roles-in-this-group)

**Target profile:** [Data Architect](professions-architecture.md#data-architect)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Can query relational data and explain keys, joins and basic integrity constraints.
- Have worked with data moving between at least two files, services or databases.
- Can use invented data and document uncertain business definitions.

**What you will produce:** A cross-system data model, glossary, small transformation example and explicit governance questions.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Establish shared entities and definitions](#stage-1)
2. [Trace one transformation across boundaries](#stage-2)
3. [Identify ownership and governance requirements](#stage-3)
4. [Deliver a shared-data mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Establish shared entities and definitions

**Learn:**

- Entities
- Keys
- Relational integrity

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [CS50's Introduction to Databases with SQL](https://cs50.harvard.edu/sql/) — beginner in this topic; free access. [Details](area-data.md#resource-cs50-sql).

**Practise:** Model a fictional training organisation's learners, enrolments and invoices; record definitions and show how stable identifiers connect records.

**Advance when:** The model can represent repeated enrolments without confusing a person with an enrolment or duplicating the definition of an invoice.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Trace one transformation across boundaries

**Learn:**

- Source and target models
- Transformations
- Data-quality checks

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [dbt Learn (free courses)](https://learn.getdbt.com/catalog) — beginner in this topic; free access. [Details](area-data.md#resource-dbt-learn).

**Practise:** Use a small invented enrolment dataset to define a source-to-report transformation, list required fields and add checks for missing identifiers and duplicate records.

**Advance when:** A sample output is traceable to its input records, and the documented checks detect deliberately introduced missing or duplicate identifiers.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Identify ownership and governance requirements

**Learn:**

- Data stewardship
- Retention
- Access decisions

**Resource still needed:** No verified resource currently teaches a complete introductory treatment of data stewardship, retention governance and enterprise data ownership.

**Practise:** Assign fictional owners to the three datasets, propose access and retention questions for each and label decisions that need business, privacy or legal review rather than inventing compliance rules.

**Advance when:** Every dataset has an owner and an unresolved-decision list, and no proposed retention period is presented as a legal requirement without evidence.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver a shared-data mini-project

**Learn:**

- Data contracts
- Lineage
- Change impact

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).
- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).

**Practise:** Package the glossary, model and transformation evidence, then assess adding a second billing system and record which definitions or interfaces must remain stable.

**Advance when:** A reviewer can follow one learner record to the report and identify the owner, transformation and likely impact of a changed invoice field.

## After this recipe

Fill the governance gaps with verified material and work with data owners and privacy specialists; a schema and glossary alone do not establish an enterprise data strategy.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)
- [ACM Computing Curricula Recommendations](profession-references.md#reference-acm-curricula)

[Back to roles in this group](professions-architecture.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
