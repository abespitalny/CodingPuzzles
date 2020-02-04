import sys
import traceback
import numpy as np 

def handle_input(prompt, input_handler, err_msg="Invalid input. Please try again.", exit_on_err=False):
    while True:
        try:
            return input_handler(input(prompt))
        except Exception as e:
            # if no error message is specified then print the stacktrace
            if err_msg is None:
                e.print_exc(file=sys.stderr)
            else:
                print(err_msg, file=sys.stderr)

            if exit_on_err:
                sys.exit(e.errno)

class Board:
    def __init__(self, rows=9, columns=9, mines=10):
        # these defaults if given invalid input is based on http://minesweeperonline.com/
        if rows < 1:
            rows = 1
        if columns < 8:
            columns = 8
        if mines < 0:
            mines = 0
        elif mines >= (rows * columns):
            mines = (rows * columns) - 1

        self.board = np.empty((rows, columns), dtype=int)
        self.mines = mines

        # place all the mines on the board
        mine_locs = np.array(([0] * (self.board.size - mines)) + ([-1] * mines))
        np.random.shuffle(mine_locs)
        # index into the array of mine locations
        k = 0
        for i in range(rows):
            for j in range(columns):
                self.board[i][j] = mine_locs[k]
                k += 1

        # go over the board and calculate the number of neighboring bombs for each cell
        for i in range(rows):
            for j in range(columns):
                # add 1 to all the non-mine neighbors of a mine
                if self.board[i][j] == -1:
                    neighbors = self._get_neighbors(i, j)
                    for n_i, n_j in neighbors:
                        cell = self.board[n_i][n_j]
                        # ignore the cells that are mines
                        if cell == -1:
                            continue
                        self.board[n_i][n_j] = cell + 1

        # boolean for each cell indicating if it's revealed or not
        self.revealed = np.zeros((rows, columns), dtype=bool)
        # boolean for each cell indicating if it has been flagged or not
        self.flagged = np.zeros((rows, columns), dtype=bool)
        # is the game over
        self.game_over = False
        self.win = False

    def _get_neighbors(self, r, c):
        rows, columns = self.board.shape

        left = -1
        if (left + c) < 0:
            left = 0
        right = 1
        if (right + c) >= columns:
            right = 0

        up = -1
        if (up + r) < 0:
            up = 0
        down = 1
        if (down + r) >= rows:
            down = 0

        neighbors = [0] * (((down - up + 1) * (right - left + 1)) - 1)
        k = 0
        for i in range(up, down+1):
            for j in range(left, right+1):
                if i == 0 and j == 0:
                    continue
                neighbors[k] = (i + r, j + c)
                k += 1
        return neighbors

    def _reveal_cells(self, r, c):
        if self.revealed[r][c]:
            return

        self.revealed[r][c] = True
        if self.board[r][c] > 0:
            return
        # if this cell does not border any bombs than reveal all of its neighbors recursively
        for n_i, n_j in self._get_neighbors(r, c):
            self._reveal_cells(n_i, n_j)

    def move(self, flag, r, c):
        r -= 1
        c -= 1
        # there is no move to make
        if self.revealed[r][c] or (not(flag) and self.flagged[r][c]):
            return False

        if flag:
            # toggle flag on cell
            self.flagged[r][c] = not(self.flagged[r][c])
        else:
            # hit a mine :(
            if self.board[r][c] == -1:
                rows, columns = self.board.shape
                # reveal all the mines that aren't flagged
                for i in range(rows):
                    for j in range(columns):
                        if self.board[i][j] == -1 and not(self.flagged[i][j]):
                            self.revealed[i][j] = True
                self.game_over = True
                self.win = False
            # keep revealing cells recursively until you run into a cell that neighbors a mine
            else:
                self._reveal_cells(r, c)
                # check if there are no unreaveled cells that aren't mines
                unrevealed = ~self.revealed
                if self.mines == -(np.sum(self.board[unrevealed])):
                    # flag all the mines
                    self.flagged[unrevealed] = True
                    self.game_over = True
                    self.win = True
        return True

    def get_shape(self):
        return self.board.shape

    def is_game_over(self):
        return self.game_over

    def won(self):
        return self.win

    def __str__(self):
        rows, columns = self.board.shape
        board_str = ""
        row_cells = [0] * columns
        for i in range(rows):
            for j in range(columns):
                if self.flagged[i][j]:
                    # reveal if the flag is incorrect if the game is over
                    if self.game_over and (self.board[i][j] != -1):
                        row_cells[j] = 'X'
                    else:
                        row_cells[j] = '?'
                elif not(self.revealed[i][j]):
                    row_cells[j] = '#'
                else:
                    cell = self.board[i][j]
                    if cell == -1:
                        row_cells[j] = '*'
                    elif cell == 0:
                        row_cells[j] = '_'
                    else:
                        row_cells[j] = str(cell)
            board_str += ' '.join(row_cells) + '\n'
        return board_str

# I'm using the property of closure here
def move_handler(board):
    def handler(user_in):
        user_in = user_in.split(' ')
        if (len(user_in) > 3) or (len(user_in) < 2):
            raise ValueError

        flag = False
        if len(user_in) == 3:
            if user_in[0].upper() == 'F':
                flag = True
                user_in = user_in[1:]
            else:
                raise ValueError

        r, c = list(map(int, user_in))
        rows, columns = board.get_shape()
        if r < 1 or r > rows or c < 1 or c > columns:
            raise ValueError
        return (flag, r, c)
    return handler

def main():
    print(("1) Beginner\n"
           "2) Medium\n"
           "3) Expert\n"
           "4) Custom"))
    menu_prompt = "Choose a difficulty level or create a custom board by typing its corresponding number: "
    # raise ValueError is not allowed in a lambda function
    menu_input = handle_input(menu_prompt, lambda x: x if len(x) == 1 and x <= '4' and x >= '1' else int(''))

    board = None
    # the sizes and number of mines for each level is taken from http://minesweeperonline.com/
    if menu_input == '1':
        board = Board(9, 9, 10)
    elif menu_input == '2':
        board = Board(16, 16, 40)
    elif menu_input == '3':
        board = Board(16, 30, 99)
    # custom board
    else:
        custom_board = [20, 30, 145]
        custom_board_prompt = "Enter height, width, or number of mines to create a custom board (default values: 20 30 145): "
        custom_vals = handle_input(custom_board_prompt, lambda x: list(map(int, x.split(' '))))
        for i in range(len(custom_vals)):
            custom_board[i] = custom_vals[i]
        board = Board(*custom_board)

    move_prompt = "Enter a row and column to reveal the cell or precede them with a F to flag the cell: "
    h = move_handler(board)
    while True:
        # show board
        print(board)
        if board.is_game_over():
            if board.won():
                print("You won! :)")
            else:
                print("You lost :(")
            break

        while True:
            user_move = handle_input(move_prompt, h)
            if not(board.move(*user_move)):
                continue
            break

if __name__ == "__main__":
    main()
