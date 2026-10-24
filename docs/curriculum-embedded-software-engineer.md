# Learning curriculum: Embedded Software Engineer

Connect programs to device inputs and outputs with explicit timing checks.

[Home](../README.md) / [Curricula](curricula.md) / [Software, interfaces and embedded systems](professions-software.md#roles-in-this-group)

**Target profile:** [Embedded Software Engineer](professions-software.md#embedded-software-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic programming and loops
- Binary numbers and units
- A supported board or suitable simulator

**What you will produce:** A nonblocking device-state prototype with input handling and labelled hardware or simulation evidence.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Understand device execution](#stage-1)
2. [Read inputs and track state](#stage-2)
3. [Avoid blocking the device](#stage-3)
4. [Deliver the device mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Understand device execution

**Learn:**

- Pins and peripherals
- Main loop
- Build and flash

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Arduino Built-in Examples - Blink](https://github.com/arduino/docs-content/blob/main/content/built-in-examples/01.basics/Blink/Blink.md) — beginner in this topic; free access. [Details](area-embedded.md#resource-arduino-built-in-examples).

**Practise:** Follow Blink on supported equipment and label the required board and output.

**Advance when:** Explain what runs on the device and distinguish a measured signal from simulated behavior.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Read inputs and track state

**Learn:**

- Digital inputs
- State machines
- Input noise

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Raspberry Pi Pico SDK Examples](https://github.com/raspberrypi/pico-examples) — intermediate in this topic; free access. [Details](area-embedded.md#resource-raspberry-pi-pico-examples).

**Practise:** Use a matching-board input example to design button-controlled operating states.

**Advance when:** Predict and record output for a sequence of inputs, including repeated transitions.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Avoid blocking the device

**Learn:**

- Timers
- Scheduling
- Debug output

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Zephyr - Basic Synchronization Sample](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/synchronization) — intermediate in this topic; free access. [Details](area-embedded.md#resource-zephyr-synchronization-sample).

**Practise:** Study the synchronization example and compare blocking behavior with scheduled updates in a lab.

**Advance when:** Demonstrate that a second periodic action continues while the first waits.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver the device mini-project

**Learn:**

- State-table tests
- Timing observations
- Fault states

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Arduino Built-in Examples - Blink](https://github.com/arduino/docs-content/blob/main/content/built-in-examples/01.basics/Blink/Blink.md) — beginner in this topic; free access. [Details](area-embedded.md#resource-arduino-built-in-examples).
- [Raspberry Pi Pico SDK Examples](https://github.com/raspberrypi/pico-examples) — intermediate in this topic; free access. [Details](area-embedded.md#resource-raspberry-pi-pico-examples).

**Practise:** Build a button-controlled indicator with timing checks and a documented safe output state.

**Advance when:** Reproduce normal input, a noisy-input case and restart, labelling each hardware or simulation result.

## After this recipe

Choose one platform for deeper study; electrical design, real-time assurance and safety engineering require specialist instruction.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [ACM Computing Curricula Recommendations](profession-references.md#reference-acm-curricula)
- [CS2023 — Computer Science Curricula](profession-references.md#reference-cs2023)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)
- [IoT for Beginners](profession-references.md#reference-microsoft-iot)

[Back to roles in this group](professions-software.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
