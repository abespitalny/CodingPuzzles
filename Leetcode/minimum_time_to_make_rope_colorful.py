from leetcode import *

class Solution:
    # Time: O(n) where n is the length of colors / neededTime.
    # Space: O(1)
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = 1
        time = 0
        while i < len(colors):
            if colors[i] == colors[i - 1]:
                j = i + 1
                while j < len(colors):
                    if colors[j] != colors[i]:
                        break
                    j += 1
                
                sumTime = 0
                maxTime = 0
                for k in range(i - 1, j):
                    if neededTime[k] > maxTime:
                        maxTime = neededTime[k]
                    sumTime += neededTime[k]
                
                time += (sumTime - maxTime)
                i = j
            else:
                i += 1
        return time

solution = Solution()

# Expected: 3
print(solution.minCost(colors = "abaac", neededTime = [1,2,3,4,5]))

# Expected: 0
print(solution.minCost(colors = "abc", neededTime = [1,2,3]))

# Expected: 2
print(solution.minCost(colors = "aabaa", neededTime = [1,2,3,4,1]))
