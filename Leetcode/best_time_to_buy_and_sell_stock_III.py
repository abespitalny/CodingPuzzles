'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''
from leetcode import *

class Solution:
    # Special case of part IV.
    # DP approach from Leetcode has same runtime and space complexity as this one, but it optimizes an O(n^2) divide and conquer algorithm instead.
    # Time: O(n)
    # Space: O(n)
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        k = 2
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

    # Very brilliant solution from Leetcode. Simulation / state machine approach
    # Time: O(n)
    # Space: O(1)
    def maxProfit2(self, prices: List[int]) -> int:
        transaction1 = [0, -prices[0]]
        transaction2 = [0, -math.inf]
        for i in range(1, len(prices)):
            prevTransaction1Profit = transaction1[0]
            transaction1[0] = max(transaction1[0], prices[i] + transaction1[1])
            transaction1[1] = max(transaction1[1], -prices[i])

            transaction2[1] = max(transaction2[1], prevTransaction1Profit - prices[i])
            transaction2[0] = max(transaction2[0], prices[i] + transaction2[1])        

        return max(transaction1[0], transaction2[0])


solution = Solution()

assert solution.maxProfit([3,3,5,0,0,3,1,4]) == 6
assert solution.maxProfit2([3,3,5,0,0,3,1,4]) == 6

assert solution.maxProfit([1,2,3,4,5]) == 4
assert solution.maxProfit2([1,2,3,4,5]) == 4

assert solution.maxProfit([7,6,4,3,1]) == 0
assert solution.maxProfit2([7,6,4,3,1]) == 0
