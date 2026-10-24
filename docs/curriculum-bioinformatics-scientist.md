# Learning curriculum: Bioinformatics Scientist

An editorial route that explicitly requires biology and assay-specific training beyond general data science.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [Bioinformatics Scientist](professions-data-ai.md#bioinformatics-scientist)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Molecular biology and genetics
- Basic Python and command-line use
- Probability and statistics
- Research data ethics

**What you will produce:** A documented analysis plan and small supervised biological-data study with provenance and assay limitations.

**Resource coverage:** 1 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Define the biological question and assay](#stage-1)
2. [Establish provenance and a reproducible data table](#stage-2)
3. [Select assay-specific quality checks and inference](#stage-3)
4. [Capstone - produce a bounded biological analysis report](#stage-4)

<a id="stage-1"></a>
## 1. Define the biological question and assay

**Learn:**

- Biological mechanism and hypothesis
- Assay measurement limits
- Experimental units and controls

**Resource still needed:** No verified molecular-biology or assay-design curriculum is currently catalogued; obtain domain instruction before selecting an analysis.

**Practise:** Describe one biological question and how a chosen assay could measure evidence relevant to it.

**Advance when:** Identify the biological replicate, a relevant control and a measurement limitation with domain-review input.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Establish provenance and a reproducible data table

**Learn:**

- Sample identifiers and metadata
- Data permissions and consent
- Reproducible parsing and joins

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [pandas Getting Started Tutorials](https://pandas.pydata.org/docs/getting_started/index.html) — beginner in this topic; free access. [Details](area-data.md#resource-pandas-getting-started).
- [Pro Git](https://git-scm.com/book/en/v2) — beginner in this topic; free access. [Details](area-software.md#resource-pro-git).

**Practise:** Use a permitted teaching dataset or synthetic metadata to create an auditable sample-to-file manifest.

**Advance when:** Every analysis row traces back to a sample and source; duplicates and missing identifiers are reported.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Select assay-specific quality checks and inference

**Learn:**

- Assay quality metrics
- Normalization and batch effects
- Multiple comparisons and uncertainty

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [OpenIntro Statistics](https://www.openintro.org/book/os/) — beginner in this topic; free access. [Details](area-data.md#resource-openintro-statistics).
- [Think Bayes (2nd edition)](https://allendowney.github.io/ThinkBayes2/) — intermediate in this topic; free access. [Details](area-data.md#resource-think-bayes).

**Resource still needed:** These resources cover statistical foundations, not sequencing, alignment or assay-specific normalization; verified specialist material is still missing.

**Practise:** Write a quality-control and analysis plan specifying which domain-specific decisions require review, then evaluate a small approved example.

**Advance when:** Separate statistical uncertainty from technical artefacts and avoid interpreting a batch effect as biology.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - produce a bounded biological analysis report

**Learn:**

- Biological interpretation
- Reproducible workflow and parameters
- Limitations and ethical reporting

**Resource still needed:** No verified end-to-end bioinformatics practical is available in the catalogue; a domain-appropriate teaching workflow and reviewer are required.

**Practise:** Complete the reviewed small study with an input manifest, parameter record, results and biological limitations.

**Advance when:** A reviewer can reproduce the workflow and trace each interpretation to evidence without exposing sensitive sample data.

## After this recipe

Study the relevant experimental and computational biology methods; generic Python or ML training does not replace them.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [ACM Computing Curricula Recommendations](profession-references.md#reference-acm-curricula)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
