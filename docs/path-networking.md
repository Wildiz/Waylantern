# First project: networking

Network engineers connect devices and services, keep communication working and investigate failures. Start here if you can manage files and run basic terminal commands; programming experience is not required. If the terminal is unfamiliar, begin with Path 0. Use one small lab throughout this route instead of trying to finish every course. The textbook is a reference for the topic in front of you, not a prerequisite to complete cover to cover. These checkpoints introduce the work; they do not establish professional readiness or guarantee employment.

[Back to the start](../README.md)

**Short first-project guide.** To study toward a profession over a longer sequence, [choose a curriculum](curricula.md).

## Before you start

Basic file management and terminal commands; programming experience is not required.

If a step assumes programming or terminal skills you have not learned, use the relevant parts of [Path 0](path-0-fundamentals.md) first. Work through one small step at a time; you do not need to finish every linked course.

## Step 1: Explain how one request reaches another device

Read the relevant foundation and internetworking sections to distinguish a local network, an IP address, a router and a name lookup. Draw a laptop, a local router and a remote service. Label which part uses an IP address and where DNS helps translate a name. Leave advanced routing and congestion control for later.

- [Computer Networks: A Systems Approach](https://github.com/SystemsApproach/book) (Free): Open textbook by Larry Peterson and Bruce Davie covering network foundations, internetworking, scaling, end-to-end protocols, congestion, security and applications.

**Advance when:** You can use your drawing to explain the difference between reaching another device on the same network and reaching a service through a router, and why a DNS failure can stop a name-based request even when the network connection works.

## Step 2: Build a tiny simulated local network

Use Packet Tracer to connect two simulated PCs through a switch. Set addresses in the same subnet, test communication and save the lab with a simple diagram and address table. Follow Cisco's setup instructions; a free Networking Academy account may be needed. This is a simulated lab, so you do not need to buy or reconfigure physical network equipment.

- [Cisco Packet Tracer](https://www.netacad.com/cisco-packet-tracer) (Free): Cisco's network simulation software for building and testing virtual networks (routers, switches, IoT, basic cybersecurity) without hardware, with free training from Cisco Networking Academy.

**Advance when:** Both simulated PCs can reach each other, and you can point to the address and subnet mask of each device and explain why a router is not needed for this particular connection.

## Step 3: Inspect a small packet capture

Use the official documentation to open an example capture or a capture from your own authorized lab. Begin with one protocol, such as DNS or TCP, and apply a display filter. Identify the source, destination and the order of a few related packets. Opening a saved capture is enough for this checkpoint; live capture is optional. Avoid sharing captures containing private traffic.

- [Wireshark](https://www.wireshark.org/) (Free): Network traffic analyzer for inspecting packet captures and filtering protocol traffic, with a graphical application, TShark command-line tools and official documentation.

**Advance when:** You can filter the capture to a relevant conversation, identify its endpoints and explain what at least two packets contribute to the exchange without treating every packet as an error.

## Step 4: Break and repair your lab deliberately

Return to the saved two-PC lab. Record the working addresses, then deliberately give one PC an address in a different subnet and confirm that communication fails. Inspect the configuration, restore a suitable address and test again. Keep a short note with the symptom, your hypothesis, the change and the result; change only one thing at a time.

- [Cisco Packet Tracer](https://www.netacad.com/cisco-packet-tracer) (Free): Cisco's network simulation software for building and testing virtual networks (routers, switches, IoT, basic cybersecurity) without hardware, with free training from Cisco Networking Academy.

**Advance when:** You have a before-and-after connectivity result and can explain why the changed address caused this failure and why your repair restored communication.

## Where to go next

After the last checkpoint, improve your project or browse the related areas for a specific gap:

- [Computer networks](area-networking.md)

[Compare first-project guides](learning-paths.md) · [Choose a profession curriculum](curricula.md)

---
Tell us what worked for you: see [CONTRIBUTING](../CONTRIBUTING.md).
