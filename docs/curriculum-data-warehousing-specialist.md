# Learning curriculum: Data Warehousing Specialist

An editorial recipe for warehouse grain, dimensional history and reconciled analytical queries, with specialist modelling gaps explicit.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [Data Warehousing Specialist](professions-data-ai.md#data-warehousing-specialist)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Relational modelling and SQL
- Experience building a data pipeline
- Understanding business measures

**What you will produce:** A small warehouse prototype with documented grain, history rules, loads and reconciled query results.

**Resource coverage:** 1 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Define an analytical workload and grain](#stage-1)
2. [Design history and late-arriving data rules](#stage-2)
3. [Build and test analytical transformations](#stage-3)
4. [Capstone - deliver a small warehouse prototype](#stage-4)

<a id="stage-1"></a>
## 1. Define an analytical workload and grain

**Learn:**

- Business processes and measures
- Fact grain and dimensions
- Source-to-model reconciliation

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [CS50's Introduction to Databases with SQL](https://cs50.harvard.edu/sql/) — beginner in this topic; free access. [Details](area-data.md#resource-cs50-sql).
- [DuckDB Documentation](https://duckdb.org/docs/stable/) — intermediate in this topic; free access. [Details](area-data.md#resource-duckdb-docs).

**Resource still needed:** These sources support SQL and analytical execution, not a verified full dimensional-modelling curriculum.

**Practise:** Choose one business process and specify a fact table's grain and the dimensions needed to answer a few questions.

**Advance when:** Detect a mixed-grain design and explain how it could double-count a measure.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Design history and late-arriving data rules

**Learn:**

- Changing dimension attributes
- Effective dates and unknown members
- Late data and corrections

**Resource still needed:** No verified specialist dimensional-history or warehouse modelling course is currently catalogued.

**Practise:** Create a reviewed design for one changing customer attribute and one late transaction using synthetic examples.

**Advance when:** Explain which dimension state applies to each example and distinguish a historical fact from a corrected current attribute.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Build and test analytical transformations

**Learn:**

- Layered model dependencies
- Data-quality checks
- Query workload and storage tradeoffs

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [dbt Learn (free courses)](https://learn.getdbt.com/catalog) — beginner in this topic; free access. [Details](area-data.md#resource-dbt-learn).
- [Use The Index, Luke](https://use-the-index-luke.com/) — intermediate in this topic; free access. [Details](area-data.md#resource-use-the-index-luke).

**Practise:** Implement the reviewed small model, test relationship assumptions and run representative analytical queries.

**Advance when:** Reconcile aggregate measures against sources and demonstrate that history handling preserves the intended answer.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - deliver a small warehouse prototype

**Learn:**

- Model and history documentation
- Repeatable loads
- Performance and correctness evidence

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Data Engineering Zoomcamp (DataTalks.Club)](https://github.com/DataTalksClub/data-engineering-zoomcamp) — intermediate in this topic; free access. [Details](area-data.md#resource-datatalks-data-engineering-zoomcamp).

**Resource still needed:** The engineering course supports implementation; the specialist history design still requires suitable domain instruction or review.

**Practise:** Package the fact and dimension model, synthetic history changes, load code, tests and a set of business queries.

**Advance when:** Rebuild the prototype and correctly answer the same question for two historical dates without mixing grain or history semantics.

## After this recipe

Study specialist dimensional modelling and the chosen warehouse platform before extending to enterprise-scale integration.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
