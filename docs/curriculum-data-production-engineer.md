# Learning curriculum: Data Production Engineer

An editorial operations recipe centred on repeatable runs, data freshness and recovery evidence.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [Data Production Engineer](professions-data-ai.md#data-production-engineer)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Python and SQL
- Experience running a small data pipeline
- Logs and command-line diagnosis

**What you will produce:** A small operated pipeline with freshness checks, a simulated incident and a tested local recovery runbook.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Map the production data flow](#stage-1)
2. [Add operational signals and checks](#stage-2)
3. [Practise replay and safe recovery](#stage-3)
4. [Capstone - run a local data incident exercise](#stage-4)

<a id="stage-1"></a>
## 1. Map the production data flow

**Learn:**

- Inputs outputs and dependencies
- Freshness and completeness
- Expected service behavior

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Data Engineering Zoomcamp (DataTalks.Club)](https://github.com/DataTalksClub/data-engineering-zoomcamp) — intermediate in this topic; free access. [Details](area-data.md#resource-datatalks-data-engineering-zoomcamp).
- [Apache Airflow Tutorials](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html) — intermediate in this topic; free access. [Details](area-data.md#resource-airflow-tutorial).

**Practise:** Document a small existing pipeline's dependencies and expected run schedule and output conditions.

**Advance when:** Trace one output back to its input and define how lateness differs from incorrect or incomplete data.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Add operational signals and checks

**Learn:**

- Run status and task logs
- Volume and schema checks
- Actionable failure messages

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Apache Airflow Tutorials](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html) — intermediate in this topic; free access. [Details](area-data.md#resource-airflow-tutorial).
- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).

**Practise:** Instrument a local pipeline with checks for a missing input, changed schema and unexpected row count.

**Advance when:** Each injected fault produces a distinguishable signal and useful diagnostic context rather than a silent empty output.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Practise replay and safe recovery

**Learn:**

- Retries and idempotency
- Partial-write handling
- Backfill and downstream verification

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Apache Airflow Tutorials](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html) — intermediate in this topic; free access. [Details](area-data.md#resource-airflow-tutorial).
- [DuckDB Documentation](https://duckdb.org/docs/stable/) — intermediate in this topic; free access. [Details](area-data.md#resource-duckdb-docs).

**Practise:** Interrupt a disposable run after one stage, inspect partial state and replay only the necessary work.

**Advance when:** Recover the correct output without duplicate rows and reconcile downstream totals after the replay.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - run a local data incident exercise

**Learn:**

- Triage timeline
- Recovery evidence
- Preventive follow-up

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Data Engineering Zoomcamp (DataTalks.Club)](https://github.com/DataTalksClub/data-engineering-zoomcamp) — intermediate in this topic; free access. [Details](area-data.md#resource-datatalks-data-engineering-zoomcamp).

**Practise:** Inject one documented failure, diagnose it from logs and produce an incident note with cause, recovery steps and one concrete prevention change.

**Advance when:** Reproduce the failure and recovery from the runbook and demonstrate that the prevention change catches the same failure earlier.

## After this recipe

Add access control, deployment and real operational monitoring under supervision before supporting consequential production workflows.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
