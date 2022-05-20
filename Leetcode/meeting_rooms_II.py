'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
'''
from leetcode import *

class Solution:
    # Time: O(n*log(n)) because of sorting and then there can be potential n popping from / pushing into the heap.
    # Space: O(n) for the heap.
    # Looking at Leetcode's solution, the while loop is unnecessary here because we can just pop the first available meeting for the new meeting.
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        numRooms = 1
        heap = [intervals[0][1]]
        for i in range(1, len(intervals)):
            while len(heap) != 0:
                if heap[0] <= intervals[i][0]:
                    heapq.heappop(heap)
                else:
                    break
            heapq.heappush(heap, intervals[i][1])
            numRooms = max(numRooms, len(heap))

        return numRooms
    
    # There's also a weird solution where you can sort the start and end times individually (see Leetcode).

solution = Solution()

# Expected: 2
print(solution.minMeetingRooms([[0,30],[5,10],[15,20]]))

# Expected: 1
print(solution.minMeetingRooms([[7,10],[2,4]]))
