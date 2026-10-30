import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PlatformShellTests(unittest.TestCase):
    def test_shell_links_all_three_tools(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('src="advisory-analysis.html"', html)
        self.assertIn('data-src="vulnerability-dashboard.html"', html)
        self.assertIn('data-src="ssvc-dashboard.html"', html)

    def test_original_vulnerability_dashboard_is_standalone(self):
        html = (ROOT / "vulnerability-dashboard.html").read_text(encoding="utf-8")
        self.assertIn("<title>Vulnerability Dashboard</title>", html)
        self.assertIn("services.nvd.nist.gov/rest/json/cves/2.0", html)
        self.assertNotIn('src="vulnerability-dashboard.js"', html)

    def test_each_tool_file_exists(self):
        for name in (
            "advisory-analysis.html",
            "vulnerability-dashboard.html",
            "ssvc-dashboard.html",
            "app.js",
            "styles.css",
        ):
            self.assertTrue((ROOT / name).is_file(), name)


if __name__ == "__main__":
    unittest.main()
