"""
general_scraper.py
------------------
Scrapes general websites using Requests and BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """
    Scrape the specified URL and return the raw text.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()
    else:
        return ""
