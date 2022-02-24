'''
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
'''
from leetcode import *

# Time: O(n), Space: O(n).
# The idea is that if you encounter a remainder you have already seen then you know a subarray sum exists.
# x_1 = n_1 * k + r
# x_2 = n_2 * k + r
# x_2 - x_1 = (n_2 - n_1) * k + (r - r) = (n_2 - n_1) * k
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        total = nums[0]
        prevRemainder = total % k
        remainders = set()
        for i in range(1, len(nums)):
            total += nums[i]
            remainder = total % k
            
            if remainder == 0:
                return True
            if remainder in remainders:
                return True
            
            remainders.add(prevRemainder)
            prevRemainder = remainder
        return False

solution = Solution()

# Expected: True
print(solution.checkSubarraySum([23,2,4,6,7], 6))

# Expected: True
print(solution.checkSubarraySum([23,2,6,4,7], 6))

# Expected: False
print(solution.checkSubarraySum([23,2,6,4,7], 13))
