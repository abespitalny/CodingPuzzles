'''
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

nums[i] != nums[i + 1] for all valid i.
'''
from leetcode import *

class Solution:
    # Binary search approach
    # Time: O(log(n))
    # Space: O(1)
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + ((right - left) // 2)
            leftElem = -math.inf if mid == 0 else nums[mid - 1]
            rightElem = -math.inf if mid == (len(nums) - 1) else nums[mid + 1]

            # Peak!
            if nums[mid] > leftElem and nums[mid] > rightElem:
                return mid
            # Slope down
            elif nums[mid] < leftElem and nums[mid] > rightElem:
                right = mid - 1
            # Slope up
            elif nums[mid] > leftElem and nums[mid] < rightElem:
                left = mid + 1
            # Valley
            else:
                left = mid + 1
        return left

    # A simpler version from Leetcode.
    def findPeakElement2(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # Rising slope
            if nums[mid] > nums[mid + 1]:
                right = mid
            # Falling slope
            else:
                left = mid + 1
        return left

solution = Solution()

# Expected: 2
print(solution.findPeakElement([1,2,3,1]))
print(solution.findPeakElement2([1,2,3,1]))

# Expected: 5
print(solution.findPeakElement([1,2,1,3,5,6,4]))
print(solution.findPeakElement2([1,2,1,3,5,6,4]))
