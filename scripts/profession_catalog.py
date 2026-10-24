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
        return "Verified: source content read"
    return "Link only: source content not read; network access may be unavailable"


def render_professions(groups, guidelines, areas, paths):
    """Render Markdown without a trailing newline; callers control file writes."""
    sources = {source["id"]: source for source in guidelines}
    path_titles = {slug: data["title"] for slug, data in paths}
    files = {}
    index = [
        "# Explore technology professions", "",
        "Choose a role to understand its scope, related study areas and available learning paths. Job titles overlap across employers; these profiles are editorial starting points, not promises of employment or complete qualifications.", "",
        "[Back to the start](../README.md)", "",
        "## How to use the references", "",
        "Academic curricula describe programmes of study; curriculum directories collect such recommendations. Competency frameworks describe skills and responsibility levels. Bodies of knowledge organise a discipline. Vendor-published curricula are educational courses; certification objectives describe an exam's scope, and professional guides give practice guidance. These sources serve different purposes.", "",
        "No profession-specific curriculum has been verified for the profiles below. The references are related discipline guidelines, skills frameworks, exam objectives or introductory courses. Use their type, scope and verification status to judge what they cover; an unverified link does not show that a profession has no curriculum.", "",
        "A related reference does not establish an official curriculum for a particular job title or an endorsement of this profile. Check each source's scope and verification status below. A link-only source has not had its content read, for example because network access was unavailable; this does not mean the source does not exist.", "",
        "## Profession groups", "",
    ]
    for group in groups:
        page = f"professions-{group['id']}.md"
        index += [f"### [{group['title']}]({page})", "", group["description"], "",
                  "Related areas: " + _area_links(group["areas"], areas), ""]
        index += [f"- [{role['title']}]({page}#{role['id']})" for role in group["roles"]]
        index += [""]
        content = [f"# {group['title']}", "", group["description"], "",
                   "[All profession groups and reference sources](professions.md) · [Back to the start](../README.md)", "",
                   "Role titles and requirements vary by employer. No profession-specific curriculum has been verified for these profiles; the reference links point to related study material, frameworks and guidelines, with verification status shown individually.", ""]
        for role in group["roles"]:
            content += [f'<a id="{role["id"]}"></a>', f"## {role['title']}", "", role["description"], ""]
            if role.get("aliases"):
                content += ["Also called: " + ", ".join(role["aliases"]), ""]
            content += ["Related areas: " + _area_links(role["areas"], areas), ""]
            if role["paths"]:
                content += ["Related starting paths (not complete professional curricula):", ""]
                content += [f"- [{path_titles[slug]}]({slug}.md)" for slug in role["paths"]]
                content += [""]
            else:
                content += ["No dedicated learning path is available in this directory yet. Browse the related areas above and the references below for context.", ""]
            content += ["Related reference sources:", ""]
            content += [f"- [{sources[ref]['title']}](professions.md#reference-{ref}) — {GUIDELINE_TYPES[sources[ref]['type']]}; {_verification(sources[ref])}." for ref in role["guidance"]]
            content += ["", "[Compare profession groups](professions.md#profession-groups)", ""]
        files[f"docs/{page}"] = "\n".join(content).rstrip()
    index += ["## Reference sources", ""]
    for source in guidelines:
        index += [f'<a id="reference-{source["id"]}"></a>', f"### {source['title']}", "",
                  f"- Publisher: {source['publisher']}",
                  f"- Type: {GUIDELINE_TYPES[source['type']]}",
                  f"- Source: [{source['title']}]({source['url']})",
                  f"- Scope: {source['scope']}",
                  f"- Status: {_verification(source)}",
                  f"- Checked: {source['checked']}",
                  f"- Verification notes: {source['notes']}", ""]
    files["docs/professions.md"] = "\n".join(index).rstrip()
    return files
