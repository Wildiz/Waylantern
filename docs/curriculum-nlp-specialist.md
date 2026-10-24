# Learning curriculum: Natural Language Processing Specialist

An editorial route from text representation to error analysis and a reproducible language-processing project.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [Natural Language Processing Specialist](professions-data-ai.md#nlp-specialist)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Python and basic machine learning
- Linear algebra and probability
- Understanding training and evaluation splits

**What you will produce:** A small text-processing system with a baseline, held-out evaluation and language-specific error analysis.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Define the text task and inspect its data](#stage-1)
2. [Compare text representations](#stage-2)
3. [Investigate language-specific failures](#stage-3)
4. [Capstone - deliver a bounded NLP experiment](#stage-4)

<a id="stage-1"></a>
## 1. Define the text task and inspect its data

**Learn:**

- Language and annotation conventions
- Text normalization and leakage
- Task-specific metrics

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [AI for Beginners (Microsoft)](https://github.com/microsoft/AI-For-Beginners) — beginner in this topic; free access. [Details](area-ai.md#resource-microsoft-ai-for-beginners).
- [Hugging Face Course](https://github.com/huggingface/course) — intermediate in this topic; free access. [Details](area-ai.md#resource-huggingface-llm-course).

**Practise:** Choose a bounded task such as classifying short texts and inspect examples, labels and duplicate documents.

**Advance when:** State the unit of prediction, identify label ambiguity and create an evaluation split that avoids duplicated-text leakage.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Compare text representations

**Learn:**

- Tokenization and vocabulary
- Sparse features and embeddings
- Baseline classification

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Machine Learning for Beginners (Microsoft)](https://github.com/microsoft/ML-For-Beginners) — beginner in this topic; free access. [Details](area-ai.md#resource-microsoft-ml-for-beginners).
- [Stanford CS224N - NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) — advanced in this topic; free access. [Details](area-ai.md#resource-stanford-cs224n).

**Practise:** Build a simple representation-based baseline before using a more complex pretrained model.

**Advance when:** Explain how tokens become model inputs and compare the approaches using the same metric and split.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Investigate language-specific failures

**Learn:**

- Class imbalance and rare expressions
- Language variation and bias
- Error categories and uncertainty

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Hugging Face Course](https://github.com/huggingface/course) — intermediate in this topic; free access. [Details](area-ai.md#resource-huggingface-llm-course).
- [Stanford CS224N - NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) — advanced in this topic; free access. [Details](area-ai.md#resource-stanford-cs224n).

**Practise:** Group mistakes by meaningful text characteristics and test a few controlled variations of wording.

**Advance when:** Provide examples of systematic failure and distinguish measured behavior from an assumption about all speakers or languages.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - deliver a bounded NLP experiment

**Learn:**

- Data and model permissions
- Reproducible preprocessing
- Evaluation and model limitations

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Made With ML](https://madewithml.com) — intermediate in this topic; free access. [Details](area-ai.md#resource-made-with-ml).

**Practise:** Package the text task, preprocessing, baseline, selected model and evaluation report using permitted data without personal information.

**Advance when:** Reproduce the comparison and document which languages, domains and input conditions were actually evaluated.

## After this recipe

Add linguistics and domain-specific annotation methods; performance on one text collection does not establish general language understanding.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [CS2023 — Computer Science Curricula](profession-references.md#reference-cs2023)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)
- [AI for Beginners](profession-references.md#reference-microsoft-ai)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
