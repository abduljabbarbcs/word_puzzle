import numpy as np
class PuzzleSolver(object):
    WORDS = ['OX', 'CAT', 'TOY', 'AT', 'DOG',  'CATAPULT', 'T']

    def __init__(self,grid):

        self.grid =grid
        """
            grid dimensions
        """
        self.nrows, self.ncols = len(self.grid), len(self.grid[0])
        self.prefixes = set(word[:i] for word in self.WORDS
                       for i in range(2, len(word) + 1))

    def is_word(self, word):
        """
        Returns true of word is in the dictionary, false otherwise.
        """
        return word in self.WORDS


    def find_words(self):
        """
        Should return the number of all non-distinct  occurrences
        of the words found in puzzle, horizontally, vertically
        or diagonally,  and also the reverse in each direction.
        The input to find_words (i.e. puzzle ) is a rectangular
        matrix of characters (list of strings).
        """
        result =[]
        matrix = np.array([[letter for letter in word] for word in self.grid])
        result += self.get_all_diagonal_words(matrix)
        result += self.get_all_horizontal_words()
        result += self.get_all_veritcal_words(matrix=matrix)
        return result



    def get_all_diagonal_words(self,matrix):
        """
             find words in diagnols
        """
        result=[]
        diags = [matrix[::-1, :].diagonal(i) for i in range(-(self.nrows  - 1), self.ncols )]
        diags.extend(matrix.diagonal(i) for i in range(self.ncols - 1, -self.nrows, -1))
        diagnols = [n.tolist() for n in diags]
        for diagnal in diagnols:
            for str in self.get_all_substrings(''.join(letter for letter in diagnal if len(diagnal) > 1)):
                word = self.get_all_words_in_string(str, 1)
                if word:
                    result.append(word)
        return result

    def get_all_horizontal_words(self):
        """
            return all possible words in grid rows
        """
        result=[]
        for horizontal_word in self.grid:
            for str in self.get_all_substrings(''.join(letter for letter in horizontal_word)):
                word = self.get_all_words_in_string(str)
                if word:
                    result.append(word)
        return result

    def get_all_veritcal_words(self,matrix):
        """
            return all possible words in grid cols
        """
        result=[]
        for col in range(matrix.shape[1]):
            for str in self.get_all_substrings(''.join(letter for letter in matrix[:,col])):
               word=self.get_all_words_in_string(str,1)
               if word:
                   result.append(word)
        return result

    def get_all_words_in_string(self,str,size=0):
        "check valid word "
        if (len(str) > size):
            if self.is_word(str):
                return str
            elif self.is_word(str[::-1]):
                return str[::-1]
        return None

    def get_all_substrings(self,input_string):
        """
            Return all possible substring of input string
        """
        length = len(input_string)
        return [input_string[i:j + 1] for i in range(length) for j in range(i, length)]




if __name__ == '__main__':
    """
        Input grid
    """
    grid = [
        "CATAPULT",
        "XZTTOYOO",
        "YOTOXTXX"
    ]
    """
        Puzzle object creation and intializing grid
    """
    puzzle = PuzzleSolver(grid)
    """
        find words in grid
    """
    words = puzzle.find_words()
    """
        printing output
    """
    print(len(words))
    print("This 8 words are:")
    print(tuple(words))










