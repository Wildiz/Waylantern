"""Small entry points; detailed indexes stay off the home page."""
from collections import Counter


PATH_LEVELS = {
    "start-here": "No previous programming needed to begin",
    "after-basics": "Learn the named foundations first",
    "some-experience": "Some programming experience required",
}


def render_home(total, english, other, roles, spanish=False):
    if spanish:
        lines = [
            "# Waylantern", "", "**Encuentra qué aprender en tecnología y cuál es tu siguiente paso.**", "",
            "No necesitas conocer todas las profesiones ni leer todo el catálogo. Elige una entrada:", "",
            "| Tu situación | Empieza aquí | Qué encontrarás |", "|---|---|---|",
            "| Empiezo desde cero | [Mi primer paso](docs/path-0-fundamentals.md) | Una actividad inicial y cómo comprobar que la entendiste. |",
            "| No sé qué hace cada profesión | [Explorar profesiones](docs/professions.md) | Seis grupos con explicaciones sencillas de cada perfil. |",
            "| Sé qué perfil quiero estudiar | [Elegir un currículo](docs/curricula.md) | La receta: requisitos, etapas, práctica y criterios de avance. |",
            "| Busco un tema, curso o herramienta | [Consultar el catálogo](docs/catalogue.md) | Recursos por área y formato, con costes y requisitos. |",
            "", "**Si estás perdido, empieza por la primera entrada.** Avanza por lo que puedas demostrar, sin plazos fijos.", "",
            "Las páginas detalladas están en inglés. Cada recurso indica sus idiomas y sus requisitos; no hace falta saber programar para explorar las profesiones.", "",
            f"{total} recursos: {english} disponibles en inglés y {other} en otros idiomas. {roles} perfiles con recetas editoriales.", "",
            "[English](README.md) · [Probar un área con un proyecto corto](docs/learning-paths.md) · [Fuentes y estado de revisión](docs/profession-references.md)", "",
            "¿Encontraste un error o falta un recurso? [Abre una sugerencia](https://github.com/Wildiz/Waylantern/issues/new/choose) o consulta [cómo contribuir](CONTRIBUTING.md).", "",
            "[CC BY 4.0](LICENSE). Contenido organizado con ayuda de IA; el catálogo conserva las notas de comprobación y las limitaciones de cada fuente.",
        ]
    else:
        lines = [
            "# Waylantern", "", "**Find what to learn in technology and what to do next.**", "",
            "You do not need to know every job title or read the whole catalogue. Choose one starting point:", "",
            "| Your situation | Start here | What you will find |", "|---|---|---|",
            "| I am starting from zero | [Take my first step](docs/path-0-fundamentals.md) | One first activity and a way to check your understanding. |",
            "| I do not know what the jobs involve | [Understand the professions](docs/professions.md) | Six groups with plain-language explanations of each profile. |",
            "| I know which role I want to study | [Choose a curriculum](docs/curricula.md) | The recipe: prerequisites, stages, practice and progress checks. |",
            "| I need a subject, course or tool | [Browse the catalogue](docs/catalogue.md) | Resources by topic and format, with access costs and requirements. |",
            "", "**Unsure? Start with the first row.** Move on when you can demonstrate the checkpoint; there are no fixed deadlines.", "",
            f"{total} resources: {english} available in English and {other} in other languages. {roles} profession profiles with editorial learning recipes.", "",
            "[Español](README.es.md)", "",
            "<details><summary>Other ways to explore</summary>", "",
            '<a id="choose-a-learning-path"></a>',
            "- [Try an area with a short first-project guide](docs/learning-paths.md).",
            '<a id="looking-for-one-specific-area"></a>',
            "- [Browse all subjects and selected repositories](docs/catalogue.md#by-area).",
            '<a id="browse-by-format"></a>',
            "- [Find a book, course, exercise or tool](docs/catalogue.md#by-format).",
            '<a id="how-to-read-the-tables"></a>',
            "- [Understand resource labels and source checks](docs/catalogue.md#read-resource-labels).",
            "- [Inspect official guidance and its verification status](docs/profession-references.md).",
            "", "</details>", "",
            "Found an error or a missing resource? [Suggest a correction](https://github.com/Wildiz/Waylantern/issues/new/choose) or read [how to contribute](CONTRIBUTING.md).", "",
            "[CC BY 4.0](LICENSE). Compiled with AI assistance; each resource's details record what was checked and what remains uncertain.",
        ]
    return "\n".join(lines).rstrip()


def render_catalogue(entries, areas, categories):
    main = [e for _, e in entries if "en" in e["languages"]]
    other = len(entries) - len(main)
    counts = Counter(e["category"] for e in main)
    lines = [
        "# Resource catalogue", "",
        "Use this page when you want a particular topic or resource. If you want an ordered learning recipe, [choose a profession curriculum](curricula.md). If you only want to try an activity, [choose a short first-project guide](learning-paths.md).", "",
        "[Home](../README.md) · [Understand the professions](professions.md)", "",
        f"**{len(entries)} resources:** {len(main)} available in English and {other} in other languages. Area counts overlap because one resource may cover more than one subject.", "",
        "## By area", "",
        "Open an area for its first-project guides, full resource list and selected source repositories. The repository is where a project or learning material is stored; it does not tell you its difficulty.", "",
        "| Subject | What you can learn | Resources in English |", "|---|---|---|",
    ]
    for area, (title, summary) in areas.items():
        count = sum(area in e["areas"] for e in main)
        if count:
            lines.append(f"| [{title}](area-{area}.md) | {summary} | {count} |")
    lines += ["", "## By format", "", "| What you need | Open | Resources in English |", "|---|---|---|"]
    for category, (title, summary) in categories.items():
        if counts[category]:
            lines.append(f"| {summary} | [{title}]({category}.md) | {counts[category]} |")
    if other:
        lines += ["", "[Resources available only in other languages](other-languages.md)."]
    lines += [
        "", "## Read resource labels", "",
        "- **Curriculum:** an ordered learning recipe for a target profession. Waylantern's recipes are editorial and show their exact resource gaps; official sources are separate.",
        "- **First-project guide:** a short sequence for trying an area. Finishing one is a starting point for further study.",
        "- **External programme:** a third party's longer course sequence or curriculum. Its scope and costs depend on that provider.",
        "- **Topic map:** a roadmap showing subjects and their relationships; it may not teach them or define a study order.",
        "- **Topic level:** beginner means introductory in that subject. A beginner resource may still require another skill, such as Python or JavaScript. Read its prerequisites and requirements before choosing it.",
        "- **Access:** free describes access to the listed material or software. Hardware, API calls, cloud compute, certificates and optional products can cost extra; inspect the details.",
        "- **Languages:** availability recorded from the source. Notes distinguish partial translations, website language and app-interface availability when known.",
        "- **Source checked:** the date and method describe inspection of source material. They do not mean every exercise was executed or every claim remains current.",
        "", "Each catalogue table has expandable details for prerequisites, requirements, languages, pros and cons, and source-check notes. Focus-friendly ratings are editorial judgments and are also kept in those details.", "",
        "[Repository research notes](../research/2026-10-24-repositories-and-careers.md) · [Navigation and consistency audit](../research/2026-10-25-usability-audit.md)",
    ]
    return "\n".join(lines).rstrip()


def render_path_index(paths):
    lines = [
        "# Try an area: first-project guides", "",
        "Choose a small project to discover whether you enjoy an area. These guides have a few steps and checkpoints. For a longer sequence toward a profession, [choose a curriculum](curricula.md).", "",
        "[Home](../README.md) · [Understand the professions](professions.md) · [Resource catalogue](catalogue.md)", "",
    ]
    for level, label in PATH_LEVELS.items():
        subset = [(slug, path) for slug, path in paths if path.get("entry_level", "start-here") == level]
        if not subset:
            continue
        lines += [f"## {label}", "", "| Guide | First project | What you need first |", "|---|---|---|"]
        for slug, path in subset:
            lines.append(f"| [{path['title']}]({slug}.md) | {path['summary']} | {path.get('prerequisites', path['intro'].strip())} |")
    return "\n".join(lines).rstrip()


def render_software_study_preview(entries):
    resources = dict(entries)

    def resource(slug):
        entry = resources[slug]
        return f"[{entry['name']}]({entry['url']})"

    return "\n".join([
        "# Software: connecting a study plan to resources", "",
        "**Block 1 preview.** The academic reference inspected so far is CS2023. Individual university plans are still awaiting inspection, so this is a topic-matching example, not a finished degree plan or semester sequence.", "",
        "[Home](../README.md) / [Software professions](professions-software.md)", "",
        "## The idea", "",
        "An academic plan tells you what to learn. For each requirement, Waylantern helps you choose something to study and something to practise. The same resource can support several profiles without being listed twice in the catalogue.", "",
        "This example concerns computing/software foundations. Design/HCI and physical engineering need their own programme comparisons within this block.", "",
        "## Programming fundamentals", "",
        f"**Study:** {resource('cs50-python')}", "",
        f"**Practise:** {resource('exercism')}", "",
        "**Goal:** understand functions, conditions and loops, then write and explain a small working program.", "",
        "**Starting point:** CS50 Python is introductory; use exercises matching what you have learned. This selection does not cover the whole academic foundation.", "",
        "## Algorithms", "",
        f"**Study:** {resource('mit-6006-introduction-to-algorithms')}", "",
        f"**Explore examples:** {resource('the-algorithms-python')}", "",
        "**Goal:** understand an algorithm, explain why it works and analyse its efficiency. Reading an implementation alone does not demonstrate that understanding.", "",
        "**Starting point:** intermediate material with mathematical prerequisites; check the course's exact prerequisites before choosing it.", "",
        "## Software testing", "",
        f"**Study and practise:** {resource('pytest-getting-started')}", "",
        "**Goal:** write a check that passes for the intended behaviour and fails after a deliberate mistake.", "",
        "**Starting point:** basic Python and terminal use. This is practice in one part of software engineering, not complete coverage of that discipline.", "",
        "## What comes next", "",
        "The accepted university plan must supply the actual subjects, prerequisites and assessment requirements. We then compare their learning outcomes with specific lessons and exercises, showing any gaps. Specialisations such as frontend or backend add their requirements after the shared foundation.", "",
        "<details><summary>Academic evidence and matching notes</summary>", "",
        "These examples relate to CS2023's Software Development Fundamentals (SDF), Algorithmic Foundations (AL) and Software Engineering (SE) knowledge areas. Resource selection is Waylantern's editorial correlation; course equivalence, credit recognition and complete outcome coverage have not been verified.", "",
        "[Read the academic-source investigation](../research/2026-10-25-block-1-academic-bases.md) · [Read the broader resource-mapping example](../research/2026-10-25-block-1-resource-mapping.md)", "",
        "</details>", "",
        "<details><summary>Other resources and existing practice plans</summary>", "",
        "[Explore the software catalogue](area-software.md) · [Read the existing editorial practice plans](professions-software.md#roles-in-this-group)", "",
        "The practice plans were written for Waylantern and have not been derived from a verified university programme. They remain separate from the academic-plan work.", "",
        "</details>",
    ]).rstrip()
