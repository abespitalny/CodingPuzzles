# There's a very nice solution that requires O(1) time for each move and O(n) space. Basically increment number in rows, cols, diagonal, anti-diagonal
# when one player moves and decrement when the other player moves. If the number is n or -n in either row, column, diagonal, or anti-diagonal, then we
# know we've got a winner.

class TicTacToe:
    # Brute force approach
    # Time: O(n^2)
    # Space: O(n^2)
    def __init__(self, n: int):
        self.board = [[0]*n for i in range(n)]

    # Time: O(n)
    # Space: O(1)
    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        n = len(self.board)
        
        # Check row
        count = 0
        for i in range(n):
            if self.board[row][i] != player:
                break
            count += 1

        if count == n:
            return player
        
        # Check column
        count = 0
        for i in range(n):
            if self.board[i][col] != player:
                break
            count += 1

        if count == n:
            return player

        # Check forward diagonal 
        if row == col:
            count = 0
            for i in range(n):
                if self.board[i][i] != player:
                    break
                count += 1

            if count == n:
                return player
        
        # Check backward diagonal
        if (row + col) == (n - 1):
            count = 0
            for i in range(n):
                if self.board[i][n - i - 1] != player:
                    break
                count += 1

            if count == n:
                return player

        return 0

ticTacToe = TicTacToe(3)

# Expected: 0
print(ticTacToe.move(0, 0, 1))
# Expected: 0
print(ticTacToe.move(0, 2, 2))
# Expected: 0
print(ticTacToe.move(2, 2, 1))
# Expected: 0
print(ticTacToe.move(1, 1, 2))
# Expected: 0
print(ticTacToe.move(2, 0, 1))
# Expected: 0
print(ticTacToe.move(1, 0, 2))
# Expected: 1
print(ticTacToe.move(2, 1, 1))
