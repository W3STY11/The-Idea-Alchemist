"""
topic_modeling.py
-----------------
Implements LDA or other topic modeling techniques.
"""

from gensim import corpora, models
import logging

def perform_lda(documents, num_topics=5):
    """
    Performs LDA topic modeling on a list of documents.
    """
    logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO)
    dictionary = corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(doc) for doc in documents]
    lda_model = models.LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics
    )
    return lda_model
