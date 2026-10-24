# Learning curriculum: AI Engineer

An editorial route from an explicit user task to a bounded AI application with measurable failure handling.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [AI Engineer](professions-data-ai.md#ai-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Python programming
- Basic HTTP and application development
- Introductory algebra and statistics

**What you will produce:** A small AI-backed feature with a baseline, evaluation set, cost record and documented limitations.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Define the task and a non-model baseline](#stage-1)
2. [Build a narrow application boundary](#stage-2)
3. [Measure behavior and resource use](#stage-3)
4. [Capstone - deliver a bounded AI feature](#stage-4)

<a id="stage-1"></a>
## 1. Define the task and a non-model baseline

**Learn:**

- Inputs and expected outputs
- Task-specific acceptance criteria
- Data permissions and misuse boundaries

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [AI for Beginners (Microsoft)](https://github.com/microsoft/AI-For-Beginners) — beginner in this topic; free access. [Details](area-ai.md#resource-microsoft-ai-for-beginners).
- [Generative AI for Beginners (Microsoft)](https://github.com/microsoft/generative-ai-for-beginners) — beginner in this topic; free access. [Details](area-ai.md#resource-microsoft-generative-ai-for-beginners).

**Practise:** Choose one small task such as answering questions over permitted notes and define cases where the feature should decline an answer.

**Advance when:** Write an evaluation set and a simple baseline before selecting a model or provider.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Build a narrow application boundary

**Learn:**

- Model API or local-model interface
- Input and output validation
- Retrieval and source handling

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [LLM Zoomcamp (DataTalks.Club)](https://github.com/DataTalksClub/llm-zoomcamp) — intermediate in this topic; free access. [Details](area-ai.md#resource-datatalks-llm-zoomcamp).
- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/) — intermediate in this topic; free access. [Details](area-web.md#resource-fastapi-tutorial).

**Practise:** Implement one model-backed endpoint with clear inputs, outputs and handling for unavailable dependencies.

**Advance when:** Demonstrate a successful request and an explicit failure path without exposing credentials or private data.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Measure behavior and resource use

**Learn:**

- Task evaluation and error analysis
- Latency and usage cost
- Unsupported answers and adversarial inputs

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [OpenAI Cookbook](https://cookbook.openai.com) — intermediate in this topic; free access. [Details](area-ai.md#resource-openai-cookbook).
- [Made With ML](https://madewithml.com) — intermediate in this topic; free access. [Details](area-ai.md#resource-made-with-ml).

**Practise:** Compare the feature with the baseline on the saved cases and record incorrect answers, time and any provider charges.

**Advance when:** Report both successes and failures and show that a model change can be evaluated against the same cases.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - deliver a bounded AI feature

**Learn:**

- Reproducible configuration
- Operational fallbacks
- User-visible limitations

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [The Full Stack (Full Stack Deep Learning and LLM Bootcamp)](https://fullstackdeeplearning.com) — intermediate in this topic; free access. [Details](area-ai.md#resource-full-stack-deep-learning).

**Practise:** Package the feature, evaluation script, configuration example without secrets and a short operating guide; use local inference or explicitly budget external API use.

**Advance when:** A fresh run reproduces the evaluation and demonstrates graceful handling of an unsupported question or model outage.

## After this recipe

Add authentication, monitoring and domain review before real deployment; model availability and provider costs require separate checking.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [CS2023 — Computer Science Curricula](profession-references.md#reference-cs2023)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)
- [AI for Beginners](profession-references.md#reference-microsoft-ai)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
