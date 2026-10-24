"""Reader-facing navigation stays small, honest about counts and clear about prerequisites."""
import copy
import html
import re
import unittest

from scripts import build, navigation


def destinations(markdown):
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", markdown)


class HomeNavigationTests(unittest.TestCase):
    def test_english_and_spanish_offer_the_same_four_primary_destinations(self):
        expected = {
            "docs/path-0-fundamentals.md", "docs/professions.md",
            "docs/curricula.md", "docs/catalogue.md",
        }
        for spanish in (False, True):
            with self.subTest(spanish=spanish):
                page = navigation.render_home(325, 315, 10, 133, spanish=spanish)
                primary_rows = [line for line in page.splitlines()
                                if line.startswith("| ") and destinations(line)]
                primary_links = [url for row in primary_rows for url in destinations(row)]
                self.assertEqual(set(primary_links), expected)
                self.assertEqual(len(primary_links), 4)
                self.assertLessEqual(len(destinations(page)), 20)
                self.assertIn("325", page)
                self.assertIn("315", page)
                self.assertIn("133", page)
                self.assertNotRegex(page.casefold(), r"two weeks|dos semanas")
                self.assertNotIn("Selected repositories", page)
                self.assertNotIn("(docs/area-", page)
                self.assertEqual(page, page.rstrip())

    def test_language_switch_links_to_the_other_homepage(self):
        english = navigation.render_home(3, 2, 1, 5)
        spanish = navigation.render_home(3, 2, 1, 5, spanish=True)
        self.assertIn("README.es.md", destinations(english))
        self.assertIn("README.md", destinations(spanish))


class CatalogueNavigationTests(unittest.TestCase):
    def setUp(self):
        self.areas = {
            "software": ("Software", "Write and inspect programs."),
            "web": ("Web", "Build browser interfaces."),
        }
        self.categories = {"course": ("Courses", "Study one topic.")}
        self.entries = [
            ("overlapping", {"name": "Overlapping course", "category": "course",
                             "areas": ["software", "web"], "languages": ["en"]}),
            ("bilingual", {"name": "Bilingual course", "category": "course",
                           "areas": ["software"], "languages": ["en", "es"]}),
            ("spanish-only", {"name": "Spanish course", "category": "course",
                              "areas": ["web"], "languages": ["es"]}),
        ]

    def test_totals_count_resources_once_and_disclose_overlapping_area_counts(self):
        page = navigation.render_catalogue(self.entries, self.areas, self.categories)
        self.assertRegex(page, r"3 resources[^\n]*2 available in English[^\n]*1 in other languages")
        self.assertRegex(page.casefold(), r"area counts overlap")
        software = next(line for line in page.splitlines() if "[Software](area-software.md)" in line)
        web = next(line for line in page.splitlines() if "[Web](area-web.md)" in line)
        self.assertRegex(software, r"\| 2 \|$")
        self.assertRegex(web, r"\| 1 \|$")
        course = next(line for line in page.splitlines() if "[Courses](course.md)" in line)
        self.assertRegex(course, r"\| 2 \|$")
        self.assertIn("other-languages.md", destinations(page))

    def test_catalogue_exposes_subject_format_and_label_destinations(self):
        page = navigation.render_catalogue(self.entries, self.areas, self.categories)
        for heading in ("## By area", "## By format", "## Read resource labels"):
            with self.subTest(heading=heading):
                self.assertIn(heading, page)
        self.assertIn("curricula.md", destinations(page))
        self.assertIn("learning-paths.md", destinations(page))
        self.assertEqual(page, page.rstrip())


class FirstProjectNavigationTests(unittest.TestCase):
    def test_three_entry_groups_present_their_own_prerequisites_in_study_order(self):
        paths = [
            ("path-experienced", {"title": "Build after programming", "summary": "Make a tested service.",
                                  "intro": "An experienced project.", "entry_level": "some-experience",
                                  "prerequisites": "Write and debug a small program first."}),
            ("path-foundations", {"title": "Learn after foundations", "summary": "Inspect one dataset.",
                                  "intro": "A foundations project.", "entry_level": "after-basics",
                                  "prerequisites": "Understand tables and run basic Python first."}),
            ("path-first", {"title": "A first activity", "summary": "Make a tiny page.",
                            "intro": "An introductory project.", "entry_level": "start-here",
                            "prerequisites": "Use files and a web browser."}),
        ]
        page = navigation.render_path_index(paths)
        self.assertEqual(sum(line.startswith("## ") for line in page.splitlines()), 3)
        positions = [page.index(f"({slug}.md)") for slug in ("path-first", "path-foundations", "path-experienced")]
        self.assertEqual(positions, sorted(positions))
        for slug, path in paths:
            with self.subTest(path=slug):
                row = next(line for line in page.splitlines() if f"({slug}.md)" in line)
                self.assertIn(path["summary"], row)
                self.assertIn(path["prerequisites"], row)
        self.assertIn("curricula.md", destinations(page))
        self.assertNotRegex(page.casefold(), r"two weeks|dos semanas")

    def test_guide_without_new_metadata_keeps_a_usable_introductory_entry(self):
        path = {"title": "Legacy guide", "summary": "Try a small activity.", "intro": "Read a short example first."}
        page = navigation.render_path_index([("path-legacy", path)])
        self.assertIn("(path-legacy.md)", page)
        self.assertIn(path["intro"], page)


class ResourceTableTests(unittest.TestCase):
    def setUp(self):
        self.resource = {
            "name": "Pipe | Name\ncontinued", "url": "https://example.com/lesson",
            "category": "course", "price": "free", "level": "intermediate",
            "languages": ["en"], "structure": "guided", "focus_friendly": "unknown",
            "description": "First part | second part.\nRead the next example.",
            "areas": ["software"],
            "verified": {"date": "2026-10-24", "method": "official-site", "notes": "Fixture inspected."},
        }

    def test_literal_pipes_and_newlines_cannot_create_extra_table_cells_or_rows(self):
        for detailed in (False, True):
            with self.subTest(detailed=detailed):
                page = build.table([copy.deepcopy(self.resource)], detailed)
                rows = [line for line in page.splitlines() if line.startswith("|")]
                self.assertGreaterEqual(len(rows), 3)
                header_cells = len(re.findall(r"(?<!\\)\|", rows[0]))
                row = next(line for line in rows[2:] if "Pipe" in line)
                self.assertEqual(len(re.findall(r"(?<!\\)\|", row)), header_cells)
                visible_text = html.unescape(row).replace("\\|", "|")
                self.assertIn("Pipe | Name", visible_text)
                self.assertIn("First part | second part.", visible_text)
                self.assertIn("continued", row)
                self.assertIn("Read the next example.", row)

    def test_resource_topic_level_is_visible_at_the_point_of_choice(self):
        page = build.table([self.resource], True)
        row = next(line for line in page.splitlines() if line.startswith("|") and "Pipe" in line)
        self.assertIn("intermediate", row)
        self.assertIn("Free", row)


if __name__ == "__main__":
    unittest.main()
