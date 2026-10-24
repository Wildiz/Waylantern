# Learning curriculum: Machine Learning Engineer

An editorial recipe connecting model evaluation to reproducible training and a small prediction interface.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [Machine Learning Engineer](professions-data-ai.md#machine-learning-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Python and basic software testing
- Linear algebra and elementary probability
- Basic data manipulation

**What you will produce:** A versioned training pipeline and prediction interface with tests, model metrics and reproducible inputs.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Establish data splits and a modelling baseline](#stage-1)
2. [Make training repeatable](#stage-2)
3. [Test a prediction boundary](#stage-3)
4. [Capstone - package an evaluated model service](#stage-4)

<a id="stage-1"></a>
## 1. Establish data splits and a modelling baseline

**Learn:**

- Feature and target definitions
- Training versus evaluation data
- Metrics and baseline models

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Machine Learning for Beginners (Microsoft)](https://github.com/microsoft/ML-For-Beginners) — beginner in this topic; free access. [Details](area-ai.md#resource-microsoft-ml-for-beginners).
- [Machine Learning Crash Course (Google)](https://developers.google.com/machine-learning/crash-course) — beginner in this topic; free access. [Details](area-ai.md#resource-google-machine-learning-crash-course).

**Practise:** Fit a baseline on a small teaching dataset and preserve an untouched evaluation split.

**Advance when:** Explain the metric, detect a deliberately leaked feature and remove it before the reported evaluation.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Make training repeatable

**Learn:**

- Preprocessing pipelines
- Experiment configuration
- Artefact and dependency records

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Made With ML](https://madewithml.com) — intermediate in this topic; free access. [Details](area-ai.md#resource-made-with-ml).
- [Machine Learning Zoomcamp (DataTalks.Club)](https://github.com/DataTalksClub/machine-learning-zoomcamp) — beginner in this topic; free access. [Details](area-data.md#resource-datatalks-machine-learning-zoomcamp).

**Practise:** Move the experiment from a notebook into a repeatable training command with saved settings and output metrics.

**Advance when:** Recreate a comparable model and evaluation from the recorded inputs and explain any nondeterminism.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Test a prediction boundary

**Learn:**

- Input contracts and invalid data
- Training-serving consistency
- Model and software tests

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/) — intermediate in this topic; free access. [Details](area-web.md#resource-fastapi-tutorial).
- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).

**Practise:** Expose a small local prediction interface and test valid records, missing fields and preprocessing consistency.

**Advance when:** Invalid requests fail explicitly and a saved example receives the same preprocessing during training and prediction.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - package an evaluated model service

**Learn:**

- Model versioning
- Evaluation regression checks
- Monitoring and rollback design

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [MLOps Zoomcamp (DataTalks.Club)](https://github.com/DataTalksClub/mlops-zoomcamp) — intermediate in this topic; free access. [Details](area-ai.md#resource-datatalks-mlops-zoomcamp).

**Practise:** Deliver training code, an evaluation report, the local service and a documented plan to detect model degradation and restore a previous artefact.

**Advance when:** Rebuild and test the service from the recorded artefacts and demonstrate switching between two declared model versions.

## After this recipe

Study production data quality, deployment and model monitoring in the chosen environment; a local service is not proof of production readiness.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [CS2023 — Computer Science Curricula](profession-references.md#reference-cs2023)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
