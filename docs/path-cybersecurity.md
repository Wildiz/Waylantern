# Path: cybersecurity

Cybersecurity practitioners investigate how systems fail and help people reduce the risk. This route is for beginners exploring command-line and web-security work. You need basic file skills and a computer where you are allowed to use an SSH client; Python 3 is used for the local web-server exercise. No prior security experience is required. Practise only on the named training platforms and within their published rules. Owning an account on a real service does not authorize testing that service. Keep practice credentials and challenge answers out of public project reports.

[Back to the start](../README.md)

If a step assumes programming or terminal skills you have not learned, use the relevant parts of [Path 0](path-0-fundamentals.md) first. Work through one small step at a time; you do not need to finish every linked course.

## Step 1: Get comfortable with the command line

Start with the Bandit instructions and the first few levels. Learn how to connect to the training host, list files, read text and search for information using the commands suggested by each level. Keep private notes about what each command does. Stay within the documented game targets and do not scan unrelated systems.

- [OverTheWire Wargames](https://overthewire.org/wargames/) (Free): Security wargames played over SSH (Bandit for Linux command-line basics, Natas for web security, and others) that teach security concepts as puzzle levels.

**Advance when:** You can repeat the first few levels, explain the commands you used and distinguish your local shell from the shell on the training host.

## Step 2: Understand what a browser sends

Read the introductory HTTP material. Put a simple HTML page in a practice folder, run python3 -m http.server 8000 --bind 127.0.0.1 from that folder and open the page through the local HTTP server in your browser. Inspect it using the browser's network tools; opening a file directly does not provide an HTTP exchange. Identify a request, a response, a method and a status code. Draw the browser and server and explain where user input would enter a web application. Stop the practice server when finished.

- [MDN Web Docs](https://developer.mozilla.org/) (Free): Mozilla-run documentation hub for HTML, CSS, JavaScript, Web APIs and HTTP, with reference pages, guides and a Learn web development section.

**Advance when:** You can describe one request and response, distinguish page content from response headers and explain why HTTPS does not by itself make application input trustworthy.

## Step 3: Complete one guided web-security lab

Choose one beginner-level lab and read its explanation before attempting it. Use only the lab instance supplied by the Academy and follow its setup instructions; the free Burp Suite Community Edition may be useful. Take private notes about the input, the behavior you observed and the underlying mistake. Repeat the same lab until you can explain the steps without copying a solution.

- [PortSwigger Web Security Academy](https://portswigger.net/web-security) (Free): Free online web application security training from the makers of Burp Suite, with learning paths, written material and interactive labs on topics such as SQL injection, XSS and API testing, for legal, authorized practice only.

**Advance when:** The training platform marks the lab solved and you can explain the vulnerable behavior and a suitable fix without applying the technique to any other target.

## Step 4: Write a small security report

Find the risk category related to your completed lab and use it to structure a short report. State the authorized lab scope, observed behavior, possible impact and a mitigation that addresses the cause. Clearly separate what you demonstrated in the lab from consequences you did not test. Remove credentials, flags and session tokens from any shared notes or screenshots.

- [OWASP Top 10](https://owasp.org/www-project-top-ten/) (Free): The OWASP reference document listing the ten most critical web application security risks, currently the 2025 edition, with earlier editions kept available.

**Advance when:** A reader can identify the affected lab behavior, understand your evidence and suggested fix, and tell which conclusions were observed and which remain assumptions.

## Where to go next

After the last checkpoint, improve your project or browse the related areas for a specific gap:

- [Cybersecurity](area-security.md)

[Compare the learning paths](../README.md#choose-a-learning-path)

---
This path is an editorial starting point, not an exhaustive curriculum or certification. Tell us what worked for you: see [CONTRIBUTING](../CONTRIBUTING.md).
