'''
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, or return -1 otherwise.
'''
from leetcode import *

class Solution:
    # Time: O(n)
    # Space: O(1)
    def dominantIndex(self, nums: List[int]) -> int:
        maxNum = max(nums)
        maxNumIdx = -1
        for i in range(len(nums)):
            if nums[i] == maxNum:
                maxNumIdx = i
            elif nums[i]*2 > maxNum:
                return -1
        return maxNumIdx

solution = Solution()

assert solution.dominantIndex([3,6,1,0]) == 1
assert solution.dominantIndex([1,2,3,4]) == -1
