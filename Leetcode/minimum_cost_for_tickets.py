'''
You have planned some train traveling one year in advance.
The days of the year in which you will travel are given as an integer array days.
Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:
    - a 1-day pass is sold for costs[0] dollars,
    - a 7-day pass is sold for costs[1] dollars, and
    - a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.
For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.
'''
from leetcode import *

class Solution:
    # Bottom-up DP approach
    # Time: O(3*W) = O(W) where W is the range of days (365)
    # Space: O(W)
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayRange = days[-1]
        passes = [1, 7, 30]
        dp = [0]*(dayRange + 1)

        dayIdx = 0
        for i in range(1, dayRange + 1):
            if days[dayIdx] == i:
                minCost = math.inf
                for cost, d in zip(costs, passes):
                    prevCost = 0 if (i - d) < 0 else dp[i - d]
                    minCost = min(minCost, cost + prevCost)

                dp[i] = minCost
                dayIdx += 1
            else:
                dp[i] = dp[i - 1]

        return dp[-1]

solution = Solution()

assert solution.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]) == 11
assert solution.mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]) == 17
