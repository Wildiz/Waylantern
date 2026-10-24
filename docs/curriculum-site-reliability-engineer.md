# Learning curriculum: Site Reliability Engineer

Measure a small service, define a user-facing reliability target and practise recovery from one failure.

[Home](../README.md) / [Curricula](curricula.md) / [Operations, platforms and IT support](professions-operations.md#roles-in-this-group)

**Target profile:** [Site Reliability Engineer](professions-operations.md#site-reliability-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Program and test a small service.
- Read Linux logs and understand basic HTTP responses.

**What you will produce:** A reproducible service lab with a measured reliability indicator, failure exercise and learning review.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Identify the user-visible service](#stage-1)
2. [Define a measurable objective](#stage-2)
3. [Exercise safe recovery](#stage-3)
4. [Capstone: learn from an outage](#stage-4)

<a id="stage-1"></a>
## 1. Identify the user-visible service

**Learn:**

- Request outcomes
- Dependencies and failure modes

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [The System Design Primer](https://github.com/donnemartin/system-design-primer) — intermediate in this topic; free access. [Details](area-cs.md#resource-system-design-primer).

**Practise:** Draw the request path of a tiny local service and distinguish latency, errors and complete unavailability.

**Advance when:** Each selected metric has a defined observation point and a user-visible meaning.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Define a measurable objective

**Learn:**

- Service-level indicators
- Objective windows and error budgets

**Resource still needed:** No reviewed SRE objectives or error-budget guide is currently catalogued; this stage states explicit editorial assumptions.

**Practise:** Choose a success indicator, a time window and a hypothetical objective; calculate results from a synthetic request log.

**Advance when:** Show the numerator, denominator and remaining failure allowance without claiming it is an industry-mandated target.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Exercise safe recovery

**Learn:**

- Failure injection
- Rollback and evidence

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Container Training](https://github.com/jpetazzo/container.training) — intermediate in this topic; free access. [Details](area-devops.md#resource-container-training).

**Practise:** Stop a dependency in a disposable service lab, observe the effect and restore it using a recorded procedure.

**Advance when:** Requests and logs demonstrate the failure and recovery, not merely a restarted process.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone: learn from an outage

**Learn:**

- Timeline and contributing factors
- Follow-up actions

**Resource still needed:** A complete reviewed SRE incident-management curriculum is missing; this capstone is a bounded service experiment.

**Practise:** Combine the indicator, outage evidence and a short review that separates observation, hypothesis and corrective action.

**Advance when:** The review names one measurable reliability improvement and how its effect would be checked.

## After this recipe

Practise on-call, capacity planning and production changes under supervision; a local outage exercise is not operational experience.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [CNCF certification exam objectives](profession-references.md#reference-cncf)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-operations.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
