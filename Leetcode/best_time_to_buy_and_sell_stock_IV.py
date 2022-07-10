'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''
from leetcode import *

class Solution:
    # Bottom-up DP approach
    # Time: O(n*k)
    # Space: O(n)
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        dp = [(0, -prices[0])]
        for i in range(1, n):
            dp.append((0, max(dp[i - 1][1], -prices[i])))

        for i in range(1, k + 1):
            nextDp = [dp[0]]
            for j in range(1, n):
                profit = max(nextDp[j - 1][0], dp[j - 1][1] + prices[j])
                balance = max(nextDp[j - 1][1], nextDp[j - 1][0] - prices[j])
                nextDp.append((profit, balance))
            dp = nextDp
        return dp[-1][0]

    # From Leetcode, a beautiful solution with an alternative recurrence relation that doesn't use the idea of balances:
    # The recurrence relation:
    # dp(i, transactionsRemaining, holding) = max(doNothing, sellStock) if holding == 1 otherwise max(doNothing, buyStock)
    #
    # Where:
    # doNothing = dp(i + 1, transactionsRemaining, holding),
    # sellStock = prices[i] + dp(i + 1, transactionsRemaining - 1, 0), and
    # buyStock = -prices[i] + dp(i + 1, transactionsRemaining, 1).


solution = Solution()

assert solution.maxProfit(k = 2, prices = [2,4,1]) == 2
assert solution.maxProfit(k = 2, prices = [3,2,6,5,0,3]) == 7
