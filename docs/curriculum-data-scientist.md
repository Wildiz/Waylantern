# Learning curriculum: Data Scientist

An editorial study recipe connecting statistical reasoning to a reproducible modelling experiment.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [Data Scientist](professions-data-ai.md#data-scientist)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic Python and data manipulation
- Algebra and descriptive statistics
- Ability to read simple plots

**What you will produce:** A reproducible experiment comparing a baseline and a model with leakage checks, uncertainty and stated limitations.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Define the population and investigation](#stage-1)
2. [Build a trustworthy analysis table](#stage-2)
3. [Compare a baseline with a model](#stage-3)
4. [Capstone - report a reproducible experiment](#stage-4)

<a id="stage-1"></a>
## 1. Define the population and investigation

**Learn:**

- Sampling and measurement
- Hypotheses and confounding
- Data provenance and ethics

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [OpenIntro Statistics](https://www.openintro.org/book/os/) — beginner in this topic; free access. [Details](area-data.md#resource-openintro-statistics).
- [Microsoft Data Science for Beginners](https://github.com/microsoft/Data-Science-For-Beginners) — beginner in this topic; free access. [Details](area-data.md#resource-microsoft-data-science-for-beginners).

**Practise:** Write a question, intended population and data dictionary before exploring a small permitted dataset.

**Advance when:** Identify a sampling limitation and distinguish an association question from a causal claim.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Build a trustworthy analysis table

**Learn:**

- Missingness and outliers
- Joins and data leakage
- Reproducible transformations

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [pandas Getting Started Tutorials](https://pandas.pydata.org/docs/getting_started/index.html) — beginner in this topic; free access. [Details](area-data.md#resource-pandas-getting-started).
- [Think Stats (3rd edition)](https://allendowney.github.io/ThinkStats/) — beginner in this topic; free access. [Details](area-data.md#resource-think-stats).

**Practise:** Create a cleaning pipeline that preserves raw data and records exclusions and derived variables.

**Advance when:** Reconcile row counts at every transformation and show that evaluation data do not inform fitted preprocessing.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Compare a baseline with a model

**Learn:**

- Training and evaluation splits
- Appropriate metrics
- Uncertainty and error analysis

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Machine Learning for Beginners (Microsoft)](https://github.com/microsoft/ML-For-Beginners) — beginner in this topic; free access. [Details](area-ai.md#resource-microsoft-ml-for-beginners).
- [Think Bayes (2nd edition)](https://allendowney.github.io/ThinkBayes2/) — intermediate in this topic; free access. [Details](area-data.md#resource-think-bayes).

**Practise:** Train a simple baseline and one model, then inspect mistakes across meaningful data slices.

**Advance when:** Explain why the metric fits the question and report cases where improvement is uncertain or misleading.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - report a reproducible experiment

**Learn:**

- Experiment records
- Sensitivity checks
- Communicating model limits

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Made With ML](https://madewithml.com) — intermediate in this topic; free access. [Details](area-ai.md#resource-made-with-ml).
- [storytelling with data: free resources](https://www.storytellingwithdata.com/resources) — beginner in this topic; freemium access. [Details](area-data.md#resource-storytelling-with-data-resources).

**Practise:** Deliver code, data provenance, saved configuration, baseline comparison and a concise technical report.

**Advance when:** Reproduce the reported result from a clean run and explain one failure case without claiming causation or universal accuracy.

## After this recipe

Study experimental design and the chosen application domain before attempting high-stakes conclusions or production deployment.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)
- [CS2023 — Computer Science Curricula](profession-references.md#reference-cs2023)
- [Data Science for Beginners](profession-references.md#reference-microsoft-data-science)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
