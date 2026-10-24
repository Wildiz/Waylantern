# First project: software architecture

Software architects help teams choose system boundaries, interfaces and technical tradeoffs that fit a project's requirements. Start after you can write and debug a small program, use Git and explain a basic automated test; Path 0 is a better starting point if those are new. Use a small application you understand, such as a local task tracker, rather than starting with a large distributed system. Read only the sections needed for the current decision. This route introduces architectural reasoning; it does not make someone a professional architect or promise a job after completing a checklist. If writing a test is unfamiliar, first use the software testing first-project guide; Path 0 alone does not teach test automation.

[Back to the start](../README.md)

**Short first-project guide.** To study toward a profession over a longer sequence, [choose a curriculum](curricula.md).

## Before you start

Ability to write and debug a small program, use Git and write a basic automated test.

If a step assumes programming or terminal skills you have not learned, use the relevant parts of [Path 0](path-0-fundamentals.md) first. Work through one small step at a time; you do not need to finish every linked course.

## Step 1: Define the problem before choosing technologies

Read the introductory system design section, then describe a tiny task tracker that can add a task, list tasks and mark one complete. State who uses it, what data must survive a restart and which features are outside your first version. Keep the first version local and single-user so the design has a clear boundary.

- [System Design (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design) (Free): Written system design course covering networking, databases, architecture patterns, reliability and worked design discussions for services such as a URL shortener.

**Advance when:** You have a one-page brief containing the three user actions, the persistence requirement, one failure to handle and explicit exclusions that another person could use to check the app.

## Step 2: Trace the boundaries in one small implementation

Choose one chapter with code in a language you can follow. Read its explanation alongside the implementation and sketch the main components and their interfaces. Follow one input through the program to its result, then identify one design decision and a possible alternative. You do not need to read or run every chapter.

- [500 Lines or Less](https://github.com/aosabook/500lines) (Free): Architecture of Open Source Applications book explaining design decisions and tradeoffs through walkthroughs of programs implemented in at most 500 source lines each.

**Advance when:** You can explain the path of one input through the chosen example and describe a concrete benefit and cost of one boundary or interface used by its author.

## Step 3: Build the smallest version and record one decision

Apply the idea of explicit boundaries to your task tracker. Keep task rules separate from file storage behind a small interface; a command-line interface is sufficient. Implement the three actions, save tasks between runs and test the completion rule. Write a short decision note explaining the storage choice, an alternative and the tradeoff. This is your own exercise inspired by the book, not an assignment supplied by it.

- [500 Lines or Less](https://github.com/aosabook/500lines) (Free): Architecture of Open Source Applications book explaining design decisions and tradeoffs through walkthroughs of programs implemented in at most 500 source lines each.

**Advance when:** Your three actions work, a task survives a restart, a test checks the completion rule, and you can identify which code would change if file storage were replaced.

## Step 4: Revisit the design when one requirement changes

Imagine that two people now need to share the task list. Use the relevant system design sections to compare extending your single application with a shared database against splitting it into separate services. Draw the changed boundary and discuss conflicting updates, failures and operational work. Propose the simplest justified next version; you do not need to deploy either option or add infrastructure just to finish this step.

- [The System Design Primer](https://github.com/donnemartin/system-design-primer) (Free): Open-source guide to designing large-scale systems and preparing for system design interviews.

**Advance when:** You have a revised diagram and a decision note that names a benefit and cost of each option, explains your choice for two users and states what evidence could change that choice.

## Where to go next

After the last checkpoint, improve your project or browse the related areas for a specific gap:

- [Software and systems architecture](area-architecture.md)

[Compare first-project guides](learning-paths.md) · [Choose a profession curriculum](curricula.md)

---
Tell us what worked for you: see [CONTRIBUTING](../CONTRIBUTING.md).
