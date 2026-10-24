# Learning curriculum: Cloud Software Engineer

Make an application portable and observable in a local cloud-style lab.

[Home](../README.md) / [Curricula](curricula.md) / [Software, interfaces and embedded systems](professions-software.md#roles-in-this-group)

**Target profile:** [Cloud Software Engineer](professions-software.md#cloud-software-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- A working small application
- Basic Linux commands
- HTTP and Git

**What you will produce:** A containerized local service with external configuration, readiness checks and recovery evidence.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Separate configuration and state](#stage-1)
2. [Build a portable service](#stage-2)
3. [Observe dependency failures](#stage-3)
4. [Deliver a recovery mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Separate configuration and state

**Learn:**

- External settings
- Persistent state
- Application logs

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Docker Docs: Get started](https://docs.docker.com/get-started/) — beginner in this topic; free access. [Details](area-devops.md#resource-docker-docs-get-started).

**Practise:** Move settings out of application code and identify the records that must survive restart.

**Advance when:** Change a non-secret setting without editing source and locate the persisted sample data.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Build a portable service

**Learn:**

- Container images
- Ports and volumes
- Process lifecycle

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Docker Docs: Get started](https://docs.docker.com/get-started/) — beginner in this topic; free access. [Details](area-devops.md#resource-docker-docs-get-started).
- [Container Training](https://github.com/jpetazzo/container.training) — intermediate in this topic; free access. [Details](area-devops.md#resource-container-training).

**Practise:** Containerize the service and run it with a disposable local database volume.

**Advance when:** Rebuild the image and retrieve the saved sample record from the retained volume.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Observe dependency failures

**Learn:**

- Readiness checks
- Timeouts
- Recovery behavior

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Container Training](https://github.com/jpetazzo/container.training) — intermediate in this topic; free access. [Details](area-devops.md#resource-container-training).
- [The System Design Primer](https://github.com/donnemartin/system-design-primer) — intermediate in this topic; free access. [Details](area-cs.md#resource-system-design-primer).

**Practise:** Stop the local dependency and compare logs and readiness before and after recovery.

**Advance when:** Show an unavailable readiness result during the outage and a successful request after recovery.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver a recovery mini-project

**Learn:**

- Deployment configuration
- Version rollback
- Resource observations

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Container Training](https://github.com/jpetazzo/container.training) — intermediate in this topic; free access. [Details](area-devops.md#resource-container-training).
- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).

**Practise:** Provide repeatable local deployment instructions, a previous image version and a measured restart exercise.

**Advance when:** Recreate the lab and roll back while preserving the agreed sample records.

## After this recipe

Choose a cloud provider only when needed, check billing explicitly and study its access model before provisioning resources.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Software Engineering Body of Knowledge](profession-references.md#reference-swebok)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)
- [CNCF certification exam objectives](profession-references.md#reference-cncf)

[Back to roles in this group](professions-software.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
