# Learning curriculum: Full Stack Developer

Connect a browser workflow to a service and database while keeping their responsibilities clear.

[Home](../README.md) / [Curricula](curricula.md) / [Software, interfaces and embedded systems](professions-software.md#roles-in-this-group)

**Target profile:** [Full Stack Developer](professions-software.md#full-stack-developer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic JavaScript and HTML
- Basic Python
- HTTP and Git basics

**What you will produce:** A reading-list application with browser interaction, server validation and persistent records.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Trace a complete user action](#stage-1)
2. [Build the server slice](#stage-2)
3. [Connect interactive feedback](#stage-3)
4. [Deliver an end-to-end mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Trace a complete user action

**Learn:**

- User journey
- Browser and server boundaries
- Data flow

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [MDN Web Docs](https://developer.mozilla.org/) — all in this topic; free access. [Details](area-web.md#resource-mdn-web-docs).
- [Open Practice Library](https://github.com/openpracticelibrary/openpracticelibrary) — intermediate in this topic; free access. [Details](area-design-product.md#resource-open-practice-library).

**Practise:** Diagram adding a book from the form through server validation to storage, then build the static form.

**Advance when:** Identify which layer displays results, validates records and persists them.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Build the server slice

**Learn:**

- Models and records
- Server validation
- Request handling

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Django: Writing your first Django app](https://docs.djangoproject.com/en/stable/intro/tutorial01/) — beginner in this topic; free access. [Details](area-web.md#resource-django-tutorial).

**Practise:** Create the reading-list model and a server-backed list using the tutorial structure.

**Advance when:** Submit a book, reload the application and retrieve its stored data.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Connect interactive feedback

**Learn:**

- Client requests
- Loading and error states
- Accessible status messages

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [The Modern JavaScript Tutorial (javascript.info)](https://javascript.info/) — beginner in this topic; free access. [Details](area-web.md#resource-javascript-info).
- [MDN Web Docs](https://developer.mozilla.org/) — all in this topic; free access. [Details](area-web.md#resource-mdn-web-docs).

**Practise:** Add a browser interaction that reports submission status and preserves input when a request fails.

**Advance when:** Demonstrate a successful request and a simulated error without losing the typed title.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver an end-to-end mini-project

**Learn:**

- Browser tests
- Test fixtures
- Reproducible setup

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Playwright - Getting Started](https://github.com/microsoft/playwright) — intermediate in this topic; free access. [Details](area-testing.md#resource-playwright-getting-started).
- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).

**Practise:** Deliver an add-and-complete-book workflow with synthetic fixtures and automated checks.

**Advance when:** Recreate the application locally and verify a saved book through a browser test after reload.

## After this recipe

Add one feature at a time and study authentication and deployment as separate engineering topics.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Software Engineering Body of Knowledge](profession-references.md#reference-swebok)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-software.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
