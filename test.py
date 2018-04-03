
import unittest
from puzzle import PuzzleSolver
class PuzzleUnitTest(unittest.TestCase):
    def setUp(self):
        self.input = ["CATAPULT","XZTTOYOO","YOTOXTXX" ]
        self.output = 22
        self.puzzle = PuzzleSolver(self.input)

    def test_find_words(self):
        self.assertEqual(len(self.puzzle.find_words()), self.output,
                         'Wrong output')

if __name__ == '__main__':
    unittest.main()