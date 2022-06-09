'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
'''
from leetcode import *

class Solution:
    # Backtracking approach
    # Time: O(n!)
    # Analysis from Leetcode: We have n options for the first queen, n-2 options for the next one, and n-4 for the third one, and so on.
    # This is upper bounded by n!. We do perform n^2 for each solutions but n! dominates.
    # Space: O(n^2) if we ignore the space needed for output. The recursion stack is a depth of at most n, so the only space needed is to store the board.
    # Leetcode optimized the runtime by performing the canPlaceQueen check in O(1) time.
    # Basically, we can keep a set for the columns, diagonals, and anti-diagonals
    # and check if col in columns or (row - col) in diagonals or (row + col) in anti-diagonals.
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def canPlaceQueen(row, col, board):
            # Check column above
            i = row - 1
            while i >= 0:
                if board[i][col]:
                    return False
                i -= 1
            
            # Check "hill" diagonal
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j]:
                    return False
                i -= 1
                j -= 1

            # Check "dale" diagonal
            i = row - 1
            j = col + 1
            while i >= 0 and j < len(board[0]):
                if board[i][j]:
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(row, board):
            if row == n:
                boardStr = [''.join(['Q' if board[i][j] else '.' for j in range(len(board[0]))]) for i in range(len(board))]
                ans.append(boardStr)
                return

            for i in range(len(board[0])):
                # Check if we can place a queen at this square.
                if canPlaceQueen(row, i, board):
                    board[row][i] = 1
                    backtrack(row + 1, board)
                    # Remove queen and try next square
                    board[row][i] = 0
            return

        backtrack(0, [[0]*n for i in range(n)])
        return ans

solution = Solution()

# Expected: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
print(solution.solveNQueens(4))

# Expected: [["Q"]]
print(solution.solveNQueens(1))
