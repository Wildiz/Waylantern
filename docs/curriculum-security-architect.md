# Learning curriculum: Security Architect

An editorial security-design exercise using a fictional service and authorized training labs rather than unapproved targets.

[Home](../README.md) / [Curricula](curricula.md) / [Architecture and systems design](professions-architecture.md#roles-in-this-group)

**Target profile:** [Security Architect](professions-architecture.md#security-architect)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Have built or operated an application and understand HTTP, identity and network boundaries.
- Can distinguish an observed vulnerability from an untested risk hypothesis.
- Will use invented data and only authorized local or training environments.

**What you will produce:** A trust-boundary diagram, risk-to-control table and an authorized lab report with a clear validation scope.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Identify assets, trust boundaries and uncertain threats](#stage-1)
2. [Link relevant risks with concrete controls](#stage-2)
3. [Validate one control in an authorized lab](#stage-3)
4. [Deliver a security-design mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Identify assets, trust boundaries and uncertain threats

**Learn:**

- Assets
- Trust boundaries
- Threat assumptions

**Resource still needed:** A verified introductory threat-modelling curriculum is not yet available; architecture templates and vulnerability lists are not substitutes for that instruction.

**Practise:** Draw a fictional booking service's users, API and database, mark where trust changes and list valuable data and three threat hypotheses with their assumptions.

**Advance when:** Each hypothesis names an asset and boundary and is explicitly labelled as a hypothesis, not an exploited weakness.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Link relevant risks with concrete controls

**Learn:**

- Application risks
- Access control
- Input handling

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — beginner in this topic; free access. [Details](area-web.md#resource-owasp-top-10).
- [PortSwigger Web Security Academy](https://portswigger.net/web-security) — beginner in this topic; free access. [Details](area-web.md#resource-portswigger-web-security-academy).

**Practise:** Select one risk relevant to the service, study its explanation and record a corresponding control, its enforcement point and how a failure could be observed.

**Advance when:** The control addresses the stated cause, and the proposal does not treat a Top 10 checklist as a complete security architecture.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Validate one control in an authorized lab

**Learn:**

- Lab scope
- Reproduction evidence
- Mitigation reasoning

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [PortSwigger Web Security Academy](https://portswigger.net/web-security) — beginner in this topic; free access. [Details](area-web.md#resource-portswigger-web-security-academy).

**Practise:** Complete one suitable supplied lab, record the observed behavior and explain the mitigation; restrict activity to that lab and omit credentials or challenge answers from shared evidence.

**Advance when:** The lab outcome and report support the specific claim, while proposed controls in the fictional service remain marked untested.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver a security-design mini-project

**Learn:**

- Risk-to-control traceability
- Residual risk
- Review decisions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).
- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).

**Practise:** Assemble the boundary diagram, risk table and lab report, then document one security-versus-usability tradeoff and a residual risk needing a qualified review.

**Advance when:** A reviewer can distinguish implemented, lab-tested and merely proposed controls, and every unresolved risk has a next validation action.

## After this recipe

Study verified threat-modelling methods and participate in supervised security reviews; training-lab success does not authorize testing or establish system security.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [NICE Workforce Framework for Cybersecurity](profession-references.md#reference-nice)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-architecture.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
