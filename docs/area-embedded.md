# Embedded systems and firmware

_Microcontrollers, hardware programming and software that interacts with physical devices._

6 resources. [Home](../README.md) / [Catalogue](catalogue.md)

## Not sure where to start?

- [First project: embedded systems](path-embedded-systems.md): Choose Arduino or Raspberry Pi Pico and build a small, explainable LED firmware project.
  Before you start: Basic programming concepts, a compatible Arduino or Raspberry Pi Pico board, its cable and the matching toolchain.

For a longer learning recipe, [choose a profession curriculum](curricula.md).

The catalogue below is a reference shelf. You do not need to use every resource. [Read the access and level labels](catalogue.md#read-resource-labels).

<details><summary>Explore selected repositories after the first steps</summary>

## Selected repositories

- [Microsoft IoT for Beginners](https://github.com/microsoft/IoT-For-Beginners): Microsoft's 24-lesson project-based IoT curriculum covering device code, sensors, actuators, MQTT messaging, cloud connectivity and telemetry, with physical or virtual hardware options. (beginner in this topic; Free)
- [Rust Embedded Discovery - micro:bit v2](https://github.com/rust-embedded/discovery-mb2): Project-based book introducing microcontrollers through Rust on a BBC micro:bit v2, with setup, debugging and hardware exercises such as LED roulette. (intermediate in this topic; Free)

</details>

Jump to: [Courses and books](#courses-and-books) | [Lists, docs and articles](#lists-docs-and-articles)

## Courses and books

| Resource | Access | Topic level | What it offers |
|---|---|---|---|
| [Comprehensive Rust](https://github.com/google/comprehensive-rust) · [details](#resource-comprehensive-rust) | Free | intermediate | Google's Rust course for experienced programmers, combining language lessons and exercises with specialist material on Android, Chromium, bare-metal systems and concurrency. |
| [Microsoft IoT for Beginners](https://github.com/microsoft/IoT-For-Beginners) · [details](#resource-microsoft-iot-for-beginners) | Free | beginner | Microsoft's 24-lesson project-based IoT curriculum covering device code, sensors, actuators, MQTT messaging, cloud connectivity and telemetry, with physical or virtual hardware options. |
| [Rust Embedded Discovery - micro:bit v2](https://github.com/rust-embedded/discovery-mb2) · [details](#resource-rust-embedded-discovery-microbit-v2) | Free | intermediate | Project-based book introducing microcontrollers through Rust on a BBC micro:bit v2, with setup, debugging and hardware exercises such as LED roulette. |

<a id="resource-comprehensive-rust"></a>
<details><summary>Comprehensive Rust: requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Ordered topics with exercises such as implementing Fibonacci
- Freely licensed code examples and course documentation

**Requirements, costs and limitations:**

- Assumes programming experience, typically in languages such as C++ or Java
- Designed for classroom teaching; the authors say self-study misses discussions

**Source checked:** 2026-10-24 (github-repo).

Read the official README.md, LICENSE, LICENSE-CC-BY, src/SUMMARY.md and src/types-and-values/exercise.md via raw.githubusercontent.com. README describes experienced engineers as the audience and explicitly warns about classroom versus self-study limitations. The Fibonacci exercise asks learners to implement a function and consider panics, with instructor discussion notes. Code is Apache-2.0 and documentation CC-BY-4.0. Free refers to these course materials; English checked. Focus rating reflects sequenced lessons and small exercises. The course and code were not run.

**Study format:** guided. **Focus-friendly rating:** medium (editorial judgment).

</details>

<a id="resource-microsoft-iot-for-beginners"></a>
<details><summary>Microsoft IoT for Beginners: requirements and source notes</summary>

**Topic level:** beginner. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- MIT-licensed lesson material with quizzes, assignments and solutions
- A virtual hardware option lets learners start without buying a board
- Projects connect device programming with messages and observable outputs

**Requirements, costs and limitations:**

- Physical boards and sensors must be obtained separately if using that option
- Cloud lessons require Azure setup and may incur usage costs; current free allowances were not checked
- A Microsoft educational course rather than a professional-role standard or job qualification

**Source checked:** 2026-10-24 (github-repo).

Read the official README at https://raw.githubusercontent.com/microsoft/IoT-For-Beginners/main/README.md, MIT license at https://raw.githubusercontent.com/microsoft/IoT-For-Beginners/main/LICENSE, hardware guidance at https://raw.githubusercontent.com/microsoft/IoT-For-Beginners/main/hardware.md, introductory assignment at https://raw.githubusercontent.com/microsoft/IoT-For-Beginners/main/1-getting-started/lessons/1-introduction-to-iot/assignment.md, MQTT lesson at https://raw.githubusercontent.com/microsoft/IoT-For-Beginners/main/1-getting-started/lessons/4-connect-internet/README.md and cloud migration lesson at https://raw.githubusercontent.com/microsoft/IoT-For-Beginners/main/2-farm/lessons/4-migrate-your-plant-to-the-cloud/README.md. The README describes 12 weeks and 24 lessons; hardware.md explicitly allows virtual hardware for assignments. The MQTT lesson connects a nightlight to messaging and local server code. Free refers to reading and using the course material, not supplied hardware or unrestricted cloud services. English content checked; no device, simulator, cloud service or exercise was run.

**Study format:** guided. **Focus-friendly rating:** unknown (editorial judgment).

</details>

<a id="resource-rust-embedded-discovery-microbit-v2"></a>
<details><summary>Rust Embedded Discovery - micro:bit v2: requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Documentation is CC BY 4.0; source code offers a choice of MIT or Apache-2.0
- Ordered chapters connect tool setup to concrete hardware challenges
- LED roulette chapter includes a challenge and an optional partially completed solution template

**Requirements, costs and limitations:**

- Requires some Rust, including using closures; generics and traits are helpful
- Requires a micro:bit v2 board and data-capable micro-B USB cable, which are not included
- Using another board makes the instructions harder to follow and may require adaptation

**Source checked:** 2026-10-24 (github-repo).

Read rust-embedded/discovery-mb2 main README.md, mdbook/src/SUMMARY.md, mdbook/src/02-requirements/README.md and mdbook/src/07-led-roulette/the-challenge.md via raw.githubusercontent.com. Also read the actual CC-BY, MIT and Apache license files under mdbook/src/appendix/4-licenses-and-attribution/; root license paths are symlink text. Requirements specify prior Rust, micro:bit v2 and a data-capable cable. The challenge points to a partially completed solution template. Chose this version because the older rust-embedded/discovery README marks its micro:bit and F3 editions deprecated and recommends discovery-mb2. Free refers to the book and source, not hardware. English checked; hardware exercises were not executed and maintenance activity was not independently assessed.

**Study format:** guided. **Focus-friendly rating:** unknown (editorial judgment).

</details>


## Lists, docs and articles

| Resource | Access | Topic level | What it offers |
|---|---|---|---|
| [Arduino Built-in Examples - Blink](https://github.com/arduino/docs-content/blob/main/content/built-in-examples/01.basics/Blink/Blink.md) · [details](#resource-arduino-built-in-examples) | Free | beginner | Official beginner Arduino tutorial explaining how to blink an onboard LED, with hardware requirements, circuit guidance and annotated code. |
| [Raspberry Pi Pico SDK Examples](https://github.com/raspberrypi/pico-examples) · [details](#resource-raspberry-pi-pico-examples) | Free | intermediate | Official C/C++ examples for Raspberry Pi Pico-series microcontrollers covering serial output, LEDs, analog inputs and other peripherals. |
| [Zephyr - Basic Synchronization Sample](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/synchronization) · [details](#resource-zephyr-synchronization-sample) | Free | intermediate | Official real-time operating system example demonstrating two threads coordinating console greetings with semaphores and timing, with instructions for running in QEMU. |

<a id="resource-arduino-built-in-examples"></a>
<details><summary>Arduino Built-in Examples - Blink: requirements and source notes</summary>

**Topic level:** beginner. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- A small physical output makes the program's behavior visible
- Explains LED_BUILTIN, digital output and timing
- Documentation source is openly licensed under CC BY-SA 4.0

**Requirements, costs and limitations:**

- Requires a compatible Arduino board and a computer to run the example
- Hardware and any additional components are not included in the free documentation
- Pin assignments and electrical details depend on the board; follow the tutorial's circuit guidance

**Source checked:** 2026-10-24 (github-repo).

Read arduino/docs-content main README.md, LICENSE.md and content/built-in-examples/01.basics/Blink/Blink.md via raw.githubusercontent.com. The tutorial marks difficulty beginner, lists an Arduino board as required hardware, and explains the onboard LED, optional external LED and resistor, LED_BUILTIN, digitalWrite and delay. README and the full LICENSE.md identify CC BY-SA 4.0; the license file's introductory link label omits ShareAlike, but its linked target and full text include it. Hosted docs.arduino.cc access returned a proxy denial, so this entry links the verified source. Free refers to reading the tutorial, not hardware. English checked; no circuit was built or code executed.

**Study format:** guided. **Focus-friendly rating:** unknown (editorial judgment).

</details>

<a id="resource-raspberry-pi-pico-examples"></a>
<details><summary>Raspberry Pi Pico SDK Examples: requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Repository code is distributed under a BSD-3-Clause license
- Includes small Hello World and LED examples before more specialized topics
- README lists examples and links official getting-started and SDK documentation

**Requirements, costs and limitations:**

- Requires a compatible board, a development toolchain and the Pico SDK for hands-on use
- Some examples require a specific chip, board or wireless capability
- Free example code does not include hardware or additional electronic components

**Source checked:** 2026-10-24 (github-repo).

Read raspberrypi/pico-examples master README.md and LICENSE.TXT via raw.githubusercontent.com. README lists hello_serial, hello_usb, blink and ADC examples, links official getting-started and C/C++ SDK resources, and explains RP2040/RP2350 and wireless-board compatibility constraints. LICENSE.TXT contains the three-clause BSD redistribution terms. Free refers to the source examples and documentation, not required hardware. English checked; SDK setup, compilation and hardware behavior were not tested.

**Study format:** self-directed. **Focus-friendly rating:** unknown (editorial judgment).

</details>

<a id="resource-zephyr-synchronization-sample"></a>
<details><summary>Zephyr - Basic Synchronization Sample: requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Sample source explicitly uses Apache-2.0
- Demonstrates kernel synchronization beyond a single LED program
- Documented qemu_x86 emulation route allows studying this sample without purchasing a board

**Requirements, costs and limitations:**

- Assumes C knowledge and requires setting up the Zephyr build environment and QEMU
- An emulator demonstration does not validate behavior on a physical board
- This is one sample rather than a complete embedded systems course

**Source checked:** 2026-10-24 (github-repo).

Read zephyrproject-rtos/zephyr main README.rst, LICENSE, samples/synchronization/README.rst and samples/synchronization/src/main.c via raw.githubusercontent.com. README describes Zephyr as an RTOS and links getting-started documentation and code samples. The sample documentation explains alternating greetings from two threads using sleep and semaphores, supplies a qemu_x86 run example and expected console output. Source contains Apache-2.0 SPDX identification, matching the repository root license. Free refers to sample code and documentation; tool installation, execution and maintenance activity were not verified. English checked. No physical hardware is required for the documented QEMU route, but physical-board use may involve hardware costs.

**Study format:** semi. **Focus-friendly rating:** unknown (editorial judgment).

</details>
