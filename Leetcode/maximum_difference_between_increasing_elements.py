'''
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]),
such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.
'''
from leetcode import *

class Solution:
    # Similar to Best Time to Buy and Sell Stock problem.
    # Time: O(n)
    # Space: O(1)
    def maximumDifference(self, nums: List[int]) -> int:
        minElem = nums[0]
        maxDiff = -math.inf
        for i in range(1, len(nums)):
            if nums[i] < minElem:
                minElem = nums[i]
            else:
                maxDiff = max(nums[i] - minElem, maxDiff)

        if maxDiff <= 0:
            return -1
        return maxDiff

solution = Solution()

assert solution.maximumDifference([7,1,5,4]) == 4
assert solution.maximumDifference([9,4,3,2]) == -1
assert solution.maximumDifference([1,5,2,10]) == 9
