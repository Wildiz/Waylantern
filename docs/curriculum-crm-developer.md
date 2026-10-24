# Editorial practice plan: CRM Developer

Explore CRM records and customization through a local surrogate rather than inventing platform coverage.

[Home](../README.md) / [Curricula](curricula.md) / [Software, interfaces and embedded systems](professions-software.md#roles-in-this-group)

[Academic-plan work and resource-matching preview](software-study-preview.md). This page is an existing editorial practice plan; it is not derived from an inspected university curriculum.

**Target profile:** [CRM Developer](professions-software.md#crm-developer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic programming
- Relational data and SQL
- Basic HTTP

**What you will produce:** A synthetic lead-management prototype with access checks and an explicit vendor-training gap.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Model customer records](#stage-1)
2. [Identify extension boundaries](#stage-2)
3. [Protect and exchange records](#stage-3)
4. [Deliver the CRM workflow study](#stage-4)

<a id="stage-1"></a>
## 1. Model customer records

**Learn:**

- Leads and accounts
- Relationships
- Record lifecycle

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [SQLBolt](https://sqlbolt.com/) — beginner in this topic; free access. [Details](area-data.md#resource-sqlbolt).
- [DB Browser for SQLite](https://github.com/sqlitebrowser/sqlitebrowser) — beginner in this topic; free access. [Details](area-data.md#resource-db-browser-for-sqlite).

**Practise:** Create synthetic lead and account tables and document lead-status changes.

**Advance when:** Query relationships and reject a lead referencing an absent account.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Identify extension boundaries

**Learn:**

- Objects and metadata
- Validation rules
- Transaction limits

**Resource still needed:** No Salesforce or other CRM-specific developer curriculum is verified; select official platform documentation before writing vendor-specific code.

**Practise:** Map a hypothetical workflow to vendor configuration and code responsibilities.

**Advance when:** Explain which behavior could be configured without claiming a working platform implementation.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Protect and exchange records

**Learn:**

- Record-level access
- Audit trails
- API mapping

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Django: Writing your first Django app](https://docs.djangoproject.com/en/stable/intro/tutorial01/) — beginner in this topic; free access. [Details](area-web.md#resource-django-tutorial).
- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/) — intermediate in this topic; free access. [Details](area-web.md#resource-fastapi-tutorial).

**Resource still needed:** Web resources support the surrogate only; vendor permissions, bulk limits and deployment procedures remain unverified.

**Practise:** Build a local surrogate with synthetic users, access rules and an export schema.

**Advance when:** Demonstrate that one test user cannot retrieve another user's private record.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver the CRM workflow study

**Learn:**

- Acceptance cases
- Reconciliation
- Platform distinctions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).
- [Django: Writing your first Django app](https://docs.djangoproject.com/en/stable/intro/tutorial01/) — beginner in this topic; free access. [Details](area-web.md#resource-django-tutorial).

**Practise:** Deliver valid transitions, rejected updates and access-boundary tests for the surrogate.

**Advance when:** Reproduce each case and separate generic application behavior from unimplemented platform features.

## After this recipe

Select one verified vendor curriculum and permitted developer sandbox; a local surrogate does not demonstrate Salesforce proficiency.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-software.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
