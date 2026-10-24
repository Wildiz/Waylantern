# Learning curriculum: Database Administrator

An editorial local-database operations recipe that exposes missing vendor-specific administration instruction.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [Database Administrator](professions-data-ai.md#database-administrator)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- SQL and relational database basics
- Basic Linux or host-system administration
- Ability to use a disposable local database

**What you will produce:** A documented practice database with access tests, a reviewed recovery exercise and a maintenance runbook.

**Resource coverage:** 1 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Inventory the database and its dependencies](#stage-1)
2. [Define and test access boundaries](#stage-2)
3. [Perform a reviewed backup and restore drill](#stage-3)
4. [Capstone - deliver a database operations exercise](#stage-4)

<a id="stage-1"></a>
## 1. Inventory the database and its dependencies

**Learn:**

- Storage and transaction fundamentals
- Schema and workload inventory
- Operational responsibilities

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [CMU 15-445/645 Intro to Database Systems](https://15445.courses.cs.cmu.edu/) — advanced in this topic; free access. [Details](area-cs.md#resource-cmu-15-445).
- [PostgreSQL Tutorial](https://neon.com/postgresql/tutorial) — beginner in this topic; free access. [Details](area-data.md#resource-postgresql-tutorial).

**Practise:** Build a disposable database and document its tables, data size, users and expected workload.

**Advance when:** Explain where durable state lives and which dependencies must exist before the service can work.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Define and test access boundaries

**Learn:**

- Accounts and least privilege
- Read versus write permissions
- Auditable configuration

**Resource still needed:** No verified database-engine-specific account and privilege administration lab is currently catalogued.

**Practise:** Using suitable engine documentation, create separate practice reader and writer identities without using production credentials.

**Advance when:** Demonstrate an allowed read and a denied write under the reader identity and record how permissions are reviewed.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Perform a reviewed backup and restore drill

**Learn:**

- Backup consistency
- Recovery objectives
- Restoration and integrity checks

**Resource still needed:** No verified engine-specific backup, restore or point-in-time recovery tutorial is currently catalogued.

**Practise:** On disposable data, follow a reviewed engine procedure to make a backup and restore into a separate instance.

**Advance when:** Verify restored record counts and representative queries and state the measured recovery time and untested recovery conditions.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - deliver a database operations exercise

**Learn:**

- Routine checks and alerts
- Change and rollback notes
- Recovery evidence

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Use The Index, Luke](https://use-the-index-luke.com/) — intermediate in this topic; free access. [Details](area-data.md#resource-use-the-index-luke).

**Resource still needed:** Query-tuning material is supplementary; full operational procedures still require verified administration guidance for the selected engine.

**Practise:** Package the database inventory, access evidence, restore report and runbook for a simulated small service.

**Advance when:** A practice operator can identify the database, run the checks and follow the reviewed recovery steps without guessing credentials.

## After this recipe

Add engine-specific administration and supervised recovery work before operating on important data.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
