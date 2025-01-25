"""
idea_generator.py
-----------------
Interfaces with AI models (OpenAI, Cohere, etc.) to generate innovative ideas.
"""

import os
import openai
from idea_generation.prompts import generate_prompt_for_ideas

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ideas(pain_points):
    """
    Uses OpenAI's API to generate solutions for given pain points.
    """
    prompt = generate_prompt_for_ideas(pain_points)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return response["choices"][0]["text"].strip()
