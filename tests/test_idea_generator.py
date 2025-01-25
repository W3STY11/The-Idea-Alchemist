"""
test_idea_generator.py
---------------------
Unit tests for idea generation functionality.
"""

import unittest
from idea_generation.idea_generator import generate_ideas

class TestIdeaGenerator(unittest.TestCase):
    def test_generate_ideas(self):
        pain_points = ["Test pain point"]
        ideas = generate_ideas(pain_points)
        self.assertIsInstance(ideas, str)
        self.assertTrue(len(ideas) > 0)

if __name__ == "__main__":
    unittest.main()
