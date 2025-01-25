"""
feedback_analysis.py
--------------------
Analyzes user feedback from surveys or prototype testing.
"""

def analyze_feedback(feedback_list):
    """
    Simple placeholder for analyzing feedback text or scores.
    """
    positive_count = sum("good" in feedback.lower() for feedback in feedback_list)
    negative_count = len(feedback_list) - positive_count
    return {"positive": positive_count, "negative": negative_count}
