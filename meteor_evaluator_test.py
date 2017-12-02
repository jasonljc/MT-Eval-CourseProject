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

if __name__ == '__main__':
    unittest.main()