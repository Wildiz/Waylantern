# Learning curriculum: Cybersecurity Technician

A hands-on defensive setup recipe for accounts, updates, logs and recovery on a disposable practice system.

[Home](../README.md) / [Curricula](curricula.md) / [Cybersecurity, audit and risk](professions-security.md#roles-in-this-group)

**Target profile:** [Cybersecurity Technician](professions-security.md#cybersecurity-technician)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic operating-system and network concepts.
- A disposable local Linux practice system.

**What you will produce:** A documented baseline configuration with tested controls, log observations and a rollback record.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Establish the baseline](#stage-1)
2. [Configure access carefully](#stage-2)
3. [Verify protection and recovery](#stage-3)
4. [Assemble the maintenance handoff](#stage-4)

<a id="stage-1"></a>
## 1. Establish the baseline

**Learn:**

- Inventory, versions and service exposure
- Routine maintenance versus incidents

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Linux Upskill Challenge](https://github.com/livialima/linuxupskillchallenge) — beginner in this topic; free access. [Details](area-it-support.md#resource-linux-upskill-challenge).
- [Professor Messer (CompTIA Network+ and Security+ videos)](https://www.professormesser.com/security-plus/sy0-701/sy0-701-video/sy0-701-comptia-security-plus-course/) — beginner in this topic; free access. [Details](area-devops.md#resource-professor-messer).

**Practise:** Record installed services, account types and pending updates on your own lab before changing anything.

**Advance when:** The baseline identifies what runs, who administers it and how to restore the initial state.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Configure access carefully

**Learn:**

- Least privilege and permissions
- Change approval and rollback

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [The Linux Command Line (William Shotts)](https://linuxcommand.org/tlcl.php) — beginner in this topic; free access. [Details](area-software.md#resource-the-linux-command-line).

**Practise:** Create separate practice accounts, limit a test directory and record before-and-after permissions.

**Advance when:** A normal account can perform its intended task but cannot read the restricted test file.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Verify protection and recovery

**Learn:**

- Updates and configuration checks
- Logs and recoverable backups

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Linux Upskill Challenge](https://github.com/livialima/linuxupskillchallenge) — beginner in this topic; free access. [Details](area-it-support.md#resource-linux-upskill-challenge).

**Practise:** Apply a routine lab update, verify the affected service and restore a harmless file after deletion.

**Advance when:** The record shows successful service checks and restore evidence, plus the logs consulted.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Assemble the maintenance handoff

**Learn:**

- Repeatable checks and exception records
- Incident escalation and ownership

**Resource still needed:** No product-specific endpoint protection or technician assessment has been verified; the capstone covers foundational local controls only.

**Practise:** Write a technician runbook for the baseline, execute it on a second disposable instance or reset lab and record an intentional failed check.

**Advance when:** Another learner can repeat the runbook and route the failed check with sufficient evidence.

## After this recipe

Learn the approved tools and change process of a supervised support or security team before operating production controls.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [NICE Workforce Framework for Cybersecurity](profession-references.md#reference-nice)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-security.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
