'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''
from leetcode import *

class Solution:
    # Time: O(n^2)
    # Space: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        nums_len = len(nums)
        j = 0
        for i in range(nums_len):
            if nums[j] == 0:
                nums.pop(j)
                nums.append(0)
                j -= 1
            j += 1

    # Two pointer approach
    # Time: O(n)
    # Space: O(1)
    def moveZeroes2(self, nums: List[int]) -> None:
        left = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[left] = nums[i]
                left += 1
            i += 1

        while left < len(nums):
            nums[left] = 0
            left += 1

solution = Solution()

arr = [0, 1, 0, 3, 12]
solution.moveZeroes(arr)
print(arr)

arr = [0, 0, 1]
solution.moveZeroes(arr)
print(arr)
