# Learning curriculum: Configuration Manager

Maintain a useful configuration baseline and investigate drift without treating an inventory as a complete service model.

[Home](../README.md) / [Curricula](curricula.md) / [Operations, platforms and IT support](professions-operations.md#roles-in-this-group)

**Target profile:** [Configuration Manager](professions-operations.md#configuration-manager)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Have practical experience with service operations and controlled changes.
- Understand assets, configuration records and version history.

**What you will produce:** A fictional configuration register, baselines, drift investigation and a reconciled change record.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Define the register boundary](#stage-1)
2. [Record controlled baselines](#stage-2)
3. [Investigate configuration drift](#stage-3)
4. [Capstone: reconcile a service baseline](#stage-4)

<a id="stage-1"></a>
## 1. Define the register boundary

**Learn:**

- Configuration items
- Service relationships and ownership

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [GLPI](https://github.com/glpi-project/glpi) — intermediate in this topic; free access. [Details](area-it-support.md#resource-glpi).

**Practise:** Use fictional assets to model one small service and state which item types and relationships the register will track.

**Advance when:** Every item has an owner and identifier, and the register scope is explicit; GLPI supplies the lab tool, not a management standard.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Record controlled baselines

**Learn:**

- Approved configuration
- Version and evidence links

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Pro Git](https://git-scm.com/book/en/v2) — beginner in this topic; free access. [Details](area-software.md#resource-pro-git).

**Practise:** Version the practice service configuration and link its approved values to the corresponding asset records.

**Advance when:** A reader can distinguish an asset identifier, a configuration version and an approval record.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Investigate configuration drift

**Learn:**

- Discovery versus approval
- Reconciliation and audit trail

**Resource still needed:** No reviewed configuration-management process or discovery-tool administration guide is currently catalogued.

**Practise:** Introduce an undocumented synthetic configuration difference and compare observed evidence with the baseline.

**Advance when:** Record whether the difference is a data-quality problem, an unauthorised change or an unresolved observation.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone: reconcile a service baseline

**Learn:**

- Corrective action
- Register quality checks

**Resource still needed:** This is an editorial configuration-governance exercise, not an official ITIL process or a complete configuration-management qualification.

**Practise:** Resolve the fictional discrepancy through a documented decision and update the baseline and related records consistently.

**Advance when:** The register, version history and change note agree, and the evidence explains who authorised the correction.

## After this recipe

Review the organisation's actual configuration policy and practise ownership, discovery and audit controls under supervision.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-operations.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
