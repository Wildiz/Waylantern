# Learning curriculum: DataOps Engineer

Make a small data workflow testable, repeatable and explainable when an input or scheduled run fails.

[Home](../README.md) / [Curricula](curricula.md) / [Operations, platforms and IT support](professions-operations.md#roles-in-this-group)

**Target profile:** [DataOps Engineer](professions-operations.md#dataops-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Write basic Python and SQL.
- Use Git and understand a table schema.

**What you will produce:** A repeatable synthetic-data pipeline with quality checks, retry evidence and a recovery note.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Define input and output expectations](#stage-1)
2. [Schedule a traceable transformation](#stage-2)
3. [Handle failure without corrupting results](#stage-3)
4. [Capstone: recover and hand over a data run](#stage-4)

<a id="stage-1"></a>
## 1. Define input and output expectations

**Learn:**

- Schema and ownership
- Data-quality rules

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Data Engineering Zoomcamp (DataTalks.Club)](https://github.com/DataTalksClub/data-engineering-zoomcamp) — intermediate in this topic; free access. [Details](area-data.md#resource-datatalks-data-engineering-zoomcamp).

**Practise:** Describe a small synthetic source table and the fields and quality rules expected by a downstream consumer.

**Advance when:** Examples include a valid row and two rejected cases with reasons.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Schedule a traceable transformation

**Learn:**

- Workflow dependencies
- Run identifiers

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Apache Airflow Tutorials](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html) — intermediate in this topic; free access. [Details](area-data.md#resource-airflow-tutorial).

**Practise:** Follow the relevant tutorial to run a small transformation, preserving the input version and a per-run result.

**Advance when:** A run can be traced from its input through its tasks to a recorded output.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Handle failure without corrupting results

**Learn:**

- Retries and idempotency
- Quality gates

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Apache Airflow Tutorials](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html) — intermediate in this topic; free access. [Details](area-data.md#resource-airflow-tutorial).

**Practise:** Inject a missing input or duplicate row into the practice data and record how the pipeline rejects or safely reprocesses it.

**Advance when:** Rerunning the same input does not duplicate accepted output, and the failure is visible to an operator.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone: recover and hand over a data run

**Learn:**

- Consumer impact
- Recovery evidence

**Resource still needed:** This complete data-operations handover is an editorial exercise; the workflow tutorials do not define an organisation-wide DataOps process.

**Practise:** Demonstrate a failed run and a corrected rerun, then write the incident and the downstream validation required before releasing the output.

**Advance when:** A reader can locate the faulty input, recovery action and checks protecting the consumer.

## After this recipe

Study access control, data lineage and supervised backfills before operating pipelines with sensitive or business-critical data.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-operations.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
