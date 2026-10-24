# Learning curriculum: Cloud Engineer

Translate service requirements into reproducible infrastructure and a documented deployment check.

[Home](../README.md) / [Curricula](curricula.md) / [Operations, platforms and IT support](professions-operations.md#roles-in-this-group)

**Target profile:** [Cloud Engineer](professions-operations.md#cloud-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Understand a Linux service and basic IP networking.
- Use Git and inspect command output.

**What you will produce:** A disposable infrastructure configuration and a design explaining how it would map to a chosen cloud provider.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Choose service requirements](#stage-1)
2. [Understand network exposure](#stage-2)
3. [Provision a local infrastructure example](#stage-3)
4. [Capstone: make a reviewed deployment package](#stage-4)

<a id="stage-1"></a>
## 1. Choose service requirements

**Learn:**

- Compute and storage needs
- Security and cost constraints

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [AWS Skill Builder](https://skillbuilder.aws/) — beginner in this topic; freemium access. [Details](area-devops.md#resource-aws-skill-builder).

**Practise:** Describe a small practice service and identify the compute, storage, identity and network categories it needs.

**Advance when:** Each proposed component has a requirement and a documented assumption rather than an unexplained provider choice.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Understand network exposure

**Learn:**

- Addressing and routing
- Ports and trust boundaries

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Computer Networks: A Systems Approach](https://github.com/SystemsApproach/book) — intermediate in this topic; free access. [Details](area-networking.md#resource-computer-networks-systems-approach).

**Practise:** Draw the service network and mark which clients may connect to each port.

**Advance when:** Explain the path of a request and distinguish public exposure from local or private access.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Provision a local infrastructure example

**Learn:**

- Declarative resources
- State and repeatability

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Terraform Tutorials (HashiCorp Developer)](https://developer.hashicorp.com/terraform/tutorials) — intermediate in this topic; free access. [Details](area-devops.md#resource-terraform-tutorials).

**Practise:** Use the Docker tutorial to provision, inspect, change and remove a local practice resource.

**Advance when:** Show the plan, resulting resource and cleanup, and explain why state must be protected.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone: make a reviewed deployment package

**Learn:**

- Configuration review
- Validation and cleanup

**Resource still needed:** No single reviewed resource covers this complete cloud-engineering handover; the local project does not establish real cloud permissions, cost or resilience.

**Practise:** Deliver the local configuration with a cloud mapping diagram, explicit unsupported assumptions and a fresh setup/removal trial.

**Advance when:** Another person can reproduce the local deployment and identify what still requires current provider documentation.

## After this recipe

Choose and verify a provider-specific implementation guide before applying infrastructure to a paid account or a shared environment.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [CNCF certification exam objectives](profession-references.md#reference-cncf)
- [Microsoft Learn training directory](profession-references.md#reference-microsoft-learn)

[Back to roles in this group](professions-operations.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
