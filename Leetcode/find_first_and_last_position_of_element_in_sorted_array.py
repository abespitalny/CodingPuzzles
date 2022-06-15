'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''
from leetcode import *

class Solution:
    # Binary search approach.
    # Time: O(log(n))
    # Space: O(1)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        elif len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            return [-1, -1]

        # Find left position
        start = 0
        end = len(nums) - 1
        while (start + 1) < end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
            
        if nums[start] == target:
            left = start
        elif nums[end] == target:
            left = end
        else:
            return [-1, -1]

        # Find right position
        start = 0
        end = len(nums) - 1
        while (start + 1) < end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        
        if nums[end] == target:
            right = end
        else:
            right = start

        return [left, right]

solution = Solution()

# Expected: [3, 4]
print(solution.searchRange(nums = [5,7,7,8,8,10], target = 8))

# Expected: [-1, -1]
print(solution.searchRange(nums = [5,7,7,8,8,10], target = 6))

# Expected: [-1, -1]
print(solution.searchRange(nums = [], target = 0))
