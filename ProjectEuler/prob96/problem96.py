import re
import numpy as np
import pandas as pd

class SudokuBoard:
    '''
    This constructor takes a string of a 9x9 grid of numbers (0 represents a blank).
    ** NOTE ** I am assuming the board provided by the user has a unique solution
    '''
    def __init__(self, grid=None):
        if grid is None:
            self.board = None
            self.possible = None
            return

        # create a data structure to efficiently operate on
        grid = grid.strip().split('\n')
        if len(grid) != 9 or any([len(r) != 9 for r in grid]):
            raise ValueError("Grid input is of an inproper size.")

        board_dict = {j: [] for j in range(9)}
        initial_moves = []
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                v = int(v)
                if v < 0 or v > 9:
                    raise ValueError("Grid entry is invalid.")
                board_dict[j].append(v)
                if v != 0:
                    initial_moves.append((j, i, v-1))

        self.board = pd.DataFrame(board_dict, dtype=np.uint8)
        if not(self.validate()):
            raise ValueError("Not a valid Sudoku board.")

        # all the possible numbers that can be placed in each cell
        self.possible = pd.DataFrame({j: [np.ones(9, dtype=np.uint8) for i in range(9)] for j in range(9)})
        # eliminate using the initially supplied values
        self.eliminate(initial_moves)

    # assuming that the board provided by the user
    def validate(self):
        # check that for each row, column, and subgrid, it contains exactly
        # the numbers 1 through 9 allowing for missing entries
        count = np.zeros(9, dtype=np.uint8)
        for i in range(9):
            for j in range(3):
                # column
                if j == 0:
                    num_set = self.board[i]
                # row
                elif j == 1:
                    num_set = self.board.iloc[i]
                # subgrid
                else:
                    # it's a little faster if you flatten the array according to how its stored in memory
                    num_set = self.subgrid(i).values.flatten(order='K')
 
                for n in num_set:
                    # ignore if the entry is a blank
                    if n == 0:
                        continue
                    c = count[n-1]
                    # if there is a duplicate use of a number in the num_set then return False
                    if c == 1:
                        return False
                    count[n-1] = c + 1
                # reset the count array
                count[:] = 0
        return True

    # n ranges from [0, 9) and corresponds to the subgrids in row-major order
    # possibilities is a boolean to determine whether to get the values or the possibilities for the cells
    def subgrid(self, n, possibilities=False):
        i = 3 * (n // 3)
        j = 3 * (n % 3)
        return self.possible.iloc[i:(i+3), j:(j+3)] if possibilities else self.board.iloc[i:(i+3), j:(j+3)]

    # the subgrid that contains this cell (i, j)
    def containing_subgrid(self, i, j, possibilities=False):
        i = 3 * (i // 3)
        j = 3 * (j // 3)
        return self.possible.iloc[i:(i+3), j:(j+3)] if possibilities else self.board.iloc[i:(i+3), j:(j+3)]

    # Use the new cells to start eliminating possibilities. Cells are in the form of:
    # (col_ind, row_ind, value)
    # note: value ranges from [0, 9)
    def eliminate(self, cells):
        # iterate through each new cell and use it to eliminate possibilities
        for (j, i, v) in cells:
            self.possible[j][i] = None
            # eliminate any possibilities that occur in the row, column, or subgrid
            for c, r, g in zip(self.possible[j], self.possible.iloc[i], self.containing_subgrid(i, j, True).values.flatten(order='K')):
                for p in (c, r, g):
                    # if the cell has no possibilities left or the possibility is already eliminated then ignore this cell
                    if (p is None) or (p[v] == 0):
                        continue
                    # eliminate the possibility
                    p[v] = 0

    # tries to make as many moves as possible before eliminating possibilities and trying again
    def move(self):
        # for each column, row, and subgrid check for any cell that contains a number where it's the only possibility
        moves = []
        for n in range(9):
            # sum up the possibilities for each row, column, and subgrid and check if the sum equals the 1
            # for one of the entries because that means the value only occurs once
            for t, sigmas in enumerate((self.possible[n].sum(), self.possible.iloc[n].sum(), pd.Series(self.subgrid(n, True).values.flatten(order='K')).sum())):
                # the entire column/row/subgrid is already filled then the sum is not an array
                if isinstance(sigmas, np.ndarray):
                    for i, s in enumerate(sigmas):
                        # this value only occurs once in the column, row, or subgrid so add it to the array of moves
                        if s == 1:
                            # t, denoting whether it's a column, row, or subgrid
                            # n, denoting which specific column/row/subgrid
                            moves.append((t, n, i))

        cells = len(moves) * [0]
        # now we actually perform the moves and remember its location and value so we can use it in the eliminate method
        for m_i, (t, n, v) in enumerate(moves):
            # column
            if t == 0:
                poss_set = self.possible[n]
            # row
            elif t == 1:
                poss_set = self.possible.iloc[n]
            # subgrid
            else:
                poss_set = self.subgrid(n, True).values.flatten(order='C')

            for i, p in enumerate(poss_set):
                # ignore if the cell is already filled
                if p is None:
                    continue
                # this is the cell that contains the possibility
                if p[v] == 1:
                    # get the index of the cell
                    c_i = i if t == 0 else n if t == 1 else ((3 * (n // 3)) + (i // 3))
                    c_j = n if t == 0 else i if t == 1 else ((3 * (n % 3)) + (i % 3))
                    # set the value of the cell
                    self.board[c_j][c_i] = v+1
                    cells[m_i] = (c_j, c_i, v)
        # return the cells that were used in this move
        return cells

    # checks if there is still blank cells
    def is_game_not_over(self):
        return (self.board == 0).any(axis=None)

    # determines if there is a contradiction in the board, that is, if there is a blank cell with no possibilities
    def contradiction(self):
        return ((self.possible.applymap(np.count_nonzero) == 0) & (self.board == 0)).any(axis=None)

    # returns a deep copy of the board
    def deepcopy(self):
        copy = SudokuBoard()
        copy.board = self.board.copy(deep=True)
        copy.possible = self.possible.applymap(np.copy)
        return copy

    # returns the (j, i) coordinate of the cell with the min number of possibilities
    def get_min_poss_cell(self):
        poss_count = self.possible.applymap(np.count_nonzero)
        # the upper bound on the number of possibilities is 10, exclusive
        min_poss = 10
        cell = None
        for j in range(9):
            for i in range(9):
                c = poss_count[j][i]
                if (c != 0) and (c < min_poss):
                    min_poss = c
                    cell = (j, i)
        return cell

    @staticmethod
    def solve(board):
        while board.is_game_not_over():
            # make a move by filling in as much numbers as you can and get the filled-in cells
            cells = board.move()
            # could not make a move then we must guess
            if len(cells) == 0:
                # get the cell with the least number of possibilities
                j, i = board.get_min_poss_cell()
                # iterate through the possibilities
                for p_i, p in enumerate(board.possible[j][i]):
                    if p == 1:
                        board_copy = board.deepcopy()
                        board_copy.board[j][i] = p_i + 1
                        board_copy.eliminate([(j, i, p_i)])
                        board_copy = SudokuBoard.solve(board_copy)
                        if board_copy is not None:
                            return board_copy
                # all guesses lead to a dead end
                return None
            # use the filled-in cells to eliminate possibilities
            # note: a guess is treated like a move
            board.eliminate(cells)
            # this means that the guess was wrong
            if board.contradiction():
                return None
        return board

    def __str__(self):
        board_str = ''
        for i in range(9):
            if i != 0 and i % 3 == 0:
                board_str += (11 * '-') + '\n'
            for j in range(9):
                board_str += ('|' if ((j != 0) and (j % 3 == 0)) else '') + str(self.board[j][i])
            board_str += '\n'
        return board_str

def main():
    boards = []
    not_digit_regex = re.compile(r"[^\d]")
    # read in the file of grids
    with open("./sudoku.txt") as f:
        k = 0
        grid = ''
        for line in f:
            if not_digit_regex.search(line.strip()) is not None:
                continue
            grid += line
            k += 1
            if k == 9:
                boards.append(grid)
                grid = ''
                k = 0

    euler_ans = 0
    for b in boards:
        b = SudokuBoard(b)
        b = SudokuBoard.solve(b).board
        euler_ans += (100 * b[0][0]) + (10 * b[1][0]) + b[2][0]
    print("Euler's answer:", euler_ans)

if __name__ == "__main__":
    main()
