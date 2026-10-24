# Learning curriculum: Digital Forensics Examiner

A preservation-first recipe using learner-created evidence to practise provenance, repeatability and limited conclusions.

[Home](../README.md) / [Curricula](curricula.md) / [Cybersecurity, audit and risk](professions-security.md#roles-in-this-group)

**Target profile:** [Digital Forensics Examiner](professions-security.md#digital-forensics-examiner)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- File-system and operating-system fundamentals.
- Ability to work with copies and record commands.
- A disposable lab and only evidence you own or are authorized to examine.

**What you will produce:** A reproducible examination report for a benign self-created evidence set with an integrity and handling record.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Understand evidence and examination scope](#stage-1)
2. [Preserve and document a working copy](#stage-2)
3. [Examine and build a cautious timeline](#stage-3)
4. [Report a reproducible examination](#stage-4)

<a id="stage-1"></a>
## 1. Understand evidence and examination scope

**Learn:**

- File metadata and timestamps
- Authority, privacy and preservation

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [The Linux Command Line (William Shotts)](https://linuxcommand.org/tlcl.php) — beginner in this topic; free access. [Details](area-software.md#resource-the-linux-command-line).
- [Professor Messer (CompTIA Network+ and Security+ videos)](https://www.professormesser.com/security-plus/sy0-701/sy0-701-video/sy0-701-comptia-security-plus-course/) — beginner in this topic; free access. [Details](area-devops.md#resource-professor-messer).

**Practise:** Create harmless sample files in your own lab and write a narrow examination question and a list of authorized sources.

**Advance when:** The plan states the evidence boundary and why ordinary use could change some metadata.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Preserve and document a working copy

**Learn:**

- Integrity hashes and provenance
- Handling records and original versus working copies

**Resource still needed:** No verified forensic acquisition, write-blocking or chain-of-custody training is supplied; copying files here is not a forensic disk acquisition.

**Practise:** Copy the benign files, compute hashes with an appropriate local utility and record every transfer and examination action.

**Advance when:** The record identifies the original and working copy and detects a deliberate change to one copied file.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Examine and build a cautious timeline

**Learn:**

- Metadata interpretation and time zones
- Corroboration and alternative explanations

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Wireshark](https://www.wireshark.org/) — intermediate in this topic; free access. [Details](area-networking.md#resource-wireshark).

**Practise:** Use your self-generated files and an authorized saved capture to build a small timeline; compare known actions with recorded timestamps.

**Advance when:** The timeline cites each source and explains why an isolated timestamp does not prove who performed an action.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Report a reproducible examination

**Learn:**

- Methods, limitations and integrity checks
- Clear answers to the examination question

**Resource still needed:** Specialist device acquisition, deleted-file recovery and legal evidentiary requirements remain unverified gaps; no courtroom admissibility is claimed.

**Practise:** Produce an evidence index, handling log, methods appendix and report answering only the initial benign examination question.

**Advance when:** A peer can repeat the examination from the working copy and identify every inference and limitation.

## After this recipe

Pursue supervised specialist training in acquisition and the applicable legal context before examining real case material; confirm defensive lab access and cost separately.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [NICE Workforce Framework for Cybersecurity](profession-references.md#reference-nice)

[Back to roles in this group](professions-security.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
