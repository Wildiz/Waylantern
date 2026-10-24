"""Editorial learning recipes with explicit resource gaps and evidence gates."""
import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ENTRY_LABELS = {
    "from-zero": "Start with the basics",
    "after-basics": "Learn the stated foundations first",
    "experience-required": "Prior practical experience required",
}
GROUP_ORDER = ["software", "data-ai", "operations", "security", "architecture", "leadership"]


def load_curricula(root, entries, professions):
    root = Path(root)
    validator = Draft202012Validator(json.loads((root / "data/curriculum-schema.json").read_text()))
    roles = {role["id"]: group["id"] for group in professions for role in group["roles"]}
    resources = dict(entries)
    found, errors, seen = [], [], set()
    for path in sorted((root / "data/curricula").glob("*.yml")):
        try:
            data = yaml.safe_load(path.read_text())
        except (OSError, yaml.YAMLError) as exc:
            errors.append(f"{path.name}: cannot read valid YAML: {exc}")
            continue
        problems = list(validator.iter_errors(data))
        errors.extend(f"{path.name}: {'/'.join(map(str, err.path))}: {err.message}" for err in problems)
        if problems:
            continue
        if data["group"] != path.stem:
            errors.append(f"{path.name}: group must match filename")
        for curriculum in data["curricula"]:
            role = curriculum["role"]
            if role in seen:
                errors.append(f"{path.name}: duplicate curriculum for '{role}'")
            seen.add(role)
            if roles.get(role) != data["group"]:
                errors.append(f"{path.name}: unknown role or incorrect group for '{role}'")
            for number, stage in enumerate(curriculum["stages"], 1):
                for slug in stage["resources"]:
                    if slug not in resources:
                        errors.append(f"{path.name}: '{role}' stage {number}: unknown resource '{slug}'")
            found.append(curriculum)
    for role in sorted(roles.keys() - seen):
        errors.append(f"data/curricula: missing curriculum for '{role}'")
    return found, errors


def render_curricula(curricula, professions, entries, sources):
    resources = dict(entries)
    source_map = {source["id"]: source for source in sources}
    roles = {role["id"]: (group, role) for group in professions for role in group["roles"]}
    groups = sorted(professions, key=lambda group: GROUP_ORDER.index(group["id"]) if group["id"] in GROUP_ORDER else 99)
    index = [
        "# Choose a profession curriculum", "",
        "A curriculum is your learning recipe: foundations, specialist skills, practice and evidence before the next stage. Choose a group, then a profession. Each recipe states what you need first and what you will produce.", "",
        "[Home](../README.md) · [Understand the professions](professions.md) · [Try a small first project](learning-paths.md)", "",
        "## Choose a group", "",
        "| Kind of work | Choose a profession and its recipe | Recipes |", "|---|---|---|",
    ]
    for group in groups:
        count = sum(role["id"] in {c["role"] for c in curricula} for role in group["roles"])
        index.append(f"| {group['description']} | [{group['title']}](professions-{group['id']}.md#roles-in-this-group) | {count} |")
    index += [
        "", "## How to follow a recipe", "",
        "1. Read the prerequisites. If you lack a foundation, learn it before the specialist stage.",
        "2. Study the listed topics and consult the resources needed for that task; some resources teach complementary skills.",
        "3. Do the practice task and keep its output: code, diagrams, test results, notes or a report.",
        "4. Check the evidence against the checkpoint before continuing. There are no fixed deadlines.",
        "", "## What the labels mean", "",
        "- **Start with the basics:** the recipe begins with introductory work; check its tools and hardware requirements.",
        "- **Foundations first:** learn the named programming, mathematics or systems skills before the specialist work.",
        "- **Experience required:** senior, management or specialist work relies on prior practical responsibility. Exercises help study decisions; reading alone cannot supply that experience.",
        "", "## Editorial recipes and official sources", "",
        "These recipes were created for Waylantern. They are not institution-issued curricula. Official recommendations, skill frameworks and exam objectives are listed separately with their scope and inspection status in [reference sources](profession-references.md).",
        "", "Every listed profession has a recipe. Some stages still need a verified learning resource: each page shows its resource coverage and marks the exact gaps. This is not a claim that the catalogue contains a complete course for every profession.", "",
        "Need to try the work before committing? [Choose a short first-project guide](learning-paths.md). Need a specific book, course or tool? [Browse the catalogue](catalogue.md).",
    ]
    pages = {"docs/curricula.md": "\n".join(index).rstrip()}
    for curriculum in curricula:
        group, role = roles[curriculum["role"]]
        stages = curriculum["stages"]
        missing = sum(bool(stage.get("gap")) for stage in stages)
        page_kind = "Editorial practice plan" if group["id"] == "software" else "Learning curriculum"
        body = [
            f"# {page_kind}: {role['title']}", "", curriculum["summary"], "",
            f"[Home](../README.md) / [Curricula](curricula.md) / [{group['title']}](professions-{group['id']}.md#roles-in-this-group)", "",
            f"**Target profile:** [{role['title']}](professions-{group['id']}.md#{role['id']})", "",
            f"**Starting point:** {ENTRY_LABELS[curriculum['entry_level']]}", "",
            "**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.", "",
            "## Before you start", "",
            *[f"- {item}" for item in curriculum["prerequisites"]], "",
            f"**What you will produce:** {curriculum['outcome']}", "",
            f"**Resource coverage:** {len(stages) - missing} of {len(stages)} stages have no recorded resource gap. Read the marked gaps before planning your study.", "",
            "Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.", "",
            "## Your sequence", "",
        ]
        if group["id"] == "software":
            body[6:6] = ["[Academic-plan work and resource-matching preview](software-study-preview.md). This page is an existing editorial practice plan; it is not derived from an inspected university curriculum.", ""]
        body += [f"{i}. [{stage['title']}](#stage-{i})" for i, stage in enumerate(stages, 1)]
        for i, stage in enumerate(stages, 1):
            body += ["", f'<a id="stage-{i}"></a>', f"## {i}. {stage['title']}", "", "**Learn:**", ""]
            body += [f"- {topic}" for topic in stage["topics"]]
            if stage["resources"]:
                body += ["", "**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:", ""]
                for slug in stage["resources"]:
                    resource = resources[slug]
                    details = f"area-{resource['areas'][0]}" if "en" in resource.get("languages", ["en"]) else "other-languages"
                    body.append(f"- [{resource['name']}]({resource['url']}) — {resource['level']} in this topic; {resource['price']} access. [Details]({details}.md#resource-{slug}).")
            if stage.get("gap"):
                body += ["", f"**Resource still needed:** {stage['gap']}"]
            body += ["", f"**Practise:** {stage['practice']}", "", f"**Advance when:** {stage['checkpoint']}"]
            if i < len(stages):
                body += ["", f"After the checkpoint, [continue to stage {i + 1}](#stage-{i + 1})."]
        body += ["", "## After this recipe", "", curriculum["next_steps"], "", "## Related guidance", "",
                 "These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.", ""]
        body += [f"- [{source_map[ref]['title']}](profession-references.md#reference-{ref})" for ref in role["guidance"]]
        body += ["", f"[Back to roles in this group](professions-{group['id']}.md#roles-in-this-group) · [Find a specific resource](catalogue.md)"]
        pages[f"docs/curriculum-{role['id']}.md"] = "\n".join(body).rstrip()
    return pages
