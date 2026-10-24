# Learning curriculum: Data Analyst

An editorial route from a first SQL query to a small reproducible analysis, not an institutional programme.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [Data Analyst](professions-data-ai.md#data-analyst)

**Starting point:** Start with the basics

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic computer and file handling
- Arithmetic with percentages and averages

**What you will produce:** A small analysis with saved queries, a reproducible cleaning script and a chart answering a stated question.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Ask a question and retrieve relevant rows](#stage-1)
2. [Learn enough Python to clean a small table](#stage-2)
3. [Summarize variation and communicate a result](#stage-3)
4. [Capstone - deliver an answer someone can check](#stage-4)

<a id="stage-1"></a>
## 1. Ask a question and retrieve relevant rows

**Learn:**

- Questions and units of observation
- SELECT and filtering
- GROUP BY and simple joins

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [SQLBolt](https://sqlbolt.com/) — beginner in this topic; free access. [Details](area-data.md#resource-sqlbolt).
- [PostgreSQL Exercises](https://pgexercises.com/) — beginner in this topic; free access. [Details](area-data.md#resource-postgresql-exercises).

**Practise:** Choose one question about a practice dataset and write queries for its row counts, groups and totals.

**Advance when:** Explain each query and independently reconcile one grouped total with the source rows.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Learn enough Python to clean a small table

**Learn:**

- Variables and loops
- Functions and files
- Missing values and data types

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) — beginner in this topic; free access. [Details](area-software.md#resource-automate-the-boring-stuff).
- [pandas Getting Started Tutorials](https://pandas.pydata.org/docs/getting_started/index.html) — beginner in this topic; free access. [Details](area-data.md#resource-pandas-getting-started).

**Practise:** Complete the introductory Python examples before using pandas to load a CSV, standardize a column and record rejected rows.

**Advance when:** Run the script twice on the same source and obtain identical output and an explicit rejection count.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Summarize variation and communicate a result

**Learn:**

- Distributions and outliers
- Suitable chart choices
- Correlation versus explanation

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [OpenIntro Statistics](https://www.openintro.org/book/os/) — beginner in this topic; free access. [Details](area-data.md#resource-openintro-statistics).
- [From Data to Viz](https://www.data-to-viz.com/) — beginner in this topic; free access. [Details](area-data.md#resource-from-data-to-viz).

**Practise:** Compare a mean with a median and make a labelled chart that answers the original question without hiding missing data.

**Advance when:** State the units, sample size and one limitation; reproduce the chart from saved data and code.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - deliver an answer someone can check

**Learn:**

- Source provenance
- Query and code reproducibility
- Conclusions and uncertainty

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [storytelling with data: free resources](https://www.storytellingwithdata.com/resources) — beginner in this topic; freemium access. [Details](area-data.md#resource-storytelling-with-data-resources).

**Practise:** Package a small permitted dataset, a question, SQL, cleaning code and a one-page findings report.

**Advance when:** A reader can rerun the analysis, reconcile the key number and distinguish the finding from speculation.

## After this recipe

Add larger datasets and domain knowledge gradually; this introductory project does not cover every analyst responsibility.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)
- [CS2023 — Computer Science Curricula](profession-references.md#reference-cs2023)
- [Data Science for Beginners](profession-references.md#reference-microsoft-data-science)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
