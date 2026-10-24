# Learning curriculum: ETL Developer

An editorial implementation recipe for validated extraction, transformation and loading with replayable batches.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [ETL Developer](professions-data-ai.md#etl-developer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Python scripting
- SQL and database tables
- File formats and basic command-line use

**What you will produce:** A local ETL job that accounts for accepted and rejected rows and safely replays a batch.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Write a source-to-target mapping](#stage-1)
2. [Implement transformations with fixtures](#stage-2)
3. [Load a batch safely](#stage-3)
4. [Capstone - deliver a replayable ETL package](#stage-4)

<a id="stage-1"></a>
## 1. Write a source-to-target mapping

**Learn:**

- Field and type mappings
- Keys and null semantics
- Business transformation rules

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [PostgreSQL Tutorial](https://neon.com/postgresql/tutorial) — beginner in this topic; free access. [Details](area-data.md#resource-postgresql-tutorial).
- [pandas Getting Started Tutorials](https://pandas.pydata.org/docs/getting_started/index.html) — beginner in this topic; free access. [Details](area-data.md#resource-pandas-getting-started).

**Practise:** Map a small CSV into destination tables and document conversions, required fields and rejected-value handling.

**Advance when:** Trace each target column to a source field or explicit derivation and explain what happens to malformed input.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Implement transformations with fixtures

**Learn:**

- Parsing and normalization
- Deterministic functions
- Transformation tests

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [pandas Getting Started Tutorials](https://pandas.pydata.org/docs/getting_started/index.html) — beginner in this topic; free access. [Details](area-data.md#resource-pandas-getting-started).
- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).

**Practise:** Implement the mapping on a tiny fixture containing missing values, invalid dates and duplicated identifiers.

**Advance when:** Tests verify expected outputs and the rejected-record report accounts for every invalid fixture row.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Load a batch safely

**Learn:**

- Staging and transactional writes
- Idempotent batch identifiers
- Reconciliation and retry behavior

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [PostgreSQL Tutorial](https://neon.com/postgresql/tutorial) — beginner in this topic; free access. [Details](area-data.md#resource-postgresql-tutorial).
- [Apache Airflow Tutorials](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html) — intermediate in this topic; free access. [Details](area-data.md#resource-airflow-tutorial).

**Practise:** Load validated rows through a staging step and simulate a failure before finalizing the batch.

**Advance when:** Rerunning the same batch does not double-count records and source counts reconcile with accepted and rejected totals.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - deliver a replayable ETL package

**Learn:**

- Job configuration
- Run logs and audit counts
- Recovery and source-change notes

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Apache Airflow Tutorials](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html) — intermediate in this topic; free access. [Details](area-data.md#resource-airflow-tutorial).

**Practise:** Package extraction, mapping, tests, load steps and a runbook for a small two-table destination.

**Advance when:** A fresh run loads the expected data, a repeated run is safe and a changed source field produces an actionable failure.

## After this recipe

Add verified connector-specific extraction and change-data-capture instruction before working with live source systems.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
