# Learning curriculum: Penetration Tester

A scoped progression from web and network fundamentals to an authorized lab assessment and retest.

[Home](../README.md) / [Curricula](curricula.md) / [Cybersecurity, audit and risk](professions-security.md#roles-in-this-group)

**Target profile:** [Penetration Tester](professions-security.md#penetration-tester)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic HTTP and networking knowledge.
- Comfort using a terminal and reading simple code.

**What you will produce:** A reproducible report for a deliberately vulnerable lab, including boundaries, impact, fixes and a retest.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Understand the system and permission boundary](#stage-1)
2. [Reproduce a guided web weakness](#stage-2)
3. [Assess a small application deliberately](#stage-3)
4. [Deliver and retest](#stage-4)

<a id="stage-1"></a>
## 1. Understand the system and permission boundary

**Learn:**

- HTTP requests, authentication and sessions
- Written scope, test rules and safe stopping conditions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Professor Messer (CompTIA Network+ and Security+ videos)](https://www.professormesser.com/security-plus/sy0-701/sy0-701-video/sy0-701-comptia-security-plus-course/) — beginner in this topic; free access. [Details](area-devops.md#resource-professor-messer).
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — beginner in this topic; free access. [Details](area-web.md#resource-owasp-top-10).

**Practise:** Diagram a locally hosted practice application and write a test agreement covering only that lab.

**Advance when:** The agreement names allowed targets, excluded actions and conditions for stopping.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Reproduce a guided web weakness

**Learn:**

- Input handling and access control
- Observations versus assumptions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [PortSwigger Web Security Academy](https://portswigger.net/web-security) — beginner in this topic; free access. [Details](area-web.md#resource-portswigger-web-security-academy).

**Practise:** Complete an available introductory lab within its authorized environment and record each request and response needed to reproduce the issue.

**Advance when:** Another learner can reproduce the lab outcome from your notes without guessing missing steps.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Assess a small application deliberately

**Learn:**

- Coverage and repeatable test cases
- Impact, remediation and evidence handling

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [OWASP Juice Shop](https://owasp-juice.shop/) — beginner in this topic; free access. [Details](area-web.md#resource-owasp-juice-shop).

**Practise:** Select two permitted challenges in a private local lab; keep a coverage checklist and avoid collecting unrelated data.

**Advance when:** Each finding has evidence, a bounded impact explanation and a proposed fix; untested coverage is explicit.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver and retest

**Learn:**

- Clear reporting and residual risk
- Verification of remediation

**Resource still needed:** No comprehensive penetration-testing engagement standard or supervisor-reviewed assessment has been verified in this catalogue.

**Practise:** Write an executive summary and technical appendix; apply or simulate one lab remediation and repeat the original test.

**Advance when:** The final report separates confirmed findings, limitations and retest results, with authorization attached.

## After this recipe

Have an experienced tester review your lab report and broaden practice only through systems for which testing is explicitly authorized.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [NICE Workforce Framework for Cybersecurity](profession-references.md#reference-nice)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-security.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
