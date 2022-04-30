'''
Given an integer n, return the least number of perfect square numbers that sum to n.
'''
from leetcode import *

# NOTE: There's a brilliant mathematical solution with O(n^1/2) time and O(1) space on leetcode.
class Solution:
    # Bottom-up DP solution.
    # Time: O(n^(3/2))
    # Space: O(n)
    def numSquares(self, n: int) -> int:
        dp = [0]*n
        perfectSquares = [1]
        while perfectSquares[-1] <= n:
            dp[perfectSquares[-1] - 1] = 1
            nextSquare = len(perfectSquares) + 1
            perfectSquares.append(nextSquare * nextSquare)

        # n is a perfect square
        if dp[n - 1] == 1:
            return 1

        for i in range(2, n+1):
            if dp[i - 1] == 1:
                continue

            minSquares = math.inf
            squareIdx = 0
            while perfectSquares[squareIdx] < i:
                numSquares = dp[i - perfectSquares[squareIdx] - 1] + 1
                if numSquares < minSquares:
                    minSquares = numSquares
                squareIdx += 1
            dp[i - 1] = minSquares
        return dp[n - 1]

solution = Solution()

# Expected: 3
print(solution.numSquares(12))

# Expected: 2
print(solution.numSquares(13))
