'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
'''
from typing import List

# Time: O(n), Space: O(n)
def find_max_length(nums: List[int]) -> int:
    nums_size = len(nums)
    if nums_size < 2:
        return 0

    # Summation of all the 0s and 1s where 0 is represented as -1.
    net_sum = 1 if nums[0] else -1
    # Keeps track on when it first encountered a certain net sum:
    prev_net_sums = {net_sum: 0}
    max_array = 0
    for i in range(1, nums_size):
        net_sum += 1 if nums[i] else -1
        if net_sum == 0:
            max_array = i + 1
            continue

        prev_net_sum_ind = prev_net_sums.get(net_sum, None)
        if prev_net_sum_ind is None:
            prev_net_sums[net_sum] = i
        else:
            array_len = i - prev_net_sum_ind
            if array_len > max_array:
                max_array = array_len
    return max_array


print(find_max_length([0, 1]))
print(find_max_length([0, 1, 0]))
print(find_max_length([1, 1, 1, 1, 0, 0, 0]))
print(find_max_length([0, 1, 0, 0, 1, 0, 0, 1]))
print(find_max_length([1, 1, 1, 1]))
print(find_max_length([0, 1, 1, 0, 1, 1, 1, 0]))
