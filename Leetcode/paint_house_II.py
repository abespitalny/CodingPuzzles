'''
There are a row of n houses, each house can be painted with one of the k colors.
The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x k cost matrix costs.

Return the minimum cost to paint all houses.
'''
from leetcode import *

class Solution:
    # Bottom-up DP approach optimized for space and time.
    # Time: O(n*k)
    # Space: O(k)
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])

        minLeft = [0]*k
        minRight = [0]*k
        for i in range(1, n):
            minLeft[0] = costs[i - 1][0]
            for j in range(1, k):
                minLeft[j] = min(minLeft[j - 1], costs[i - 1][j])
            
            minRight[-1] = costs[i - 1][-1]
            for j in reversed(range(k - 1)):
                minRight[j] = min(minRight[j + 1], costs[i - 1][j])

            for j in range(k):
                minCost = math.inf
                if (j - 1) >= 0:
                    minCost = min(minCost, minLeft[j - 1])
                if (j + 1) < k:
                    minCost = min(minCost, minRight[j + 1])

                costs[i][j] += minCost

        return min(costs[-1])


    # Bottom-up DP that's even more optimized.
    # You could also modify this solution so that you're not overwriting the input by keeping track of just the min and second min for the previous row.
    # Time: O(n*k)
    # Space: O(1)
    def minCostII2(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])

        for i in range(1, n):
            minCost = costs[i - 1][0]
            minCostIdx = 0
            secondMinCost = math.inf
            secondMinCostIdx = -1
            for j in range(1, k):
                cost = costs[i - 1][j]

                if cost <= minCost:
                    minCost, secondMinCost = cost, minCost
                    minCostIdx, secondMinCostIdx = j, minCostIdx
                elif cost < secondMinCost:
                    secondMinCost = cost
                    secondMinCostIdx = j

            for j in range(k):
                cost = 0
                if j != minCostIdx:
                    cost = minCost
                elif j != secondMinCostIdx and secondMinCostIdx != -1:
                    cost = secondMinCost

                costs[i][j] += cost

        return min(costs[-1])


solution = Solution()

assert solution.minCostII([[1,5,3],[2,9,4]]) == 5
assert solution.minCostII([[1,3],[2,4]]) == 5

assert solution.minCostII2([[1,5,3],[2,9,4]]) == 5
assert solution.minCostII2([[1,3],[2,4]]) == 5
