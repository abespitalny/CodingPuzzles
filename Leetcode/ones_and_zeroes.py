'''
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
'''
from leetcode import *

class Solution:
    # Bottom-up DP approach.
    # Recurrence relation: dp(i, m, n) = max(dp(i - 1, m, n), dp(i - 1, m - 0s, n - 1s) + 1)
    # Time: O(m*n*k + s) where k is the number of strings and s is the max length of the strings.
    # Space: O(m*n)
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n + 1) for i in range(m + 1)]
        for i in range(len(strs)):
            numZeros = 0
            numOnes = 0
            for j in strs[i]:
                if j == '0':
                    numZeros += 1
                else:
                    numOnes += 1

            for j in range(m, numZeros - 1, -1):
                for k in range(n, numOnes - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - numZeros][k - numOnes] + 1)

        return dp[-1][-1]

solution = Solution()

assert solution.findMaxForm(strs = ["10","0001","111001","1","0"], m = 5, n = 3) == 4
assert solution.findMaxForm(strs = ["10","0","1"], m = 1, n = 1) == 2
