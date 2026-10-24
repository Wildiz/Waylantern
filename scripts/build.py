#!/usr/bin/env python3
"""Validate resource, path and profession data, then generate README.md and docs/*.md."""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlsplit

import yaml
from jsonschema import Draft202012Validator

if __package__:
    from .profession_catalog import load_professions, render_professions
else:
    from profession_catalog import load_professions, render_professions

ROOT = Path(__file__).resolve().parent.parent
REPO = "Wildiz/Waylantern"  # GitHub owner/name, used in generated links
ISSUES_URL = f"https://github.com/{REPO}/issues/new/choose"


def anchor(title):
    """GitHub heading anchor: lowercase, drop punctuation, spaces become hyphens."""
    return re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")

# slug -> (title, one-line explanation for beginners)
CATEGORIES = {
    "path": ("Full paths (a free university)", "A complete road from zero, in order. Best if you want structure and do not want to decide what to study next."),
    "course": ("Courses and books", "Individual courses and books on one topic. Good once you know roughly what you want to learn."),
    "practice": ("Practice by doing", "You write code or solve problems and get instant feedback. Best for staying engaged."),
    "roadmap": ("Roadmaps", "Maps that show what to learn and in what order. Use one to see the big picture."),
    "reference": ("Lists, docs and articles", "Big collections of links, documentation and guides. Great to browse or look things up, overwhelming if you start here."),
    "tool": ("Tools and apps", "Apps and software for taking notes, remembering, staying focused or building your own projects."),
    "community": ("Communities", "Places to ask for help and find people learning alongside you."),
}

AREAS = {
    "cs": ("Computer science and algorithms", "How computers work, data structures, algorithms and the theory behind them."),
    "software": ("Programming and software engineering", "Learn languages, Git, the command line and how to build software well."),
    "web": ("Web development", "HTML, CSS, JavaScript, frameworks and everything for building websites and web apps."),
    "networking": ("Computer networks", "Protocols, packet analysis, network simulation and how computers communicate."),
    "architecture": ("Software and systems architecture", "Design decisions, system structure, scalability and examples of how applications are built."),
    "testing": ("Software testing and QA", "Automated tests, browser testing and techniques for checking software quality."),
    "embedded": ("Embedded systems and firmware", "Microcontrollers, hardware programming and software that interacts with physical devices."),
    "design-product": ("UX, UI and product design", "Interface design, design systems, prototyping and tools for exploring user experiences."),
    "data": ("Data, databases and statistics", "SQL, data analysis, data engineering, visualization and statistics."),
    "ai": ("AI, machine learning and LLMs", "Machine learning, deep learning, language models and AI agents."),
    "devops": ("DevOps, cloud and Linux", "Containers, Kubernetes, cloud platforms, infrastructure and Linux administration."),
    "it-support": ("IT support and service management", "System troubleshooting, technical support, help desks and managing IT services."),
    "security": ("Cybersecurity", "Legal, authorized practice to learn how systems are attacked and defended."),
    "math": ("Math for tech", "Linear algebra, calculus, discrete math and probability for CS, data and AI."),
    "games-mobile": ("Games and mobile apps", "Game engines and mobile app development."),
    "career": ("Career, interviews and open source", "Interview practice, your first open-source contributions and portfolio hosting."),
    "study-skills": ("Study skills and memory", "How to learn, take notes and remember what you study, including AI study helpers."),
    "focus": ("Focus and ADHD-friendly tools", "Tools and techniques to start, stay focused and finish. Not medical advice."),
    "general": ("General platforms (any topic)", "Big platforms and directories that cover many areas."),
}
PRICE_LABEL = {"free": "Free", "freemium": "Free + paid extras", "paid-cheap": "Low cost", "paid": "Paid", "unverified": "Price not confirmed yet"}
FOCUS_LABEL = {"high": "high", "medium": "medium", "low": "low", "unknown": "-"}


def load_entries():
    schema = json.loads((ROOT / "data" / "schema.json").read_text())
    validator = Draft202012Validator(schema)
    entries, errors = [], []
    for path in sorted((ROOT / "data" / "tools").glob("*.yml")):
        entry = yaml.safe_load(path.read_text())
        if isinstance(entry, dict) and isinstance(entry.get("verified"), dict):
            entry["verified"]["date"] = str(entry["verified"].get("date"))
        for err in validator.iter_errors(entry):
            errors.append(f"{path.name}: {'/'.join(map(str, err.path)) or '<root>'}: {err.message}")
        if path.stem != path.stem.lower():
            errors.append(f"{path.name}: file name must be lowercase")
        entries.append((path.stem, entry))
    return entries, errors


def load_paths(entries):
    schema = json.loads((ROOT / "data" / "path-schema.json").read_text())
    validator = Draft202012Validator(schema)
    resources = {slug for slug, _ in entries}
    paths, errors = [], []
    for path in sorted((ROOT / "data" / "paths").glob("*.yml")):
        try:
            data = yaml.safe_load(path.read_text())
        except yaml.YAMLError as exc:
            errors.append(f"{path.name}: invalid YAML: {exc}")
            continue
        problems = list(validator.iter_errors(data))
        for err in problems:
            errors.append(f"{path.name}: {'/'.join(map(str, err.path)) or '<root>'}: {err.message}")
        if problems:
            continue
        for area in data["areas"]:
            if area not in AREAS:
                errors.append(f"{path.name}: unknown area '{area}'")
        sections = [(f"steps/{i}", step) for i, step in enumerate(data["steps"])]
        if "helpers" in data:
            sections.append(("helpers", data["helpers"]))
        for location, section in sections:
            for slug in section["tools"]:
                if slug not in resources:
                    errors.append(f"{path.name}: {location}/tools: unknown resource '{slug}'")
        paths.append((path.stem, data))
    if not any(slug == "path-0-fundamentals" for slug, _ in paths):
        errors.append("path-0-fundamentals.yml: a valid fundamentals path is required")
    return paths, errors


def link(e):
    return f"[{e['name']}]({e['url']})"


def repository_url(entry):
    parsed = urlsplit(entry.get("repository", entry["url"]))
    parts = [part for part in parsed.path.split("/") if part]
    if (parsed.scheme != "https" or parsed.hostname not in {"github.com", "gitlab.com"}
            or parsed.username or parsed.password or len(parts) < 2):
        return None
    return f"https://{parsed.hostname}/{'/'.join(parts[:2])}"


def load_area_repositories(entries):
    path = ROOT / "data" / "area-repositories.yml"
    try:
        selections = yaml.safe_load(path.read_text())
    except yaml.YAMLError as exc:
        return {}, [f"{path.name}: invalid YAML: {exc}"]
    schema = {"type": "object", "additionalProperties": {
        "type": "array", "minItems": 1, "maxItems": 3, "uniqueItems": True,
        "items": {"type": "string", "minLength": 1}}}
    errors = [f"{path.name}: {err.message}" for err in Draft202012Validator(schema).iter_errors(selections)]
    if errors:
        return {}, errors
    resources = dict(entries)
    for area, slugs in selections.items():
        if area not in AREAS:
            errors.append(f"{path.name}: unknown area '{area}'")
        for slug in slugs:
            entry = resources.get(slug)
            if entry is None:
                errors.append(f"{path.name}: unknown resource '{slug}'")
            elif area not in entry["areas"] or "en" not in entry["languages"]:
                errors.append(f"{path.name}: '{slug}' is not in the English catalogue for '{area}'")
            elif not repository_url(entry):
                errors.append(f"{path.name}: '{slug}' has no supported repository link")
    return selections, errors


def table(items, detailed):
    items = sorted(items, key=lambda e: e["name"].lower())
    if detailed:
        head = "| Name | Cost | Level | Guided? | Focus-friendly | Languages | What it is |\n|---|---|---|---|---|---|---|"
        rows = [
            f"| {link(e)} | {PRICE_LABEL[e['price']]} | {e['level']} | {e['structure']} | {FOCUS_LABEL[e['focus_friendly']]} | "
            f"{', '.join(e['languages'])} | {e['description']} |"
            for e in items
        ]
    else:
        head = "| Name | Cost | What it is |\n|---|---|---|"
        rows = [f"| {link(e)} | {PRICE_LABEL[e['price']]} | {e['description']} |" for e in items]
    return "\n".join([head] + rows)


LEVEL_TITLES = [("beginner", "Beginner (no previous knowledge)"), ("intermediate", "Intermediate"), ("advanced", "Advanced"), ("all", "Any level")]


def render_category(cat, items):
    title, blurb = CATEGORIES[cat]
    out = [f"# {title}", "", f"_{blurb}_", "", "[Back to the start](../README.md)", ""]
    if len(items) > 25:
        out += ["Jump to: " + " | ".join(f"[{t.split(' (')[0]}](#{anchor(t)})" for lv, t in LEVEL_TITLES if any(e["level"] == lv for e in items)), ""]
    for lv, lv_title in LEVEL_TITLES:
        group = [e for e in items if e["level"] == lv]
        if group:
            out += [f"## {lv_title}", "", table(group, True), ""]
    notes = [e for e in sorted(items, key=lambda e: e["name"].lower()) if e.get("pros") or e.get("cons")]
    if notes:
        out += ["## Pros and cons", "", "<details><summary>Show pros and cons for each entry</summary>", ""]
        for e in notes:
            out.append(f"**{e['name']}**")
            out.append("")
            for p in e.get("pros", []):
                out.append(f"- Good: {p}")
            for c in e.get("cons", []):
                out.append(f"- Watch out: {c}")
            out.append("")
        out += ["</details>", ""]
    out += ["---", "Entries marked 'Price not confirmed yet' have a detail we could not verify from an official source. Help us confirm it: see [CONTRIBUTING](../CONTRIBUTING.md).", ""]
    return "\n".join(out)


def path0_readme_table(data, by_slug):
    rows = ["| Step | What you do | Pick |", "|---|---|---|"]
    if "helpers" in data:
        h = data["helpers"]
        rows.append("| Optional helpers | Stay focused and remember what you learn | " + ", ".join(link(by_slug[t]) for t in h["tools"]) + " |")
    for i, step in enumerate(data["steps"], 1):
        separator = " → " if step.get("sequence", False) else " or "
        rows.append(f"| {i} | {step['short']} | " + separator.join(link(by_slug[t]) for t in step["tools"]) + " |")
    return rows


def render_readme(entries, groups, n_other=0, path0=None, by_slug=None, paths=(), selections=None):
    main_entries = [e for _, e in entries]
    es = [e for _, e in entries if "es" in e["languages"]]
    out = [
        "# Waylantern",
        "",
        "_A lantern for your first steps in IT._",
        "",
        "**A free, community-style guide to resources for learning IT** (software, data, AI, networks, hardware and IT operations).",
        "Courses, books, practice labs, open-source projects and study tools, organized by topic and format.",
        "Not sure what a role involves or what to do next? Choose a short learning path with a first project and checkpoints, then use the catalogue to explore further.",
        "",
        "[Español](README.es.md)",
        "",
        "[Explore areas and professions](docs/professions.md) · [Compare learning paths](#choose-a-learning-path)",
        "",
        f"> **Made with AI.** This directory was put together by an AI assistant (Claude) working for its owner, who is a beginner in IT. The goal is to gather in one place the free resources people can use to study. Entries were checked against official pages whenever possible, but mistakes, outdated prices and broken links can still happen. Please confirm details on the official site and [tell us what is wrong]({ISSUES_URL}).",
        "",
        "## Never studied IT before? Start here",
        "",
        "Follow **[Path 0: fundamentals](docs/path-0-fundamentals.md)**: a few small steps, no deadlines. Do one step at a time and move on when you can do the check at the end of it, not when a calendar says so.",
        "",
    ]
    out += path0_readme_table(path0, by_slug)
    out += [
        "",
        "The [full page](docs/path-0-fundamentals.md) explains why each resource is there and when to move on.",
        "",
        "## Choose a learning path",
        "",
        "Each path explains what a related role does, the knowledge you need first and a small project to build. Choose one and follow its checkpoints. If you are unsure, begin with Path 0. You can change direction later.",
        "",
        "| Path | What you will try |",
        "|---|---|",
    ]
    out += [f"| [{data['title']}](docs/{slug}.md) | {data['summary']} |" for slug, data in paths]
    out += [
        "",
        "## Looking for one specific area?",
        "",
        "Start with a short route or a selected repository. Open the full area for all its courses, books, practice and tools. Repository links include educational materials and applications to explore; each resource's page explains its level and requirements.",
        "",
        "| Area | What is inside | Start here | Selected repositories | All resources |",
        "|---|---|---|---|---|",
    ]
    for area, (a_title, a_blurb) in AREAS.items():
        n = sum(1 for e in main_entries if area in e["areas"])
        if n:
            related = [(slug, data) for slug, data in paths if area in data["areas"]]
            start = ", ".join(f"[{data['title']}](docs/{slug}.md)" for slug, data in related) or f"[Browse](docs/area-{area}.md)"
            repos = ", ".join(f"[{by_slug[slug]['name']}]({repository_url(by_slug[slug])})" for slug in (selections or {}).get(area, [])) or "—"
            out.append(f"| [{a_title}](docs/area-{area}.md) | {a_blurb} | {start} | {repos} | [{n}](docs/area-{area}.md) |")
    out += ["", "[How these repositories were researched](research/2026-10-24-repositories-and-careers.md)."]
    out += [
        "",
        "## What do you need?",
        "",
        "| I want... | Go to |",
        "|---|---|",
    ]
    needs = [
        ("docs/path.md", "A full, ordered path like a university degree", "path"),
        ("docs/practice.md", "To learn by writing code and getting instant feedback", "practice"),
        ("docs/roadmap.md", "To see the big picture of what exists", "roadmap"),
        ("docs/area-focus.md", "Help staying focused (ADHD-friendly ideas)", None),
        ("docs/area-study-skills.md", "Notes, flashcards and remembering things", None),
        ("docs/community.md", "People to learn with", "community"),
    ]
    out += [f"| {text} | [Open]({page}) |" for page, text, c in needs if c is None or groups.get(c)]
    out += [
        "",
        "## Browse by format",
        "",
        "| Format | What is inside | Entries |",
        "|---|---|---|",
    ]
    for cat, (title, blurb) in CATEGORIES.items():
        if groups.get(cat):
            out.append(f"| [{title}](docs/{cat}.md) | {blurb} | {len(groups[cat])} |")
    out += [
        "",
        f"**{len(entries)} entries in total**, {len(es)} of them with Spanish available.",
        "",
    ]
    if n_other:
        out += [f"**Optional:** {n_other} more resources that are only available in other languages (Spanish) are in [Resources in other languages](docs/other-languages.md).", ""]
    out += [
        "## How to read the tables",
        "",
        "- **Cost**: `Free` means free to learn. Some free sites sell optional certificates. `Price not confirmed yet` means we have not verified it on the official page yet.",
        "- **Level**: `beginner` needs no previous knowledge.",
        "- **Guided?**: `guided` has a path to follow; `self-directed` means you choose your own way.",
        "- **Focus-friendly**: our judgment of how easy it is to stay engaged (short sessions, instant feedback, clear next step). `-` means we do not know yet.",
        "",
        "## Tips that come from the community",
        "",
        "- Free content has plenty of material but little structure. The most common reason people quit is not knowing what to do next, so pick a path and stick to it.",
        "- After each lesson, build something small of your own. Watching tutorials alone is a trap.",
        "- Free lists go out of date and links break. That is why every entry here has a verification date, and a bot checks the links regularly.",
        "",
        "## Want to help?",
        "",
        f"Found a tool that is missing, or a wrong detail? You do **not** need to know Git: [open a suggestion]({ISSUES_URL}) and fill in the form. Developers can send a pull request: see [CONTRIBUTING](CONTRIBUTING.md).",
        "",
        "## License",
        "",
        "[CC BY 4.0](LICENSE): copy it, adapt it, share it, just give credit.",
        "",
        "> README and `docs/` are generated from the YAML source files in `data/` by `scripts/build.py`. Edit the data files, not the generated pages.",
        "",
    ]
    return "\n".join(out)


def render_other_languages(items):
    out = [
        "# Resources in other languages (optional)",
        "",
        "_The main directory is in English. These resources are **not available in English**, so they are listed separately. Many English resources in the main tables also offer Spanish: look for `es` in the Languages column._",
        "",
        "[Back to the start](../README.md)",
        "",
        table(items, True),
        "",
    ]
    return "\n".join(out)


def render_path(data, by_slug, path_slug):
    out = [f"# {data['title']}", "", data["intro"].strip(), "", "[Back to the start](../README.md)", ""]
    if path_slug != "path-0-fundamentals":
        out += ["If a step assumes programming or terminal skills you have not learned, use the relevant parts of [Path 0](path-0-fundamentals.md) first. Work through one small step at a time; you do not need to finish every linked course.", ""]
    if "helpers" in data:
        helpers = data["helpers"]
        out += ["## Optional helpers for focus and memory", "", helpers["why"], ""]
        out += [f"- {link(by_slug[slug])} ({PRICE_LABEL[by_slug[slug]['price']]}): {by_slug[slug]['description']}" for slug in helpers["tools"]]
        out += [""]
    for i, step in enumerate(data["steps"], 1):
        out += [f"## Step {i}: {step['title']}", "", step["why"], ""]
        for slug in step["tools"]:
            e = by_slug[slug]
            out.append(f"- {link(e)} ({PRICE_LABEL[e['price']]}): {e['description']}")
        out += ["", f"**Advance when:** {step['advance_when']}", ""]
    out += ["## Where to go next", "", "After the last checkpoint, improve your project or browse the related areas for a specific gap:", ""]
    out += [f"- [{AREAS[area][0]}](area-{area}.md)" for area in data["areas"]]
    out += ["", "[Compare the learning paths](../README.md#choose-a-learning-path)", "", "---", "This path is an editorial starting point, not an exhaustive curriculum or certification. Tell us what worked for you: see [CONTRIBUTING](../CONTRIBUTING.md).", ""]
    return "\n".join(out)


def render_area(area, items, paths=(), selected=()):
    title, blurb = AREAS[area]
    out = [f"# {title}", "", f"_{blurb}_", "", f"{len(items)} resources. [Back to the start](../README.md)", ""]
    if selected:
        out += ["## Selected repositories", ""]
        out += [f"- [{e['name']}]({repository_url(e)}): {e['description']} ({e['level']}; {PRICE_LABEL[e['price']]})" for e in selected]
        out += ["", "Need to understand a job title first? [Explore areas and professions](professions.md).", ""]
    related = [(slug, data) for slug, data in paths if area in data["areas"]]
    if related:
        out += ["## Not sure where to start?", ""]
        out += [f"- [{data['title']}]({slug}.md): {data['summary']}" for slug, data in related]
        out += [""]
    present = [c for c in CATEGORIES if any(e["category"] == c for e in items)]
    out += ["Jump to: " + " | ".join(f"[{CATEGORIES[c][0]}](#{anchor(CATEGORIES[c][0])})" for c in present), ""]
    for c in present:
        out += [f"## {CATEGORIES[c][0]}", "", table([e for e in items if e["category"] == c], True), ""]
    return "\n".join(out)


def render_all(entries, paths, selections=None, professions=None, guidelines=None):
    main = [(s, e) for s, e in entries if "en" in e["languages"]]
    other = [e for _, e in entries if "en" not in e["languages"]]
    groups = defaultdict(list)
    for _, e in main:
        groups[e["category"]].append(e)
    by_slug = {s: e for s, e in entries}
    path0 = dict(paths)["path-0-fundamentals"]
    files = {"README.md": render_readme(main, groups, len(other), path0, by_slug, paths, selections)}
    for cat, items in groups.items():
        files[f"docs/{cat}.md"] = render_category(cat, items)
    for area in AREAS:
        items = [e for _, e in main if area in e["areas"]]
        if items:
            selected = [by_slug[slug] for slug in (selections or {}).get(area, [])]
            files[f"docs/area-{area}.md"] = render_area(area, items, paths, selected)
    for slug, data in paths:
        files[f"docs/{slug}.md"] = render_path(data, by_slug, slug)
    if other:
        files["docs/other-languages.md"] = render_other_languages(other)
    if professions is not None:
        files.update(render_professions(professions, guidelines or [], AREAS, paths))
    return {name: body.rstrip() for name, body in files.items()}


def main():
    entries, errors = load_entries()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    paths, errors = load_paths(entries)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    selections, selection_errors = load_area_repositories(entries)
    professions, guidelines, profession_errors = load_professions(ROOT, AREAS, paths)
    errors = selection_errors + profession_errors
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    files = render_all(entries, paths, selections, professions, guidelines)
    if "--check" in sys.argv:
        stale = [name for name, text in files.items() if not (ROOT / name).exists() or (ROOT / name).read_text() != text + "\n"]
        stale += [f"docs/{p.name} (obsolete)" for p in (ROOT / "docs").glob("*.md") if f"docs/{p.name}" not in files]
        if stale:
            print(f"out of date: {', '.join(stale)}; run `make build`", file=sys.stderr)
            return 1
        return 0
    (ROOT / "docs").mkdir(exist_ok=True)
    for old in (ROOT / "docs").glob("*.md"):
        if f"docs/{old.name}" not in files:
            old.unlink()
    for name, text in files.items():
        (ROOT / name).write_text(text + "\n")
    print(f"ok: {len(entries)} entries, {len(files)} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
