"""
youtube_scraper.py
------------------
Scrapes YouTube data using the official YouTube API or third-party tools.
"""

import os
from googleapiclient.discovery import build

def fetch_youtube_comments(video_id, max_results=20):
    """
    Fetch comments from a specific YouTube video.
    """
    api_key = os.getenv("YOUTUBE_API_KEY")
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_results
    )
    response = request.execute()
    return response.get("items", [])
