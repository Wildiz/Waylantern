# Computer networks

_Protocols, packet analysis, network simulation and how computers communicate._

11 resources. [Home](../README.md) / [Catalogue](catalogue.md)

## Not sure where to start?

- [First project: networking](path-networking.md): Understand connections, build a small network and diagnose a broken link.
  Before you start: Basic file management and terminal commands; programming experience is not required.

For a longer learning recipe, [choose a profession curriculum](curricula.md).

The catalogue below is a reference shelf. You do not need to use every resource. [Read the access and level labels](catalogue.md#read-resource-labels).

<details><summary>Explore selected repositories after the first steps</summary>

## Selected repositories

- [Computer Networks: A Systems Approach](https://github.com/SystemsApproach/book): Open textbook by Larry Peterson and Bruce Davie covering network foundations, internetworking, scaling, end-to-end protocols, congestion, security and applications. (intermediate in this topic; Free)
- [Mininet](https://github.com/mininet/mininet): Linux network emulator with Python examples for building virtual hosts, switches and links and experimenting with connectivity, bandwidth, delay and packet loss on one machine. (intermediate in this topic; Free)

</details>

Jump to: [Courses and books](#courses-and-books) | [Practice by doing](#practice-by-doing) | [Roadmaps](#roadmaps) | [Tools and apps](#tools-and-apps)

## Courses and books

| Resource | Access | Topic level | What it offers |
|---|---|---|---|
| [Beej's Guides](https://beej.us/guide/) · [details](#resource-beejs-guides) | Free | intermediate | Free online guides to C programming, network (socket) programming, Git, Unix IPC and related topics by Brian 'Beej' Hall. |
| [Computer Networks: A Systems Approach](https://github.com/SystemsApproach/book) · [details](#resource-computer-networks-systems-approach) | Free | intermediate | Open textbook by Larry Peterson and Bruce Davie covering network foundations, internetworking, scaling, end-to-end protocols, congestion, security and applications. |
| [Microsoft IoT for Beginners](https://github.com/microsoft/IoT-For-Beginners) · [details](#resource-microsoft-iot-for-beginners) | Free | beginner | Microsoft's 24-lesson project-based IoT curriculum covering device code, sensors, actuators, MQTT messaging, cloud connectivity and telemetry, with physical or virtual hardware options. |
| [Professor Messer (CompTIA Network+ and Security+ videos)](https://www.professormesser.com/security-plus/sy0-701/sy0-701-video/sy0-701-comptia-security-plus-course/) · [details](#resource-professor-messer) | Free | beginner | Free video training courses for the CompTIA Security+ (SY0-701), Network+ (N10-009) and A+ exams, with optional paid course notes and practice exams. |
| [System Design (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design) · [details](#resource-karan-system-design) | Free | intermediate | Written system design course covering networking, databases, architecture patterns, reliability and worked design discussions for services such as a URL shortener. |

<a id="resource-beejs-guides"></a>
<details><summary>Beej&#x27;s Guides: requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Clear, informal writing
- Also free to download as PDF

**Requirements, costs and limitations:**

- Text only, no interactive exercises

**Source checked:** 2026-10-21 (official-site).

Index page: 'Free downloads!'; guides on C, network programming, network concepts (Python), Git, IPC. Paperbacks optional.

**Study format:** self-directed. **Focus-friendly rating:** unknown (editorial judgment).

</details>

<a id="resource-computer-networks-systems-approach"></a>
<details><summary>Computer Networks: A Systems Approach: requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Online textbook source available under CC BY 4.0
- Chapters build from network foundations to applications
- Authors invite corrections and improvements through the source repository

**Requirements, costs and limitations:**

- A substantial textbook rather than short interactive lessons
- Print and other book editions are separate from reading the online source
- Local rendering of the book needs additional build tools

**Source checked:** 2026-10-24 (github-repo).

Read the official README at https://raw.githubusercontent.com/SystemsApproach/book/master/README.rst, table of contents at https://raw.githubusercontent.com/SystemsApproach/book/master/index.rst, print information at https://raw.githubusercontent.com/SystemsApproach/book/master/print.rst and CC BY 4.0 license at https://raw.githubusercontent.com/SystemsApproach/book/master/LICENSE. The README names the authors and links the online book at book.systemsapproach.org. Free refers to reading the online source; print and ebook pricing was not checked. English text checked. Exercises, local builds and recent maintenance were not tested.

**Study format:** guided. **Focus-friendly rating:** unknown (editorial judgment).

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

<a id="resource-professor-messer"></a>
<details><summary>Professor Messer (CompTIA Network+ and Security+ videos): requirements and source notes</summary>

**Topic level:** beginner. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Videos are completely free; Security+ course is 121 videos, about 15 hours
- Short, topic-per-video lessons

**Requirements, costs and limitations:**

- Course notes (PDF/print) and practice exams are sold separately
- Exam-oriented rather than hands-on

**Source checked:** 2026-10-21 (official-site).

Security+ index page: 'All of my training videos are completely free', 121 videos, 15h11m; 96-page course notes sold separately. Menu shows free Network+ and A+ video courses. Exam voucher/cert costs not checked.

**Study format:** guided. **Focus-friendly rating:** unknown (editorial judgment).

</details>

<a id="resource-karan-system-design"></a>
<details><summary>System Design (Karan Pratap Singh): requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Readable course organized into chapters with a detailed table of contents
- Connects network and storage foundations with architecture patterns
- Includes concrete system design examples

**Requirements, costs and limitations:**

- CC BY-NC-ND 4.0 restricts commercial reuse and distribution of adaptations; this is not an open-source license
- Reading material rather than an interactive implementation lab
- Separate website and ebook editions may have different terms

**Source checked:** 2026-10-24 (github-repo).

Read the author's README course at https://raw.githubusercontent.com/karanpratapsingh/system-design/main/README.md and license at https://raw.githubusercontent.com/karanpratapsingh/system-design/main/LICENSE. The table of contents covers IP, TCP/UDP, DNS, scaling, databases, distributed transactions, architecture patterns, reliability and example systems. The LICENSE is CC BY-NC-ND 4.0, so the material must not be described as open-source software. Free refers only to reading the public repository; website and ebook pricing were not verified. English course checked. Implementation exercises and recent maintenance were not independently tested.

**Study format:** guided. **Focus-friendly rating:** unknown (editorial judgment).

</details>


## Practice by doing

| Resource | Access | Topic level | What it offers |
|---|---|---|---|
| [Cisco Packet Tracer](https://www.netacad.com/cisco-packet-tracer) · [details](#resource-cisco-packet-tracer) | Free | beginner | Cisco's network simulation software for building and testing virtual networks (routers, switches, IoT, basic cybersecurity) without hardware, with free training from Cisco Networking Academy. |
| [iximiuz Labs](https://labs.iximiuz.com/) · [details](#resource-iximiuz-labs) | Free + paid extras | intermediate | Hands-on platform with playgrounds, tutorials, challenges and paths for Linux, Docker, Kubernetes and networking. |
| [P4-Learning (ETH Zurich)](https://github.com/nsg-ethz/p4-learning) · [details](#resource-p4-learning) | Free | advanced | Data-plane programming exercises, examples and lecture material for writing P4-16 programs and testing virtual network switches, including packet reflection, forwarding and load balancing. |

<a id="resource-cisco-packet-tracer"></a>
<details><summary>Cisco Packet Tracer: requirements and source notes</summary>

**Topic level:** beginner. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Free download, no hardware needed
- Visualises how networks work

**Requirements, costs and limitations:**

- Requires a free Cisco Networking Academy account to download
- Simulator only: some commands and features differ from real devices

**Source checked:** 2026-10-21 (official-site).

Page title 'Free Training and Download'; description says 'download the latest version of Cisco Packet Tracer for free'. Account requirement and simulator limits are general knowledge not read on the JS-rendered page, so left as noted caveats; Networking Academy course catalogue pricing not verified.

**Study format:** self-directed. **Focus-friendly rating:** unknown (editorial judgment).

</details>

<a id="resource-iximiuz-labs"></a>
<details><summary>iximiuz Labs: requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Real servers in the browser
- Free forever Basic plan

**Requirements, costs and limitations:**

- Basic: 1 playground and 1 hour per day, only some content free
- Bundle is $10 per month billed $120 per year

**Source checked:** 2026-10-21 (official-site).

Pricing page: Basic free forever, $0, no card; Complete Bundle $120 per year.

**Study format:** semi. **Focus-friendly rating:** unknown (editorial judgment).

</details>

<a id="resource-p4-learning"></a>
<details><summary>P4-Learning (ETH Zurich): requirements and source notes</summary>

**Topic level:** advanced. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Exercises include descriptions, program skeletons and solutions
- A packet reflector provides a concrete first experiment in the environment
- GPLv3 source repository with material from an ETH Zurich networking lecture

**Requirements, costs and limitations:**

- Assumes networking and programming knowledge; not a first networking course
- Requires P4-Utils, Mininet, a compiler and software-switch dependencies in a suitable local or virtual environment
- The authors warn that older environments and configuration formats can be incompatible

**Source checked:** 2026-10-24 (github-repo).

Read https://raw.githubusercontent.com/nsg-ethz/p4-learning/master/README.md, https://raw.githubusercontent.com/nsg-ethz/p4-learning/master/LICENSE, https://raw.githubusercontent.com/nsg-ethz/p4-learning/master/exercises/README.md and https://raw.githubusercontent.com/nsg-ethz/p4-learning/master/exercises/01-Reflector/README.md. The reflector exercise provides a topology, Python packet sender and P4 skeleton to complete, and launches an emulated host and switch through P4-Utils. The main README lists dependencies and compatibility warnings; LICENSE contains GPLv3. Free refers to the public material and local software, not a supplied hosted lab or machine. English files checked. No VM, dependency installation, exercise execution or recent maintenance check was performed.

**Study format:** semi. **Focus-friendly rating:** unknown (editorial judgment).

</details>


## Roadmaps

| Resource | Access | Topic level | What it offers |
|---|---|---|---|
| [Teach Yourself Computer Science](https://teachyourselfcs.com/) · [details](#resource-teachyourselfcs) | Free | intermediate | A guide recommending one book and one video lecture series for each of nine core CS subjects (programming, architecture, algorithms, math, OS, networking, databases, languages, distributed systems), with a suggested 100-200 hours per subject. |

<a id="resource-teachyourselfcs"></a>
<details><summary>Teach Yourself Computer Science: requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en, es

**Useful for:**

- Opinionated and short - tells you what to study and in what order
- Pairs a book and a video series per subject
- Many community translations

**Requirements, costs and limitations:**

- Is a reading list, not a platform - no exercises or feedback of its own
- Some recommended books must be bought
- Last major update was May 2020 per the page

**Source checked:** 2026-10-21 (official-site).

Page loads; TL;DR and translation list read. Individual resources not re-checked.

**Study format:** semi. **Focus-friendly rating:** unknown (editorial judgment).

</details>


## Tools and apps

| Resource | Access | Topic level | What it offers |
|---|---|---|---|
| [Mininet](https://github.com/mininet/mininet) · [details](#resource-mininet) | Free | intermediate | Linux network emulator with Python examples for building virtual hosts, switches and links and experimenting with connectivity, bandwidth, delay and packet loss on one machine. |
| [Wireshark](https://www.wireshark.org/) · [details](#resource-wireshark) | Free | intermediate | Network traffic analyzer for inspecting packet captures and filtering protocol traffic, with a graphical application, TShark command-line tools and official documentation. |

<a id="resource-mininet"></a>
<details><summary>Mininet: requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- BSD 3-Clause open-source software
- Python examples make small network experiments inspectable and modifiable
- Emulated networks avoid requiring a rack of physical switches

**Requirements, costs and limitations:**

- Needs Linux network features, installation and administrative privileges
- Requires networking basics and some Python to modify the examples
- Emulated behavior and performance do not establish real hardware performance

**Source checked:** 2026-10-24 (github-repo).

Read https://raw.githubusercontent.com/mininet/mininet/master/README.md, https://raw.githubusercontent.com/mininet/mininet/master/LICENSE and https://raw.githubusercontent.com/mininet/mininet/master/examples/simpleperf.py. The README describes Linux namespace-based networks, the Python API, diagnostic commands and examples. The inspected example creates a switch topology and configures bandwidth, delay and loss; its comments warn that loss can make ping or throughput tests fail or hang. LICENSE is BSD 3-Clause. Free refers to the local software; a suitable machine or VM is still needed and any hosted infrastructure may cost money. English files checked. No network experiment, installation or maintenance assessment was performed.

**Study format:** self-directed. **Focus-friendly rating:** unknown (editorial judgment).

</details>

<a id="resource-wireshark"></a>
<details><summary>Wireshark: requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Open-source software distributed under the GNU GPLv2
- Inspect saved captures as well as live traffic
- Available for Windows, macOS and Linux

**Requirements, costs and limitations:**

- Understanding captures requires networking knowledge
- Live capture needs appropriate permissions; the authors advise against running the main application as root
- Capture only traffic you are authorized to inspect and avoid sharing captures containing private data

**Source checked:** 2026-10-24 (github-repo).

Read the official README at https://raw.githubusercontent.com/wireshark/wireshark/master/README.md and license at https://raw.githubusercontent.com/wireshark/wireshark/master/COPYING. The README identifies wireshark.org as the official home, describes supported platforms, packet-file handling, TShark, capture permissions and documentation. It states that Wireshark is distributed under GPLv2, with most parts GPL version 2 or later and some components under other licenses. Free refers to the open-source software. English README checked; installation, packet capture, documentation exercises and recent maintenance were not tested.

**Study format:** self-directed. **Focus-friendly rating:** unknown (editorial judgment).

</details>
