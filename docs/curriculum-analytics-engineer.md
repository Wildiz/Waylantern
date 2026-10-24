# Learning curriculum: Analytics Engineer

An editorial route through model grain, SQL transformations, data tests and documented metrics.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [Analytics Engineer](professions-data-ai.md#analytics-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- SQL joins and aggregation
- Relational keys
- Basic Git workflow

**What you will produce:** A small versioned analytical model with tests, lineage and a reconciled metric definition.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Define model grain and metric meaning](#stage-1)
2. [Organize repeatable SQL transformations](#stage-2)
3. [Test and document the analytical contract](#stage-3)
4. [Capstone - deliver a trustworthy reporting model](#stage-4)

<a id="stage-1"></a>
## 1. Define model grain and metric meaning

**Learn:**

- Source table contracts
- Grain and dimensional relationships
- Business metric definitions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [CS50's Introduction to Databases with SQL](https://cs50.harvard.edu/sql/) — beginner in this topic; free access. [Details](area-data.md#resource-cs50-sql).
- [PostgreSQL Exercises](https://pgexercises.com/) — beginner in this topic; free access. [Details](area-data.md#resource-postgresql-exercises).

**Practise:** Model a small set of transactions and customers and state exactly what one row represents at each stage.

**Advance when:** Detect a join that duplicates measures and reconcile one reported metric to source records.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Organize repeatable SQL transformations

**Learn:**

- Staging and derived models
- Dependencies and materialization
- Version-controlled changes

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [dbt Learn (free courses)](https://learn.getdbt.com/catalog) — beginner in this topic; free access. [Details](area-data.md#resource-dbt-learn).
- [Pro Git](https://git-scm.com/book/en/v2) — beginner in this topic; free access. [Details](area-software.md#resource-pro-git).

**Practise:** Build a small layered transformation project using the supported training environment and record account or warehouse requirements.

**Advance when:** Rebuild the models in dependency order and explain which source changes invalidate a downstream result.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Test and document the analytical contract

**Learn:**

- Uniqueness and relationship checks
- Null and accepted-value checks
- Lineage and column documentation

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [dbt Learn (free courses)](https://learn.getdbt.com/catalog) — beginner in this topic; free access. [Details](area-data.md#resource-dbt-learn).

**Practise:** Add checks for key assumptions and documentation for a measure, then introduce a known duplicate or missing key.

**Advance when:** The relevant check fails on the injected error and the documentation explains why that error matters to a user.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - deliver a trustworthy reporting model

**Learn:**

- Metric reconciliation
- Change review
- Rebuild and handoff instructions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [dbt Learn (free courses)](https://learn.getdbt.com/catalog) — beginner in this topic; free access. [Details](area-data.md#resource-dbt-learn).

**Practise:** Deliver a small tested model project, lineage explanation and a metric comparison against the raw source.

**Advance when:** A reader can rebuild the result, trace a measure through transformations and review the effect of one model change.

## After this recipe

Add warehouse performance and team deployment practices; dbt training and cloud warehouse free-tier limits require checking separately.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
