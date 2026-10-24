# Learning curriculum: Quantitative Analyst

An editorial preparation route with explicit gaps in financial economics and specialist quantitative methods.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [Quantitative Analyst](professions-data-ai.md#quantitative-analyst)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Calculus and linear algebra
- Probability and statistical estimation
- Python programming
- Financial-market fundamentals

**What you will produce:** A small research notebook documenting a toy financial hypothesis, evaluation assumptions and backtest limitations.

**Resource coverage:** 1 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Refresh mathematical and statistical foundations](#stage-1)
2. [Establish the financial model and data contract](#stage-2)
3. [Design an honest historical experiment](#stage-3)
4. [Capstone - write a bounded quantitative research note](#stage-4)

<a id="stage-1"></a>
## 1. Refresh mathematical and statistical foundations

**Learn:**

- Linear algebra and optimization
- Probability and estimation
- Numerical stability

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Mathematics for Machine Learning (book)](https://mml-book.github.io/) — intermediate in this topic; free access. [Details](area-ai.md#resource-mathematics-for-machine-learning).
- [Think Bayes (2nd edition)](https://allendowney.github.io/ThinkBayes2/) — intermediate in this topic; free access. [Details](area-data.md#resource-think-bayes).

**Practise:** Solve a small estimation problem analytically where possible and compare it with a numerical calculation.

**Advance when:** Explain assumptions, units and numerical sensitivity instead of treating a computed number as exact.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Establish the financial model and data contract

**Learn:**

- Returns and valuation assumptions
- Corporate actions and trading calendars
- Market conventions and instrument risk

**Resource still needed:** No verified financial-economics or instrument-specific curriculum is currently catalogued; obtain suitable specialist instruction before interpreting financial results.

**Practise:** Specify a toy instrument and write the required fields, time conventions and assumptions without substituting generic machine learning for financial theory.

**Advance when:** A domain reviewer can identify how each assumption affects the proposed analysis; unresolved conventions remain explicit.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Design an honest historical experiment

**Learn:**

- Chronological evaluation
- Look-ahead and survivorship bias
- Transaction costs and parameter sensitivity

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [pandas Getting Started Tutorials](https://pandas.pydata.org/docs/getting_started/index.html) — beginner in this topic; free access. [Details](area-data.md#resource-pandas-getting-started).
- [Think Stats (3rd edition)](https://allendowney.github.io/ThinkStats/) — beginner in this topic; free access. [Details](area-data.md#resource-think-stats).

**Resource still needed:** The linked resources support data handling and statistics, not a verified financial backtesting methodology.

**Practise:** Build a toy chronological analysis and compare results before and after simple declared cost and parameter changes.

**Advance when:** Show that later observations never determine earlier decisions and explain why a historical result is not a return guarantee.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - write a bounded quantitative research note

**Learn:**

- Baseline comparisons
- Stress assumptions
- Reproducibility and risk disclosure

**Resource still needed:** No verified specialist quantitative-finance capstone is available in the catalogue; the proposed project requires domain review.

**Practise:** Package the toy experiment with data permissions, assumptions, baseline, sensitivity table and reasons the hypothesis may fail.

**Advance when:** Another reader can rerun the notebook and distinguish model evidence, financial assumptions and unverified domain conclusions.

## After this recipe

Complete specialist finance, time-series and risk education; this route neither qualifies trading decisions nor supplies investment advice.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)
- [ACM Computing Curricula Recommendations](profession-references.md#reference-acm-curricula)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
