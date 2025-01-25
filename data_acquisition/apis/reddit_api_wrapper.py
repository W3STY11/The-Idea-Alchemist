"""
reddit_api_wrapper.py
---------------------
High-level wrapper around PRAW or other Reddit data access methods.
"""

from data_acquisition.reddit_scraper.reddit_api import fetch_reddit_posts

def get_top_posts(subreddit, limit=5):
    """
    Example function that fetches top posts from a subreddit
    and processes them in some way.
    """
    posts = fetch_reddit_posts(subreddit, limit)
    # Additional processing can go here
    return posts
