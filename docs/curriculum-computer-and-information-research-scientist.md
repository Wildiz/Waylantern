# Learning curriculum: Computer and Information Research Scientist

An editorial research-method recipe built on prior computer science education, with a literature-method gap made explicit.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [Computer and Information Research Scientist](professions-data-ai.md#computer-and-information-research-scientist)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Undergraduate algorithms and discrete mathematics
- Strong programming skills
- Ability to read technical papers

**What you will produce:** A small research-style artefact comparing a proposed method with a baseline under stated assumptions.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [State the problem and formal assumptions](#stage-1)
2. [Position a research question in existing work](#stage-2)
3. [Implement a controlled comparison](#stage-3)
4. [Capstone - publish a local research artefact](#stage-4)

<a id="stage-1"></a>
## 1. State the problem and formal assumptions

**Learn:**

- Problem definitions and models
- Complexity and invariants
- Baseline selection

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [MIT 6.006 Introduction to Algorithms (Spring 2020)](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — intermediate in this topic; free access. [Details](area-cs.md#resource-mit-6006-introduction-to-algorithms).
- [Mathematics for Computer Science (MIT 6.042 text)](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf) — intermediate in this topic; free access. [Details](area-cs.md#resource-mit-mathematics-for-computer-science).

**Practise:** Choose a bounded computational problem and specify inputs, outputs and a baseline algorithm.

**Advance when:** Explain the correctness conditions and asymptotic cost of the baseline before optimizing it.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Position a research question in existing work

**Learn:**

- Literature search and critical reading
- Reproduction versus novelty
- Research ethics and attribution

**Resource still needed:** No verified general research-methods or literature-review curriculum is currently catalogued; specialist supervision or an appropriate methods source is still needed.

**Practise:** Build an annotated comparison of a few relevant papers and mark every claim you have not independently checked.

**Advance when:** Distinguish a reproduced result, a proposed extension and an unsupported novelty claim.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Implement a controlled comparison

**Learn:**

- Reference implementations
- Experimental controls
- Performance and correctness measurements

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Pytudes](https://github.com/norvig/pytudes) — intermediate in this topic; free access. [Details](area-cs.md#resource-norvig-pytudes).
- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).

**Practise:** Implement the baseline and one bounded variation with correctness tests and a documented measurement procedure.

**Advance when:** Show equivalent outputs on declared test cases and separate run-to-run variation from an apparent improvement.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - publish a local research artefact

**Learn:**

- Reproducibility instructions
- Negative results
- Threats to validity

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Pro Git](https://git-scm.com/book/en/v2) — beginner in this topic; free access. [Details](area-software.md#resource-pro-git).
- [Project Jupyter](https://jupyter.org/) — all in this topic; free access. [Details](area-data.md#resource-project-jupyter).

**Practise:** Prepare a versioned implementation, input generator or permitted dataset, experiment script and short research report.

**Advance when:** A fresh local run reproduces the reported comparison and the report states what remains unproven.

## After this recipe

Seek field-specific methods training and peer feedback; a small research artefact is not equivalent to a research degree or publication.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [ACM Computing Curricula Recommendations](profession-references.md#reference-acm-curricula)
- [CS2023 — Computer Science Curricula](profession-references.md#reference-cs2023)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
