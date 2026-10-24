"""Validate and render an editorial catalogue of technology professions."""
import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


GUIDELINE_TYPES = {
    "academic_curriculum": "Academic curriculum",
    "curriculum_directory": "Curriculum directory",
    "competency_framework": "Competency framework",
    "body_of_knowledge": "Body of knowledge",
    "vendor_curriculum": "Vendor curriculum",
    "certification_objectives": "Certification objectives",
    "professional_guide": "Professional guide",
}


def load_professions(root, areas, paths):
    """Load catalogue data, returning groups, references and actionable errors."""
    root = Path(root)
    errors = []
    try:
        schema = json.loads((root / "data" / "profession-schema.json").read_text())
    except (OSError, ValueError) as exc:
        return [], [], [f"profession-schema.json: cannot read schema: {exc}"]
    group_validator = Draft202012Validator(schema)
    guideline_validator = Draft202012Validator({"$ref": "#/$defs/guideline", "$defs": schema["$defs"]})
    unreadable = object()

    def read_yaml(path):
        try:
            return yaml.safe_load(path.read_text())
        except (OSError, yaml.YAMLError) as exc:
            errors.append(f"{path.name}: cannot read valid YAML: {exc}")
            return unreadable

    def validate(data, validator, filename, location=""):
        problems = list(validator.iter_errors(data))
        for error in problems:
            field = "/".join(str(part) for part in error.path)
            errors.append(f"{filename}: {location}{field or '<root>'}: {error.message}")
        return not problems

    guidelines = []
    guideline_file = root / "data" / "profession-guidelines.yml"
    source_data = read_yaml(guideline_file)
    if source_data is not unreadable:
        if not isinstance(source_data, list):
            errors.append("profession-guidelines.yml: expected a list of reference sources")
        else:
            for index, item in enumerate(source_data):
                if validate(item, guideline_validator, guideline_file.name, f"{index}/"):
                    guidelines.append(item)
    guidance_ids = set()
    for source in guidelines:
        if source["id"] in guidance_ids:
            errors.append(f"profession-guidelines.yml: duplicate reference id '{source['id']}'")
        guidance_ids.add(source["id"])

    groups = []
    profession_dir = root / "data" / "professions"
    group_files = sorted(profession_dir.glob("*.yml"))
    if not group_files:
        errors.append("data/professions: no profession group YAML files found")
    group_ids, role_ids, role_titles = {}, {}, {}
    path_ids = {slug for slug, _ in paths}
    for filename in group_files:
        group = read_yaml(filename)
        if group is unreadable or not validate(group, group_validator, filename.name):
            continue
        groups.append(group)
        if filename.stem != group["id"]:
            errors.append(f"{filename.name}: group id '{group['id']}' must match filename '{filename.stem}'")
        if group["id"] in group_ids:
            errors.append(f"{filename.name}: duplicate group id '{group['id']}' (also in {group_ids[group['id']]})")
        group_ids[group["id"]] = filename.name
        for area in group["areas"]:
            if area not in areas:
                errors.append(f"{filename.name}: group areas: unknown area '{area}'")
        for role in group["roles"]:
            location = f"{filename.name}: role '{role['id']}'"
            title_key = " ".join(role["title"].split()).casefold()
            for value, seen, label in [(role["id"], role_ids, "id"), (title_key, role_titles, "title")]:
                if value in seen:
                    errors.append(f"{location}: duplicate role {label} '{role[label]}' (also in {seen[value]})")
                seen[value] = filename.name
            for area in role["areas"]:
                if area not in areas:
                    errors.append(f"{location}: unknown area '{area}'")
            for path in role["paths"]:
                if path not in path_ids:
                    errors.append(f"{location}: unknown learning path '{path}'")
            for reference in role["guidance"]:
                if reference not in guidance_ids:
                    errors.append(f"{location}: unknown guidance reference '{reference}'")
    return groups, guidelines, errors


def _area_links(area_ids, areas):
    def label(value):
        return value[0] if isinstance(value, (tuple, list)) else str(value)
    return ", ".join(f"[{label(areas[area])}](area-{area}.md)" for area in area_ids)


def _verification(source):
    if source["verification"] == "verified":
        return "Source content read"
    return "Link only: source content not read"


def _table_cell(text):
    return " ".join(text.split()).replace("|", "\\|")


def render_professions(groups, guidelines, areas, paths, curricula=()):
    """Render profession navigation and references without writing any files."""
    order = {name: index for index, name in enumerate(
        ("software", "data-ai", "operations", "security", "architecture", "leadership")
    )}
    groups = sorted(groups, key=lambda group: (order.get(group["id"], len(order)), group["title"].casefold()))
    sources = {source["id"]: source for source in guidelines}
    path_titles = {slug: data["title"] for slug, data in paths}
    recipes = {curriculum["role"]: curriculum for curriculum in curricula}
    entry_labels = {"from-zero": "Start with the basics", "after-basics": "Foundations first", "experience-required": "Experience required"}
    reference_page = "profession-references.md"
    files = {}
    index = [
        "# Explore technology professions", "",
        "Choose a group, compare its roles, then open a study recipe to see what to learn, practise and demonstrate. Job titles and responsibilities vary by employer.", "",
        "[Back to the start](../README.md) · [About the reference sources](profession-references.md)", "",
        "## Profession groups", "",
        "| Group | What it covers | Roles |", "|---|---|---|",
    ]
    for group in groups:
        page = f"professions-{group['id']}.md"
        index.append(f"| [{group['title']}]({page}) | {_table_cell(group['description'])} | {len(group['roles'])} |")
        content = [
            f"# {group['title']}", "", group["description"], "",
            "[All profession groups](professions.md#profession-groups) · [Reference sources](profession-references.md) · [Back to the start](../README.md)", "",
            "Study recipes are editorial learning sequences; starting paths are shorter introductions. Related sources provide context, not a verified qualification for a job. Title variants may indicate seniority or responsibility rather than an identical role.", "",
            "## Roles in this group", "",
            "| Role | What they do | Study recipe |", "|---|---|---|",
        ]
        for role in group["roles"]:
            recipe = f"[Curriculum](curriculum-{role['id']}.md) — {entry_labels.get(recipes[role['id']].get('entry_level'), 'Check prerequisites')}" if role["id"] in recipes else "Not added yet"
            content.append(f"| [{role['title']}](#{role['id']}) | {_table_cell(role['description'])} | {recipe} |")
        content += [""]
        for role in group["roles"]:
            content += [f'<a id="{role["id"]}"></a>', f"## {role['title']}", "", role["description"], ""]
            if role.get("aliases"):
                content += ["Title variants: " + ", ".join(role["aliases"]), ""]
            content += ["Related areas: " + _area_links(role["areas"], areas), ""]
            if role["id"] in recipes:
                content += [f"Study recipe: [Curriculum for {role['title']}](curriculum-{role['id']}.md)", ""]
            else:
                content += ["Study recipe: not added yet.", ""]
            if role["paths"]:
                links = ", ".join(f"[{path_titles[slug]}]({slug}.md)" for slug in role["paths"])
                content += ["Starting paths: " + links, ""]
            else:
                content += ["Starting path: not added yet.", ""]
            content += ["<details><summary>Related references</summary>", ""]
            content += [f"- [{sources[ref]['title']}]({reference_page}#reference-{ref}) — {GUIDELINE_TYPES[sources[ref]['type']]}; {_verification(sources[ref])}." for ref in role["guidance"]]
            content += ["", "</details>", "", "[Back to roles in this group](#roles-in-this-group)", ""]
        files[f"docs/{page}"] = "\n".join(content).rstrip()
    index += ["", "## Reference sources", "",
              "[Read source details, types and verification notes](profession-references.md).", "",
              "<details><summary>Reference list</summary>", ""]
    # Retain the original fragment targets so existing source bookmarks still lead somewhere useful.
    for source in guidelines:
        index += [f'<a id="reference-{source["id"]}"></a>',
                  f"- [{source['title']}]({reference_page}#reference-{source['id']})", ""]
    index += ["</details>"]
    references = [
        "# Profession reference sources", "",
        "[All profession groups](professions.md#profession-groups) · [Back to the start](../README.md)", "",
        "## How to use the references", "",
        "Academic curricula describe programmes of study; curriculum directories collect such recommendations. Competency frameworks describe skills and responsibility levels. Bodies of knowledge organise a discipline. Vendor-published curricula are educational courses; certification objectives describe an exam's scope, and professional guides give practice guidance.", "",
        "No externally prescribed profession-specific curriculum has been verified for these profiles. Waylantern's study recipes are editorial sequences, while these references supply related context. Reading a source does not verify a role mapping or establish an endorsement, accreditation or complete qualification.", "",
        "A link-only source has not had its content read; this does not mean the source does not exist. Check the scope and notes before treating a reference as relevant to your goal.", "",
        "## Reference sources", "",
    ]
    for source in guidelines:
        references += [f'<a id="reference-{source["id"]}"></a>', f"### {source['title']}", "",
                       f"- Publisher: {source['publisher']}",
                       f"- Type: {GUIDELINE_TYPES[source['type']]}",
                       f"- Source: [{source['title']}]({source['url']})",
                       f"- Scope: {source['scope']}",
                       f"- Status: {_verification(source)}",
                       f"- Checked: {source['checked']}",
                       f"- Verification notes: {source['notes']}", ""]
    files["docs/professions.md"] = "\n".join(index).rstrip()
    files[f"docs/{reference_page}"] = "\n".join(references).rstrip()
    return files
