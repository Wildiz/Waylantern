# Learning curriculum: BI Developer

An editorial Power BI-based recipe for modelling, measures and a tested interactive report.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [BI Developer](professions-data-ai.md#bi-developer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic SQL and tabular data
- Arithmetic and business metrics
- Access to a supported Power BI environment

**What you will produce:** A small reporting model and dashboard with reconciled measures and documented refresh requirements.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Define the reporting question and model grain](#stage-1)
2. [Prepare data and create relationships](#stage-2)
3. [Implement measures and interaction checks](#stage-3)
4. [Capstone - hand off a reproducible BI report](#stage-4)

<a id="stage-1"></a>
## 1. Define the reporting question and model grain

**Learn:**

- Audience and decisions
- Facts and dimensions
- Metric definitions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [CS50's Introduction to Databases with SQL](https://cs50.harvard.edu/sql/) — beginner in this topic; free access. [Details](area-data.md#resource-cs50-sql).
- [Microsoft Learn: Power BI training](https://learn.microsoft.com/en-us/training/powerplatform/power-bi) — beginner in this topic; freemium access. [Details](area-data.md#resource-power-bi-microsoft-learn).

**Practise:** Choose a simple reporting question and sketch source tables, relationships and the meaning of each measure.

**Advance when:** Explain the grain and reconcile one total before using it in a report visual.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Prepare data and create relationships

**Learn:**

- Data types and cleaning
- Relationship direction and cardinality
- Refresh inputs

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Microsoft Learn: Power BI training](https://learn.microsoft.com/en-us/training/powerplatform/power-bi) — beginner in this topic; freemium access. [Details](area-data.md#resource-power-bi-microsoft-learn).

**Practise:** Load permitted practice tables, clean their fields and build relationships without hiding unmatched records.

**Advance when:** Report unmatched keys and show that relationships do not inflate a known source total.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Implement measures and interaction checks

**Learn:**

- Calculated measures
- Filtering and context
- Visual choice and usability

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Microsoft Learn: Power BI training](https://learn.microsoft.com/en-us/training/powerplatform/power-bi) — beginner in this topic; freemium access. [Details](area-data.md#resource-power-bi-microsoft-learn).
- [From Data to Viz](https://www.data-to-viz.com/) — beginner in this topic; free access. [Details](area-data.md#resource-from-data-to-viz).

**Practise:** Build a few measures and inspect them under different date, group and cross-filter selections.

**Advance when:** Reconcile selected report values with independent SQL or manual calculations and identify an intentionally misleading visual.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - hand off a reproducible BI report

**Learn:**

- Refresh procedure
- Permissions and sharing limits
- User instructions and acceptance checks

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Microsoft Learn: Power BI training](https://learn.microsoft.com/en-us/training/powerplatform/power-bi) — beginner in this topic; freemium access. [Details](area-data.md#resource-power-bi-microsoft-learn).

**Practise:** Deliver a small local report, model notes, measure definitions and refresh instructions; do not assume paid sharing features are included.

**Advance when:** Reopen and refresh from the documented inputs and demonstrate the report's agreed questions and limitations.

## After this recipe

Add governed distribution and operational refresh in the chosen environment; Power BI Desktop platform and publishing licence requirements remain separate.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)
- [Microsoft Learn training directory](profession-references.md#reference-microsoft-learn)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
