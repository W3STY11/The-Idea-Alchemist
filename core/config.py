"""
config.py
---------
Holds global configuration settings.
"""

import os

# Example configuration
SCRAPER_BATCH_SIZE = int(os.getenv("SCRAPER_BATCH_SIZE", 100))
