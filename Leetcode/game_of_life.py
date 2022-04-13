'''
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:
    - Any live cell with fewer than two live neighbors dies as if caused by under-population.
    - Any live cell with two or three live neighbors lives on to the next generation.
    - Any live cell with more than three live neighbors dies, as if by over-population.
    - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
Given the current state of the m x n grid board, return the next state.
'''
from leetcode import *

# Time: O(n^2).
# Space: O(1).
# If the board were infinite, then we would only store the live cells.
# Also, if the board is too big to fit in memory, then we can read 3 lines at a time to obtain the value in each cell.
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                alive = 0
                for k, l in neighbors:
                    k += i
                    l += j
                    if (k >= 0 and k < len(board)) and (l >= 0 and l < len(board[0])) and board[k][l] % 2 == 1:
                        alive += 1
                
                if alive < 2 and board[i][j] == 1:
                    board[i][j] = 3
                elif alive > 3 and board[i][j] == 1:
                    board[i][j] = 3
                elif alive == 3 and board[i][j] == 0:
                    board[i][j] = 2
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0

        return

solution = Solution()

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
solution.gameOfLife(board)
# Expected: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
print(board)

board = [[1,1],[1,0]]
solution.gameOfLife(board)
# Expected: [[1,1],[1,1]]
print(board)
