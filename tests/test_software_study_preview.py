"""Keep the first block's academic matching example small and explicit."""
import unittest

from scripts.navigation import render_software_study_preview


class SoftwareStudyPreviewTests(unittest.TestCase):
    def setUp(self):
        slugs = ["cs50-python", "exercism", "mit-6006-introduction-to-algorithms",
                 "the-algorithms-python", "pytest-getting-started"]
        self.entries = [(slug, {"name": slug, "url": f"https://example.com/{slug}"}) for slug in slugs]

    def test_selected_topics_show_study_and_practice_from_existing_entries(self):
        page = render_software_study_preview(self.entries)
        for slug, entry in self.entries:
            self.assertIn(f"[{entry['name']}]({entry['url']})", page)
        self.assertIn("**Study:**", page)
        self.assertIn("**Practise:**", page)
        self.assertIn("**Goal:**", page)
        self.assertIn("**Starting point:**", page)

    def test_university_requirements_and_editorial_correlations_remain_distinct(self):
        page = render_software_study_preview(self.entries)
        self.assertIn("not a finished degree plan or semester sequence", page)
        self.assertIn("course equivalence, credit recognition and complete outcome coverage have not been verified", page)
        self.assertIn("<details><summary>Academic evidence", page)
        self.assertIn("(professions-software.md)", page)
        self.assertIn("(../research/2026-10-25-block-1-academic-bases.md)", page)


if __name__ == "__main__":
    unittest.main()
