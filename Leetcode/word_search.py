'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''
from leetcode import *

# Time: O(m*n*(3^L)) where the board is m x n and the length of the word is L.
# Space: O(L) where the length of the word is L. The depth of the recursion and the set of points in the path is L.
# A way to improve this solution is to prune edge cases where the word can definitely not be in the board. For example, the board has only 5 A's, but the word has 6 A's.
# This can be achieved with a simple character count in O(m*n + L).
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.searchForWord(0, (i, j), set(), board, word):
                        return True
        return False

    def searchForWord(self, wordPos: int, currentSquare: Tuple[int], path: Set[Tuple[int]], board: List[List[str]], word: str) -> bool:
        nextWordPos = wordPos + 1
        # Found word!
        if nextWordPos == len(word):
            return True

        path.add(currentSquare)

        # Top square
        nextSquare = (currentSquare[0] - 1, currentSquare[1])
        if nextSquare[0] >= 0 and board[nextSquare[0]][nextSquare[1]] == word[nextWordPos] and nextSquare not in path:
            if self.searchForWord(nextWordPos, nextSquare, path.copy(), board, word):
                return True

        # Bottom square
        nextSquare = (currentSquare[0] + 1, currentSquare[1])
        if nextSquare[0] < len(board) and board[nextSquare[0]][nextSquare[1]] == word[nextWordPos] and nextSquare not in path:
            if self.searchForWord(nextWordPos, nextSquare, path.copy(), board, word):
                return True

        # Left square
        nextSquare = (currentSquare[0], currentSquare[1] - 1)
        if nextSquare[1] >= 0 and board[nextSquare[0]][nextSquare[1]] == word[nextWordPos] and nextSquare not in path:
            if self.searchForWord(nextWordPos, nextSquare, path.copy(), board, word):
                return True

        # Right square
        nextSquare = (currentSquare[0], currentSquare[1] + 1)
        if nextSquare[1] < len(board[0]) and board[nextSquare[0]][nextSquare[1]] == word[nextWordPos] and nextSquare not in path:
            if self.searchForWord(nextWordPos, nextSquare, path.copy(), board, word):
                return True

        return False

solution = Solution()

# Expected: True
print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))

# Expected: True
print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))

# Expected: False
print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
