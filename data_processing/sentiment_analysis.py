"""
sentiment_analysis.py
---------------------
Performs sentiment analysis using VADER, TextBlob, or other libraries.
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    """
    Returns VADER sentiment scores for the given text.
    """
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)
