'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount.
If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.
'''
from leetcode import *

class Solution:
    # Bottom-up DP approach
    # Time: O(n*m^2) where n is the amount and m is the number of coins
    # Space: O(n*m)
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [{} for _ in range(amount + 1)]
        dpTot = [0]*(amount + 1)

        dp[0][0] = 1
        dpTot[0] = 1

        for i in range(1, amount + 1):
            totalNumWays = 0
            for coin in coins:
                change = i - coin

                if change >= 0:
                    numWays = 0

                    if change <= coin:
                        numWays = dpTot[change]
                    else:
                        for k in dp[change]:
                            if k <= coin:
                                numWays += dp[change][k]

                    dp[i][coin] = numWays
                    totalNumWays += numWays

            dpTot[i] = totalNumWays

        return dpTot[-1]

    # A much better DP approach
    # Time: O(n*m)
    # Space: O(n)
    def change2(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount + 1)

        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                change = i - coin
                if change >= 0:
                    dp[i] += dp[change]

        return dp[-1]


solution = Solution()

assert solution.change(amount = 5, coins = [1,2,5]) == 4
assert solution.change2(amount = 5, coins = [1,2,5]) == 4

assert solution.change(amount = 3, coins = [2]) == 0
assert solution.change2(amount = 3, coins = [2]) == 0

assert solution.change(amount = 10, coins = [10]) == 1
assert solution.change2(amount = 10, coins = [10]) == 1
