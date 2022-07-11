'''
You are painting a fence of n posts with k different colors. You must paint the posts following these rules:
    - Every post must be painted exactly one color.
    - There cannot be three or more consecutive posts with the same color.

Given the two integers n and k, return the number of ways you can paint the fence.
'''

class Solution:
    # Bottom-up DP approach. My recurrence relation is very different from the solution on Leetcode:
    # dp(n, k) = k * (dp(n - 1, k) - [number of ways (n - 1) posts end with the last two posts painted the same color])
    # That last term is: (dp(n - 2, k) // k) - [number of ways (n - 3) posts with the last two posts painted the same color]
    # Time: O(n)
    # Space: O(1)
    def numWays(self, n: int, k: int) -> int:
        dp = [k, 0]
        for i in range(2, n + 1):
            temp = dp[0]
            dp[0] = k*(dp[0] - dp[1])
            dp[1] = (temp // k) - dp[1]
        return dp[0]

    # Same idea, but a better recurrence relation:
    # dp(i) = ((k - 1) * dp(i - 1)) + ((k - 1) * dp(i - 2))
    #       = (k - 1) * (dp(i - 1) + dp(i - 2))
    def numWays2(self, n: int, k: int) -> int:
        if n == 1:
            return k
        elif n == 2:
            return k*k

        dp = [k, k*k]
        for i in range(3, n + 1):
            dp[0], dp[1] = dp[1], (k - 1)*(dp[0] + dp[1])
        return dp[1]


solution = Solution()

assert solution.numWays(3, 2) == 6
assert solution.numWays2(3, 2) == 6
assert solution.numWays(1, 1) == 1
assert solution.numWays2(1, 1) == 1
assert solution.numWays(7, 2) == 42
assert solution.numWays2(7, 2) == 42
