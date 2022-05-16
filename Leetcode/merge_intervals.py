'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''
from leetcode import *

class Solution:
    # Time: O(n*log(n) + n) = O(n*log(n))
    # Space: O(log(n)) for sorting.
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals
        intervals.sort()
        
        mergedIntervals = []
        prevInterval = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start <= prevInterval[1]:
                prevInterval[1] = max(prevInterval[1], end)
            else:
                mergedIntervals.append(prevInterval)
                prevInterval = intervals[i]

        mergedIntervals.append(prevInterval)
        return mergedIntervals

solution = Solution()

# Expected: [[1,6],[8,10],[15,18]]
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))

# Expected: [[1,5]]
print(solution.merge([[1,4],[4,5]]))
