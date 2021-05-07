'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have
security systems connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
'''
from leetcode import *

# Time: O(n), Space: O(n)
def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    max_money = [nums[0], max(nums[0], nums[1])]
    for i in range(2, len(nums)):
        max_money.append(max(max_money[-2] + nums[i], max_money[-1]))
    return max_money[-1]

# Expected: 4
print(rob([1,2,3,1]))
# Expected: 12
print(rob([2,7,9,3,1]))