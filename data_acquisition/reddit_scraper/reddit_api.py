"""
reddit_api.py
-------------
Handles Reddit data retrieval using PRAW.
"""

import praw
import os

def get_reddit_client():
    """
    Returns an authenticated Reddit client using environment variables.
    """
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT", "the_idea_alchemist")
    )

def fetch_reddit_posts(subreddit_name, limit=10):
    """
    Fetch posts from a subreddit.
    """
    client = get_reddit_client()
    subreddit = client.subreddit(subreddit_name)
    return [post for post in subreddit.hot(limit=limit)]
