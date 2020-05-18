'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
'''
from typing import List

# Time: O(n), Space: O(n) [the hashtable can contain upto n entries in the worst case].
def subarray_sum(nums: List[int], k: int) -> int:
    num_sums = 0
    total = 0
    # All the previous sums encountered so far.
    prev_sums = {}
    for i in range(len(nums)):
        total += nums[i]
        if total == k:
            num_sums += 1
        num_sums += prev_sums.get(total - k, 0)

        prev_sums[total] = prev_sums.get(total, 0) + 1
    return num_sums


print(subarray_sum([1, 1, 1], 2))
print(subarray_sum([1, 1, 1, -1], 2))
print(subarray_sum([1, 1, 1, -1], 1))
