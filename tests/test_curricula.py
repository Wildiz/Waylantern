"""Learning recipes must cover roles honestly and preserve usable study navigation."""
import copy
import shutil
import tempfile
import unittest
from pathlib import Path

import yaml

from scripts import curricula


class CurriculumTests(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory(prefix="waylantern-curricula-")
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        (self.root / "data" / "curricula").mkdir(parents=True)
        schema = Path(__file__).resolve().parents[1] / "data" / "curriculum-schema.json"
        shutil.copyfile(schema, self.root / "data" / "curriculum-schema.json")
        self.resource = {
            "name": "Example foundations", "url": "https://example.com/foundations",
            "category": "course", "areas": ["software"], "price": "free",
            "level": "beginner", "languages": ["en"], "structure": "guided",
            "focus_friendly": "unknown", "description": "Learn the foundations through a small exercise.",
            "verified": {"date": "2026-10-24", "method": "official-site", "notes": "Fixture source."},
        }
        self.entries = [("example-foundations", self.resource)]
        self.professions = [{
            "id": "software", "title": "Software careers", "description": "Build and test software.",
            "areas": ["software"], "roles": [{
                "id": "software-engineer", "title": "Software Engineer",
                "description": "Builds and maintains software.", "areas": ["software"],
                "paths": [], "guidance": ["example-guide"],
            }],
        }]
        self.sources = [{
            "id": "example-guide", "title": "Example skills guide", "publisher": "Example publisher",
            "type": "competency_framework", "url": "https://example.com/guide",
            "verification": "link_only", "checked": "2026-10-24",
            "scope": "Related software skills, not an endorsed role curriculum.",
            "notes": "Source contents not inspected.",
        }]
        self.recipe = {
            "role": "software-engineer", "title": "Software Engineer",
            "summary": "Build a small program and demonstrate its behaviour.",
            "entry_level": "from-zero", "prerequisites": ["Use files and a text editor."],
            "outcome": "A small program with reproducible checks and a handover note.",
            "stages": [{
                "title": "Understand a small problem", "topics": ["Inputs and outputs", "Explicit requirements"],
                "resources": ["example-foundations"], "practice": "Write down one input and the expected result.",
                "checkpoint": "Another reader can identify the expected behaviour.",
            }, {
                "title": "Implement one behaviour", "topics": ["Program structure", "Simple error handling"],
                "resources": ["example-foundations"], "practice": "Implement the agreed behaviour in a tiny program.",
                "checkpoint": "The program produces the expected result for the recorded input.",
            }, {
                "title": "Review a failure", "topics": ["Failure observations", "Limits of evidence"],
                "resources": [], "practice": "Record one invalid input and explain the observed failure.",
                "checkpoint": "The report distinguishes an observation from an untested explanation.",
                "gap": "A reviewed guide to this failure-analysis activity is still needed.",
            }, {
                "title": "Capstone: hand over the program", "topics": ["Repeatable checks", "Clear handover"],
                "resources": ["example-foundations"], "practice": "Package the program and instructions for a new reader.",
                "checkpoint": "A clean run reproduces the recorded result using the instructions.",
            }],
            "next_steps": "Practise a second problem before adding specialist features.",
        }
        self.data = {"group": "software", "curricula": [self.recipe]}
        self.write_data()

    def write_data(self, data=None, name="software"):
        target = self.root / "data" / "curricula" / f"{name}.yml"
        target.write_text(yaml.safe_dump(self.data if data is None else data, sort_keys=False))

    def load(self):
        return curricula.load_curricula(self.root, self.entries, self.professions)

    def render(self):
        recipes, errors = self.load()
        self.assertEqual(errors, [])
        return curricula.render_curricula(recipes, self.professions, self.entries, self.sources)

    def test_valid_complete_catalogue_loads_all_four_stages(self):
        recipes, errors = self.load()
        self.assertEqual(errors, [])
        self.assertEqual([recipe["role"] for recipe in recipes], ["software-engineer"])
        self.assertEqual(len(recipes[0]["stages"]), 4)

    def test_uncovered_profession_is_rejected_instead_of_silently_hidden(self):
        missing = copy.deepcopy(self.professions[0]["roles"][0])
        missing.update(id="another-role", title="Another Role")
        self.professions[0]["roles"].append(missing)
        _, errors = self.load()
        self.assertTrue(any("missing curriculum" in error and "another-role" in error for error in errors), errors)

    def test_no_curriculum_files_reports_missing_coverage(self):
        (self.root / "data" / "curricula" / "software.yml").unlink()
        recipes, errors = self.load()
        self.assertEqual(recipes, [])
        self.assertTrue(any("missing curriculum" in error and "software-engineer" in error for error in errors), errors)

    def test_duplicate_recipe_for_one_role_is_rejected(self):
        self.data["curricula"].append(copy.deepcopy(self.recipe))
        self.write_data()
        _, errors = self.load()
        self.assertTrue(any("duplicate curriculum" in error and "software-engineer" in error for error in errors), errors)

    def test_unknown_role_is_rejected(self):
        self.recipe["role"] = "invented-role"
        self.write_data()
        _, errors = self.load()
        self.assertTrue(any("unknown role" in error and "invented-role" in error for error in errors), errors)

    def test_recipe_cannot_be_assigned_to_another_profession_group(self):
        (self.root / "data" / "curricula" / "software.yml").unlink()
        self.data["group"] = "operations"
        self.write_data(name="operations")
        _, errors = self.load()
        self.assertTrue(any("incorrect group" in error and "software-engineer" in error for error in errors), errors)

    def test_group_must_match_its_file(self):
        self.data["group"] = "operations"
        self.write_data()
        _, errors = self.load()
        self.assertTrue(any("software.yml" in error and "group must match filename" in error for error in errors), errors)

    def test_unknown_resource_names_the_role_and_stage(self):
        self.recipe["stages"][1]["resources"] = ["missing-course"]
        self.write_data()
        _, errors = self.load()
        self.assertTrue(any("software-engineer" in error and "stage 2" in error and "missing-course" in error for error in errors), errors)

    def test_stage_without_resources_requires_an_explicit_gap(self):
        del self.recipe["stages"][2]["gap"]
        self.write_data()
        _, errors = self.load()
        self.assertTrue(any("stages/2" in error and "gap" in error for error in errors), errors)

    def test_invalid_yaml_is_an_actionable_error(self):
        (self.root / "data" / "curricula" / "software.yml").write_text("curricula: [\n")
        _, errors = self.load()
        self.assertTrue(any("software.yml" in error and "YAML" in error for error in errors), errors)

    def test_missing_or_blank_checkpoint_cannot_pass_validation(self):
        stage = self.recipe["stages"][0]
        for value in [None, "   "]:
            with self.subTest(checkpoint=value):
                if value is None:
                    stage.pop("checkpoint", None)
                else:
                    stage["checkpoint"] = value
                self.write_data()
                _, errors = self.load()
                self.assertTrue(any("stages/0" in error and "checkpoint" in error for error in errors), errors)

    def test_renderer_exposes_a_followable_recipe_and_its_resource_gap(self):
        pages = self.render()
        page = pages["docs/curriculum-software-engineer.md"]
        self.assertIn("Start with the basics", page)
        self.assertIn(self.recipe["prerequisites"][0], page)
        self.assertIn(self.recipe["outcome"], page)
        self.assertIn("Waylantern editorial learning recipe", page)
        self.assertIn("3 of 4 stages", page)
        for number, stage in enumerate(self.recipe["stages"], 1):
            with self.subTest(stage=number):
                self.assertIn(f'<a id="stage-{number}"></a>', page)
                self.assertIn(f"(#stage-{number})", page)
                for topic in stage["topics"]:
                    self.assertIn(topic, page)
                self.assertIn(stage["practice"], page)
                self.assertIn(stage["checkpoint"], page)
        self.assertIn(self.recipe["stages"][2]["gap"], page)
        self.assertIn("Resource still needed:", page)
        self.assertIn(f"[{self.resource['name']}]({self.resource['url']})", page)
        self.assertIn("(area-software.md#resource-example-foundations)", page)
        self.assertIn(self.recipe["next_steps"], page)
        for body in pages.values():
            self.assertEqual(body, body.rstrip())

    def test_partial_coverage_is_visible_even_when_a_stage_has_a_resource(self):
        stage = self.recipe["stages"][0]
        stage["gap"] = "The linked introduction does not cover the specialist task."
        self.write_data()
        page = self.render()["docs/curriculum-software-engineer.md"]
        self.assertIn(self.resource["url"], page)
        self.assertIn(stage["gap"], page)
        self.assertIn("2 of 4 stages", page)

    def test_index_links_to_the_group_and_explains_editorial_status(self):
        index = self.render()["docs/curricula.md"]
        self.assertIn("(professions-software.md#roles-in-this-group)", index)
        self.assertIn("| 1 |", index)
        self.assertIn("not institution-issued curricula", index)
        self.assertIn("(profession-references.md)", index)

    def test_experience_required_is_not_presented_as_a_from_zero_role(self):
        self.recipe["entry_level"] = "experience-required"
        self.recipe["prerequisites"] = ["Have practical responsibility for an operational service."]
        self.write_data()
        page = self.render()["docs/curriculum-software-engineer.md"]
        self.assertIn("**Starting point:** Prior practical experience required", page)
        self.assertIn(self.recipe["prerequisites"][0], page)
        self.assertNotIn("**Starting point:** Start with the basics", page)

    def test_profile_backlinks_and_related_sources_preserve_context(self):
        page = self.render()["docs/curriculum-software-engineer.md"]
        self.assertIn("(professions-software.md#software-engineer)", page)
        self.assertIn("(professions-software.md#roles-in-this-group)", page)
        self.assertIn("(profession-references.md#reference-example-guide)", page)
        self.assertIn("not an endorsement of this recipe", page)
        self.assertNotIn("(professions.md#reference-example-guide)", page)


if __name__ == "__main__":
    unittest.main()
