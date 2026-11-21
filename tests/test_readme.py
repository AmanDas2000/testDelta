import unittest
from pathlib import Path


class ReadmeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.readme = Path(__file__).resolve().parents[1] / "README.md"
        cls.content = cls.readme.read_text(encoding="utf-8").strip()

    def test_readme_exists(self):
        self.assertTrue(self.readme.is_file())

    def test_readme_is_not_empty(self):
        self.assertTrue(self.content)

    def test_readme_has_welcoming_greeting(self):
        self.assertIn("Hello, and welcome!", self.content)


if __name__ == "__main__":
    unittest.main()
