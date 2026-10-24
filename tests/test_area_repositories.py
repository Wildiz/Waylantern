"""Validate selected repositories and their links in area navigation."""
import copy
import tempfile
import unittest
from collections import defaultdict
from pathlib import Path
from unittest.mock import patch

import yaml

from scripts import build


class RepositoryUrlTests(unittest.TestCase):
    def test_repository_subpages_link_to_the_repository_root(self):
        cases = [
            ("https://github.com/example/lessons/blob/main/README.md", "https://github.com/example/lessons"),
            ("https://github.com/example/lessons/tree/main/examples?tab=readme", "https://github.com/example/lessons"),
            ("https://gitlab.com/example/lessons/-/tree/main/examples", "https://gitlab.com/example/lessons"),
            ("https://gitlab.com/example/lessons/-/blob/main/README.md", "https://gitlab.com/example/lessons"),
        ]
        for source, expected in cases:
            with self.subTest(source=source):
                self.assertEqual(build.repository_url({"url": source}), expected)

    def test_explicit_repository_overrides_a_project_website(self):
        entry = {
            "url": "https://example.org/course",
            "repository": "https://github.com/example/lessons/tree/main",
        }
        self.assertEqual(build.repository_url(entry), "https://github.com/example/lessons")

    def test_unsupported_or_credentialed_urls_are_not_repository_links(self):
        invalid = [
            "http://github.com/example/lessons",
            "https://example.org/example/lessons",
            "https://github.com/example",
            "https://github.com/",
            "https://viewer@github.com/example/lessons",
            "https://viewer:example-only@gitlab.com/example/lessons",
        ]
        for source in invalid:
            for field in ("url", "repository"):
                with self.subTest(source=source, field=field):
                    entry = {"url": "https://github.com/example/fallback", field: source}
                    self.assertIsNone(build.repository_url(entry))


class AreaRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory(prefix="waylantern-area-repositories-")
        self.addCleanup(self.scratch.cleanup)
        self.root = Path(self.scratch.name)
        (self.root / "data").mkdir()
        root_patch = patch.object(build, "ROOT", self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)
        self.entry = {
            "name": "Practical software lessons",
            "url": "https://example.org/lessons",
            "repository": "https://github.com/example/lessons/blob/main/README.md",
            "category": "course",
            "areas": ["software"],
            "languages": ["en"],
            "level": "intermediate",
            "price": "free",
            "structure": "guided",
            "focus_friendly": "unknown",
            "description": "Build a small program with explained examples.",
        }
        self.other = dict(self.entry, name="Another resource", url="https://example.org/other")
        self.entries = [("lessons", self.entry), ("other", self.other)]
        self.path = {
            "title": "Software first steps",
            "summary": "Build one small program.",
            "areas": ["software"],
            "intro": "Start with a small project.",
            "steps": [{
                "title": "Try the example", "short": "First example", "tools": ["lessons"],
                "why": "Read and modify one example.", "advance_when": "You can explain the result.",
            }],
        }

    def write_selections(self, selections):
        (self.root / "data" / "area-repositories.yml").write_text(yaml.safe_dump(selections))

    def test_valid_selection_preserves_area_and_resource_order(self):
        expected = {"software": ["lessons", "other"]}
        self.write_selections(expected)
        selections, errors = build.load_area_repositories(self.entries)
        self.assertEqual(errors, [])
        self.assertEqual(selections, expected)

    def test_unknown_resource_has_a_named_diagnostic(self):
        self.write_selections({"software": ["missing-lessons"]})
        _, errors = build.load_area_repositories(self.entries)
        self.assertTrue(any("unknown resource 'missing-lessons'" in error for error in errors))

    def test_unknown_area_has_a_named_diagnostic(self):
        self.write_selections({"invented-area": ["lessons"]})
        _, errors = build.load_area_repositories(self.entries)
        self.assertTrue(any("unknown area 'invented-area'" in error for error in errors))

    def test_resource_must_belong_to_the_selected_area(self):
        self.write_selections({"networking": ["lessons"]})
        _, errors = build.load_area_repositories(self.entries)
        self.assertTrue(any("'lessons' is not in the English catalogue for 'networking'" in error
                            for error in errors))

    def test_non_english_resource_is_not_selected(self):
        entries = [("lessons", dict(self.entry, languages=["es"]))]
        self.write_selections({"software": ["lessons"]})
        _, errors = build.load_area_repositories(entries)
        self.assertTrue(any("'lessons' is not in the English catalogue" in error for error in errors))

    def test_resource_without_a_supported_repository_is_rejected(self):
        entry = copy.deepcopy(self.entry)
        del entry["repository"]
        self.write_selections({"software": ["lessons"]})
        _, errors = build.load_area_repositories([("lessons", entry)])
        self.assertTrue(any("'lessons' has no supported repository link" in error for error in errors))

    def test_invalid_yaml_is_reported(self):
        (self.root / "data" / "area-repositories.yml").write_text("software: [\n")
        selections, errors = build.load_area_repositories(self.entries)
        self.assertEqual(selections, {})
        self.assertTrue(any("area-repositories.yml: invalid YAML:" in error for error in errors))

    def test_invalid_selection_shapes_and_duplicate_or_excessive_slugs_are_rejected(self):
        cases = [
            None,
            ["lessons"],
            {"software": "lessons"},
            {"software": []},
            {"software": ["lessons", "lessons"]},
            {"software": ["lessons", "other", "third", "fourth"]},
        ]
        for selections in cases:
            with self.subTest(selections=selections):
                self.write_selections(selections)
                loaded, errors = build.load_area_repositories(self.entries)
                self.assertEqual(loaded, {})
                self.assertTrue(errors)
                self.assertTrue(all("area-repositories.yml:" in error for error in errors))

    def test_readme_area_row_has_path_repository_and_full_resource_count(self):
        by_slug = dict(self.entries)
        groups = defaultdict(list)
        groups["course"] = [self.entry, self.other]
        rendered = build.render_readme(
            self.entries, groups, path0=self.path, by_slug=by_slug,
            paths=[("path-software", self.path)], selections={"software": ["lessons"]},
        )
        row = next(line for line in rendered.splitlines()
                   if line.startswith("| [Programming and software engineering]"))
        self.assertIn("[Software first steps](docs/path-software.md)", row)
        self.assertIn("[Practical software lessons](https://github.com/example/lessons)", row)
        self.assertIn("[2](docs/area-software.md)", row)
        self.assertNotIn("blob/main", row)
        self.assertNotIn("Another resource", row)

    def test_area_page_shows_selected_repository_level_and_learning_path(self):
        rendered = build.render_area(
            "software", [self.entry, self.other],
            paths=[("path-software", self.path)], selected=[self.entry],
        )
        self.assertIn("## Selected repositories", rendered)
        selected_section = rendered.split("## Selected repositories", 1)[1].split("## Not sure", 1)[0]
        self.assertIn("[Practical software lessons](https://github.com/example/lessons)", selected_section)
        self.assertIn("intermediate", selected_section)
        self.assertIn("Free", selected_section)
        self.assertNotIn("Another resource", selected_section)
        self.assertIn("[Software first steps](path-software.md)", rendered)
        self.assertIn("2 resources.", rendered)
        self.assertIn("[Another resource](https://example.org/other)", rendered)


if __name__ == "__main__":
    unittest.main()
