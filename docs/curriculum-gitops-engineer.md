# Learning curriculum: GitOps Engineer

Use version-controlled desired state and reconciliation evidence to reason about controlled deployments.

[Home](../README.md) / [Curricula](curricula.md) / [Operations, platforms and IT support](professions-operations.md#roles-in-this-group)

**Target profile:** [GitOps Engineer](professions-operations.md#gitops-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Use Git branches and review changes.
- Understand YAML and basic Kubernetes resources.

**What you will produce:** A desired-state repository and a reconciliation demonstration that distinguishes approved change, drift and rollback.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Describe the workload declaratively](#stage-1)
2. [Review desired-state changes](#stage-2)
3. [Understand reconciliation and drift](#stage-3)
4. [Capstone: demonstrate change and recovery](#stage-4)

<a id="stage-1"></a>
## 1. Describe the workload declaratively

**Learn:**

- Resource manifests
- Desired versus observed state

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Kubernetes Tutorials (official docs)](https://kubernetes.io/docs/tutorials/) — intermediate in this topic; free access. [Details](area-devops.md#resource-kubernetes-tutorials).

**Practise:** Create a small local workload using the relevant basics tutorial and record its manifest and observed state.

**Advance when:** Explain which fields express intent and which observations show what actually runs.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Review desired-state changes

**Learn:**

- Version history
- Environment boundaries

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Pro Git](https://git-scm.com/book/en/v2) — beginner in this topic; free access. [Details](area-software.md#resource-pro-git).

**Practise:** Commit the manifest, propose a configuration change on a branch and document what must be reviewed before merge.

**Advance when:** A reviewer can identify the intended environment, changed behaviour and previous working revision.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Understand reconciliation and drift

**Learn:**

- Controller behaviour
- Credential and deletion boundaries

**Resource still needed:** No reviewed GitOps-controller setup or security guide is catalogued; this stage models behaviour rather than inventing controller commands.

**Practise:** Write a dry-run reconciliation table for approved state, manual drift and a deleted resource; state what a controller should restore or leave untouched.

**Advance when:** Distinguish a Git change, a reconciliation action and a deployment result, including failure handling.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone: demonstrate change and recovery

**Learn:**

- Reconciliation records
- Rollback limitations

**Resource still needed:** A complete automated GitOps-controller lab is missing; its absence must remain visible in this editorial capstone.

**Practise:** In a disposable local lab, apply the approved manifest changes and record a simulated reconciliation/rollback sequence; clearly mark manual actions.

**Advance when:** Show the repository versions and observed states, and explain that a manual simulation does not demonstrate an actual GitOps controller.

## After this recipe

Add a reviewed controller-specific lab and least-privilege credentials before describing the workflow as fully automated GitOps.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [CNCF certification exam objectives](profession-references.md#reference-cncf)

[Back to roles in this group](professions-operations.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
