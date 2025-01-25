"""
dynamic_scraper.py
------------------
Uses Selenium to scrape JavaScript-heavy sites.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def scrape_dynamic_site(url):
    """
    Scrape a JS-heavy site by rendering in Selenium.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    with webdriver.Chrome(options=chrome_options) as driver:
        driver.get(url)
        content = driver.page_source
    return content
