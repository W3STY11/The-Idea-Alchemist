"""
orchestrator.py
---------------
Main script to orchestrate the entire pipeline.
"""

from data_acquisition.reddit_scraper.reddit_api import fetch_reddit_posts
from data_processing.text_cleaning import tokenize_and_remove_stopwords
from data_processing.topic_modeling import perform_lda
from data_processing.sentiment_analysis import analyze_sentiment
from idea_generation.idea_generator import generate_ideas

def run_pipeline():
    # 1. Data Acquisition
    raw_posts = fetch_reddit_posts("AskReddit", 10)

    # 2. Data Processing
    cleaned_texts = []
    for post in raw_posts:
        tokens = tokenize_and_remove_stopwords(post.title)
        cleaned_texts.append(tokens)

    # 3. Topic Modeling
    lda_model = perform_lda(cleaned_texts, num_topics=3)
    print("LDA Model Topics:", lda_model.print_topics())

    # 4. Sentiment Analysis
    if raw_posts:
        sentiment = analyze_sentiment(raw_posts[0].title)
        print("Sample Sentiment:", sentiment)

    # 5. Idea Generation
    # Convert tokens back to text
    pain_points = [" ".join(tokens) for tokens in cleaned_texts]
    ideas = generate_ideas(pain_points)
    print("AI-Generated Ideas:\n", ideas)

if __name__ == "__main__":
    run_pipeline()
