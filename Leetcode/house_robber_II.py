'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''
from leetcode import *

class Solution:
    # Time: O(n)
    # Space: O(n)
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        # Use first
        max_moneys_first = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums) - 1):
            max_money = max_moneys_first[len(max_moneys_first) - 2] + nums[i]
            max_moneys_first.append(max(max_money, max_moneys_first[-1]))
        
        # Use last
        max_moneys_last = [nums[1], max(nums[1], nums[2])]
        for i in range(3, len(nums)):
            max_money = max_moneys_last[len(max_moneys_last) - 2] + nums[i]
            max_moneys_last.append(max(max_money, max_moneys_last[-1]))
        
        return max(max_moneys_first[-1], max_moneys_last[-1])

solution = Solution()

assert solution.rob([2,3,2]) == 3
assert solution.rob([1,2,3,1]) == 4
assert solution.rob([1,2,3]) == 3
