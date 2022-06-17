'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.
'''
from leetcode import *

class Solution:
    # Optimized to find a smaller range where the dip can be using binary search from the first part of the problem.
    # Once a range is found, we then need to do a linear scan on it to find the dip.
    # Time: O(n). In the worst case where the array is filled with just one number, we'll scan through the entire array.
    # Space: O(1)
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while (left + 1) < right:
            mid = (left + right) // 2

            if (nums[mid] < nums[mid - 1]) and (nums[mid] <= nums[mid + 1]):
                return nums[mid]
            elif nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
            else:
                break

        if (left + 1) == right:
            return nums[left] if nums[left] < nums[right] else nums[right]

        for i in range(left + 1, right + 1):
            if nums[i] < nums[i - 1]:
                return nums[i]
        return nums[left]

    # A nice solution from Leetcode that does exactly what I do above but a little nicer. Same runtime and space complexity.
    def findMin2(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            # nums[mid] == nums[right]
            else:
                right -= 1

        return nums[left]


solution = Solution()

assert solution.findMin([1,3,5]) == 1
assert solution.findMin2([1,3,5]) == 1

assert solution.findMin([2,2,2,0,1]) == 0
assert solution.findMin2([2,2,2,0,1]) == 0

assert solution.findMin([3, 3, 1, 3]) == 1
assert solution.findMin2([3, 3, 1, 3]) == 1

assert solution.findMin([1, 2, 1]) == 1
assert solution.findMin2([1, 2, 1]) == 1

assert solution.findMin([1, 2, 2]) == 1
assert solution.findMin2([1, 2, 2]) == 1
