# Learning curriculum: Bioinformatics Technician

An editorial workflow-practice recipe with explicit gaps in laboratory procedures and assay tooling.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [Bioinformatics Technician](professions-data-ai.md#bioinformatics-technician)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic biology and laboratory terminology
- File handling and command-line basics
- Awareness of confidential sample information

**What you will produce:** A small practice workflow with a sample manifest, logged processing steps and a clear escalation record.

**Resource coverage:** 1 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Learn the sample and file conventions](#stage-1)
2. [Automate manifest checks](#stage-2)
3. [Operate a reviewed quality-control step](#stage-3)
4. [Capstone - hand off an auditable practice batch](#stage-4)

<a id="stage-1"></a>
## 1. Learn the sample and file conventions

**Learn:**

- Sample chain of custody
- Assay file formats
- Laboratory procedures and acceptance criteria

**Resource still needed:** No verified laboratory informatics, assay-format or sample-handling curriculum is currently catalogued.

**Practise:** With an approved procedure or training example, map sample identifiers to expected files and acceptance checks.

**Advance when:** Explain which identifier joins files to samples and when a mismatch must be escalated rather than corrected by guessing.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Automate manifest checks

**Learn:**

- Directory and file handling
- Structured metadata validation
- Reproducible processing logs

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) — beginner in this topic; free access. [Details](area-software.md#resource-automate-the-boring-stuff).
- [pandas Getting Started Tutorials](https://pandas.pydata.org/docs/getting_started/index.html) — beginner in this topic; free access. [Details](area-data.md#resource-pandas-getting-started).

**Practise:** On synthetic sample records, flag duplicate identifiers, missing files and invalid metadata while retaining the original records.

**Advance when:** Known injected errors appear in the report and no original sample information is silently overwritten.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Operate a reviewed quality-control step

**Learn:**

- Standard operating procedures
- Quality thresholds and exceptions
- Version and parameter records

**Resource still needed:** A verified assay-specific quality-control tool and training procedure are missing; do not substitute a generic data-cleaning tutorial.

**Practise:** Follow a supervised teaching procedure, record tool versions and classify results against its supplied thresholds.

**Advance when:** Repeat the same inputs with the same settings and document an exception without changing acceptance criteria retrospectively.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - hand off an auditable practice batch

**Learn:**

- Batch reconciliation
- Traceable outputs
- Exception reporting

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Pro Git](https://git-scm.com/book/en/v2) — beginner in this topic; free access. [Details](area-software.md#resource-pro-git).

**Resource still needed:** Git supports code history only; biological SOP compliance and quality interpretation still require a verified domain procedure.

**Practise:** Package a synthetic or approved batch manifest, processing instructions, output inventory and escalation note.

**Advance when:** Each input is accounted for as processed, rejected or pending, and a colleague can follow the handoff without private sample data.

## After this recipe

Learn the laboratory's actual SOPs and supervised assay tools before operating on real biological or clinical samples.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [ACM Computing Curricula Recommendations](profession-references.md#reference-acm-curricula)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
