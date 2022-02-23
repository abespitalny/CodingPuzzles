'''
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.
'''
from leetcode import *

# Time: O(n), Space: O(1). There was a more dynamic programming approach that I should try.
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        prevDiff = (nums[1] - nums[0])
        numberOfSlices = 0
        lengthOfSlice = 1
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff == prevDiff:
                lengthOfSlice += 1
            else:
                numberOfSlices += ((lengthOfSlice - 1) * lengthOfSlice) // 2
                lengthOfSlice = 1
            
            prevDiff = diff
        # Handle the case where the slice is at the end of array. 
        numberOfSlices += ((lengthOfSlice - 1) * lengthOfSlice) // 2
        
        return numberOfSlices

solution = Solution()

# Expected: 3
print(solution.numberOfArithmeticSlices([1,2,3,4]))

# Expected: 0
print(solution.numberOfArithmeticSlices([1]))
