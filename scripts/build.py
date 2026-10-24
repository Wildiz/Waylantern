#!/usr/bin/env python3
"""Validate data/tools/*.yml against data/schema.json and generate README.md and docs/*.md."""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

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
    "data": ("Data, databases and statistics", "SQL, data analysis, data engineering, visualization and statistics."),
    "ai": ("AI, machine learning and LLMs", "Machine learning, deep learning, language models and AI agents."),
    "devops": ("DevOps, cloud and Linux", "Containers, Kubernetes, cloud platforms, infrastructure and Linux administration."),
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


def link(e):
    return f"[{e['name']}]({e['url']})"


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
    h = data["helpers"]
    rows.append("| Optional helpers | Stay focused and remember what you learn | " + ", ".join(link(by_slug[t]) for t in h["tools"]) + " |")
    for i, step in enumerate(data["steps"], 1):
        separator = " → " if step.get("sequence", False) else " or "
        rows.append(f"| {i} | {step['short']} | " + separator.join(link(by_slug[t]) for t in step["tools"]) + " |")
    return rows


def render_readme(entries, groups, n_other=0, path0=None, by_slug=None):
    main_entries = [e for _, e in entries]
    es = [e for _, e in entries if "es" in e["languages"]]
    out = [
        "# Waylantern",
        "",
        "_A lantern for your first steps in IT._",
        "",
        "**A free, community-style guide to the best tools for learning IT** (software, data, AI and LLMs).",
        "Courses, free \"universities\", practice sites, study tools and focus tools: all checked against their official pages.",
        "",
        "[Español](README.es.md)",
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
        "## Looking for one specific area?",
        "",
        "| Area | What is inside | Resources |",
        "|---|---|---|",
    ]
    for area, (a_title, a_blurb) in AREAS.items():
        n = sum(1 for e in main_entries if area in e["areas"])
        if n:
            out.append(f"| [{a_title}](docs/area-{area}.md) | {a_blurb} | {n} |")
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
        "> README and `docs/` are generated from `data/tools/*.yml` by `scripts/build.py`. Edit the data files, not the generated pages.",
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


def render_path(path_file, by_slug):
    data = yaml.safe_load(path_file.read_text())
    out = [f"# {data['title']}", "", data["intro"].strip(), "", "[Back to the start](../README.md)", ""]
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
    out += ["---", "This path is a general suggestion built from the community's most recommended free resources. Tell us what worked for you: see [CONTRIBUTING](../CONTRIBUTING.md).", ""]
    return "\n".join(out)


def render_area(area, items):
    title, blurb = AREAS[area]
    out = [f"# {title}", "", f"_{blurb}_", "", f"{len(items)} resources. [Back to the start](../README.md)", ""]
    present = [c for c in CATEGORIES if any(e["category"] == c for e in items)]
    out += ["Jump to: " + " | ".join(f"[{CATEGORIES[c][0]}](#{anchor(CATEGORIES[c][0])})" for c in present), ""]
    for c in present:
        out += [f"## {CATEGORIES[c][0]}", "", table([e for e in items if e["category"] == c], True), ""]
    return "\n".join(out)


def render_all(entries):
    main = [(s, e) for s, e in entries if "en" in e["languages"]]
    other = [e for _, e in entries if "en" not in e["languages"]]
    groups = defaultdict(list)
    for _, e in main:
        groups[e["category"]].append(e)
    by_slug = {s: e for s, e in entries}
    path0 = yaml.safe_load((ROOT / "data" / "paths" / "path-0-fundamentals.yml").read_text())
    files = {"README.md": render_readme(main, groups, len(other), path0, by_slug)}
    for cat, items in groups.items():
        files[f"docs/{cat}.md"] = render_category(cat, items)
    for area in AREAS:
        items = [e for _, e in main if area in e["areas"]]
        if items:
            files[f"docs/area-{area}.md"] = render_area(area, items)
    by_slug = {s: e for s, e in entries}
    for pf in sorted((ROOT / "data" / "paths").glob("*.yml")):
        files[f"docs/{pf.stem}.md"] = render_path(pf, by_slug)
    if other:
        files["docs/other-languages.md"] = render_other_languages(other)
    return files


def main():
    entries, errors = load_entries()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    files = render_all(entries)
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
