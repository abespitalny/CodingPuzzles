'''
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A subarray may only include each element of the fixed buffer nums at most once.
'''
from leetcode import *

class Solution:
    # Kadane's algorithm
    # Time: O(2*n) = O(n)
    # Space: O(1)
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Perform ordinary Kadane's algorithm
        current = nums[0]
        bestMax = current
        for i in range(1, len(nums)):
            current = max(current + nums[i], nums[i])
            bestMax = max(bestMax, current)

        # If bestMax is negative, then the whole array is negative and bestMin is the entire array.
        if bestMax < 0:
            return bestMax

        # Perform Kadane's algorithm to find minimum subarray and subtract that from total to get best wrapped around subarray.
        current = nums[0]
        total = nums[0]
        bestMin = current
        for i in range(1, len(nums)):
            current = min(current + nums[i], nums[i])
            bestMin = min(bestMin, current)
            total += nums[i]

        return max(bestMax, total - bestMin)


solution = Solution()

assert solution.maxSubarraySumCircular([1,-2,3,-2]) == 3
assert solution.maxSubarraySumCircular([5,-3,5]) == 10
assert solution.maxSubarraySumCircular([-3,-2,-3]) == -2
