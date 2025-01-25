"""
test_reddit_scraper.py
----------------------
Unit tests for the Reddit scraper.
"""

import unittest
from data_acquisition.reddit_scraper.reddit_api import fetch_reddit_posts

class TestRedditScraper(unittest.TestCase):
    def test_fetch_reddit_posts(self):
        # This test won't fully work without valid API credentials.
        # It's just a placeholder example.
        posts = fetch_reddit_posts("AskReddit", limit=1)
        self.assertIsInstance(posts, list)

if __name__ == "__main__":
    unittest.main()
