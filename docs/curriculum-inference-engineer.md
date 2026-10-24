# Learning curriculum: Inference Engineer

An editorial performance route for an existing model, with explicit gaps in backend-specific optimization.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [Inference Engineer](professions-data-ai.md#inference-engineer)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Model inference and deployment experience
- Python and systems profiling basics
- Understanding latency and throughput
- Access to suitable local compute

**What you will produce:** A repeatable benchmark showing an inference tradeoff with correctness, resource and workload controls.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Specify the serving workload](#stage-1)
2. [Profile the unoptimized path](#stage-2)
3. [Evaluate one controlled optimization](#stage-3)
4. [Capstone - produce a defensible serving benchmark](#stage-4)

<a id="stage-1"></a>
## 1. Specify the serving workload

**Learn:**

- Latency distributions and throughput
- Workload size and concurrency
- Model correctness tolerances

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [The Full Stack (Full Stack Deep Learning and LLM Bootcamp)](https://fullstackdeeplearning.com) — intermediate in this topic; free access. [Details](area-ai.md#resource-full-stack-deep-learning).
- [Made With ML](https://madewithml.com) — intermediate in this topic; free access. [Details](area-ai.md#resource-made-with-ml).

**Practise:** Choose a small existing model and define representative request sizes, concurrency and a reference output set.

**Advance when:** Publish a benchmark protocol separating cold start from steady-state measurements and explaining the quality tolerance.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Profile the unoptimized path

**Learn:**

- Preprocessing and model time
- Memory and transfer costs
- Measurement noise

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Dive into Deep Learning (d2l.ai)](https://d2l.ai) — intermediate in this topic; free access. [Details](area-ai.md#resource-d2l-dive-into-deep-learning).

**Resource still needed:** The textbook supplies model-computation foundations; a verified profiler and serving-backend performance guide are not yet catalogued.

**Practise:** Break a local request into measured stages and repeat measurements under recorded hardware and software conditions.

**Advance when:** Identify the dominant measured cost with repeated observations rather than assuming the model is the bottleneck.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Evaluate one controlled optimization

**Learn:**

- Batching and concurrency
- Precision and output tolerance
- Resource versus latency tradeoffs

**Resource still needed:** No verified runtime-specific quantization, compiler or inference-server optimization curriculum is currently catalogued.

**Practise:** Following suitable backend documentation, change one setting at a time and compare latency, throughput, memory and output differences.

**Advance when:** Demonstrate a measured improvement or negative result while preserving the declared correctness tolerance.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - produce a defensible serving benchmark

**Learn:**

- Reproducible load generation
- Quality regression gates
- Deployment recommendations and limits

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Made With ML](https://madewithml.com) — intermediate in this topic; free access. [Details](area-ai.md#resource-made-with-ml).

**Practise:** Deliver benchmark inputs, raw measurements, baseline and optimized configurations and a recommendation tied to the target workload.

**Advance when:** Another run reproduces the direction of the result and the report identifies workloads or hardware where it may not hold.

## After this recipe

Add verified backend documentation and capacity testing before operational deployment; rented accelerators may incur costs.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [CS2023 — Computer Science Curricula](profession-references.md#reference-cs2023)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
