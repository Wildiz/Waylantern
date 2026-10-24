# Learning curriculum: Network Architect

An editorial sequence for experienced networking learners to connect a small topology, test results and a resilience proposal.

[Home](../README.md) / [Curricula](curricula.md) / [Architecture and systems design](professions-architecture.md#roles-in-this-group)

**Target profile:** [Network Architect](professions-architecture.md#network-architect)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Can explain IP addressing, subnets, routing and DNS and diagnose basic connectivity.
- Have completed a small simulated network lab or equivalent practical work.
- Can read basic Python and use an isolated Linux lab for the emulation track.

**What you will produce:** A network requirements sheet, annotated topology, controlled failure evidence and a bounded redesign proposal.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Translate communication needs into a network brief](#stage-1)
2. [Draw the topology and its failure domains](#stage-2)
3. [Test a constrained topology rather than assuming it works](#stage-3)
4. [Deliver a network-redesign mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Translate communication needs into a network brief

**Learn:**

- Traffic endpoints
- Addressing
- Reachability constraints

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Computer Networks: A Systems Approach](https://github.com/SystemsApproach/book) — intermediate in this topic; free access. [Details](area-networking.md#resource-computer-networks-systems-approach).

**Practise:** Describe a fictional office with users and a service, list required communications and assign an address plan with no overlapping subnets.

**Advance when:** The brief identifies each endpoint, permitted communication and the routing needed between its networks.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Draw the topology and its failure domains

**Learn:**

- Switching and routing
- Shared dependencies
- Failure boundaries

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Computer Networks: A Systems Approach](https://github.com/SystemsApproach/book) — intermediate in this topic; free access. [Details](area-networking.md#resource-computer-networks-systems-approach).
- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).

**Practise:** Diagram the office connections and mark where a failed device or link disconnects multiple endpoints; explain one proposed change that reduces that dependency.

**Advance when:** The topology is consistent with the address plan and a reader can trace the effect of one named link failure.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Test a constrained topology rather than assuming it works

**Learn:**

- Network emulation
- Connectivity checks
- Controlled faults

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Mininet](https://github.com/mininet/mininet) — intermediate in this topic; free access. [Details](area-networking.md#resource-mininet).

**Practise:** Adapt a small Python topology example in an isolated Linux environment, record host connectivity and deliberately disable one lab link before restoring it.

**Advance when:** The saved connectivity results show the expected working, failed and restored states and identify which proposed production features were not represented by the emulator.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver a network-redesign mini-project

**Learn:**

- Design rationale
- Validation scope
- Operational handover

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).
- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).

**Practise:** Assemble the brief, address plan, topology and emulation evidence; compare your original design with one resilience improvement and document operational and cost assumptions.

**Advance when:** A reviewer can trace the improvement to an observed failure and distinguish tested connectivity from untested throughput or hardware behavior.

## After this recipe

Validate equipment capabilities, routing policies, monitoring and failover with an experienced network team; a small emulation is not a production network design sign-off.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)
- [Network Programmability Basics course material](profession-references.md#reference-cisco-network-programmability)

[Back to roles in this group](professions-architecture.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
