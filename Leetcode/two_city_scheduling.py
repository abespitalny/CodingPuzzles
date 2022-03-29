'''
A company is planning to interview 2n people.
Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti,
and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
'''
from leetcode import *

# Time: O(n*log(n)) because we sort the array of costs by the difference between aCost_i - bCost_i.
# Space: O(1) because we sort the array in-place.
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost: cost[0] - cost[1])

        totalCost = 0
        n = len(costs) // 2

        for i in range(n):
            totalCost += costs[i][0]
        for i in range(n, 2*n):
            totalCost += costs[i][1]
        return totalCost

solution = Solution()

# Expected: 110
print(solution.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))

# Expected: 1859
print(solution.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))

# Expected: 3086
print(solution.twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]))
