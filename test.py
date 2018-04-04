import numpy as np
import unittest
from puzzle import PuzzleSolver
class PuzzleUnitTest(unittest.TestCase):
    '''intial setup for each test case'''
    def setUp(self):
        self.input = ["CATAPULT","XZTTOYOO","YOTOXTXX" ]
        self.output = 22
        self.puzzle = PuzzleSolver(self.input)

    '''
        unit test to check word
    '''
    def test_is_word(self):
        self.assertEqual(self.puzzle.is_word('CAT'), True,
                         'Word is not available in dictionary')
    '''
        Check string is a valid word of any size
    '''
    def test_get_all_words_in_string(self):
        self.assertEqual(self.puzzle.get_all_words_in_string('CAT'), 'CAT',
                         'Word is not available in dictionary')
    '''
        Check string is a valid word of size greater than 1
    '''
    def test_get_all_words_in_string_gt_1(self):
        self.assertEqual(self.puzzle.get_all_words_in_string('CAT',1), 'CAT',
                         'Word is not available in dictionary')

    '''
        Check all possible strings
    '''
    def test_get_all_substrings(self):
        self.assertEqual(len(self.puzzle.get_all_substrings('abc')), 6,
                         'total substrings count in invalid')

    '''
            Check all possible words in diagonals
    '''
    def test_get_all_diagonal_words(self):
        matrix = np.array([[letter for letter in word] for word in self.input])
        self.assertEqual(len(self.puzzle.get_all_diagonal_words(matrix)), 5,
                         'Words count in digonal is not correct')

    '''
            Check all possible words in rows
    '''
    def test_get_all_horizontal_words(self):
        self.assertEqual(len(self.puzzle.get_all_horizontal_words()), 13,
                         'Words count in rows is not correct')

    '''
        Check all possible words in columns
    '''

    def test_get_all_veritcal_words(self):
        matrix = np.array([[letter for letter in word] for word in self.input])
        self.assertEqual(len(self.puzzle.get_all_veritcal_words(matrix=matrix)), 4,
                         'Words count in columns is not correct')

    '''
        Check all posible words horizontally, vertically and diagonally.
    '''
    def test_find_words(self):
        self.assertEqual(len(self.puzzle.find_words()), self.output,
                         'Wrong output')

if __name__ == '__main__':
    unittest.main()