# Editorial practice plan: Server Side Game Developer

Build an authoritative local game service that rejects untrusted moves.

[Home](../README.md) / [Curricula](curricula.md) / [Software, interfaces and embedded systems](professions-software.md#roles-in-this-group)

[Academic-plan work and resource-matching preview](software-study-preview.md). This page is an existing editorial practice plan; it is not derived from an inspected university curriculum.

**Target profile:** [Server Side Game Developer](professions-software.md#server-side-game-developer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Programming functions and state
- Basic sockets or HTTP
- Simple data structures

**What you will produce:** A two-client turn-based game with server-validated moves and replayable logs.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Specify authoritative rules](#stage-1)
2. [Connect two local clients](#stage-2)
3. [Handle repeats and disconnects](#stage-3)
4. [Deliver the multiplayer mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Specify authoritative rules

**Learn:**

- Server-owned state
- Legal moves and turns
- Message schemas

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Beej's Guides](https://beej.us/guide/) — intermediate in this topic; free access. [Details](area-cs.md#resource-beejs-guides).

**Practise:** Define a small grid game and identify state that only the server can change.

**Advance when:** Classify valid, out-of-turn and impossible moves before implementation.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Connect two local clients

**Learn:**

- Sockets and framing
- Connection lifecycle
- Error responses

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Beej's Guides](https://beej.us/guide/) — intermediate in this topic; free access. [Details](area-cs.md#resource-beejs-guides).

**Practise:** Run a local server and two clients exchanging bounded move messages.

**Advance when:** Both clients observe the same accepted move and malformed messages are rejected.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Handle repeats and disconnects

**Learn:**

- Sequence numbers
- Duplicate messages
- Session recovery

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).
- [Computer Networks: A Systems Approach](https://github.com/SystemsApproach/book) — intermediate in this topic; free access. [Details](area-networking.md#resource-computer-networks-systems-approach).

**Practise:** Add message IDs and a game log and simulate retry after disconnect.

**Advance when:** A repeated move is applied once and a reconnecting client receives current state.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver the multiplayer mini-project

**Learn:**

- Rule tests
- Replay consistency
- Failure cases

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).

**Practise:** Deliver a deterministic replay and tests for illegal moves, duplicate delivery and disconnects.

**Advance when:** Replay to the same final state and demonstrate that clients cannot set score directly.

## After this recipe

Study latency compensation and scaling afterward; turn-based lab results do not validate real-time multiplayer architecture.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Software Engineering Body of Knowledge](profession-references.md#reference-swebok)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-software.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
