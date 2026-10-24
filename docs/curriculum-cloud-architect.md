# Learning curriculum: Cloud Architect

An editorial cloud-design exercise that separates workload requirements, provider choices and unverified cost assumptions.

[Home](../README.md) / [Curricula](curricula.md) / [Architecture and systems design](professions-architecture.md#roles-in-this-group)

**Target profile:** [Cloud Architect](professions-architecture.md#cloud-architect)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Have deployed and troubleshot a small service and understand networking and access control basics.
- Can explain stateless application processes and persistent data.
- Understand that cloud accounts and managed services can incur charges; deployment is optional here.

**What you will produce:** A cloud deployment proposal with a local container demonstration, explicit failure scenarios and a cost-verification checklist.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Characterise the workload before choosing services](#stage-1)
2. [Understand provider building blocks](#stage-2)
3. [Model deployment and identify unanswered operating costs](#stage-3)
4. [Present a cloud-architecture mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Characterise the workload before choosing services

**Learn:**

- Traffic assumptions
- Persistence
- Availability expectations

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).
- [System Design (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design) — intermediate in this topic; free access. [Details](area-architecture.md#resource-karan-system-design).

**Practise:** Define an invented document-index service, estimate its small starting workload and state what must survive process failure and what downtime is acceptable.

**Advance when:** The brief distinguishes measured requirements from assumptions and identifies the data that cannot be lost.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Understand provider building blocks

**Learn:**

- Compute options
- Managed storage
- Shared responsibility

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [AWS Skill Builder](https://skillbuilder.aws/) — beginner in this topic; freemium access. [Details](area-devops.md#resource-aws-skill-builder).

**Practise:** Use an introductory cloud module in the provider catalogue to identify compute and storage building blocks relevant to the service; note the exact module used and which responsibility remains yours.

**Advance when:** The design names the purpose of each proposed service and does not assume that using a managed service transfers all security responsibility to the provider.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Model deployment and identify unanswered operating costs

**Learn:**

- Container deployment
- Recovery assumptions
- Pricing inputs

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Docker Docs: Get started](https://docs.docker.com/get-started/) — beginner in this topic; free access. [Details](area-devops.md#resource-docker-docs-get-started).

**Resource still needed:** A verified provider-specific cost-modelling and disaster-recovery curriculum is not currently available in this catalogue; do not treat generic container tutorials as that training.

**Practise:** Containerise the service locally, identify the persistent data outside its process and list provider prices, traffic charges and recovery capabilities that need checking before any paid deployment.

**Advance when:** The local image can be rebuilt and restarted, while the cost sheet clearly marks unknown rates and untested recovery claims.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Present a cloud-architecture mini-project

**Learn:**

- Deployment topology
- Failure scenarios
- Tradeoff review

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).
- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).

**Practise:** Deliver the workload brief, proposed topology, container instructions and an ADR comparing a simple deployment with a more redundant option; keep cloud execution optional.

**Advance when:** A reviewer can identify the chosen option's failure exposure and every prerequisite requiring provider documentation, budgeting or a real recovery test before use.

## After this recipe

Validate pricing, identity and recovery using current official provider documentation and supervised lab work with spending limits; this proposal does not qualify a production architecture.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [CNCF certification exam objectives](profession-references.md#reference-cncf)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-architecture.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
