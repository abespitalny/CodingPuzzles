from leetcode import *

# Assuming nums has at least one element. This algorithm runs in O(n).
def max_subarray(nums: List[int]) -> int:
    max_net = net = 0
    max_num = nums[0]
    for i in range(len(nums)):
        n = nums[i]
        if n > max_num:
            max_num = n

        net += n            
        if net > max_net:
            max_net = net
        elif net < 0:
            net = 0
    return max_num if max_net == 0 else max_net

# A much cleaner solution (inspired by Leetcode solutions):
def max_subarray_v2(nums: List[int]) -> int:
    max_net = net = nums[0]
    for i in range(1, len(nums)):
        n = nums[i]
        net = (n + net) if (n + net) > n else n
        if net > max_net:
            max_net = net
    return max_net

# A divide & conquer solution is a good exercise (note: I looked it up since the problem was taking too long). It's in O(n*log(n)) time.

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray([-1]))
print(max_subarray([-2, 1]))
print(max_subarray([-1, 1, 2, 1]))
