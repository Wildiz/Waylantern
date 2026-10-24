# Learning curriculum: Data Engineer

An editorial recipe for moving permitted source data into a checked analytical dataset.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [Data Engineer](professions-data-ai.md#data-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- SQL queries and joins
- Python scripting and files
- Basic command-line use

**What you will produce:** A small repeatable pipeline with source contracts, validation, scheduled tasks and a documented recovery procedure.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Define the source and destination contracts](#stage-1)
2. [Implement validated transformations](#stage-2)
3. [Orchestrate dependencies and recovery](#stage-3)
4. [Capstone - publish a reproducible data pipeline](#stage-4)

<a id="stage-1"></a>
## 1. Define the source and destination contracts

**Learn:**

- Schemas and data types
- Keys and update semantics
- Batch ingestion boundaries

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [PostgreSQL Tutorial](https://neon.com/postgresql/tutorial) — beginner in this topic; free access. [Details](area-data.md#resource-postgresql-tutorial).
- [DuckDB Documentation](https://duckdb.org/docs/stable/) — intermediate in this topic; free access. [Details](area-data.md#resource-duckdb-docs).

**Practise:** Specify a small source file format and destination tables, including stable identifiers and expected update behavior.

**Advance when:** Explain what happens when the same source batch arrives twice or a field changes type.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Implement validated transformations

**Learn:**

- Parsing and rejected records
- Deterministic transformations
- Data-quality assertions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [pandas Getting Started Tutorials](https://pandas.pydata.org/docs/getting_started/index.html) — beginner in this topic; free access. [Details](area-data.md#resource-pandas-getting-started).
- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).

**Practise:** Create a pipeline that retains raw inputs, records invalid rows and writes a stable output table.

**Advance when:** Inject malformed and duplicate records and show explicit handling without silent loss or double counting.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Orchestrate dependencies and recovery

**Learn:**

- Task ordering and retries
- Idempotency and backfills
- Logging and run status

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Apache Airflow Tutorials](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html) — intermediate in this topic; free access. [Details](area-data.md#resource-airflow-tutorial).
- [Data Engineering Zoomcamp (DataTalks.Club)](https://github.com/DataTalksClub/data-engineering-zoomcamp) — intermediate in this topic; free access. [Details](area-data.md#resource-datatalks-data-engineering-zoomcamp).

**Practise:** Split ingestion and transformation into explicit tasks and simulate an interruption followed by a safe rerun.

**Advance when:** Recover a failed run without duplicating output and reconcile the records for a replayed batch.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - publish a reproducible data pipeline

**Learn:**

- Operational runbook
- Output verification
- Data lineage and limitations

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Data Engineering Zoomcamp (DataTalks.Club)](https://github.com/DataTalksClub/data-engineering-zoomcamp) — intermediate in this topic; free access. [Details](area-data.md#resource-datatalks-data-engineering-zoomcamp).

**Practise:** Deliver source examples, schema, pipeline code, checks and a runbook for a local end-to-end flow.

**Advance when:** A fresh run creates the expected tables, rejects known bad records and can recover from the documented failure.

## After this recipe

Extend to real source systems, access control and scale only after the local contracts and recovery behavior are understood.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)
- [CS2023 — Computer Science Curricula](profession-references.md#reference-cs2023)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
