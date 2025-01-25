"""
text_cleaning.py
----------------
Contains functions to clean and preprocess text data further.
"""

import nltk
from data_acquisition.utils.data_cleaner import basic_clean

nltk.download("stopwords")
stopwords = set(nltk.corpus.stopwords.words("english"))

def tokenize_and_remove_stopwords(text):
    """
    Tokenizes text and removes stopwords.
    """
    tokens = nltk.word_tokenize(text)
    return [t for t in tokens if t.lower() not in stopwords]
