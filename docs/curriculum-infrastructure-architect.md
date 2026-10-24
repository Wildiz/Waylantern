# Learning curriculum: Infrastructure Architect

An editorial lab for relating compute, storage, configuration and recovery to a service's operating requirements.

[Home](../README.md) / [Curricula](curricula.md) / [Architecture and systems design](professions-architecture.md#roles-in-this-group)

**Target profile:** [Infrastructure Architect](professions-architecture.md#infrastructure-architect)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Have administered Linux systems and diagnosed a service or storage problem.
- Can explain network ports, permissions and the difference between process and data persistence.
- Have access to an isolated local container environment for the practice work.

**What you will produce:** A reproducible local service foundation with an inventory, infrastructure definition and tested rebuild evidence.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Inventory the foundations and their constraints](#stage-1)
2. [Choose an isolation and storage arrangement](#stage-2)
3. [Express the local infrastructure as a repeatable definition](#stage-3)
4. [Deliver a rebuild-and-recovery mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Inventory the foundations and their constraints

**Learn:**

- Host resources
- Service dependencies
- Permissions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Linux Upskill Challenge](https://github.com/livialima/linuxupskillchallenge) — beginner in this topic; free access. [Details](area-it-support.md#resource-linux-upskill-challenge).

**Practise:** Document a local web-service lab's host, listening port, process owner, configuration and data locations; record a basic service-status and log check.

**Advance when:** The inventory distinguishes the service's configuration, executable files and persistent data and identifies the account allowed to change each.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Choose an isolation and storage arrangement

**Learn:**

- Container boundaries
- Volumes
- Resource assumptions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Docker Docs: Get started](https://docs.docker.com/get-started/) — beginner in this topic; free access. [Details](area-devops.md#resource-docker-docs-get-started).

**Practise:** Run the lab service in a container, keep its required data outside the ephemeral process and compare that arrangement with a dedicated host on paper.

**Advance when:** Restarting or replacing the container leaves the intended data available, and the comparison names a limitation of container isolation.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Express the local infrastructure as a repeatable definition

**Learn:**

- Infrastructure as code
- State
- Planned changes

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Terraform Tutorials (HashiCorp Developer)](https://developer.hashicorp.com/terraform/tutorials) — intermediate in this topic; free access. [Details](area-devops.md#resource-terraform-tutorials).

**Practise:** Follow the Docker tutorial track in a disposable environment, save the infrastructure definition and compare a planned change before applying it; do not use a paid cloud track for this exercise.

**Advance when:** The same definition recreates the expected local resource, and you can explain the role and sensitivity of the state file.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver a rebuild-and-recovery mini-project

**Learn:**

- Rebuild procedure
- Data restoration
- Operational evidence

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Linux Upskill Challenge](https://github.com/livialima/linuxupskillchallenge) — beginner in this topic; free access. [Details](area-it-support.md#resource-linux-upskill-challenge).
- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).

**Practise:** Package the inventory and definitions, back up a small invented data file, remove only the disposable service and rebuild it; document manual restoration and remaining single points of failure.

**Advance when:** A fresh lab instance exposes the expected service and recovered sample data, with recorded commands and checks rather than an untested claim of high availability.

## After this recipe

Expand the design with an operations team to cover real capacity, backup retention and failure testing; a local rebuild does not establish production resilience.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-architecture.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
