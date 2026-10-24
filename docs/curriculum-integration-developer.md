# Learning curriculum: Integration Developer

Transfer synthetic records between systems without losing meaning or recoverability.

[Home](../README.md) / [Curricula](curricula.md) / [Software, interfaces and embedded systems](professions-software.md#roles-in-this-group)

**Target profile:** [Integration Developer](professions-software.md#integration-developer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic programming
- HTTP and JSON
- Simple SQL

**What you will produce:** A local adapter with documented mappings, bounded retries and duplicate protection.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Map two contracts](#stage-1)
2. [Implement an adapter](#stage-2)
3. [Make repeated delivery safe](#stage-3)
4. [Deliver the integration mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Map two contracts

**Learn:**

- Field semantics
- Schema mapping
- Data ownership

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [MDN Web Docs](https://developer.mozilla.org/) — all in this topic; free access. [Details](area-web.md#resource-mdn-web-docs).
- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).

**Practise:** Map a fictional shop order to a warehouse record, including units and missing values.

**Advance when:** Explain every mapped field and flag ambiguous transformations instead of guessing.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Implement an adapter

**Learn:**

- Serialization
- Validation
- Error responses

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [The Python Tutorial (official)](https://docs.python.org/3/tutorial/) — beginner in this topic; free access. [Details](area-software.md#resource-python-tutorial).
- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/) — intermediate in this topic; free access. [Details](area-web.md#resource-fastapi-tutorial).

**Practise:** Build a local endpoint that validates orders and produces the warehouse schema.

**Advance when:** Valid fixtures transform correctly and malformed fixtures return a documented error.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Make repeated delivery safe

**Learn:**

- Idempotency keys
- Retry limits
- Reconciliation

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).
- [DB Browser for SQLite](https://github.com/sqlitebrowser/sqlitebrowser) — beginner in this topic; free access. [Details](area-data.md#resource-db-browser-for-sqlite).

**Practise:** Store processed message IDs and record failed transfers in a review table.

**Advance when:** Sending the same message twice creates one record and every failure remains traceable.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver the integration mini-project

**Learn:**

- Contract tests
- Schema versions
- Recovery runbook

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).
- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).

**Practise:** Support a second message version and document a controlled replay of rejected messages.

**Advance when:** Test both supported versions and reconcile the replay without creating duplicates.

## After this recipe

Study messaging platforms and distributed transactions after understanding failures and reconciliation in the local adapter.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Software Engineering Body of Knowledge](profession-references.md#reference-swebok)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-software.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
