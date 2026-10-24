# Learning curriculum: DevOps Engineer

Connect a small application change to a repeatable build, deployment and recovery workflow.

[Home](../README.md) / [Curricula](curricula.md) / [Operations, platforms and IT support](professions-operations.md#roles-in-this-group)

**Target profile:** [DevOps Engineer](professions-operations.md#devops-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Write and test a small program.
- Use Git and navigate a Linux shell.

**What you will produce:** A versioned application with recorded tests, a reproducible container build and a demonstrated rollback.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Follow a change through Git](#stage-1)
2. [Build a checked artifact](#stage-2)
3. [Practise release and recovery](#stage-3)
4. [Capstone: deliver one repeatable change](#stage-4)

<a id="stage-1"></a>
## 1. Follow a change through Git

**Learn:**

- Commits and branches
- Reviewable changes

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [GitHub Skills: Introduction to Git](https://github.com/skills/introduction-to-git) — beginner in this topic; free access. [Details](area-software.md#resource-github-skills-introduction-to-git).
- [Pro Git](https://git-scm.com/book/en/v2) — beginner in this topic; free access. [Details](area-software.md#resource-pro-git).

**Practise:** Change one behaviour in a tiny application on a branch and record how a reviewer can test it.

**Advance when:** Show the diff and explain which commit introduced the change.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Build a checked artifact

**Learn:**

- Automated test failures
- Container images

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).
- [Docker Docs: Get started](https://docs.docker.com/get-started/) — beginner in this topic; free access. [Details](area-devops.md#resource-docker-docs-get-started).

**Practise:** Write a test for the behaviour, make it fail once deliberately, then build a container from the corrected source.

**Advance when:** Keep the failing and passing test outputs and identify the source version of the image.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Practise release and recovery

**Learn:**

- Deployment configuration
- Rollback evidence

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Container Training](https://github.com/jpetazzo/container.training) — intermediate in this topic; free access. [Details](area-devops.md#resource-container-training).

**Practise:** Run two local versions of the app, introduce a configuration fault and restore the previous working version.

**Advance when:** A local request demonstrates the fault and another demonstrates recovery; record the commands and logs.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone: deliver one repeatable change

**Learn:**

- Build and release steps
- Operational handover

**Resource still needed:** No reviewed resource covers this complete editorial delivery project; the earlier Git, testing and container material supplies its parts.

**Practise:** Package the change, checks, local deployment and rollback in a documented workflow that another person can follow.

**Advance when:** A clean run reproduces the working release and rollback, with secret-free logs and explicit local resource requirements.

## After this recipe

Add supervised CI and staging practice before taking responsibility for production releases.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [CNCF certification exam objectives](profession-references.md#reference-cncf)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-operations.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
