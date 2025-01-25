"""
prompts.py
----------
Holds sample prompts or prompt-building utilities for LLMs.
"""

def generate_prompt_for_ideas(pain_points):
    """
    Creates a prompt string to feed into an AI model based on a list of pain points.
    """
    prompt_header = "You are an expert problem-solver. Consider the following user pain points:\n"
    points_str = "\n".join(f"- {p}" for p in pain_points)
    return f"{prompt_header}{points_str}\nSuggest innovative solutions for these problems."
