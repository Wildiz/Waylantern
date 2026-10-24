# Learning curriculum: CloudOps Engineer

Operate a small cloud-style service using inventory, health checks and a controlled maintenance record.

[Home](../README.md) / [Curricula](curricula.md) / [Operations, platforms and IT support](professions-operations.md#roles-in-this-group)

**Target profile:** [CloudOps Engineer](professions-operations.md#cloudops-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Administer a basic Linux service.
- Understand cloud account permissions and that hosted services can incur charges.

**What you will produce:** An inventory, monitoring checklist and recovery record for a disposable practice deployment.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Map cloud resources and responsibilities](#stage-1)
2. [Make configuration repeatable](#stage-2)
3. [Write health and maintenance checks](#stage-3)
4. [Capstone: operate a disposable service](#stage-4)

<a id="stage-1"></a>
## 1. Map cloud resources and responsibilities

**Learn:**

- Service inventory
- Account and region boundaries

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [AWS Skill Builder](https://skillbuilder.aws/) — beginner in this topic; freemium access. [Details](area-devops.md#resource-aws-skill-builder).

**Practise:** Select introductory provider material and draw a hypothetical service using compute, storage and networking; label ownership and billing boundaries.

**Advance when:** Identify which resources would exist, who may change them and how they would be removed; reading does not require buying a lab.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Make configuration repeatable

**Learn:**

- Declared configuration
- State and cleanup

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Terraform Tutorials (HashiCorp Developer)](https://developer.hashicorp.com/terraform/tutorials) — intermediate in this topic; free access. [Details](area-devops.md#resource-terraform-tutorials).

**Practise:** Use the local Docker getting-started track to describe and recreate a practice resource without using a paid cloud account.

**Advance when:** Show the declared inputs, resulting state and successful removal; note differences from a real provider deployment.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Write health and maintenance checks

**Learn:**

- Service status and logs
- Backup and change windows

**Resource still needed:** A provider-specific reviewed CloudOps monitoring, backup and identity runbook is not available in the catalogue.

**Practise:** Draft checks for availability and resource pressure, then record a maintenance plan for the hypothetical cloud service.

**Advance when:** Each check has expected output, an escalation condition and an owner; recovery assumptions are explicitly identified.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone: operate a disposable service

**Learn:**

- Incident evidence
- Cost and resource closure

**Resource still needed:** The local simulation is an editorial operations exercise, not verification of live cloud availability or billing controls.

**Practise:** Recreate the local service, simulate one outage, restore it and reconcile the inventory with the resources left after cleanup.

**Advance when:** The report shows health before/after, the recovery timeline and evidence that no practice resources remain.

## After this recipe

Choose one provider and verify current monitoring, backup, identity and billing procedures before a supervised real deployment.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [CNCF certification exam objectives](profession-references.md#reference-cncf)
- [Microsoft Learn training directory](profession-references.md#reference-microsoft-learn)

[Back to roles in this group](professions-operations.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
