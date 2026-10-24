# Learning curriculum: MLOps Engineer

Make a trained model reproducible, deployable and observable through a small service lifecycle.

[Home](../README.md) / [Curricula](curricula.md) / [Operations, platforms and IT support](professions-operations.md#roles-in-this-group)

**Target profile:** [MLOps Engineer](professions-operations.md#mlops-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Use Python, Git and Docker confidently.
- Train and evaluate a simple model; the linked MLOps course expects substantial programming practice.

**What you will produce:** A reproducible model experiment, versioned serving artifact and monitoring/retraining decision record.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Reproduce a baseline experiment](#stage-1)
2. [Track and package the model](#stage-2)
3. [Define operational checks](#stage-3)
4. [Capstone: recover a model release](#stage-4)

<a id="stage-1"></a>
## 1. Reproduce a baseline experiment

**Learn:**

- Data and parameter versions
- Evaluation split

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Machine Learning Zoomcamp (DataTalks.Club)](https://github.com/DataTalksClub/machine-learning-zoomcamp) — beginner in this topic; free access. [Details](area-data.md#resource-datatalks-machine-learning-zoomcamp).

**Practise:** Train a small model on a fixed public or synthetic dataset and save parameters, split rules and evaluation results.

**Advance when:** A repeat run can be traced to the same data and settings without leakage from the evaluation set.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Track and package the model

**Learn:**

- Experiment tracking
- Serving interfaces

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [MLOps Zoomcamp (DataTalks.Club)](https://github.com/DataTalksClub/mlops-zoomcamp) — intermediate in this topic; free access. [Details](area-ai.md#resource-datatalks-mlops-zoomcamp).

**Practise:** Follow the relevant tracking and deployment material to package the chosen model behind a local prediction endpoint.

**Advance when:** A request returns the expected response and the running artifact can be linked to a recorded experiment.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Define operational checks

**Learn:**

- Prediction quality signals
- Drift and retraining triggers

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [MLOps Zoomcamp (DataTalks.Club)](https://github.com/DataTalksClub/mlops-zoomcamp) — intermediate in this topic; free access. [Details](area-ai.md#resource-datatalks-mlops-zoomcamp).

**Practise:** Use synthetic shifted inputs to compare baseline and changed traffic, then write a proposed retraining trigger.

**Advance when:** Separate observed input change from unmeasured real-world prediction quality and explain when labels would be needed.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone: recover a model release

**Learn:**

- Version rollback
- Monitoring handover

**Resource still needed:** The complete release-and-recovery exercise is editorial; the course supplies lifecycle topics rather than this exact assignment.

**Practise:** Release a second model locally, compare its recorded checks with the baseline and restore the first version when a chosen check fails.

**Advance when:** A fresh operator can locate the model version, reproduce a prediction and follow the documented rollback decision.

## After this recipe

Practise delayed labels, privacy and supervised production monitoring before managing live model services.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [CNCF certification exam objectives](profession-references.md#reference-cncf)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-operations.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
