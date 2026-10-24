# Learning curriculum: Network and Computer Systems Administrator

Connect host administration with network diagnosis without confusing a host fault with a network fault.

[Home](../README.md) / [Curricula](curricula.md) / [Operations, platforms and IT support](professions-operations.md#roles-in-this-group)

**Target profile:** [Network and Computer Systems Administrator](professions-operations.md#network-computer-systems-administrator)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Read shell commands and basic system settings.
- Understand IP addresses and have isolated host/network practice environments.

**What you will produce:** A combined host/network inventory and two diagnosed failures with evidence at the appropriate layer.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Document connected systems](#stage-1)
2. [Manage the host side](#stage-2)
3. [Separate connectivity failures](#stage-3)
4. [Capstone: restore a dependent service](#stage-4)

<a id="stage-1"></a>
## 1. Document connected systems

**Learn:**

- Host and service inventory
- Address and dependency mapping

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Computer Networks: A Systems Approach](https://github.com/SystemsApproach/book) — intermediate in this topic; free access. [Details](area-networking.md#resource-computer-networks-systems-approach).

**Practise:** Draw two fictional systems, their addresses and the services they require from one another.

**Advance when:** The diagram identifies host configuration separately from network path assumptions.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Manage the host side

**Learn:**

- Accounts and service startup
- Operating-system logs

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Linux Upskill Challenge](https://github.com/livialima/linuxupskillchallenge) — beginner in this topic; free access. [Details](area-it-support.md#resource-linux-upskill-challenge).

**Practise:** Set up a practice service with a restricted account and record how to check its process, listening port and logs.

**Advance when:** Explain what would be observed if the service were stopped even though the host remained reachable.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Separate connectivity failures

**Learn:**

- Routing and DNS checks
- Packet observations

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Mininet](https://github.com/mininet/mininet) — intermediate in this topic; free access. [Details](area-networking.md#resource-mininet).
- [Wireshark](https://www.wireshark.org/) — intermediate in this topic; free access. [Details](area-networking.md#resource-wireshark).

**Practise:** Compare a stopped service with an isolated network or DNS fault using only lab systems.

**Advance when:** Evidence distinguishes a transport or name-resolution problem from application unavailability.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone: restore a dependent service

**Learn:**

- Cross-layer diagnosis
- Handover notes

**Resource still needed:** No reviewed resource supplies this complete mixed administration scenario; lab commands must be adapted to the selected platform.

**Practise:** Create two simulated tickets, diagnose each at its layer and document the minimal repair and follow-up tests.

**Advance when:** Another operator can follow the host and network evidence without relying on a guessed root cause.

## After this recipe

Extend into supervised network-device administration and operating-system management for the environment you intend to support.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-operations.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
