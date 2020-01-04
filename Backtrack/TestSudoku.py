from Backtrack import Backtrack

class TestSudoku(Backtrack):
    def __init__(self):
        # Empty board 9x9
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def set(self, candidate, find, *args, **kwargs):
        """Updates the state"""
        row, col = find
        self.board[row][col] = candidate

    def reset(self, find, *args, **kwargs):
        """Resets the state"""
        row, col = find
        self.board[row][col] = 0

    def next(self, *args, **kwargs):
        """Returns the next item"""
        empty = [(i, j) for i in range(9) for j in range(9) if self.board[i][j] == 0]
        # This tuple is used to set and reset cells
        if len(empty) > 0:
            return empty[0]
        return None

    def candidates(self, find, *args, **kwargs):
        """Returns the list of candidates"""
        # candidates are values in [1, ..., 9]
        # to find different solutions, use random.shuffle(range(1, 10))
        return range(1, 10)

    def valid(self, candidate, find, *args, **kwargs):
        """Returns True if the actual state is valid"""
        # Check all row are valid, i.e. all non-zero cell are unique
        for i in range(9):
            row = [self.board[i][j] for j in range(9) if self.board[i][j] != 0]
            if len(row) != len(set(row)):
                return False
        # Check all col are valid, i.e. all non-zero cell are unique
        for j in range(9):
            col = [self.board[i][j] for i in range(9) if self.board[i][j] != 0]
            if len(col) != len(set(col)):
                return False
        # Check all block are valid, i.e. all non-zero cell are unique
        for block_x in range(3):
            for block_y in range(3):
                block = [self.board[i][j]
                    for i in range(9) for j in range(9)
                    if i//3 == block_x and j//3 == block_y
                    and self.board[i][j] != 0]
                if len(block) != len(set(block)):
                    return False
        return True

    def solved(self, *args, **kwargs):
        """Returns True when problem is solved"""
        # Is solved if it's valid and there are only non-zero values
        return self.valid(None, None, *args, **kwargs) and len([self.board[i][j] for i in range(9) for j in range(9) if self.board[i][j] != 0]) == 81

    def print_board(self):
        for i, row in enumerate(test_sudoku.board):
            for j, col in enumerate(row):
                print(" "+str(test_sudoku.board[i][j])+" ", end="")
            print("")

if __name__ == '__main__':
    test_sudoku = TestSudoku()
    print("Solving...", end = "\r")
    assert test_sudoku.solve()
    test_sudoku.print_board()
