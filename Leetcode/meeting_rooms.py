'''
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
'''
from leetcode import *

# Time: O(nlog(n))
# Space: O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True

solution = Solution()

# Expected: False
print(solution.canAttendMeetings([[0,30],[5,10],[15,20]]))

# Expected: True
print(solution.canAttendMeetings([[7,10],[2,4]]))
