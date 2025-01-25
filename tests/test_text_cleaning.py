"""
test_text_cleaning.py
--------------------
Unit tests for text cleaning functionality.
"""

import unittest
from data_processing.text_cleaning import tokenize_and_remove_stopwords

class TestTextCleaning(unittest.TestCase):
    def test_tokenize_and_remove_stopwords(self):
        text = "This is a test sentence"
        tokens = tokenize_and_remove_stopwords(text)
        self.assertIsInstance(tokens, list)
        self.assertNotIn("is", tokens)  # Common stopword should be removed

if __name__ == "__main__":
    unittest.main()
