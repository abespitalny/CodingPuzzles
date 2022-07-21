'''
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
'''
from leetcode import *

class Solution:
    # Sorting approach
    # Time: O(n*log(n))
    # Space: O(n)
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for time in timePoints:
            hours, minutes = time.split(":")
            hours = int(hours)
            minutes = int(minutes)
            times.append(minutes + (60*hours))
        
        times.sort()
        minDiff = (times[0] - times[-1]) % 1440

        for i in range(len(times) - 1):
            minDiff = min(minDiff, (times[i + 1] - times[i]))
        return minDiff

solution = Solution()

assert solution.findMinDifference(["23:59","00:00"]) == 1
assert solution.findMinDifference(["00:00","23:59","00:00"]) == 0
