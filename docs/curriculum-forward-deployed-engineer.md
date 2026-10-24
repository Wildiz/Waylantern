# Editorial practice plan: Forward Deployed Engineer

Adapt a product to a fictional customer workflow using explicit acceptance evidence.

[Home](../README.md) / [Curricula](curricula.md) / [Software, interfaces and embedded systems](professions-software.md#roles-in-this-group)

[Academic-plan work and resource-matching preview](software-study-preview.md). This page is an existing editorial practice plan; it is not derived from an inspected university curriculum.

**Target profile:** [Forward Deployed Engineer](professions-software.md#forward-deployed-engineer)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Experience building and testing a service
- SQL and HTTP fundamentals
- Ability to explain technical trade-offs

**What you will produce:** A synthetic customer integration with acceptance tests, rollback instructions and a handover.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Discover the operational need](#stage-1)
2. [Inspect integration boundaries](#stage-2)
3. [Prove a limited adaptation](#stage-3)
4. [Deliver the customer-case mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Discover the operational need

**Learn:**

- Stakeholder questions
- Workflow mapping
- Acceptance criteria

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Open Practice Library](https://github.com/openpracticelibrary/openpracticelibrary) — intermediate in this topic; free access. [Details](area-design-product.md#resource-open-practice-library).

**Practise:** Define a fictional support-team workflow with three constraints and measurable success conditions.

**Advance when:** Trace each requested change to an example or an explicitly labelled assumption.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Inspect integration boundaries

**Learn:**

- API contracts
- Data mapping
- Failure ownership

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/) — intermediate in this topic; free access. [Details](area-web.md#resource-fastapi-tutorial).
- [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) — intermediate in this topic; free access. [Details](area-architecture.md#resource-arc42-template).

**Practise:** Define source and target schemas for synthetic tickets and diagram an adapter boundary.

**Advance when:** Explain who retries transfers and which system owns each field.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Prove a limited adaptation

**Learn:**

- Input validation
- Reconciliation
- Idempotency

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [The Python Tutorial (official)](https://docs.python.org/3/tutorial/) — beginner in this topic; free access. [Details](area-software.md#resource-python-tutorial).
- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).
- [DB Browser for SQLite](https://github.com/sqlitebrowser/sqlitebrowser) — beginner in this topic; free access. [Details](area-data.md#resource-db-browser-for-sqlite).

**Practise:** Import synthetic tickets through an adapter and record rejected records separately.

**Advance when:** Repeat the import without duplicates and reconcile source, accepted and rejected counts.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver the customer-case mini-project

**Learn:**

- Acceptance tests
- Rollout and rollback
- Operational handover

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) — intermediate in this topic; free access. [Details](area-architecture.md#resource-madr).
- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).

**Practise:** Deliver a before-and-after demonstration and a rollback procedure for the fictional customer.

**Advance when:** Replay the acceptance scenarios and restore the original state from the documented procedure.

## After this recipe

Seek supervised work with organizational constraints; do not use customer data without permission or present a fictional case as customer experience.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Software Engineering Body of Knowledge](profession-references.md#reference-swebok)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-software.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
