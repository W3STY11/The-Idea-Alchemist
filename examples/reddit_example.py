"""
reddit_example.py
-----------------
Demonstrates how to fetch and process Reddit data.
"""

from data_acquisition.reddit_scraper.reddit_api import fetch_reddit_posts
from data_processing.text_cleaning import tokenize_and_remove_stopwords

if __name__ == "__main__":
    posts = fetch_reddit_posts("AskReddit", limit=5)
    for post in posts:
        tokens = tokenize_and_remove_stopwords(post.title)
        print("Cleaned Post Title:", tokens)
