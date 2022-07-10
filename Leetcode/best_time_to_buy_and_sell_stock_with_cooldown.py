from leetcode import *

class Solution:
    # Bottom-up DP approach. Recurrence relation is very similar to part 4 of this problem,
    # and can be readily determined from the code.
    # Time: O(n)
    # Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0], [0, 0]]
        for i in reversed(range(len(prices))):
            doNothing = dp[0][0]
            buyStock = dp[0][1] - prices[i]
            maxNotHolding = max(doNothing, buyStock)

            doNothing = dp[0][1]
            sellStock = dp[1][0] + prices[i]
            maxHolding = max(doNothing, sellStock)

            dp[1] = dp[0]
            dp[0] = [maxNotHolding, maxHolding]

        return dp[0][0]

    # See Leetcode for beautiful explanation of some alternative solutions.
    # Modelling the recurrence relation as a state machine is genius.

solution = Solution()

assert solution.maxProfit([1,2,3,0,2]) == 3
assert solution.maxProfit([1]) == 0
