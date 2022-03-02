'''
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
    - "a->b" if a != b
    - "a" if a == b
'''
from leetcode import *

# Time: O(n), Space: O(n).
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) <= 0:
            return []
        
        summaryRange = [nums[0], nums[0]]
        ranges = []
        for i in range(1, len(nums)):
            if nums[i] == (summaryRange[1] + 1):
                summaryRange[1] = nums[i]
            else:
                self.appendSummaryRange(summaryRange, ranges)
                summaryRange = [nums[i], nums[i]]
        
        self.appendSummaryRange(summaryRange, ranges)
        return ranges
    
    def appendSummaryRange(self, summaryRange: List[int], summaryRanges: List[str]) -> None:
        if summaryRange[0] != summaryRange[1]:
            summaryRanges.append(f"{summaryRange[0]}->{summaryRange[1]}")
        else:
            summaryRanges.append(str(summaryRange[0]))
        return

solution = Solution()

# Expected: ["0->2","4->5","7"]
print(solution.summaryRanges([0,1,2,4,5,7]))

# Expected: ["0","2->4","6","8->9"]
print(solution.summaryRanges([0,2,3,4,6,8,9]))
