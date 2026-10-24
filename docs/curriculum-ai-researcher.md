# Learning curriculum: AI Researcher

An editorial research recipe for comparing hypotheses, implementations and experimental evidence in AI.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [AI Researcher](professions-data-ai.md#ai-researcher)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Python and a deep learning framework
- Linear algebra calculus and probability
- Ability to read ML papers
- Access to a bounded compute budget

**What you will produce:** A small reproducibility report with a baseline, controlled extension and explicit limits on research claims.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Refresh the model and objective](#stage-1)
2. [Reconstruct one published experiment](#stage-2)
3. [Test one research hypothesis](#stage-3)
4. [Capstone - write an auditable research note](#stage-4)

<a id="stage-1"></a>
## 1. Refresh the model and objective

**Learn:**

- Optimization and loss functions
- Model assumptions
- Evaluation tasks and metrics

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Dive into Deep Learning (d2l.ai)](https://d2l.ai) — intermediate in this topic; free access. [Details](area-ai.md#resource-d2l-dive-into-deep-learning).
- [Mathematics for Machine Learning (book)](https://mml-book.github.io/) — intermediate in this topic; free access. [Details](area-ai.md#resource-mathematics-for-machine-learning).

**Practise:** Derive or explain the objective for a small model and verify the training loop on a tiny input.

**Advance when:** Trace the objective, gradients and evaluation metric without relying only on an opaque training command.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Reconstruct one published experiment

**Learn:**

- Data and preprocessing choices
- Hyperparameters and compute
- Baseline reproduction

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [PyProbML Notebooks](https://github.com/probml/pyprobml) — advanced in this topic; free access. [Details](area-ai.md#resource-pyprobml-notebooks).
- [Stanford CS336 - Language Modeling from Scratch](https://cs336.stanford.edu) — advanced in this topic; free access. [Details](area-ai.md#resource-stanford-cs336).

**Practise:** Select one manageable documented experiment and record which original details and artefacts are available.

**Advance when:** Separate a faithful reproduction from unavoidable deviations and report whether the baseline is reproduced within stated variation.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Test one research hypothesis

**Learn:**

- Controlled ablations
- Multiple runs and uncertainty
- Negative results and confounders

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Think Stats (3rd edition)](https://allendowney.github.io/ThinkStats/) — beginner in this topic; free access. [Details](area-data.md#resource-think-stats).
- [Dive into Deep Learning (d2l.ai)](https://d2l.ai) — intermediate in this topic; free access. [Details](area-ai.md#resource-d2l-dive-into-deep-learning).

**Practise:** Change one justified element of the baseline and evaluate it under the same data and resource constraints.

**Advance when:** Report a comparison across repeated runs and identify alternative explanations for any observed improvement.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - write an auditable research note

**Learn:**

- Claim and evidence alignment
- Reproducible artefacts
- Limitations and future experiments

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Pro Git](https://git-scm.com/book/en/v2) — beginner in this topic; free access. [Details](area-software.md#resource-pro-git).
- [Project Jupyter](https://jupyter.org/) — all in this topic; free access. [Details](area-data.md#resource-project-jupyter).

**Resource still needed:** General research supervision, peer review and literature-method training are not supplied by these software resources.

**Practise:** Deliver the hypothesis, baseline, extension, raw results, configuration and a short report that includes failures and compute use.

**Advance when:** Every major claim points to an experiment or cited source and a fresh run can reconstruct the main comparison.

## After this recipe

Seek specialist supervision and broader literature review before claiming novelty or general scientific conclusions.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Computer Science curriculum recommendations project](profession-references.md#reference-cs2023)
- [ACM Computing Curricula Recommendations](profession-references.md#reference-acm-curricula)
- [AI for Beginners](profession-references.md#reference-microsoft-ai)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
