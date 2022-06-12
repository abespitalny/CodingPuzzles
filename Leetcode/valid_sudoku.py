from leetcode import *

class Solution:
    # Time: O(n^2) where n is 9 in this case.
    # Space: O(n)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            colSet = set()
            rowSet = set()

            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in rowSet:
                        return False
                    rowSet.add(board[i][j])

                if board[j][i] != '.':
                    if board[j][i] in colSet:
                        return False
                    colSet.add(board[j][i])

        for i in range(3):
            for j in range(3):
                subgrid = set()
                for k in range(3):
                    for m in range(3):
                        cell = board[k + 3*i][m + 3*j]
                        if cell != '.':
                            if cell in subgrid:
                                return False
                            subgrid.add(cell)
        return True

solution = Solution()

# Expected: True
print(solution.isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
))

# Expected: False
print(solution.isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
))
