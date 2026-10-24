# Learning curriculum: PostgreSQL Specialist

An editorial route through relational modelling, transactions and query performance in PostgreSQL.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [PostgreSQL Specialist](professions-data-ai.md#postgresql-specialist)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic SQL and joins
- Familiarity with a local database
- Command-line basics

**What you will produce:** A small PostgreSQL schema with transaction examples, measured query improvements and reproducible setup notes.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Model a consistent relational dataset](#stage-1)
2. [Reason about transactions and shared access](#stage-2)
3. [Inspect a query before adding an index](#stage-3)
4. [Capstone - deliver a documented database workload](#stage-4)

<a id="stage-1"></a>
## 1. Model a consistent relational dataset

**Learn:**

- Keys and constraints
- Normalization and relationships
- Types and nullability

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [PostgreSQL Tutorial](https://neon.com/postgresql/tutorial) — beginner in this topic; free access. [Details](area-data.md#resource-postgresql-tutorial).
- [CS50's Introduction to Databases with SQL](https://cs50.harvard.edu/sql/) — beginner in this topic; free access. [Details](area-data.md#resource-cs50-sql).

**Practise:** Model a small booking or inventory dataset and create constraints that reject invalid records.

**Advance when:** Demonstrate a foreign-key or uniqueness failure and explain the business rule it protects.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Reason about transactions and shared access

**Learn:**

- Atomic changes
- Isolation and concurrent sessions
- Failure and rollback

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [PostgreSQL Tutorial](https://neon.com/postgresql/tutorial) — beginner in this topic; free access. [Details](area-data.md#resource-postgresql-tutorial).
- [CMU 15-445/645 Intro to Database Systems](https://15445.courses.cs.cmu.edu/) — advanced in this topic; free access. [Details](area-cs.md#resource-cmu-15-445).

**Resource still needed:** The linked materials provide foundations; a verified PostgreSQL-version-specific concurrency lab is not yet catalogued.

**Practise:** Use two local sessions to study a reviewed transaction example and record the observed behavior and rollback result.

**Advance when:** Explain which changes commit together and distinguish observed session behavior from an unverified isolation guarantee.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Inspect a query before adding an index

**Learn:**

- Query plans and selectivity
- Index tradeoffs
- Measured workload performance

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Use The Index, Luke](https://use-the-index-luke.com/) — intermediate in this topic; free access. [Details](area-data.md#resource-use-the-index-luke).
- [PostgreSQL Exercises](https://pgexercises.com/) — beginner in this topic; free access. [Details](area-data.md#resource-postgresql-exercises).

**Practise:** Choose one slow query on generated data, inspect its plan and compare a justified index with the baseline.

**Advance when:** Record the before-and-after plan and timing conditions and explain the index's storage or write tradeoff.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - deliver a documented database workload

**Learn:**

- Repeatable schema and seed data
- Transaction tests
- Performance evidence

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [PostgreSQL Tutorial](https://neon.com/postgresql/tutorial) — beginner in this topic; free access. [Details](area-data.md#resource-postgresql-tutorial).

**Practise:** Package schema creation, sample data, representative queries and a short performance note for the local database.

**Advance when:** Rebuild the workload and reproduce its integrity checks and main query comparison.

## After this recipe

Choose an application-development or administration specialization and add verified version-specific operational documentation.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
