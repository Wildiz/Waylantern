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
        self.assertIn("(professions-software.md#software-engineer)", index)
        self.assertIn('<a id="software-engineer"></a>', profile)
        self.assertIn("Also called: Developer", profile)
        self.assertIn("[Software](area-software.md)", profile)
        self.assertIn("[Software foundations](path-software.md)", profile)
        self.assertIn("(professions.md#reference-reference-one)", profile)
        self.assertIn('<a id="reference-reference-one"></a>', index)
        self.assertIn("Verified: source content read", index)
        self.assertIn("Link only: source content not read", index)
        self.assertIn("does not mean the source does not exist", index)
        self.assertIn("Publisher: Example university", index)
        self.assertIn("Type: Academic curriculum", index)
        self.assertIn("Scope: Degree-level study.", index)
        for page in pages.values():
            self.assertEqual(page, page.rstrip())

    def test_missing_path_is_explicit_and_does_not_invent_a_curriculum(self):
        self.group["roles"][0]["paths"] = []
        self.write_group()
        groups, sources, errors = self.load()
        self.assertEqual(errors, [])
        profile = profession_catalog.render_professions(groups, sources, self.areas, self.paths)["docs/professions-software.md"]
        self.assertIn("No dedicated learning path is available", profile)
        self.assertNotIn("(path-software.md)", profile)
        self.assertIn("(area-software.md)", profile)
        self.assertIn("(professions.md#reference-reference-two)", profile)

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
