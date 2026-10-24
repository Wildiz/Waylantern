# Learning curriculum: Security Operations Center Analyst

A defensive monitoring recipe focused on alert triage, evidence correlation and escalation rather than exploitation.

[Home](../README.md) / [Curricula](curricula.md) / [Cybersecurity, audit and risk](professions-security.md#roles-in-this-group)

**Target profile:** [Security Operations Center Analyst](professions-security.md#soc-analyst)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic networking and operating-system knowledge.
- Ability to read timestamps and simple log records.

**What you will produce:** A defensible alert investigation with timeline, evidence references, severity reasoning and escalation handoff.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Learn telemetry context](#stage-1)
2. [Triage an alert](#stage-2)
3. [Correlate evidence](#stage-3)
4. [Produce an operational handoff](#stage-4)

<a id="stage-1"></a>
## 1. Learn telemetry context

**Learn:**

- Network flows and authentication records
- Assets, normal behavior and time zones

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Professor Messer (CompTIA Network+ and Security+ videos)](https://www.professormesser.com/security-plus/sy0-701/sy0-701-video/sy0-701-comptia-security-plus-course/) — beginner in this topic; free access. [Details](area-devops.md#resource-professor-messer).
- [Wireshark](https://www.wireshark.org/) — intermediate in this topic; free access. [Details](area-networking.md#resource-wireshark).

**Practise:** Inspect a capture of your own benign web request and create a glossary of the fields you can explain.

**Advance when:** You can connect a flow to an endpoint and state what encrypted traffic does not reveal.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Triage an alert

**Learn:**

- False positives and prioritization
- Ownership, scope and duplicate events

**Resource still needed:** No specific SIEM triage course has been verified; synthetic events provide a local exercise, not product training.

**Practise:** Use synthetic login events to compare a mistaken password with repeated failures followed by success; fill in a triage worksheet.

**Advance when:** Your worksheet records supporting and conflicting evidence without labeling every failure an attack.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Correlate evidence

**Learn:**

- Event ordering and investigative hypotheses
- Host and network evidence limitations

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [CyberDefenders](https://cyberdefenders.org/blue-team-labs/) — intermediate in this topic; freemium access. [Details](area-security.md#resource-cyberdefenders).

**Practise:** Choose an accessible defensive investigation lab after checking its current price and availability; otherwise use your synthetic dataset and an authorized capture.

**Advance when:** The timeline cites original evidence and explains why each hypothesis is supported or rejected.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Produce an operational handoff

**Learn:**

- Severity rationale and containment recommendations
- Case notes and analyst review

**Resource still needed:** No end-to-end SOC operating procedure or assessed analyst qualification has been verified; adapt the editorial handoff to a real team under supervision.

**Practise:** Create an incident candidate with a timeline, affected assets, confidence, recommended next steps and a handoff checklist.

**Advance when:** A reviewer can continue the case without reconstructing the investigation; containment recommendations require the appropriate authorization.

## After this recipe

Obtain feedback on a second case, then learn the telemetry and escalation procedures of a supervised SOC environment.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [NICE Workforce Framework for Cybersecurity](profession-references.md#reference-nice)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-security.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
