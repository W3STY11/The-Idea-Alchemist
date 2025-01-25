"""
web_scraping_example.py
------------------------
Demonstrates how to scrape a website.
"""

from data_acquisition.web_scraper.general_scraper import scrape_website

if __name__ == "__main__":
    content = scrape_website("https://example.com")
    print("Website Content:", content[:200], "...")
