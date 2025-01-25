"""
pushshift_api.py
----------------
Fetches historical Reddit data via Pushshift.
"""

import requests

def fetch_historical_posts(subreddit, limit=100):
    """
    Fetch historical posts from a subreddit using the Pushshift API.
    """
    url = f"https://api.pushshift.io/reddit/search/submission/?subreddit={subreddit}&size={limit}"
    response = requests.get(url)
    data = response.json()
    return data.get("data", [])
