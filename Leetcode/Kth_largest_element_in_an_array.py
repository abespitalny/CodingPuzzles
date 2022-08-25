'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.
'''
from leetcode import *

class Solution:
    # Time: O(R) where R is the range of possible values in nums.
    # Space: O(n) where n is the number of numbers in nums.
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        minElem = math.inf
        maxElem = -math.inf
        
        for i in range(len(nums)):
            count[nums[i]] += 1
            if nums[i] < minElem:
                minElem = nums[i]
            if nums[i] > maxElem:
                maxElem = nums[i]

        for i in range(maxElem, minElem - 1, -1):
            k -= count[i]
            if k <= 0:
                return i

    # There's a heap solution which is O(n*log(k)) and a quickselect solution which is O(n) on average and O(n^2) in worst case.

solution = Solution()

assert solution.findKthLargest(nums = [3,2,1,5,6,4], k = 2) == 5
assert solution.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4) == 4
