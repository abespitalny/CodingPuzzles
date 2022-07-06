'''
You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year.
The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1].
Note that the person is not counted in the year that they die.

Return the earliest year with the maximum population.
'''
from leetcode import *

class Solution:
    # Brute force approach
    # Time: O(n^2)
    # Space: O(1)
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        maxPop = 0
        maxPopYear = 0
        for i in range(len(logs)):
            pop = 1
            for j in range(len(logs)):
                if (logs[i][0] < logs[j][1]) and (logs[i][0] >= logs[j][0]):
                    pop += 1

            if pop > maxPop:
                maxPop = pop
                maxPopYear = logs[i][0]
            elif pop == maxPop and logs[i][0] < maxPopYear:
                maxPopYear = logs[i][0]

        return maxPopYear

    # Combo of ideas from Leetcode discussion section.
    # Time: O(n) where n is the number of logs because we know the minYear and maxYear are within the range of 1950 to 2050.
    # Space: O(1) because the pop array's length will be no greater than 101.
    def maximumPopulation2(self, logs: List[List[int]]) -> int:
        minYear = math.inf
        maxYear = 0
        for birth, death in logs:
            minYear = min(minYear, birth, death)
            maxYear = max(maxYear, birth, death)
        
        pop = [0]*(maxYear - minYear + 1)
        for birth, death in logs:
            pop[birth - minYear] += 1
            pop[death - minYear] -= 1

        currentPop = 0
        maxPop = 0
        maxPopYear = 0
        for i in range(len(pop)):
            currentPop += pop[i]
            if currentPop > maxPop:
                maxPop = currentPop
                maxPopYear = i + minYear
        return maxPopYear

solution = Solution()

assert solution.maximumPopulation([[1993,1999],[2000,2010]]) == 1993
assert solution.maximumPopulation2([[1993,1999],[2000,2010]]) == 1993
assert solution.maximumPopulation([[1950,1961],[1960,1971],[1970,1981]]) == 1960
assert solution.maximumPopulation2([[1950,1961],[1960,1971],[1970,1981]]) == 1960
