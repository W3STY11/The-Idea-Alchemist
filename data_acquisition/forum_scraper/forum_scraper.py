"""
forum_scraper.py
----------------
Scrapes forum data (e.g., Stack Exchange).
"""

import requests

def fetch_stackexchange_questions(tag, pagesize=10):
    """
    Fetch questions from Stack Exchange for a given tag.
    """
    url = (
        "https://api.stackexchange.com/2.3/questions?"
        f"order=desc&sort=activity&tagged={tag}&site=stackoverflow"
        f"&pagesize={pagesize}"
    )
    response = requests.get(url)
    data = response.json()
    return data.get("items", [])
