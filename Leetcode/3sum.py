'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
'''
from typing import List, Tuple, Set

def all_two_sums(nums: List[int], target: int) -> Set[Tuple[int, int]]:
    two_sums = set()
    hash_table = {}
    for i in range(len(nums)):
        n = nums[i]
        complement = target - n
        # O(1) time.
        if complement in hash_table:
            two_sums.add((n, complement) if n < complement else (complement, n))
        else:
            hash_table[n] = True
    return two_sums

def three_sum(nums: List[int]) -> List[List[int]]:
    unique_nums = {}
    for i in range(len(nums)):
        n = nums[i]
        ind = unique_nums.get(n, i)
        if ind == i:
            unique_nums[n] = i

    three_sums = set()
    for n in unique_nums:
        n_ind = unique_nums[n]
        sum_pairs = all_two_sums(nums[n_ind + 1:], -n)
        if len(sum_pairs) == 0:
            continue
        for p in sum_pairs:
            if n < p[0]:
                three_sum = (n, p[0], p[1])
            elif n > p[1]:
                three_sum = (p[0], p[1], n)
            else:
                three_sum = (p[0], n, p[1])
            # This is again an O(1) operation.
            three_sums.add(three_sum)
    return [list(i) for i in three_sums]

# It's an open problem if O(n^2) is the fastest possible solution to this problem.

print(three_sum([-1, 0, 1, 2, -1, -4]))