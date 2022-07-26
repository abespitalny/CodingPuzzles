'''
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green.
The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...

Return the minimum cost to paint all houses.
'''
from leetcode import *

class Solution:
    # Bottom-up DP approach
    # Time: O(6*n) = O(n)
    # Space: O(1)
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        for i in range(1, n):
            for j in range(3):
                minCost = math.inf
                for k in range(3):
                    if k == j:
                        continue
                    minCost = min(minCost, costs[i - 1][k])

                costs[i][j] += minCost

        return min(costs[-1])

solution = Solution()

assert solution.minCost([[17,2,17],[16,16,5],[14,3,19]]) == 10
assert solution.minCost([[7,6,2]]) == 2
