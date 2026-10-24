# Learning curriculum: AIOps Engineer

Evaluate whether an anomaly detector helps operators find incidents without hiding false alarms.

[Home](../README.md) / [Curricula](curricula.md) / [Operations, platforms and IT support](professions-operations.md#roles-in-this-group)

**Target profile:** [AIOps Engineer](professions-operations.md#aiops-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Use Python and basic statistics.
- Understand service logs and the difference between metrics and incidents.

**What you will produce:** A documented baseline and anomaly experiment evaluated on labelled synthetic operational events.

**Resource coverage:** 1 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Build an operational event dataset](#stage-1)
2. [Establish a simple alert baseline](#stage-2)
3. [Compare an anomaly method](#stage-3)
4. [Capstone: propose an operator-facing alert](#stage-4)

<a id="stage-1"></a>
## 1. Build an operational event dataset

**Learn:**

- Time ordering
- Incident labels and missing data

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Microsoft Data Science for Beginners](https://github.com/microsoft/Data-Science-For-Beginners) — beginner in this topic; free access. [Details](area-data.md#resource-microsoft-data-science-for-beginners).

**Practise:** Prepare a small synthetic time series with normal intervals, missing values and known incident windows.

**Advance when:** Explain each label and preserve a time-ordered evaluation segment that was not used to tune the detector.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Establish a simple alert baseline

**Learn:**

- Threshold alerts
- Precision and recall

**Resource still needed:** No reviewed AIOps-specific evaluation resource is catalogued; this stage is an editorial operational-analysis exercise.

**Practise:** Use a fixed threshold before trying a model and count true alarms, false alarms and missed labelled incidents.

**Advance when:** Provide a confusion table and explain the operator cost of a false alarm versus a miss.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Compare an anomaly method

**Learn:**

- Temporal leakage
- Human review and drift

**Resource still needed:** A reviewed course on operational anomaly methods and safe AIOps integration is missing; do not treat general AI material as coverage.

**Practise:** Compare one simple anomaly score with the threshold on the held-out interval and inspect its largest errors.

**Advance when:** Report whether the method improves the chosen measure and document cases where it should not trigger automated remediation.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone: propose an operator-facing alert

**Learn:**

- Evidence summaries
- Escalation safeguards

**Resource still needed:** No reviewed resource covers this complete AIOps alert workflow; it remains an explicitly bounded editorial project.

**Practise:** Produce a mock alert containing evidence, uncertainty and the next diagnostic check; test it against both a true incident and a false alarm.

**Advance when:** An operator can distinguish a signal from a diagnosis and no remediation is executed automatically.

## After this recipe

Validate real alert usefulness and data handling under supervision before integrating any automated action.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-operations.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
