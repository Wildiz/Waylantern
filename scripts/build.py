#!/usr/bin/env python3
"""Validate resource, path and profession data, then generate README.md and docs/*.md."""
import json
import html
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlsplit

import yaml
from jsonschema import Draft202012Validator

if __package__:
    from .profession_catalog import load_professions, render_professions
    from .curricula import load_curricula, render_curricula
    from .navigation import render_home, render_catalogue, render_path_index
else:
    from profession_catalog import load_professions, render_professions
    from curricula import load_curricula, render_curricula
    from navigation import render_home, render_catalogue, render_path_index

ROOT = Path(__file__).resolve().parent.parent
REPO = "Wildiz/Waylantern"  # GitHub owner/name, used in generated links
ISSUES_URL = f"https://github.com/{REPO}/issues/new/choose"


def anchor(title):
    """GitHub heading anchor: lowercase, drop punctuation, spaces become hyphens."""
    return re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")

# slug -> (title, one-line explanation for beginners)
CATEGORIES = {
    "path": ("External programmes and curricula", "Longer study programmes and course sequences provided by other organisations; check their prerequisites and scope."),
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
    if parsed.hostname == "github.com":
        parts = parts[:2]
    elif "-" in parts:
        parts = parts[:parts.index("-")]
    if len(parts) < 2:
        return None
    return f"https://{parsed.hostname}/{'/'.join(parts)}"


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


def cell(text):
    """Keep user-authored text inside one Markdown table cell."""
    return str(text).replace("|", "&#124;").replace("\r", "").replace("\n", "<br>")


def resource_details(entry):
    slug = entry.get("_slug", anchor(entry["name"]))
    checked = entry.get("verified", {})
    lines = [f'<a id="resource-{slug}"></a>',
             f"<details><summary>{html.escape(entry['name'])}: requirements and source notes</summary>", ""]
    if entry.get("prerequisites"):
        lines += ["**Before you start:** " + "; ".join(entry["prerequisites"]), ""]
    lines += [f"**Topic level:** {entry['level']}. Read the requirements below before choosing it.", "",
              f"**Languages recorded:** {', '.join(entry.get('languages', []))}", ""]
    if entry.get("pros"):
        lines += ["**Useful for:**", "", *[f"- {item}" for item in entry["pros"]], ""]
    if entry.get("cons"):
        lines += ["**Requirements, costs and limitations:**", "", *[f"- {item}" for item in entry["cons"]], ""]
    if checked:
        lines += [f"**Source checked:** {checked.get('date', 'not recorded')} ({checked.get('method', 'not recorded')}).", "",
                  checked.get("notes", "No further source notes recorded."), ""]
    lines += [f"**Study format:** {entry.get('structure', 'not recorded')}. **Focus-friendly rating:** {entry.get('focus_friendly', 'unknown')} (editorial judgment).", "", "</details>"]
    return "\n".join(lines)


def table(items, detailed):
    items = sorted(items, key=lambda e: e["name"].lower())
    rows = ["| Resource | Access | Topic level | What it offers |", "|---|---|---|---|"]
    for entry in items:
        slug = entry.get("_slug", anchor(entry["name"]))
        title = f"{link(entry)} · [details](#resource-{slug})"
        rows.append("| " + " | ".join(cell(value) for value in [title, PRICE_LABEL[entry["price"]], entry["level"], entry["description"]]) + " |")
    rows += ["", *[resource_details(entry) + "\n" for entry in items]]
    return "\n".join(rows)


LEVEL_TITLES = [("beginner", "Beginner in this topic"), ("intermediate", "Intermediate"), ("advanced", "Advanced"), ("all", "Any level")]


def render_category(cat, items):
    title, blurb = CATEGORIES[cat]
    out = [f"# {title}", "", f"_{blurb}_", "", "[Back to the start](../README.md)", ""]
    out += ["[Resource catalogue](catalogue.md) · [Read access and level labels](catalogue.md#read-resource-labels)", ""]
    if cat == "path":
        out += ["These are external programmes. For Waylantern's own learning recipes, [choose a profession curriculum](curricula.md). To try an area with one small project, [compare first-project guides](learning-paths.md).", ""]
    if len(items) > 25:
        out += ["Jump to: " + " | ".join(f"[{t.split(' (')[0]}](#{anchor(t)})" for lv, t in LEVEL_TITLES if any(e["level"] == lv for e in items)), ""]
    for lv, lv_title in LEVEL_TITLES:
        group = [e for e in items if e["level"] == lv]
        if group:
            out += [f"## {lv_title}", "", table(group, True), ""]
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


def render_readme(entries, groups, n_other=0, path0=None, by_slug=None, paths=(), selections=None, role_count=0):
    return render_home(len(entries) + n_other, len(entries), n_other, role_count)



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
    out += ["**Short first-project guide.** To study toward a profession over a longer sequence, [choose a curriculum](curricula.md).", ""]
    if data.get("prerequisites"):
        out += ["## Before you start", "", data["prerequisites"], ""]
    if path_slug != "path-0-fundamentals":
        out += ["If a step assumes programming or terminal skills you have not learned, use the relevant parts of [Path 0](path-0-fundamentals.md) first. Work through one small step at a time; you do not need to finish every linked course.", ""]
    for i, step in enumerate(data["steps"], 1):
        out += [f"## Step {i}: {step['title']}", "", step["why"], ""]
        for slug in step["tools"]:
            e = by_slug[slug]
            out.append(f"- {link(e)} ({PRICE_LABEL[e['price']]}): {e['description']}")
        out += ["", f"**Advance when:** {step['advance_when']}", ""]
    if "helpers" in data:
        helpers = data["helpers"]
        out += ["<details><summary>Optional tools for focus and memory</summary>", "", helpers["why"], ""]
        out += [f"- {link(by_slug[slug])} ({PRICE_LABEL[by_slug[slug]['price']]}): {by_slug[slug]['description']}" for slug in helpers["tools"]]
        out += ["", "</details>", ""]
    out += ["## Where to go next", "", "After the last checkpoint, improve your project or browse the related areas for a specific gap:", ""]
    out += [f"- [{AREAS[area][0]}](area-{area}.md)" for area in data["areas"]]
    out += ["", "[Compare first-project guides](learning-paths.md) · [Choose a profession curriculum](curricula.md)", "", "---", "Tell us what worked for you: see [CONTRIBUTING](../CONTRIBUTING.md).", ""]
    return "\n".join(out)


def render_area(area, items, paths=(), selected=()):
    title, blurb = AREAS[area]
    out = [f"# {title}", "", f"_{blurb}_", "",
           f"{len(items)} resources. [Home](../README.md) / [Catalogue](catalogue.md)", "",
           "## Not sure where to start?", ""]
    related = [(slug, data) for slug, data in paths if area in data["areas"]]
    if related:
        for slug, data in related:
            out += [f"- [{data['title']}]({slug}.md): {data['summary']}"]
            if data.get("prerequisites"):
                out += [f"  Before you start: {data['prerequisites']}"]
    else:
        out += ["Start by [understanding the professions](professions.md) or [comparing short first-project guides](learning-paths.md). This area has no dedicated first-project guide yet."]
    out += ["", "For a longer learning recipe, [choose a profession curriculum](curricula.md).", "",
            "The catalogue below is a reference shelf. You do not need to use every resource. [Read the access and level labels](catalogue.md#read-resource-labels).", ""]
    if selected:
        out += ["<details><summary>Explore selected repositories after the first steps</summary>", "", "## Selected repositories", ""]
        out += [f"- [{e['name']}]({repository_url(e)}): {e['description']} ({e['level']} in this topic; {PRICE_LABEL[e['price']]})" for e in selected]
        out += ["", "</details>", ""]
    present = [c for c in CATEGORIES if any(e["category"] == c for e in items)]
    out += ["Jump to: " + " | ".join(f"[{CATEGORIES[c][0]}](#{anchor(CATEGORIES[c][0])})" for c in present), ""]
    for c in present:
        out += [f"## {CATEGORIES[c][0]}", "", table([e for e in items if e["category"] == c], True), ""]
    return "\n".join(out)


def render_all(entries, paths, selections=None, professions=None, guidelines=None, curricula=None):
    entries = [(slug, dict(entry, _slug=slug)) for slug, entry in entries]
    main = [(s, e) for s, e in entries if "en" in e["languages"]]
    other = [e for _, e in entries if "en" not in e["languages"]]
    groups = defaultdict(list)
    for _, e in main:
        groups[e["category"]].append(e)
    by_slug = {s: e for s, e in entries}
    path0 = dict(paths)["path-0-fundamentals"]
    role_count = sum(len(group["roles"]) for group in (professions or []))
    files = {
        "README.md": render_readme(main, groups, len(other), path0, by_slug, paths, selections, role_count),
        "README.es.md": render_home(len(entries), len(main), len(other), role_count, spanish=True),
        "docs/catalogue.md": render_catalogue(entries, AREAS, CATEGORIES),
        "docs/learning-paths.md": render_path_index(paths),
    }
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
        files.update(render_professions(professions, guidelines or [], AREAS, paths, curricula or []))
    if curricula is not None:
        files.update(render_curricula(curricula, professions or [], entries, guidelines or []))
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
    curricula, errors = load_curricula(ROOT, entries, professions)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    files = render_all(entries, paths, selections, professions, guidelines, curricula)
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
