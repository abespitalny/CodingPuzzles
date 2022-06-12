from leetcode import *

class Solution:
    # Time: O((n!)^n) so here it's (9!)^9 because if we choose a number for the first cell in the row then we have 8 possibilities for the second cell
    # in the row, and so on, and that's true for all rows. Therefore, (n!)^n. This is a much smaller search space than all possible configurations.
    # Space: O(n^2) because of the recursion stack.
    #
    # From Leetcode, we could have sped things up by storing the used digits for rows, columns, and subgrids which would have added O(n^2) space
    # but meant an O(1) runtime to check if a digit is a valid candidate.
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = len(board)

        def backtrack():
            for i in range(n):
                for j in range(n):
                    if board[i][j] == '.':
                        rowDigits = 0
                        colDigits = 0
                        subgridDigits = 0

                        subgridIdx = (3*(i // 3), 3*(j // 3))
                        for k in range(n):
                            if board[i][k] != '.':
                                rowDigits = rowDigits | (1 << (int(board[i][k]) - 1))
                            if board[k][j] != '.':
                                colDigits = colDigits | (1 << (int(board[k][j]) - 1))

                            subgridCell = board[(k // 3) + subgridIdx[0]][(k % 3) + subgridIdx[1]]
                            if subgridCell != '.':
                                subgridDigits = subgridDigits | (1 << (int(subgridCell) - 1))

                        for k in range(n):
                            mask = (1 << k)
                            if (rowDigits | colDigits | subgridDigits) & mask == 0:
                                board[i][j] = str(k + 1)
                                if backtrack():
                                    return True

                        board[i][j] = '.'
                        return False
            return True

        backtrack()

solution = Solution()

board = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

solution.solveSudoku(board)

# Expected:
# [["5","3","4","6","7","8","9","1","2"],
# ["6","7","2","1","9","5","3","4","8"],
# ["1","9","8","3","4","2","5","6","7"],
# ["8","5","9","7","6","1","4","2","3"],
# ["4","2","6","8","5","3","7","9","1"],
# ["7","1","3","9","2","4","8","5","6"],
# ["9","6","1","5","3","7","2","8","4"],
# ["2","8","7","4","1","9","6","3","5"],
# ["3","4","5","2","8","6","1","7","9"]]
print(board)
