# Learning curriculum: Database Architect

An editorial database lab connecting a workload, relational structure, integrity and query measurements.

[Home](../README.md) / [Curricula](curricula.md) / [Architecture and systems design](professions-architecture.md#roles-in-this-group)

**Target profile:** [Database Architect](professions-architecture.md#database-architect)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Can write SQL joins and aggregates and explain primary and foreign keys.
- Have implemented an application using persistent storage.
- Can run a disposable local database with invented data and read query results critically.

**What you will produce:** A small relational design with integrity tests, measured index choices and a bounded storage decision.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Model the workload and enforce its invariants](#stage-1)
2. [Examine changes as transactions](#stage-2)
3. [Measure an indexing decision](#stage-3)
4. [Deliver a database-design mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Model the workload and enforce its invariants

**Learn:**

- Entities and relationships
- Constraints
- Workload queries

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [CS50's Introduction to Databases with SQL](https://cs50.harvard.edu/sql/) — beginner in this topic; free access. [Details](area-data.md#resource-cs50-sql).

**Practise:** Model bookings for rooms and users, list the main read and write operations and add key and required-field constraints in a disposable database.

**Advance when:** Example valid records are accepted, invalid references are rejected and every requested query has a place in the model.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Examine changes as transactions

**Learn:**

- Transactions
- Integrity failures
- Consistent updates

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [PostgreSQL Tutorial](https://neon.com/postgresql/tutorial) — beginner in this topic; free access. [Details](area-data.md#resource-postgresql-tutorial).

**Practise:** Implement a booking change that updates two related records within a transaction and deliberately make the second operation fail in the lab.

**Advance when:** Recorded before-and-after queries demonstrate that the failed transaction leaves no partial update, and the test distinguishes rollback from a successful commit.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Measure an indexing decision

**Learn:**

- Index selection
- Query plans
- Write costs

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Use The Index, Luke](https://use-the-index-luke.com/) — intermediate in this topic; free access. [Details](area-data.md#resource-use-the-index-luke).

**Practise:** Generate an invented dataset, inspect a representative filtered query before and after an index and record its query plan, dataset size and repeated timings.

**Advance when:** The report explains the chosen index using the query shape and acknowledges storage or write overhead rather than treating one fast run as proof.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver a database-design mini-project

**Learn:**

- Schema documentation
- Storage alternatives
- Recovery questions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [CMU 15-445/645 Intro to Database Systems](https://15445.courses.cs.cmu.edu/) — advanced in this topic; free access. [Details](area-cs.md#resource-cmu-15-445).
- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).

**Practise:** Package the schema, representative queries and integrity evidence, compare the selected relational store with one plausible alternative and list backup-and-restore checks still required before deployment.

**Advance when:** A reader can reproduce the local workload and trace the storage choice to requirements; untested recovery and scale claims are explicitly excluded.

## After this recipe

Validate concurrent workloads, restore procedures and operational behavior with experienced database practitioners; a schema and benchmark do not establish production readiness.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)
- [ACM Computing Curricula Recommendations](profession-references.md#reference-acm-curricula)

[Back to roles in this group](professions-architecture.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
