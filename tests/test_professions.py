"""Validation and navigation contracts for the professions catalogue."""
import copy
import shutil
import tempfile
import unittest
from pathlib import Path

import yaml

from scripts import profession_catalog


class ProfessionCatalogueTests(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory(prefix="waylantern-professions-")
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        (self.root / "data" / "professions").mkdir(parents=True)
        original = Path(__file__).resolve().parents[1] / "data" / "profession-schema.json"
        shutil.copyfile(original, self.root / "data" / "profession-schema.json")
        self.areas = {"software": ("Software", "Build software.")}
        self.paths = [("path-software", {"title": "Software foundations"})]
        self.sources = [{
            "id": "reference-one", "title": "Skills framework", "publisher": "Example publisher",
            "type": "competency_framework", "url": "https://example.com/framework",
            "verification": "verified", "checked": "2026-10-24", "scope": "Related software skills.",
            "notes": "Read the primary source.",
        }, {
            "id": "reference-two", "title": "Degree recommendations", "publisher": "Example university",
            "type": "academic_curriculum", "url": "https://example.com/curriculum",
            "verification": "link_only", "checked": "2026-10-24", "scope": "Degree-level study.",
            "notes": "Network access prevented reading the content.",
        }]
        self.group = {
            "id": "software", "title": "Software careers", "description": "Roles that build software.",
            "areas": ["software"], "roles": [{
                "id": "software-engineer", "title": "Software Engineer", "description": "Builds software systems.",
                "areas": ["software"], "paths": ["path-software"],
                "guidance": ["reference-one", "reference-two"], "aliases": ["Developer"],
            }],
        }
        self.write_sources()
        self.write_group()

    def write_sources(self):
        (self.root / "data" / "profession-guidelines.yml").write_text(yaml.safe_dump(self.sources))

    def write_group(self, data=None, name="software"):
        (self.root / "data" / "professions" / f"{name}.yml").write_text(yaml.safe_dump(self.group if data is None else data))

    def load(self):
        return profession_catalog.load_professions(self.root, self.areas, self.paths)

    def test_valid_catalogue_renders_navigation_and_visible_source_status(self):
        groups, sources, errors = self.load()
        self.assertEqual(errors, [])
        pages = profession_catalog.render_professions(groups, sources, self.areas, self.paths)
        index = pages["docs/professions.md"]
        profile = pages["docs/professions-software.md"]
        references = pages["docs/profession-references.md"]
        self.assertIn("(professions-software.md)", index)
        self.assertNotIn("#software-engineer", index)
        self.assertIn("[Software Engineer](#software-engineer)", profile)
        self.assertIn('<a id="software-engineer"></a>', profile)
        self.assertIn("Title variants: Developer", profile)
        self.assertIn("[Software](area-software.md)", profile)
        self.assertIn("[Software foundations](path-software.md)", profile)
        self.assertIn("(profession-references.md#reference-reference-one)", profile)
        self.assertIn("<details><summary>Related references</summary>", profile)
        self.assertIn("(#roles-in-this-group)", profile)
        self.assertIn("## Profession groups", index)
        self.assertIn("## Reference sources", index)
        self.assertIn('<a id="reference-reference-one"></a>', index)
        self.assertIn("(profession-references.md#reference-reference-one)", index)
        self.assertIn('<a id="reference-reference-one"></a>', references)
        self.assertIn("Source content read", references)
        self.assertIn("Link only: source content not read", references)
        self.assertIn("does not mean the source does not exist", references)
        self.assertIn("Publisher: Example university", references)
        self.assertIn("Type: Academic curriculum", references)
        self.assertIn("Scope: Degree-level study.", references)
        self.assertIn("Verification notes: Network access prevented reading the content.", references)
        self.assertNotIn("Publisher:", index)
        self.assertNotIn("Source content read", index)
        for page in pages.values():
            self.assertEqual(page, page.rstrip())

    def test_missing_path_is_explicit_and_does_not_invent_a_curriculum(self):
        self.group["roles"][0]["paths"] = []
        self.write_group()
        groups, sources, errors = self.load()
        self.assertEqual(errors, [])
        profile = profession_catalog.render_professions(groups, sources, self.areas, self.paths)["docs/professions-software.md"]
        self.assertIn("Starting path: not added yet.", profile)
        self.assertIn("Study recipe: not added yet.", profile)
        self.assertNotIn("curriculum-software-engineer.md", profile)
        self.assertNotIn("(path-software.md)", profile)
        self.assertIn("(area-software.md)", profile)
        self.assertIn("(profession-references.md#reference-reference-two)", profile)

    def test_curriculum_links_appear_in_group_navigation_and_profile(self):
        groups, sources, errors = self.load()
        self.assertEqual(errors, [])
        curricula = [{"role": "software-engineer", "title": "Software Engineer", "entry_level": "after-basics"}]
        pages = profession_catalog.render_professions(groups, sources, self.areas, self.paths, curricula)
        profile = pages["docs/professions-software.md"]
        self.assertIn("[Practice plan](curriculum-software-engineer.md)", profile)
        self.assertIn("Study recipe: [Editorial practice for Software Engineer](curriculum-software-engineer.md)", profile)
        self.assertNotIn("Study recipe: not added yet.", profile)
        self.assertNotIn("curriculum-software-engineer.md", pages["docs/professions.md"])

    def test_recipe_does_not_invent_a_missing_introductory_path(self):
        self.group["roles"][0]["paths"] = []
        pages = profession_catalog.render_professions(
            [self.group], self.sources, self.areas, self.paths,
            [{"role": "software-engineer"}],
        )
        profile = pages["docs/professions-software.md"]
        self.assertIn("curriculum-software-engineer.md", profile)
        self.assertIn("Starting path: not added yet.", profile)
        self.assertNotIn("(path-software.md)", profile)

    def test_group_order_is_editorial_and_not_dependent_on_file_order(self):
        groups = []
        expected = ["software", "data-ai", "operations", "security", "architecture", "leadership"]
        for group_id in reversed(expected):
            group = copy.deepcopy(self.group)
            group["id"] = group_id
            group["title"] = group_id.title()
            groups.append(group)
        pages = profession_catalog.render_professions(groups, self.sources, self.areas, self.paths)
        index = pages["docs/professions.md"]
        positions = [index.index(f"(professions-{group_id}.md)") for group_id in expected]
        self.assertEqual(positions, sorted(positions))
        self.assertEqual(index.count(" | Roles |"), 1)

    def test_every_legacy_source_anchor_is_preserved_as_a_link_to_its_details(self):
        pages = profession_catalog.render_professions([self.group], self.sources, self.areas, self.paths)
        for source in self.sources:
            fragment = f"reference-{source['id']}"
            with self.subTest(fragment=fragment):
                self.assertIn(f'<a id="{fragment}"></a>', pages["docs/professions.md"])
                self.assertIn(f"(profession-references.md#{fragment})", pages["docs/professions.md"])
                self.assertIn(f'<a id="{fragment}"></a>', pages["docs/profession-references.md"])

    def test_unknown_area_path_and_guidance_are_actionable(self):
        role = self.group["roles"][0]
        role.update(areas=["unknown-area"], paths=["missing-path"], guidance=["missing-source"])
        self.write_group()
        _, _, errors = self.load()
        for detail in ["unknown area 'unknown-area'", "unknown learning path 'missing-path'", "unknown guidance reference 'missing-source'"]:
            with self.subTest(detail=detail):
                self.assertTrue(any("software.yml: role 'software-engineer'" in error and detail in error for error in errors), errors)

    def test_duplicate_role_ids_and_titles_across_groups_are_rejected(self):
        second = copy.deepcopy(self.group)
        second["id"] = "another-group"
        second["roles"][0]["title"] = "  SOFTWARE   engineer "
        self.write_group(second, "another-group")
        _, _, errors = self.load()
        self.assertTrue(any("duplicate role id 'software-engineer'" in error for error in errors))
        self.assertTrue(any("duplicate role title" in error for error in errors))

    def test_invalid_yaml_is_reported_for_groups_and_sources(self):
        for target in [self.root / "data" / "professions" / "software.yml", self.root / "data" / "profession-guidelines.yml"]:
            with self.subTest(filename=target.name):
                original = target.read_text()
                target.write_text("broken: [\n")
                _, _, errors = self.load()
                self.assertTrue(any(target.name in error and "YAML" in error for error in errors), errors)
                target.write_text(original)

    def test_invalid_aliases_and_verification_status_are_rejected(self):
        self.group["roles"][0]["aliases"] = [12]
        self.sources[0]["verification"] = "assumed"
        self.write_group()
        self.write_sources()
        _, _, errors = self.load()
        self.assertTrue(any("aliases/0" in error for error in errors), errors)
        self.assertTrue(any("verification" in error and "profession-guidelines.yml" in error for error in errors), errors)

    def test_duplicate_source_id_and_unknown_group_area_are_rejected(self):
        self.sources.append(copy.deepcopy(self.sources[0]))
        self.group["areas"] = ["missing-group-area"]
        self.write_group()
        self.write_sources()
        _, _, errors = self.load()
        self.assertTrue(any("duplicate reference id 'reference-one'" in error for error in errors))
        self.assertTrue(any("group areas: unknown area 'missing-group-area'" in error for error in errors))

    def test_empty_yaml_document_is_invalid_instead_of_silently_omitted(self):
        (self.root / "data" / "professions" / "software.yml").write_text("")
        _, _, errors = self.load()
        self.assertTrue(any("software.yml" in error and "object" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
