# First project: embedded systems

Embedded and firmware engineers write software that controls hardware and communicates with physical devices. This route introduces that work through an observable LED project, not a complete engineering curriculum or a promise of employment. You need a computer, basic programming concepts, a compatible board and its connection cable. Choose one route: Arduino with the Blink tutorial, or Raspberry Pi Pico with its C/C++ SDK examples. Keep that choice throughout; the resources shown together are alternatives. Documentation and example code are free to read, but hardware and additional components are not included. Follow the selected board's official setup and circuit instructions; do not assume pin assignments or example compatibility transfer unchanged to a different board. Start with the onboard LED so no extra circuit is needed.
 If unsure and choosing hardware for a first project, start with the Arduino Blink route. If you do not have a board yet, explore the virtual-hardware option in the Microsoft IoT curriculum before buying one; the physical LED checkpoint still needs a compatible board.

[Back to the start](../README.md)

**Short first-project guide.** To study toward a profession over a longer sequence, [choose a curriculum](curricula.md).

## Before you start

Basic programming concepts, a compatible Arduino or Raspberry Pi Pico board, its cable and the matching toolchain.

If a step assumes programming or terminal skills you have not learned, use the relevant parts of [Path 0](path-0-fundamentals.md) first. Work through one small step at a time; you do not need to finish every linked course.

## Step 1: Identify the board and run its matching LED example

For Arduino, follow the Blink tutorial and the setup instructions for your exact board. For Pico, follow the getting-started documentation linked from the examples repository, then choose the blink example matching your board; Pico W LED handling differs from some other Pico boards. Set up only the chosen toolchain. Note the board model, selected example and command or IDE action used to build and upload it.


- [Arduino Built-in Examples - Blink](https://github.com/arduino/docs-content/blob/main/content/built-in-examples/01.basics/Blink/Blink.md) (Free): Official beginner Arduino tutorial explaining how to blink an onboard LED, with hardware requirements, circuit guidance and annotated code.
- [Raspberry Pi Pico SDK Examples](https://github.com/raspberrypi/pico-examples) (Free): Official C/C++ examples for Raspberry Pi Pico-series microcontrollers covering serial output, LEDs, analog inputs and other peripherals.

**Advance when:** The correct onboard LED blinks, you can rebuild and upload the example again, and you can explain which board and example you used without guessing the pin number.


## Step 2: Change one timing value and predict the visible result

Stay with the same board and example. Find the timing value or delay that controls the blink interval. Before editing it, write down whether you expect the light to blink faster or slower. Change one value, rebuild and upload, then compare the observed behavior with your prediction. Restore the original value and repeat to distinguish a code change from an upload or connection problem.


- [Arduino Built-in Examples - Blink](https://github.com/arduino/docs-content/blob/main/content/built-in-examples/01.basics/Blink/Blink.md) (Free): Official beginner Arduino tutorial explaining how to blink an onboard LED, with hardware requirements, circuit guidance and annotated code.
- [Raspberry Pi Pico SDK Examples](https://github.com/raspberrypi/pico-examples) (Free): Official C/C++ examples for Raspberry Pi Pico-series microcontrollers covering serial output, LEDs, analog inputs and other peripherals.

**Advance when:** You can demonstrate both timing settings, explain the unit used by the chosen API and trace the code that turns the LED on and off.


## Step 3: Build and explain a small repeating signal

Extend the same program into a repeating signal such as two short flashes, one longer flash and a pause. Use a small helper function or named timing values so the pattern is readable. Keep it on the onboard LED rather than adding unfamiliar wiring. Write down the expected sequence, then check the output after a fresh upload and after restarting the board. Document the board, toolchain setup, build or upload steps and the one limitation you would investigate next, such as how blocking delays affect other tasks.


- [Arduino Built-in Examples - Blink](https://github.com/arduino/docs-content/blob/main/content/built-in-examples/01.basics/Blink/Blink.md) (Free): Official beginner Arduino tutorial explaining how to blink an onboard LED, with hardware requirements, circuit guidance and annotated code.
- [Raspberry Pi Pico SDK Examples](https://github.com/raspberrypi/pico-examples) (Free): Official C/C++ examples for Raspberry Pi Pico-series microcontrollers covering serial output, LEDs, analog inputs and other peripherals.

**Advance when:** The signal matches your written sequence after upload and restart, and you can explain each part of the program and reproduce the build using your notes.


## Where to go next

After the last checkpoint, improve your project or browse the related areas for a specific gap:

- [Embedded systems and firmware](area-embedded.md)

[Compare first-project guides](learning-paths.md) · [Choose a profession curriculum](curricula.md)

---
Tell us what worked for you: see [CONTRIBUTING](../CONTRIBUTING.md).
