__author__ = 'marodrig'

import unittest
from idea_grammar_rules import get_idea_rules

class IdeaGrammarRulesTest(unittest.TestCase):

    def test_rules_creation(self):
        self.assertIsNotNone(get_idea_rules(), "Error in idea rules")

if __name__ == '__main__':
    unittest.main()
