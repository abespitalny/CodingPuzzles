'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''
from leetcode import *

class Solution:
    # Bottom-up DP approach.
    # Time: O(n)
    # Space: O(1)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = cost[0]
        second = cost[1]
        
        for i in range(2, len(cost)):
            nextStep = cost[i] + min(first, second)
            first = second
            second = nextStep
        return min(first, second)

solution = Solution()

assert solution.minCostClimbingStairs([10,15,20]) == 15

assert solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) == 6
