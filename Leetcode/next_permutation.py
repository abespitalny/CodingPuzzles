'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is impossible, it must rearrange it to the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
'''
from leetcode import *

# Time: O(n^2), Space: O(1). I could get time down to O(n) if I was a little smarter about how I find the pivot.
# If you start at the end of the array, then you only need one pass.
def next_permutation(nums: List[int]) -> None:
    # Everything after the pivot is in descending order.
    is_descending = False
    pivot = -1
    while not(is_descending):
        is_descending = True
        for i in range(pivot + 1, len(nums) - 1):
            if nums[i] < nums[i + 1]:
                pivot = i
                is_descending = False
                break

    # Reorder things after the pivot into ascending order.
    num_swaps = (len(nums) - (pivot + 1)) // 2
    i = 0
    while i < num_swaps:
        swap(nums, (pivot + 1) + i, (len(nums) - 1) - i)
        i += 1

    if pivot < 0:
        return

    # Swap pivot with first number that's greater than it.
    for i in range(pivot + 1, len(nums)):
        if nums[pivot] < nums[i]:
            swap(nums, pivot, i)
            break
    return

def swap(arr: List[int], i: int, j: int) -> None:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return

nums = [1,2,3]
next_permutation(nums)
# Expected: [1,3,2]
print(nums)

nums = [3,2,1]
next_permutation(nums)
# Expected: [1,2,3]
print(nums)

nums = [1,1,5]
next_permutation(nums)
# Expected: [1,5,1]
print(nums)

nums = [1]
next_permutation(nums)
# Expected: [1]
print(nums)

nums = [1,2,1,3]
next_permutation(nums)
# Expected: [1,2,3,1]
print(nums)

nums = [1,3,2]
next_permutation(nums)
# Expected: [2,1,3]
print(nums)