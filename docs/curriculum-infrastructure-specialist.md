# Learning curriculum: Infrastructure Specialist

Connect compute, storage and networking requirements to a small reproducible infrastructure lab.

[Home](../README.md) / [Curricula](curricula.md) / [Operations, platforms and IT support](professions-operations.md#roles-in-this-group)

**Target profile:** [Infrastructure Specialist](professions-operations.md#infrastructure-specialist)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Administer a basic operating-system service.
- Understand IP addressing and resource limits.

**What you will produce:** A dependency inventory and reproducible local infrastructure setup with capacity and recovery notes.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Map the infrastructure boundary](#stage-1)
2. [Inspect capacity and connectivity](#stage-2)
3. [Reproduce a controlled configuration](#stage-3)
4. [Capstone: deliver an infrastructure handover](#stage-4)

<a id="stage-1"></a>
## 1. Map the infrastructure boundary

**Learn:**

- Compute, storage and network roles
- Resource ownership

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [The System Design Primer](https://github.com/donnemartin/system-design-primer) — intermediate in this topic; free access. [Details](area-cs.md#resource-system-design-primer).

**Practise:** Diagram the infrastructure used by a small practice service and identify dependencies outside the operator's control.

**Advance when:** Each component has an observable function and a recorded ownership assumption.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Inspect capacity and connectivity

**Learn:**

- CPU, memory and storage observations
- Network reachability

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Linux Upskill Challenge](https://github.com/livialima/linuxupskillchallenge) — beginner in this topic; free access. [Details](area-it-support.md#resource-linux-upskill-challenge).
- [Computer Networks: A Systems Approach](https://github.com/SystemsApproach/book) — intermediate in this topic; free access. [Details](area-networking.md#resource-computer-networks-systems-approach).

**Practise:** Record local resource observations and the expected network path, then identify one potential constraint without guessing production capacity.

**Advance when:** The evidence distinguishes measured usage from an untested scaling estimate.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Reproduce a controlled configuration

**Learn:**

- Infrastructure definitions
- State and removal

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Terraform Tutorials (HashiCorp Developer)](https://developer.hashicorp.com/terraform/tutorials) — intermediate in this topic; free access. [Details](area-devops.md#resource-terraform-tutorials).

**Practise:** Use the local Docker track to create a practice resource and repeat its setup and teardown from declared configuration.

**Advance when:** A clean run creates the expected local resource and cleanup is verified without affecting shared infrastructure.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone: deliver an infrastructure handover

**Learn:**

- Failure and recovery evidence
- Capacity and ownership notes

**Resource still needed:** The complete infrastructure assignment is editorial; no reviewed resource covers all physical, cloud, backup and enterprise infrastructure responsibilities.

**Practise:** Combine the diagram, configuration, checks and one local failure/recovery demonstration into an operator handover.

**Advance when:** Another person can identify dependencies, reproduce the local setup and explain what real hardware or cloud behaviour remains untested.

## After this recipe

Choose a compute, storage or network specialisation and gain supervised practice with the relevant current platform manuals.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-operations.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
