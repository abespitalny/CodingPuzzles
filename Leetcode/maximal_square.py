'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
'''
from leetcode import *

class Solution:
    # Bottom-up DP approach.
    # Time: O(m*n)
    # Space: O(m*n)
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0]*n for i in range(m)]
        # Populate first row
        for i in range(n):
            dp[0][i] = int(matrix[0][i])

        # Populate first column
        for i in range(m):
            dp[i][0] = int(matrix[i][0])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "0":
                    continue

                minSquare = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

                if minSquare == 0:
                    dp[i][j] = 1
                    continue
                
                side = int(math.sqrt(minSquare)) + 1
                dp[i][j] = side*side
        
        maxSquare = 0
        for i in range(m):
            for j in range(n):
                maxSquare = max(maxSquare, dp[i][j])

        return maxSquare

    # A cleaner version of the above solution with the same time and space complexity as the above solution but done in a single pass.
    # We could optimize this further by only keeping one row at a time which gives a space complexity of O(n).
    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0]*(n + 1) for i in range(m + 1)]
        maxSide = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "0":
                    continue

                minSide = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                
                side = minSide + 1
                dp[i][j] = side
                maxSide = max(maxSide, side)

        return maxSide*maxSide


solution = Solution()

assert solution.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 4
assert solution.maximalSquare2([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 4

assert solution.maximalSquare([["0","1"],["1","0"]]) == 1
assert solution.maximalSquare2([["0","1"],["1","0"]]) == 1

assert solution.maximalSquare([["0"]]) == 0
assert solution.maximalSquare2([["0"]]) == 0
