# Learning curriculum: Backend Developer

Build a service with explicit data rules and testable API responses.

[Home](../README.md) / [Curricula](curricula.md) / [Software, interfaces and embedded systems](professions-software.md#roles-in-this-group)

**Target profile:** [Backend Developer](professions-software.md#backend-developer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Python functions and modules
- Basic terminal use
- Basic Git

**What you will produce:** A local inventory API with SQLite persistence, validation and API tests.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Specify an API contract](#stage-1)
2. [Store consistent records](#stage-2)
3. [Separate and test business rules](#stage-3)
4. [Deliver the service mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Specify an API contract

**Learn:**

- HTTP methods
- Status codes
- Request schemas

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [MDN Web Docs](https://developer.mozilla.org/) — all in this topic; free access. [Details](area-web.md#resource-mdn-web-docs).
- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/) — intermediate in this topic; free access. [Details](area-web.md#resource-fastapi-tutorial).

**Practise:** Define create, list and update inventory operations and implement an in-memory endpoint.

**Advance when:** Send valid and invalid requests and explain their different responses.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Store consistent records

**Learn:**

- SQL queries
- Keys and constraints
- Transactions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [SQLBolt](https://sqlbolt.com/) — beginner in this topic; free access. [Details](area-data.md#resource-sqlbolt).
- [DB Browser for SQLite](https://github.com/sqlitebrowser/sqlitebrowser) — beginner in this topic; free access. [Details](area-data.md#resource-db-browser-for-sqlite).

**Practise:** Create an inventory table with unique IDs and document the rejected-duplicate case.

**Advance when:** Restart the service and recover records while preserving the uniqueness rule.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Separate and test business rules

**Learn:**

- Dependency boundaries
- Error handling
- API tests

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/) — intermediate in this topic; free access. [Details](area-web.md#resource-fastapi-tutorial).
- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).

**Practise:** Test stock calculations separately and return consistent errors for absent records.

**Advance when:** Cover successful updates, missing items and invalid quantities in tests.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver the service mini-project

**Learn:**

- Configuration
- Initialization
- Reproducible requests

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/) — intermediate in this topic; free access. [Details](area-web.md#resource-fastapi-tutorial).
- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).

**Practise:** Deliver synthetic fixtures, setup instructions and representative API requests.

**Advance when:** Initialize a fresh local database and reproduce the documented stock changes.

## After this recipe

Study authorization, migrations and concurrency in a controlled lab before exposing a service to real users.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Software Engineering Body of Knowledge](profession-references.md#reference-swebok)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-software.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
