# Learning curriculum: Platform Engineer

Build a small reusable development capability and check whether a second developer can use it.

[Home](../README.md) / [Curricula](curricula.md) / [Operations, platforms and IT support](professions-operations.md#roles-in-this-group)

**Target profile:** [Platform Engineer](professions-operations.md#platform-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Build a containerised service and use Git.
- Understand basic developer workflows and Linux tooling.

**What you will produce:** A reusable local project template with a clear interface, ownership notes and an observed setup trial.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Find a recurring developer task](#stage-1)
2. [Build the smallest paved path](#stage-2)
3. [Set support and change expectations](#stage-3)
4. [Capstone: observe a fresh setup](#stage-4)

<a id="stage-1"></a>
## 1. Find a recurring developer task

**Learn:**

- User needs
- Workflow friction

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Open Practice Library](https://github.com/openpracticelibrary/openpracticelibrary) — intermediate in this topic; free access. [Details](area-design-product.md#resource-open-practice-library).

**Practise:** Interview a willing developer or record clearly labelled assumptions about starting a new service; choose one repeated setup problem.

**Advance when:** State the target user, repeated task and an observable sign of improvement without treating workshop guesses as validated needs.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Build the smallest paved path

**Learn:**

- Reusable configuration
- Service boundaries

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Docker Docs: Get started](https://docs.docker.com/get-started/) — beginner in this topic; free access. [Details](area-devops.md#resource-docker-docs-get-started).
- [Container Training](https://github.com/jpetazzo/container.training) — intermediate in this topic; free access. [Details](area-devops.md#resource-container-training).

**Practise:** Package a minimal containerised service template with a start command, a health check and documented configuration inputs.

**Advance when:** A clean copy starts successfully with explicit prerequisites and no embedded credentials.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Set support and change expectations

**Learn:**

- Versioning and ownership
- Escape hatches and upgrades

**Resource still needed:** No reviewed platform-product or internal-developer-platform lifecycle guide is catalogued.

**Practise:** Write the template contract: supported inputs, update policy, responsible maintainer and what users should do when it cannot meet a need.

**Advance when:** A user can tell which behaviours are promised and which customisations fall outside the supported path.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone: observe a fresh setup

**Learn:**

- Developer experience evidence
- Support feedback

**Resource still needed:** This is an editorial platform-capability project, not a verified enterprise platform curriculum or a production readiness claim.

**Practise:** Ask another person to start a service from the template, or label a clean-machine self-trial explicitly, and fix one observed obstacle.

**Advance when:** Record setup success, the obstacle, the resulting change and a basic recovery procedure.

## After this recipe

Expand only after collecting user feedback; practise tenancy, access control and sustainable support before serving multiple teams.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [CNCF certification exam objectives](profession-references.md#reference-cncf)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-operations.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
