"""
twitter_scraper.py
------------------
Scrapes Twitter data using snscrape or Twitter API.
"""

import subprocess

def scrape_twitter_hashtag(hashtag, limit=100):
    """
    Uses snscrape to fetch tweets for a given hashtag.
    """
    command = [
        "snscrape", "twitter-hashtag", hashtag,
        f"--max-results={limit}"
    ]
    # Run the command and capture output
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout
