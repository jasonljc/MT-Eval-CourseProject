import unittest
import meteor_evaluator

class meteorEvaluatorTest(unittest.TestCase):
    def test_get_chunk_num(self):
        h = ['A', 'compete', 'approach', 'Meteor']
        ref1 = ['A', 'competing', 'approach', 'Meteor']
        ref2 = ['A', 'competing', 'approach', 'as', 'Meteor']
        ref3 = ['A', 'competing', 'approach', 'A', 'compete', 'Meteor']
        self.assertEqual(meteor_evaluator.get_chunk_num(h, ref1), 2)
        self.assertEqual(meteor_evaluator.get_chunk_num(h, ref2), 3)
        self.assertEqual(meteor_evaluator.get_chunk_num(h, ref3), 3)
        
    def test_word_matches(self):
        h = set(['A', 'compete', 'approach', 'Meteor'])
        ref1 = set(['A', 'compete', 'method', 'Meteor'])
        ref2 = set(['A', 'compete', 'approach', 'an', 'Meteor'])
        ref3 = set(['A', 'competing', 'approach', 'A', 'compete', 'Meteor'])
        self.assertEqual(meteor_evaluator.word_matches(h, ref1), 4)
        self.assertEqual(meteor_evaluator.word_matches(h, ref2), 5)
        self.assertEqual(meteor_evaluator.word_matches(h, ref3), 5)

if __name__ == '__main__':
    unittest.main()