'''
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
such that the sum of min(ai, bi) for all i is maximized.

Return the maximized sum.
'''
from leetcode import *

class Solution:
    # Sorting
    # Time: O(n*log(n))
    # Space: O(n)
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        
        maxSumPair = 0
        while i < len(nums):
            maxSumPair += nums[i]
            i += 2
        return maxSumPair

solution = Solution()

assert solution.arrayPairSum([1,4,3,2]) == 4
assert solution.arrayPairSum([6,2,6,5,1,2]) == 9
