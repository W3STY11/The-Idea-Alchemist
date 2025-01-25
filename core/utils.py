"""
utils.py
--------
Miscellaneous utility functions.
"""

def chunk_list(lst, chunk_size):
    """
    Splits a list into smaller chunks of a specified size.
    """
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]
