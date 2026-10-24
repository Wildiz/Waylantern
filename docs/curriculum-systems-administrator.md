# Learning curriculum: Systems Administrator

Administer a disposable system through accounts, services, updates and a tested recovery step.

[Home](../README.md) / [Curricula](curricula.md) / [Operations, platforms and IT support](professions-operations.md#roles-in-this-group)

**Target profile:** [Systems Administrator](professions-operations.md#systems-administrator)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Navigate a shell and explain files and permissions.
- Use a disposable operating-system lab rather than a daily-use or production machine.

**What you will produce:** A documented system configuration with account permissions, service checks and evidence of restoration.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Manage identities and access](#stage-1)
2. [Operate and inspect services](#stage-2)
3. [Plan and test restoration](#stage-3)
4. [Capstone: hand over a maintained system](#stage-4)

<a id="stage-1"></a>
## 1. Manage identities and access

**Learn:**

- Users and groups
- Permissions and privilege

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Linux Upskill Challenge](https://github.com/livialima/linuxupskillchallenge) — beginner in this topic; free access. [Details](area-it-support.md#resource-linux-upskill-challenge).

**Practise:** Create a fictional user and restricted practice directory, then test permitted and denied access.

**Advance when:** Show both access outcomes and explain why the user does not need full administrative privileges.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Operate and inspect services

**Learn:**

- Package changes
- Service status and logs

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Linux Upskill Challenge](https://github.com/livialima/linuxupskillchallenge) — beginner in this topic; free access. [Details](area-it-support.md#resource-linux-upskill-challenge).
- [PowerShell 101 (Microsoft)](https://github.com/MicrosoftDocs/PowerShell-Docs/tree/main/reference/docs-conceptual/learn/ps101) — beginner in this topic; free access. [Details](area-it-support.md#resource-powershell-101).

**Practise:** On one selected operating system, record an installed service, inspect status/logs and document a reversible configuration change.

**Advance when:** A functional request confirms service behaviour; distinguish Linux examples from Windows-specific commands.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Plan and test restoration

**Learn:**

- Backup scope
- Restore validation

**Resource still needed:** A reviewed cross-platform backup and restore administration guide is not yet catalogued.

**Practise:** Back up a practice configuration and sample data, remove the lab copy and restore it into a clean location.

**Advance when:** The restored content and service behaviour match the stated recovery scope, with exceptions recorded.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone: hand over a maintained system

**Learn:**

- Maintenance record
- Recovery runbook

**Resource still needed:** This editorial lab covers a small system only; it does not verify enterprise identity, endpoint management or all operating systems.

**Practise:** Combine the accounts, service checks, patch/configuration notes and restore evidence into a handover for the lab.

**Advance when:** A second operator can identify the system baseline, health test and steps for undoing the practice change.

## After this recipe

Choose an operating-system specialisation and practise identity, patching and backup procedures under experienced supervision.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)
- [Microsoft Learn training directory](profession-references.md#reference-microsoft-learn)

[Back to roles in this group](professions-operations.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
