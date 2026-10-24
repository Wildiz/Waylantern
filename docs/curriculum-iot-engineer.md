# Learning curriculum: IoT Engineer

Connect device-like measurements to a local receiver with clear failure behavior.

[Home](../README.md) / [Curricula](curricula.md) / [Software, interfaces and embedded systems](professions-software.md#roles-in-this-group)

**Target profile:** [IoT Engineer](professions-software.md#iot-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic programming
- Simple HTTP and networks
- A supported or simulated sensor environment

**What you will produce:** A local telemetry prototype with validated messages and bounded reconnect behavior.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Acquire a measurement](#stage-1)
2. [Define the message contract](#stage-2)
3. [Handle interrupted delivery](#stage-3)
4. [Deliver the telemetry mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Acquire a measurement

**Learn:**

- Sensor inputs
- Units and sampling
- Synthetic signals

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Microsoft IoT for Beginners](https://github.com/microsoft/IoT-For-Beginners) — beginner in this topic; free access. [Details](area-embedded.md#resource-microsoft-iot-for-beginners).

**Practise:** Use a virtual or supported sensor exercise to generate a labelled measurement sequence.

**Advance when:** Explain units and sampling interval and identify synthetic readings.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Define the message contract

**Learn:**

- Device identity
- Timestamps
- Payload validation

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Microsoft IoT for Beginners](https://github.com/microsoft/IoT-For-Beginners) — beginner in this topic; free access. [Details](area-embedded.md#resource-microsoft-iot-for-beginners).
- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/) — intermediate in this topic; free access. [Details](area-web.md#resource-fastapi-tutorial).

**Practise:** Send synthetic measurements to a local service using dummy device IDs and an explicit schema.

**Advance when:** Reject a message with an invalid unit or missing required field.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Handle interrupted delivery

**Learn:**

- Buffer limits
- Reconnection
- Duplicate messages

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Microsoft IoT for Beginners](https://github.com/microsoft/IoT-For-Beginners) — beginner in this topic; free access. [Details](area-embedded.md#resource-microsoft-iot-for-beginners).
- [Computer Networks: A Systems Approach](https://github.com/SystemsApproach/book) — intermediate in this topic; free access. [Details](area-networking.md#resource-computer-networks-systems-approach).

**Practise:** Disconnect the receiver and implement a bounded buffering and replay policy.

**Advance when:** Restore delivery and account for accepted, duplicate and intentionally dropped readings.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver the telemetry mini-project

**Learn:**

- Access boundaries
- Observability
- Recovery checks

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Microsoft IoT for Beginners](https://github.com/microsoft/IoT-For-Beginners) — beginner in this topic; free access. [Details](area-embedded.md#resource-microsoft-iot-for-beginners).
- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).

**Practise:** Deliver a virtual-sensor pipeline with synthetic data and an outage exercise.

**Advance when:** Reproduce normal operation, malformed input and restart without claiming production device security.

## After this recipe

Study secure provisioning and device updates separately and check hardware or cloud costs before choosing external services.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [ACM Computing Curricula Recommendations](profession-references.md#reference-acm-curricula)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)
- [IoT for Beginners](profession-references.md#reference-microsoft-iot)

[Back to roles in this group](professions-software.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
