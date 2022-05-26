'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''
from leetcode import *

class Solution:
    # Bottom-up dynamic programming approach
    # Time: O(m*n) where m is the number of coins and n is the amount.
    # Space: O(n) to store the dp array.
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0

        dp = [0]*(amount + 1)
        for i in range(1, amount + 1):
            minNumCoins = math.inf
            for j in coins:
                change = i - j
                if change < 0 or dp[change] < 0:
                    continue
                minNumCoins = min(minNumCoins, dp[change] + 1)
            
            if minNumCoins == math.inf:
                dp[i] = -1
            else:
                dp[i] = minNumCoins

        return dp[-1]

solution = Solution()

# Expected: 3
print(solution.coinChange(coins = [1,2,5], amount = 11))

# Expected: -1
print(solution.coinChange(coins = [2], amount = 3))

# Expected: 0
print(solution.coinChange(coins = [1], amount = 0))
