# Learning curriculum: Cybersecurity Practitioner

An editorial introduction to protecting a small system and choosing a defensive specialization; not a complete occupational qualification.

[Home](../README.md) / [Curricula](curricula.md) / [Cybersecurity, audit and risk](professions-security.md#roles-in-this-group)

**Target profile:** [Cybersecurity Practitioner](professions-security.md#cybersecurity-practitioner)

**Starting point:** Start with the basics

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic file handling and a disposable local practice environment.

**What you will produce:** A documented security review of a small practice system, including assets, controls, test evidence and remaining risks.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Learn systems and security language](#stage-1)
2. [Apply small preventive controls](#stage-2)
3. [Observe and investigate](#stage-3)
4. [Complete a scoped security review](#stage-4)

<a id="stage-1"></a>
## 1. Learn systems and security language

**Learn:**

- Accounts, processes and file permissions
- IP networking and confidentiality, integrity and availability

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [The Linux Command Line (William Shotts)](https://linuxcommand.org/tlcl.php) — beginner in this topic; free access. [Details](area-software.md#resource-the-linux-command-line).
- [Professor Messer (CompTIA Network+ and Security+ videos)](https://www.professormesser.com/security-plus/sy0-701/sy0-701-video/sy0-701-comptia-security-plus-course/) — beginner in this topic; free access. [Details](area-devops.md#resource-professor-messer).

**Practise:** Draw how a browser, network, server and account connect, then list the information each holds.

**Advance when:** You can trace one login and identify three assets and their owners.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Apply small preventive controls

**Learn:**

- Least privilege and patching
- Backup, recovery and change records

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Linux Upskill Challenge](https://github.com/livialima/linuxupskillchallenge) — beginner in this topic; free access. [Details](area-it-support.md#resource-linux-upskill-challenge).

**Practise:** Create a nonprivileged practice account, document access permissions and restore a harmless test file from a backup.

**Advance when:** Your evidence shows the account permissions and a successful file restore, with undo steps.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Observe and investigate

**Learn:**

- Authentication events and timestamps
- Triage, uncertainty and escalation

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Wireshark](https://www.wireshark.org/) — intermediate in this topic; free access. [Details](area-networking.md#resource-wireshark).

**Practise:** Generate a failed login on your own lab and compare its log record with a short authorized traffic capture.

**Advance when:** A timeline distinguishes what the records demonstrate from what remains unknown.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Complete a scoped security review

**Learn:**

- Risk prioritization and remediation
- Communicating findings and choosing a specialization

**Resource still needed:** No complete general-practitioner curriculum or assessment rubric has been verified; this review is an editorial exercise.

**Practise:** Combine the asset list, two control tests and one investigation into a short report; propose a follow-up in monitoring, administration or assurance.

**Advance when:** The report includes reproducible evidence, prioritized actions, owners and an explicit statement of scope.

## After this recipe

Repeat the review on another authorized lab, seek feedback on your evidence and choose one specialist recipe rather than treating this introduction as professional certification.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [NICE Workforce Framework for Cybersecurity](profession-references.md#reference-nice)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-security.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
