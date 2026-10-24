# Learning curriculum: Cloud Site Reliability Engineer

Reason about cloud failure boundaries and test the recovery assumptions of a small service.

[Home](../README.md) / [Curricula](curricula.md) / [Operations, platforms and IT support](professions-operations.md#roles-in-this-group)

**Target profile:** [Cloud Site Reliability Engineer](professions-operations.md#cloud-site-reliability-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Operate a basic service and interpret availability measurements.
- Understand cloud regions, zones and usage charges.

**What you will produce:** A cloud failure-boundary design and a documented local simulation of detection and recovery.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Map failure domains](#stage-1)
2. [Design observable recovery](#stage-2)
3. [Make the practice environment reproducible](#stage-3)
4. [Capstone: rehearse one cloud recovery plan](#stage-4)

<a id="stage-1"></a>
## 1. Map failure domains

**Learn:**

- Shared dependencies
- Zones and regional boundaries

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [AWS Skill Builder](https://skillbuilder.aws/) — beginner in this topic; freemium access. [Details](area-devops.md#resource-aws-skill-builder).
- [The System Design Primer](https://github.com/donnemartin/system-design-primer) — intermediate in this topic; free access. [Details](area-cs.md#resource-system-design-primer).

**Practise:** Use introductory provider material to diagram a hypothetical deployment and identify components that fail together.

**Advance when:** Separate a documented provider capability from an assumption that still needs verification.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Design observable recovery

**Learn:**

- Health signals
- Recovery-time and data-loss goals

**Resource still needed:** No reviewed provider-specific reliability objective or disaster-recovery curriculum is available.

**Practise:** Define detection signals and fictional recovery objectives for one component outage and one data loss scenario.

**Advance when:** Explain how each objective would be measured and which dependencies can prevent recovery.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Make the practice environment reproducible

**Learn:**

- Infrastructure state
- Change review and removal

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Terraform Tutorials (HashiCorp Developer)](https://developer.hashicorp.com/terraform/tutorials) — intermediate in this topic; free access. [Details](area-devops.md#resource-terraform-tutorials).

**Practise:** Use the local Docker tutorial to create a disposable dependency, record its state and recreate it after removal.

**Advance when:** A second setup reproduces the intended local configuration; the report states what cloud-specific behaviour it does not test.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone: rehearse one cloud recovery plan

**Learn:**

- Failover decisions
- Recovery verification

**Resource still needed:** No reviewed live-cloud failover lab is catalogued; the capstone must not claim regional resilience from a local simulation.

**Practise:** Simulate a component failure locally and write a cloud recovery plan using the observed evidence and explicitly untested provider assumptions.

**Advance when:** A reviewer can distinguish demonstrated local restoration from proposed cloud failover and data-restoration behaviour.

## After this recipe

Verify current provider guarantees and rehearse backups and regional recovery in an authorised staging environment with cost limits.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [CNCF certification exam objectives](profession-references.md#reference-cncf)
- [Microsoft Learn training directory](profession-references.md#reference-microsoft-learn)

[Back to roles in this group](professions-operations.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
