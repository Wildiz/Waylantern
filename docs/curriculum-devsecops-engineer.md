# Learning curriculum: DevSecOps Engineer

Add focused security checks and controlled failure handling to a small delivery workflow.

[Home](../README.md) / [Curricula](curricula.md) / [Operations, platforms and IT support](professions-operations.md#roles-in-this-group)

**Target profile:** [DevSecOps Engineer](professions-operations.md#devsecops-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Build and test an application.
- Understand Git, containers and basic HTTP.

**What you will produce:** A delivery demonstration with an explicit threat, a failing security check, a corrected change and evidence of enforcement.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Identify exposure in the application](#stage-1)
2. [Turn one risk into a check](#stage-2)
3. [Control delivery permissions](#stage-3)
4. [Capstone: block a risky change](#stage-4)

<a id="stage-1"></a>
## 1. Identify exposure in the application

**Learn:**

- Trust boundaries
- Input and credential risks

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — beginner in this topic; free access. [Details](area-web.md#resource-owasp-top-10).

**Practise:** Draw where input and credentials enter a tiny app and select one applicable risk from the reference.

**Advance when:** Explain the selected risk using a concrete input path rather than treating the Top 10 as a complete threat model.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Turn one risk into a check

**Learn:**

- Negative tests
- Regression evidence

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).

**Practise:** For an app you own, add a test that rejects an invalid input and demonstrate its failure before the correction.

**Advance when:** The check distinguishes the vulnerable and corrected versions without exposing credentials.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Control delivery permissions

**Learn:**

- Least privilege
- Artifact and secret handling

**Resource still needed:** No reviewed resource in the catalogue provides a complete pipeline-permissions or secret-scanning implementation guide.

**Practise:** Draft a pipeline-permissions table and an artifact review checklist; identify where a secret would be supplied securely rather than committed.

**Advance when:** Each permission has a named purpose and the design excludes secrets from artifacts and logs.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone: block a risky change

**Learn:**

- Release gates
- Exception and recovery records

**Resource still needed:** This editorial project demonstrates one gate; a reviewed DevSecOps platform-hardening and software-supply-chain course is still missing.

**Practise:** Run a local delivery script that stops on the security test failure, succeeds after correction and records the result for review.

**Advance when:** A deliberately unsafe version is blocked and a corrected version is released; document remaining threats and who may approve an exception.

## After this recipe

Study identity, dependency integrity and organisation-specific security policy with an experienced delivery/security team.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [NICE Workforce Framework for Cybersecurity](profession-references.md#reference-nice)
- [CNCF certification exam objectives](profession-references.md#reference-cncf)

[Back to roles in this group](professions-operations.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
