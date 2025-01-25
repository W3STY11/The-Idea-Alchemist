"""
data_cleaner.py
---------------
Generic data cleaning utilities for scraped data.
"""

import re

def basic_clean(text):
    """
    Removes URLs and unnecessary whitespace from text.
    """
    text_no_urls = re.sub(r"http\S+", "", text)
    text_no_extra_spaces = re.sub(r"\s+", " ", text_no_urls)
    return text_no_extra_spaces.strip()
