# Learning curriculum: IT Infrastructure Manager

Coordinate infrastructure reliability, changes, capacity and support responsibilities.

[Home](../README.md) / [Curricula](curricula.md) / [Leadership, product and technology relationships](professions-leadership.md#roles-in-this-group)

**Target profile:** [IT Infrastructure Manager](professions-leadership.md#it-infrastructure-manager)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Has operated infrastructure or supported production services.
- Can discuss compute, network and storage dependencies with the relevant specialists.
- Has experience coordinating maintenance or operational work.

**What you will produce:** An infrastructure operating plan with justified capacity, maintenance and recovery priorities.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Map the infrastructure behind a service](#stage-1)
2. [Interpret operational evidence](#stage-2)
3. [Plan maintenance and recovery](#stage-3)
4. [Present a risk-and-capacity operating plan](#stage-4)

<a id="stage-1"></a>
## 1. Map the infrastructure behind a service

**Learn:**

- Asset inventory
- Service dependencies
- Operational ownership

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [GLPI](https://github.com/glpi-project/glpi) — intermediate in this topic; free access. [Details](area-it-support.md#resource-glpi).

**Practise:** Create an invented inventory for one business service, including compute, network, storage, owners and supplier dependencies. Follow one failure path through the inventory.

**Advance when:** The map identifies the dependencies whose failure would interrupt the service and records who can act on them.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Interpret operational evidence

**Learn:**

- Service status
- Logs
- Capacity signals

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Linux Upskill Challenge](https://github.com/livialima/linuxupskillchallenge) — beginner in this topic; free access. [Details](area-it-support.md#resource-linux-upskill-challenge).

**Practise:** Use a disposable Linux lab to collect a small set of status, storage and service observations. Explain which observations support a capacity or maintenance concern and which need a specialist.

**Advance when:** You can show the evidence for one concern, its limits and the next check, instead of assuming every alert requires more hardware.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Plan maintenance and recovery

**Learn:**

- Change windows
- Recovery objectives
- Supplier coordination

**Resource still needed:** Verified learning resources on infrastructure capacity management, continuity planning and maintenance governance are not yet catalogued.

**Practise:** Draft a maintenance proposal and a tabletop recovery scenario for the service. Identify business approval, fallback conditions, specialist roles and communication points.

**Advance when:** The plan has an agreed service objective, a rollback or recovery path and named decision responsibilities.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Present a risk-and-capacity operating plan

**Learn:**

- Investment priorities
- Service reporting
- Operational review

**Resource still needed:** A verified infrastructure-management curriculum including financial and people responsibilities remains a gap.

**Practise:** Combine inventory and operational findings into a prioritised operating plan. Compare one upgrade with a lower-cost operational alternative and schedule a review of the decision.

**Advance when:** The capstone links spending and maintenance recommendations to service evidence, dependencies and a measurable operational result.

## After this recipe

Review the plan with experienced infrastructure and business owners; deepen the specialism needed by the actual estate before taking responsibility.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-leadership.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
