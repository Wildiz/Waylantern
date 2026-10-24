# Learning curriculum: Integration Architect

An editorial lab for designing an interface, proving failure behavior and recording integration tradeoffs.

[Home](../README.md) / [Curricula](curricula.md) / [Architecture and systems design](professions-architecture.md#roles-in-this-group)

**Target profile:** [Integration Architect](professions-architecture.md#integration-architect)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Can implement a small Python HTTP API and inspect request and response bodies.
- Understand relational identifiers, authentication basics and dependency failures.
- Have access to a local development environment and invented test data.

**What you will produce:** A two-component local integration with an explicit contract, duplicate-request behavior and failure evidence.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Describe the exchange before selecting a protocol](#stage-1)
2. [Compare synchronous calls and asynchronous messages](#stage-2)
3. [Prove the chosen contract locally](#stage-3)
4. [Deliver an integration mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Describe the exchange before selecting a protocol

**Learn:**

- Producer and consumer
- Contract fields
- Error responses

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/) — intermediate in this topic; free access. [Details](area-web.md#resource-fastapi-tutorial).

**Practise:** Define an enrolment-to-billing request with a stable enrolment identifier, amount and required validation rules, plus one success and two rejection examples.

**Advance when:** Producer and consumer examples agree on field names, types and response meaning, including the difference between an invalid request and an unavailable dependency.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Compare synchronous calls and asynchronous messages

**Learn:**

- Request-response
- Message queues
- Duplicate delivery

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [System Design (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design) — intermediate in this topic; free access. [Details](area-architecture.md#resource-karan-system-design).
- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).

**Practise:** Compare an immediate billing API call with queued billing work, explain when a reply is needed and record a proposed policy for receiving the same enrolment identifier twice.

**Advance when:** The ADR describes a failure mode of each approach and specifies the intended duplicate behavior without claiming exactly-once delivery.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Prove the chosen contract locally

**Learn:**

- Validation
- Duplicate handling
- Dependency failure

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/) — intermediate in this topic; free access. [Details](area-web.md#resource-fastapi-tutorial).
- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).

**Practise:** Build two small local Python components using the synchronous option, validate requests and test normal, duplicate and simulated-unavailable responses; no message broker is required.

**Advance when:** Three named checks demonstrate the specified outcomes, and a duplicate request does not create a second charge in the invented billing store.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver an integration mini-project

**Learn:**

- Sequence diagrams
- Contract evolution
- Operating instructions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).
- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).

**Practise:** Package both components, contract examples and tests, draw a request sequence and assess adding a new optional field while an older consumer remains in use.

**Advance when:** Another person can run the local exchange and failure checks and explain which contract changes preserve compatibility and which need a migration.

## After this recipe

Study a verified messaging implementation before attempting the asynchronous option and validate real identity, retries and monitoring with the owning teams.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Software Engineering Body of Knowledge](profession-references.md#reference-swebok)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-architecture.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
