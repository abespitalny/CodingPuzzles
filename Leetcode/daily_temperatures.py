'''
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''
from leetcode import *

class Solution:
    # Stack approach
    # Time: O(n)
    # Space: O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = [len(temperatures) - 1]
        for i in reversed(range(len(temperatures) - 1)):
            if temperatures[i] < temperatures[stack[-1]]:
                stack.append(i)
                answer[i] = 1
            else:
                while len(stack) != 0:
                    if temperatures[stack[-1]] > temperatures[i]:
                        break
                    stack.pop()

                if len(stack) == 0:
                    numDays = 0
                else:
                    numDays = stack[-1] - i

                stack.append(i)
                answer[i] = numDays

        return answer
    
    # From Leetcode, there's an O(n) time and O(1) space solution.
    # Pseudocode:
    # Iterate backwards through the input. At each index currDay, check if the current day is the hottest one seen so far.
    # If it is, update hottest and move on. Otherwise, do the following:
    #   - Initialize a variable days = 1 because the next warmer day must be at least one day in the future.
    #   - While temperatures[currDay + days] <= temperatures[currDay]:
    #       - Add answer[currDay + days] to days. This effectively jumps directly to the next warmer day.
    #   - Set answer[currDay] = days.


solution = Solution()

# Expected: [1,1,4,2,1,1,0,0]
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))

# Expected: [1,1,1,0]
print(solution.dailyTemperatures([30,40,50,60]))

# Expected: [1,1,0]
print(solution.dailyTemperatures([30,60,90]))
