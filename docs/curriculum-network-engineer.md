# Learning curriculum: Network Engineer

Build and diagnose a small IP network using protocol reasoning and observable packet behaviour.

[Home](../README.md) / [Curricula](curricula.md) / [Operations, platforms and IT support](professions-operations.md#roles-in-this-group)

**Target profile:** [Network Engineer](professions-operations.md#network-engineer)

**Starting point:** Start with the basics

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Use files and basic computer settings.
- Have a suitable isolated Linux/emulation lab or access to a supervised one.

**What you will produce:** An addressed network diagram, connectivity tests and a packet-backed diagnosis of one deliberate fault.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Learn what carries a request](#stage-1)
2. [Construct an isolated network](#stage-2)
3. [Diagnose using packets and commands](#stage-3)
4. [Capstone: repair a network fault](#stage-4)

<a id="stage-1"></a>
## 1. Learn what carries a request

**Learn:**

- Ethernet and IP addressing
- TCP, UDP and DNS

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Computer Networks: A Systems Approach](https://github.com/SystemsApproach/book) — intermediate in this topic; free access. [Details](area-networking.md#resource-computer-networks-systems-approach).

**Practise:** Trace a hypothetical browser request from a host through its local network and name the protocol responsibility at each step.

**Advance when:** Explain the distinction between an address, a route, a transport port and a DNS name.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Construct an isolated network

**Learn:**

- Subnets and default routes
- Switch and router roles

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Mininet](https://github.com/mininet/mininet) — intermediate in this topic; free access. [Details](area-networking.md#resource-mininet).

**Practise:** Adapt a small emulator example with multiple hosts and record addresses and expected connectivity.

**Advance when:** The diagram matches the configured hosts and tests distinguish reachable from intentionally unreachable paths.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Diagnose using packets and commands

**Learn:**

- Capture filters
- Layered fault isolation

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Wireshark](https://www.wireshark.org/) — intermediate in this topic; free access. [Details](area-networking.md#resource-wireshark).

**Practise:** Capture only lab traffic and compare a successful connection with a deliberate addressing or name-resolution fault.

**Advance when:** Use command output and packets to locate the faulty layer without sharing private traffic.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone: repair a network fault

**Learn:**

- Change evidence
- Post-change verification

**Resource still needed:** The complete fault-and-handover assignment is editorial; emulator results do not establish real equipment performance.

**Practise:** Create a short fault ticket, apply one justified correction and repeat the connectivity tests against the original diagram.

**Advance when:** Before/after evidence supports the diagnosis and the fix does not silently broaden access.

## After this recipe

Add supervised routing, switching, wireless and physical-network practice before changing organisational networks.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)
- [Network Programmability Basics course material](profession-references.md#reference-cisco-network-programmability)

[Back to roles in this group](professions-operations.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
