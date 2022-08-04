'''
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

Given an integer n, return the number of ways to tile an 2 x n board.

Since the answer may be very large, return it modulo 10^9 + 7.

In a tiling, every square must be covered by a tile.
Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.
'''

class Solution:
    # Bottom-up DP
    # Time: O(n^2)
    # Space: O(n)
    def numTilings(self, n: int) -> int:
        MOD = (10**9 + 7)
        dp = [0]*(n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            ways = 0
            
            if i - 1 >= 0:
                ways = (ways + dp[i - 1]) % MOD

            if i - 2 >= 0:
                ways = (ways + dp[i - 2]) % MOD

            j = i - 3
            while j >= 0:
                ways = (ways + 2*dp[j]) % MOD
                j -= 2
            
            j = i - 4
            while j >= 0:
                ways = (ways + 2*dp[j]) % MOD
                j -= 2
            
            dp[i] = ways

        return dp[-1]

    # Above approach is inefficient because I got the recurrence relation wrong.
    # The correct recurrence relation:
    # Fully tiled: f(n) = f(n - 1) + f(n - 2) + 2*p(n - 1)
    # Partially tiled: p(n) = p(n - 1) + f(n - 2)
    #
    # Base cases:
    # f(1) = 1, f(2) = 2, p(2) = 1
    #
    # Bottom-up DP
    # Time: O(n)
    # Space: O(n). Can easily optimize space to make it O(1).
    def numTilings2(self, n: int) -> int:
        if n < 3:
            return n

        MOD = (10**9 + 7)
        f = [0] * (n + 1)
        p = [0] * (n + 1)
        
        # Base cases
        f[1] = 1
        f[2] = 2
        p[2] = 1

        for k in range(3, n + 1):
            f[k] = (f[k - 1] + f[k - 2] + 2 * p[k - 1]) % MOD
            p[k] = (p[k - 1] + f[k - 2]) % MOD
        return f[n]

solution = Solution()

assert solution.numTilings(3) == 5
assert solution.numTilings2(3) == 5

assert solution.numTilings(1) == 1
assert solution.numTilings2(1) == 1
