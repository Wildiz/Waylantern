"""Learning-path validation and safe documentation generation."""
import copy
import io
import shutil
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from unittest.mock import patch

import yaml


from scripts import build

REPO_ROOT = Path(__file__).resolve().parents[1]


class LearningPathTests(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory(prefix="waylantern-path-tests-")
        self.addCleanup(self.scratch.cleanup)
        self.root = Path(self.scratch.name)
        self.paths_dir = self.root / "data" / "paths"
        self.paths_dir.mkdir(parents=True)
        shutil.copyfile(REPO_ROOT / "data" / "path-schema.json", self.root / "data" / "path-schema.json")
        self.root_patch = patch.object(build, "ROOT", self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        self.entry = {
            "name": "Example resource",
            "url": "https://example.com/course",
            "price": "free",
            "description": "A small practical resource for learning.",
        }
        self.entries = [("example", self.entry)]
        self.path = {
            "title": "A practical learning path",
            "summary": "Build a small project one step at a time.",
            "areas": ["software"],
            "intro": "Start with one small exercise.",
            "steps": [{
                "title": "Make something small",
                "short": "First project",
                "tools": ["example"],
                "why": "Apply the ideas in a project of your own.",
                "advance_when": "You can explain your working project.",
            }],
        }
        self.write_path("path-0-fundamentals", self.path)

    def write_path(self, slug, data):
        (self.paths_dir / f"{slug}.yml").write_text(yaml.safe_dump(data))

    def test_path_without_helpers_renders_steps_and_navigation(self):
        self.write_path("path-software", self.path)
        paths, errors = build.load_paths(self.entries)
        self.assertEqual(errors, [])
        loaded = dict(paths)["path-software"]
        rendered = build.render_path(loaded, dict(self.entries), "path-software")
        self.assertIn("## Step 1: Make something small", rendered)
        self.assertIn("[Example resource](https://example.com/course)", rendered)
        self.assertIn("**Advance when:** You can explain your working project.", rendered)
        self.assertIn("(path-0-fundamentals.md)", rendered)
        self.assertIn("(area-software.md)", rendered)
        self.assertIn("(../README.md#choose-a-learning-path)", rendered)
        self.assertNotIn("## Optional helpers", rendered)

    def test_fundamentals_summary_without_helpers_renders_first_step(self):
        rows = build.path0_readme_table(self.path, dict(self.entries))
        self.assertEqual(len(rows), 3)
        self.assertIn("| 1 | First project |", rows[2])
        self.assertIn("[Example resource](https://example.com/course)", rows[2])
        self.assertNotIn("Optional helpers", "\n".join(rows))

    def test_unknown_step_resource_has_actionable_diagnostic(self):
        broken = copy.deepcopy(self.path)
        broken["steps"][0]["tools"] = ["missing-course"]
        self.write_path("path-example", broken)
        _, errors = build.load_paths(self.entries)
        diagnostic = "\n".join(errors)
        self.assertIn("path-example.yml", diagnostic)
        self.assertIn("steps/0/tools", diagnostic)
        self.assertIn("unknown resource 'missing-course'", diagnostic)

    def test_unknown_helper_resource_has_actionable_diagnostic(self):
        broken = copy.deepcopy(self.path)
        broken["helpers"] = {"why": "Keep notes.", "tools": ["missing-helper"]}
        self.write_path("path-example", broken)
        _, errors = build.load_paths(self.entries)
        diagnostic = "\n".join(errors)
        self.assertIn("path-example.yml", diagnostic)
        self.assertIn("helpers/tools", diagnostic)
        self.assertIn("unknown resource 'missing-helper'", diagnostic)

    def test_unknown_area_is_rejected(self):
        broken = copy.deepcopy(self.path)
        broken["areas"] = ["nonexistent-area"]
        self.write_path("path-example", broken)
        _, errors = build.load_paths(self.entries)
        self.assertIn("path-example.yml: unknown area 'nonexistent-area'", errors)

    def test_missing_checkpoint_and_empty_steps_are_rejected(self):
        missing_checkpoint = copy.deepcopy(self.path)
        del missing_checkpoint["steps"][0]["advance_when"]
        empty_steps = copy.deepcopy(self.path)
        empty_steps["steps"] = []
        for label, data in [("missing checkpoint", missing_checkpoint), ("empty steps", empty_steps)]:
            with self.subTest(label=label):
                self.write_path("path-example", data)
                paths, errors = build.load_paths(self.entries)
                self.assertTrue(any("path-example.yml" in error for error in errors))
                self.assertNotIn("path-example", dict(paths))

    def test_invalid_yaml_is_reported_without_a_traceback(self):
        (self.paths_dir / "path-broken.yml").write_text("steps: [\n")
        paths, errors = build.load_paths(self.entries)
        self.assertTrue(any("path-broken.yml: invalid YAML:" in error for error in errors))
        self.assertNotIn("path-broken", dict(paths))
        self.assertIn("path-0-fundamentals", dict(paths))

    def test_invalid_path_does_not_overwrite_or_delete_existing_docs(self):
        broken = copy.deepcopy(self.path)
        broken["steps"][0]["tools"] = ["missing-course"]
        self.write_path("path-example", broken)
        docs = self.root / "docs"
        docs.mkdir()
        original_files = {
            self.root / "README.md": b"Existing README\n",
            docs / "path-0-fundamentals.md": b"Existing fundamentals\n",
            docs / "old-page.md": b"Keep this page if validation fails.\n",
        }
        for path, content in original_files.items():
            path.write_bytes(content)
        stderr = io.StringIO()
        with patch.object(build, "load_entries", return_value=(self.entries, [])), \
                patch.object(build.sys, "argv", ["build.py"]), redirect_stderr(stderr):
            result = build.main()
        self.assertEqual(result, 1)
        self.assertIn("missing-course", stderr.getvalue())
        self.assertEqual(set(docs.iterdir()), {path for path in original_files if path.parent == docs})
        for path, content in original_files.items():
            self.assertEqual(path.read_bytes(), content)


if __name__ == "__main__":
    unittest.main()
