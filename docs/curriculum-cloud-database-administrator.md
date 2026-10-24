# Learning curriculum: Cloud Database Administrator

An editorial managed-database operations recipe with explicit provider-specific training gaps and cost boundaries.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [Cloud Database Administrator](professions-data-ai.md#cloud-database-administrator)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Relational database administration basics
- Networking and access-control fundamentals
- Familiarity with cloud accounts and billing

**What you will produce:** A provider-specific practice plan or disposable deployment with documented access, recovery and cost controls.

**Resource coverage:** 0 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Compare managed-service responsibilities](#stage-1)
2. [Design a narrow access path](#stage-2)
3. [Validate recovery and operational visibility](#stage-3)
4. [Capstone - produce a managed-database operating dossier](#stage-4)

<a id="stage-1"></a>
## 1. Compare managed-service responsibilities

**Learn:**

- Service tiers and availability
- Shared operational responsibilities
- Billing and lifecycle limits

**Resource still needed:** No verified managed-database service curriculum is currently catalogued; current provider documentation is required before provisioning anything.

**Practise:** Create a responsibility and cost checklist for one provider and mark which operations remain the customer's responsibility.

**Advance when:** Identify the exact service, region, expected charges and teardown procedure; do not equate a free course with a free database.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Design a narrow access path

**Learn:**

- Network reachability
- Database and cloud identities
- Secret handling

**Resource still needed:** No verified provider-specific private-connectivity and database-identity practical is available in the catalogue.

**Practise:** Draft the network and identity configuration for a disposable instance, or apply it only in an authorized budgeted training account.

**Advance when:** Explain the intended allowed path, how denied access is tested and where credentials are stored without publishing their values.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Validate recovery and operational visibility

**Learn:**

- Backup retention and restore targets
- Monitoring and maintenance windows
- Availability versus data recovery

**Resource still needed:** Recovery and monitoring behavior depends on provider and service tier; no verified service-specific lab is currently catalogued.

**Practise:** Write a reviewed restore drill and alert checklist; if executing in an approved account, restore only disposable teaching data.

**Advance when:** Distinguish documented provider capabilities from personally tested recovery evidence and record any unperformed steps.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - produce a managed-database operating dossier

**Learn:**

- Access and recovery evidence
- Cost review and teardown
- Responsibility handoff

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).

**Resource still needed:** The template helps organize decisions but is not cloud database administration training.

**Practise:** Deliver a bounded deployment design or approved lab report containing topology, permissions, recovery plan, cost estimate and deletion checklist.

**Advance when:** Each operational claim identifies its provider evidence or lab result, and every created resource has a verified cleanup disposition.

## After this recipe

Obtain the chosen provider's current administration training; an unexecuted deployment plan is not an operational readiness result.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
