'''
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.
'''
from leetcode import *

class Solution:
    # Binary search / two pointers approach.
    # Time: O(n*log(n) + n*log(W)) for sorting and then for each binary search, we need to scan over the array using two pointers in O(n) time in order
    # to determine the number of diff pairs that are <= midDiff. We binary search in the range [minDiff, maxDiff], so W = maxDiff - minDiff.
    # Space: O(n) because of sorting.
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        # Find maxDiff
        maxDiff = nums[-1] - nums[0]
        if k == len(nums):
            return maxDiff
        
        # Find minDiff
        minDiff = maxDiff
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff < minDiff:
                minDiff = diff

        if k == 1:
            return minDiff

        start = minDiff
        end = maxDiff
    
        while start < end:
            midDiff = (start + end) // 2

            left = 0
            right = 1
            diffCount = 0
            while right < len(nums):
                if nums[right] - nums[left] <= midDiff:
                    diffCount += (right - left)
                    right += 1
                else:
                    if left == (right - 1):
                        right += 1
                    else:
                        left += 1

            if k > diffCount:
                start = midDiff + 1
            else:
                end = midDiff

        return start

solution = Solution()

assert solution.smallestDistancePair(nums = [1,3,1], k = 1) == 0

assert solution.smallestDistancePair(nums = [1,1,1], k = 2) == 0

assert solution.smallestDistancePair(nums = [1,6,1], k = 3) == 5
