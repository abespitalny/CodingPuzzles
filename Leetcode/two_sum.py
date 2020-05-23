'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
'''
from leetcode import *

def two_sum(nums: List[int], target: int) -> List[int]:
    hash_table = {}
    for i in range(len(nums)):
        n = nums[i]
        complement = target - n
        # O(1) time.
        complement_ind = hash_table.get(complement, None)
        if complement_ind is None:
            hash_table[n] = i
            continue
        return [complement_ind, i]
    return None
