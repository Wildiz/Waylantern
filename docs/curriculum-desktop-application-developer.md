# Editorial practice plan: Desktop Application Developer

Explore desktop event-driven applications while making toolkit-specific gaps visible.

[Home](../README.md) / [Curricula](curricula.md) / [Software, interfaces and embedded systems](professions-software.md#roles-in-this-group)

[Academic-plan work and resource-matching preview](software-study-preview.md). This page is an existing editorial practice plan; it is not derived from an inspected university curriculum.

**Target profile:** [Desktop Application Developer](professions-software.md#desktop-application-developer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Python functions and files
- Basic testing
- Access to a desktop computer

**What you will produce:** A local notes prototype with saved data, a graphical workflow and explicit platform limits.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Separate notes from the interface](#stage-1)
2. [Learn a desktop event loop](#stage-2)
3. [Handle desktop lifecycle choices](#stage-3)
4. [Deliver the desktop mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Separate notes from the interface

**Learn:**

- Application state
- File persistence
- Exceptions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [The Python Tutorial (official)](https://docs.python.org/3/tutorial/) — beginner in this topic; free access. [Details](area-software.md#resource-python-tutorial).

**Practise:** Implement note creation and saving before adding graphical controls.

**Advance when:** Recover notes after restart and handle a missing file predictably.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Learn a desktop event loop

**Learn:**

- Widgets and layout
- Callbacks
- UI responsiveness

**Resource still needed:** No dedicated desktop GUI toolkit tutorial is verified in the catalogue; select platform-compatible official documentation before this implementation.

**Practise:** Use separately verified toolkit material to connect a text field and save button to the note functions.

**Advance when:** Create and save a note without freezing the interface.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Handle desktop lifecycle choices

**Learn:**

- File dialogs
- Unsaved changes
- Keyboard navigation

**Resource still needed:** Toolkit-specific documentation for dialogs and application lifecycle remains unverified; the Python language tutorial does not cover these responsibilities.

**Practise:** Specify save, cancel and close behavior and implement a visible unsaved-changes state.

**Advance when:** Show cancel preserving work and keyboard access to the save action.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver the desktop mini-project

**Learn:**

- Core regression tests
- Data recovery
- Platform instructions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).
- [The Python Tutorial (official)](https://docs.python.org/3/tutorial/) — beginner in this topic; free access. [Details](area-software.md#resource-python-tutorial).

**Practise:** Deliver the notes prototype with persistence tests and instructions for its supported operating system.

**Advance when:** A repeated run restores notes and a corrupted test file produces a useful error rather than silent data loss.

## After this recipe

Verify packaging, platform accessibility and update behavior for the chosen toolkit before distributing the application.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Software Engineering Body of Knowledge](profession-references.md#reference-swebok)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-software.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
