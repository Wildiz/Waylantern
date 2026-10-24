# First project: IT support and help desk

IT support and help desk work involves understanding a reported problem, checking evidence, helping a user and documenting the result or escalation. This route introduces those habits through a Linux practice system and a separate ticketing lab. Linux administration is only part of IT support: Windows support, desktop hardware, identity administration and organisation-specific procedures are outside this short route. It is a first project, not a full support qualification or a promise of employment. Use disposable local systems and invented users, assets and tickets; GLPI is a service-desk tool, not a complete support course.

[Back to the start](../README.md)

**Short first-project guide.** To study toward a profession over a longer sequence, [choose a curriculum](curricula.md).

## Before you start

Basic computer skills and access to a disposable Linux practice environment; no programming experience is required.

If a step assumes programming or terminal skills you have not learned, use the relevant parts of [Path 0](path-0-fundamentals.md) first. Work through one small step at a time; you do not need to finish every linked course.

## Step 1: Get comfortable with a Linux practice system

Use the setup lesson to choose a practice system you control; a local lab avoids assuming a paid cloud server. Work through the early lessons on connecting, navigating files, reading help and installing software. Write down what each command tells you rather than copying commands without understanding their effect. Keep administrative experiments out of a personal or workplace production system.


- [Linux Upskill Challenge](https://github.com/livialima/linuxupskillchallenge) (Free): A sequenced hands-on Linux administration course covering server access, command-line navigation, packages, services, logs, networking, users and permissions.

**Advance when:** You can find a file, explain a basic system-status command and use its help page to check an option before running it.

## Step 2: Diagnose one small service problem

Use the course's service and log lessons to practise a small case on your lab, such as checking whether the practice web service is running. Write down the reported symptom, the checks you performed and what the status output or logs showed. If you change a setting or restart a service, record the change and verify the result. Distinguish an observation from a guessed cause; do not claim a problem is solved merely because a command completed.


- [Linux Upskill Challenge](https://github.com/livialima/linuxupskillchallenge) (Free): A sequenced hands-on Linux administration course covering server access, command-line navigation, packages, services, logs, networking, users and permissions.

**Advance when:** You can show the symptom, a relevant status or log observation, the action taken and a check confirming the result or explaining what remains unknown.

## Step 3: Turn the practice case into a support ticket

Start by writing a plain-text ticket for the service case from the previous step, with an invented user and asset. If you want to practise with a service-desk application, GLPI is an optional next lab: follow its documentation for an isolated test installation with a web server, PHP and database. Deploying GLPI is not required to complete this route. Include the symptom, impact, evidence, actions and outcome, plus a short plain-language reply to the user. Finish with either a verified resolution or an escalation note naming the next check and missing information. Export or capture an anonymised example as your microproject; do not enter real credentials or customer details.


- [GLPI](https://github.com/glpi-project/glpi) (Free): An open-source IT asset and service-desk application for practising ticket handling, incident and problem management, inventory and knowledge-base workflows in a test installation.

**Advance when:** A second reader can follow the invented ticket from the initial report to a verified result or a clear escalation, using the evidence and notes you recorded.

## Where to go next

After the last checkpoint, improve your project or browse the related areas for a specific gap:

- [IT support and service management](area-it-support.md)

[Compare first-project guides](learning-paths.md) · [Choose a profession curriculum](curricula.md)

---
Tell us what worked for you: see [CONTRIBUTING](../CONTRIBUTING.md).
