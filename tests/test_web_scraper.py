"""
test_web_scraper.py
-------------------
Unit tests for the web scraper.
"""

import unittest
from data_acquisition.web_scraper.general_scraper import scrape_website

class TestWebScraper(unittest.TestCase):
    def test_scrape_website(self):
        content = scrape_website("https://example.com")
        self.assertIn("Example Domain", content)

if __name__ == "__main__":
    unittest.main()
