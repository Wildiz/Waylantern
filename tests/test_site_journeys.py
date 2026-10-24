"""Render real catalogue data in memory and check complete reader journeys."""
import io
import posixpath
import re
import sys
import tempfile
import unittest
from collections import Counter, deque
from contextlib import ExitStack, redirect_stderr
from pathlib import Path
from unittest.mock import patch
from urllib.parse import unquote, urlsplit

from scripts import build


REPO_ROOT = Path(__file__).resolve().parents[1]


def markdown_links(body):
    """Extract inline navigation links, ignoring examples inside code fences."""
    body = re.sub(r"(?ms)^```[^\n]*\n.*?^```\s*$", "", body)
    body = re.sub(r"`[^`\n]+`", "", body)
    return [target.strip().strip("<>") for target in
            re.findall(r"(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)", body)]


def local_destination(page, target):
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None
    relative = unquote(parsed.path)
    filename = posixpath.normpath(posixpath.join(posixpath.dirname(page), relative)) if relative else page
    return filename, unquote(parsed.fragment)


def page_anchors(body):
    anchors = set(re.findall(r"\bid=[\"']([^\"']+)[\"']", body))
    counts = Counter()
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", body):
        base = build.anchor(heading)
        suffix = counts[base]
        anchors.add(f"{base}-{suffix}" if suffix else base)
        counts[base] += 1
    return anchors


class SiteJourneyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.entries, entry_errors = build.load_entries()
        cls.paths, path_errors = build.load_paths(cls.entries)
        cls.selections, selection_errors = build.load_area_repositories(cls.entries)
        cls.professions, cls.sources, profession_errors = build.load_professions(
            REPO_ROOT, build.AREAS, cls.paths,
        )
        cls.curricula, curriculum_errors = build.load_curricula(REPO_ROOT, cls.entries, cls.professions)
        errors = entry_errors + path_errors + selection_errors + profession_errors + curriculum_errors
        if errors:
            raise AssertionError("Real catalogue validation failed:\n" + "\n".join(errors))
        cls.pages = build.render_all(
            cls.entries, cls.paths, cls.selections, cls.professions, cls.sources, cls.curricula,
        )
        cls.links = {
            page: [destination for target in markdown_links(body)
                   if (destination := local_destination(page, target)) is not None]
            for page, body in cls.pages.items()
        }

    def assert_link(self, source, target):
        destination = local_destination(source, target)
        self.assertIn(destination, self.links[source], f"No navigation from {source} to {target}")

    def test_all_internal_links_resolve_to_existing_files_and_anchors(self):
        failures = []
        anchor_cache = {}
        for source, destinations in self.links.items():
            for target, fragment in destinations:
                if target.startswith("../") or target.startswith("/"):
                    failures.append(f"{source}: target escapes repository: {target}")
                    continue
                disk_path = REPO_ROOT / target
                body = self.pages.get(target)
                if body is None:
                    if not disk_path.is_file():
                        failures.append(f"{source}: missing file {target}")
                        continue
                    if fragment:
                        body = disk_path.read_text()
                if fragment:
                    if target not in anchor_cache:
                        anchor_cache[target] = page_anchors(body)
                    if fragment not in anchor_cache[target]:
                        failures.append(f"{source}: missing fragment {target}#{fragment}")
        self.assertEqual(sorted(set(failures)), [])

    def test_every_generated_page_can_be_reached_from_the_homepage(self):
        reached = {"README.md"}
        queue = deque(reached)
        while queue:
            source = queue.popleft()
            for target, _ in self.links.get(source, []):
                if target in self.pages and target not in reached:
                    reached.add(target)
                    queue.append(target)
        self.assertEqual(set(self.pages) - reached, set(), "Generated pages must not become invisible to readers")

    def test_translated_homepages_keep_the_same_four_main_choices(self):
        expected = {
            "docs/path-0-fundamentals.md", "docs/professions.md",
            "docs/curricula.md", "docs/catalogue.md",
        }
        for source in ("README.md", "README.es.md"):
            with self.subTest(source=source):
                targets = [local_destination(source, target)[0]
                           for row in self.pages[source].splitlines() if row.startswith("| ")
                           for target in markdown_links(row)]
                self.assertEqual(set(targets), expected)
                self.assertEqual(len(targets), 4)

    def test_every_role_has_one_recipe_and_round_trip_group_navigation(self):
        role_groups = {role["id"]: group["id"]
                       for group in self.professions for role in group["roles"]}
        counts = Counter(recipe["role"] for recipe in self.curricula)
        self.assertEqual(set(counts), set(role_groups))
        self.assertTrue(all(count == 1 for count in counts.values()))
        expected_pages = {f"docs/curriculum-{role}.md" for role in role_groups}
        self.assertEqual({page for page in self.pages if page.startswith("docs/curriculum-")}, expected_pages)
        for role, group in role_groups.items():
            with self.subTest(role=role):
                profile_page = f"docs/professions-{group}.md"
                recipe_page = f"docs/curriculum-{role}.md"
                self.assert_link(profile_page, f"curriculum-{role}.md")
                self.assert_link(recipe_page, f"professions-{group}.md#{role}")
                self.assert_link(recipe_page, f"professions-{group}.md#roles-in-this-group")

    def test_beginner_can_go_from_home_to_a_first_activity_and_checkpoint(self):
        slug = "path-0-fundamentals"
        self.assert_link("README.md", f"docs/{slug}.md")
        guide = dict(self.paths)[slug]
        first = guide["steps"][0]
        body = self.pages[f"docs/{slug}.md"]
        self.assertIn(first["why"].strip(), body)
        self.assertIn(first["advance_when"].strip(), body)
        self.assertTrue(any(dict(self.entries)[resource]["url"] in body for resource in first["tools"]))
        self.assert_link(f"docs/{slug}.md", "curricula.md")

    def test_role_reader_can_go_from_group_to_recipe_and_a_study_resource(self):
        role = "it-support-technician"
        group = next(group for group in self.professions if any(profile["id"] == role for profile in group["roles"]))
        group_page = f"docs/professions-{group['id']}.md"
        recipe_page = f"docs/curriculum-{role}.md"
        self.assert_link("README.md", "docs/professions.md")
        self.assert_link("docs/professions.md", f"professions-{group['id']}.md")
        self.assert_link(group_page, f"curriculum-{role}.md")
        recipe = next(item for item in self.curricula if item["role"] == role)
        stage = next(stage for stage in recipe["stages"] if stage["resources"])
        self.assertIn(stage["practice"], self.pages[recipe_page])
        self.assertIn(stage["checkpoint"], self.pages[recipe_page])
        resource = dict(self.entries)[stage["resources"][0]]
        self.assertIn(resource["url"], markdown_links(self.pages[recipe_page]))

    def test_subject_reader_finds_a_first_project_before_selected_repositories(self):
        area = "web"
        area_page = f"docs/area-{area}.md"
        guide_slug, _ = next((slug, data) for slug, data in self.paths if area in data["areas"])
        self.assert_link("README.md", "docs/catalogue.md")
        self.assert_link("docs/catalogue.md", f"area-{area}.md")
        self.assert_link(area_page, f"{guide_slug}.md")
        body = self.pages[area_page]
        self.assertLess(body.index(f"]({guide_slug}.md)"), body.index("## Selected repositories"))


class SafeGenerationTests(unittest.TestCase):
    def test_invalid_curriculum_does_not_render_rewrite_or_delete_documentation(self):
        with tempfile.TemporaryDirectory(prefix="waylantern-safe-site-") as scratch:
            root = Path(scratch)
            (root / "docs").mkdir()
            (root / "README.md").write_text("Existing home must survive.\n")
            (root / "docs" / "keep.md").write_text("Existing page must survive.\n")
            before = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
            stderr = io.StringIO()
            with ExitStack() as stack:
                stack.enter_context(patch.object(build, "ROOT", root))
                stack.enter_context(patch.object(sys, "argv", ["build.py"]))
                stack.enter_context(patch.object(build, "load_entries", return_value=([], [])))
                stack.enter_context(patch.object(build, "load_paths", return_value=([], [])))
                stack.enter_context(patch.object(build, "load_area_repositories", return_value=({}, [])))
                stack.enter_context(patch.object(build, "load_professions", return_value=([], [], [])))
                stack.enter_context(patch.object(build, "load_curricula", return_value=([], ["Invalid curriculum fixture."])))
                renderer = stack.enter_context(patch.object(build, "render_all"))
                stack.enter_context(redirect_stderr(stderr))
                result = build.main()
            self.assertEqual(result, 1)
            renderer.assert_not_called()
            self.assertIn("Invalid curriculum fixture.", stderr.getvalue())
            after = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
            self.assertEqual(after, before)


if __name__ == "__main__":
    unittest.main()
