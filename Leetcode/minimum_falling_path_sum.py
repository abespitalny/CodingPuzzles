'''
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right.
Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
'''
from leetcode import *

class Solution:
    # Bottom-up DP
    # Time: O(n^2)
    # Space: O(1) because we reuse the original matrix.
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(1, m):
            for j in range(n):
                minVal = matrix[i - 1][j]
                if (j - 1) >= 0:
                    minVal = min(minVal, matrix[i - 1][j - 1])
                if (j + 1) < n:
                    minVal = min(minVal, matrix[i - 1][j + 1])

                matrix[i][j] += minVal

        return min(matrix[-1])

solution = Solution()

assert solution.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]) == 13
assert solution.minFallingPathSum([[-19,57],[-40,-5]]) == -59
