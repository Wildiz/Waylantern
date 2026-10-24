# Learning curriculum: Computer Network Support Specialist

Narrow a user connectivity issue through host, name-resolution and network-path checks.

[Home](../README.md) / [Curricula](curricula.md) / [Operations, platforms and IT support](professions-operations.md#roles-in-this-group)

**Target profile:** [Computer Network Support Specialist](professions-operations.md#computer-network-support-specialist)

**Starting point:** Start with the basics

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Use basic system settings.
- Have permission to inspect only an isolated lab network and its traffic.

**What you will produce:** A connectivity case showing structured checks, relevant packet evidence and a bounded repair or escalation.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Understand one host connection](#stage-1)
2. [Collect reproducible connection evidence](#stage-2)
3. [Inspect a relevant capture](#stage-3)
4. [Capstone: support an affected user](#stage-4)

<a id="stage-1"></a>
## 1. Understand one host connection

**Learn:**

- Addresses, gateways and DNS
- Local versus remote failures

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Computer Networks: A Systems Approach](https://github.com/SystemsApproach/book) — intermediate in this topic; free access. [Details](area-networking.md#resource-computer-networks-systems-approach).

**Practise:** Draw how a fictional user reaches a service and identify the host, gateway, resolver and destination.

**Advance when:** Explain why a failed name lookup is different from a failed connection to a known address.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Collect reproducible connection evidence

**Learn:**

- Interface and route checks
- Transport reachability

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Mininet](https://github.com/mininet/mininet) — intermediate in this topic; free access. [Details](area-networking.md#resource-mininet).

**Practise:** Use a small emulator example to compare normal connectivity with a missing route or stopped endpoint.

**Advance when:** Record the commands and outputs and explain which part of the path each check examines.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Inspect a relevant capture

**Learn:**

- DNS queries and responses
- Connection attempts and responses

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Wireshark](https://www.wireshark.org/) — intermediate in this topic; free access. [Details](area-networking.md#resource-wireshark).

**Practise:** Capture the isolated test and compare a working name lookup or TCP connection with the failed case.

**Advance when:** Point to the relevant packets and avoid inferring a network fault solely from one timeout.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone: support an affected user

**Learn:**

- Minimal changes
- Clear escalation evidence

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [GLPI](https://github.com/glpi-project/glpi) — intermediate in this topic; free access. [Details](area-it-support.md#resource-glpi).

**Practise:** Create a fictional connectivity ticket with the host settings, failed test, justified correction or escalation and a repeated user-facing check.

**Advance when:** The receiving technician can locate the fault boundary without requesting passwords or exposing unrelated packet data.

## After this recipe

Practise supervised wireless, VPN and enterprise access cases with current approved procedures for the organisation.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-operations.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
