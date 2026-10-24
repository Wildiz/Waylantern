# Learning curriculum: Security Administrator

An operational recipe for configuring access, maintaining a secure baseline and verifying changes in a disposable practice system.

[Home](../README.md) / [Curricula](curricula.md) / [Cybersecurity, audit and risk](professions-security.md#roles-in-this-group)

**Target profile:** [Security Administrator](professions-security.md#security-administrator)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic Linux administration and networking knowledge.
- A disposable system where you can test and roll back configuration changes.

**What you will produce:** A tested access and configuration runbook with baseline evidence, rollback instructions and incident handoff details.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Document system and administration boundaries](#stage-1)
2. [Manage access through a lifecycle](#stage-2)
3. [Maintain and monitor the baseline](#stage-3)
4. [Deliver an operational runbook](#stage-4)

<a id="stage-1"></a>
## 1. Document system and administration boundaries

**Learn:**

- Accounts, services and exposure
- Administrative authority and baseline configuration

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Linux Upskill Challenge](https://github.com/livialima/linuxupskillchallenge) — beginner in this topic; free access. [Details](area-it-support.md#resource-linux-upskill-challenge).
- [Professor Messer (CompTIA Network+ and Security+ videos)](https://www.professormesser.com/security-plus/sy0-701/sy0-701-video/sy0-701-comptia-security-plus-course/) — beginner in this topic; free access. [Details](area-devops.md#resource-professor-messer).

**Practise:** Inventory a practice server and record service owners, accounts and network-facing services before changing settings.

**Advance when:** The baseline shows what is authorized, what must remain available and how to recover the initial state.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Manage access through a lifecycle

**Learn:**

- Provisioning, least privilege and removal
- Permission testing and change records

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [The Linux Command Line (William Shotts)](https://linuxcommand.org/tlcl.php) — beginner in this topic; free access. [Details](area-software.md#resource-the-linux-command-line).

**Practise:** Create two practice roles, test allowed and denied file access, then remove one account's access.

**Advance when:** Recorded positive and negative checks demonstrate both provisioning and revocation without relying on a screenshot alone.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Maintain and monitor the baseline

**Learn:**

- Updates, service checks and backups
- Log review and exception escalation

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Linux Upskill Challenge](https://github.com/livialima/linuxupskillchallenge) — beginner in this topic; free access. [Details](area-it-support.md#resource-linux-upskill-challenge).

**Practise:** Perform a documented lab maintenance change, verify service health and review the relevant logs; test recovery of a harmless file.

**Advance when:** The change record contains before-and-after results, a working rollback and a separate record for unresolved checks.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver an operational runbook

**Learn:**

- Repeatability and safe failure handling
- Evidence handoff and periodic review

**Resource still needed:** No product-specific identity, endpoint or security-appliance administration curriculum has been verified; learn approved vendor procedures before administering such systems.

**Practise:** Have another learner follow your runbook on a reset lab, including an intentional permission failure and its escalation ticket.

**Advance when:** The learner can reproduce the baseline, recognize the failed check and hand it off with logs and a clear rollback decision.

## After this recipe

Practise with an experienced administrator and learn the organization's approved tools, change controls and recovery requirements before handling production security settings.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [NICE Workforce Framework for Cybersecurity](profession-references.md#reference-nice)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-security.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
