# Learning curriculum: Solutions Architect

An editorial sequence for connecting user needs, component choices and an end-to-end proof of concept.

[Home](../README.md) / [Curricula](curricula.md) / [Architecture and systems design](professions-architecture.md#roles-in-this-group)

**Target profile:** [Solutions Architect](professions-architecture.md#solutions-architect)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Have implemented or operated an application with an API and persistent storage.
- Can interpret HTTP requests and explain basic authentication and failure handling.
- Can gather requirements and identify constraints with a stakeholder.

**What you will produce:** A scoped booking-service solution with a working local slice, acceptance evidence and documented alternatives.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Establish the problem and acceptance conditions](#stage-1)
2. [Compare two end-to-end designs](#stage-2)
3. [Validate the riskiest interface](#stage-3)
4. [Deliver the booking-solution mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Establish the problem and acceptance conditions

**Learn:**

- Stakeholder needs
- Scope boundaries
- Quality scenarios

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).

**Practise:** Specify a fictional room-booking service with create, view and cancel actions, a double-booking constraint and an explicit list of excluded features.

**Advance when:** Every required action has an example acceptance condition and the scope identifies who may create and cancel a booking.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Compare two end-to-end designs

**Learn:**

- Application boundaries
- Storage choices
- Integration points

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [System Design (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design) — intermediate in this topic; free access. [Details](area-architecture.md#resource-karan-system-design).
- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).

**Practise:** Compare a single application with a relational store against separate booking and notification components; record the operational costs of each and choose the simplest justified option.

**Advance when:** The diagram follows one request through the whole solution and the ADR explains a disadvantage of the chosen design.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Validate the riskiest interface

**Learn:**

- Request validation
- Failure responses
- Executable API examples

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/) — intermediate in this topic; free access. [Details](area-web.md#resource-fastapi-tutorial).

**Practise:** Build a small Python API that accepts a booking request, validates its fields and returns a predictable response for an invalid request, using invented data and local storage.

**Advance when:** Saved example requests demonstrate one successful booking and one rejection with the expected status and body.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver the booking-solution mini-project

**Learn:**

- Acceptance evidence
- Deployment assumptions
- Operational handover

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).
- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).

**Practise:** Package the local slice with an architecture overview, test requests, run instructions and a list of unresolved production needs such as identity and recovery.

**Advance when:** Another person can reproduce the local acceptance cases and distinguish demonstrated behavior from proposed production capabilities.

## After this recipe

Review the design with implementation and operations colleagues, then validate one unresolved requirement at a time; a proof of concept is not a production approval.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)
- [Software Engineering Body of Knowledge](profession-references.md#reference-swebok)

[Back to roles in this group](professions-architecture.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
