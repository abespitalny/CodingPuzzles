'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.

Follow up:
- This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
- Would this affect the run-time complexity? How and why?
'''
from leetcode import *

# This is an O(n) solution since you cannot have an O(log(n)) one if duplicates are allowed.
def search(nums: List[int], target: int) -> bool:
    nums_size = len(nums)
    pivot = 0
    # Find pivot in O(n):
    for i in range(1, nums_size):
        if nums[i] < nums[i - 1]:
            pivot = i
            break
    # The number of times the array was left-rotated
    num_rotated = nums_size - pivot

    start = 0
    end = nums_size - 1
    # Find the target using binary search in O(log(n))
    while start <= end:
        mid = (start + end) // 2
        # Convert the mid index to rotated array index:
        if mid >= num_rotated:
            mid_rot = mid - num_rotated
        else:
            mid_rot = mid + pivot

        mid_val = nums[mid_rot]
        if mid_val == target:
            return True
        elif mid_val > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

# If the solution is O(n) already, then why not just search through the entire array looking for the target.
def search_v2(nums: List[int], target: int) -> bool:
    for i in range(len(nums)):
        if nums[i] == target:
            return True
    return False

# There is a better algorithm that's a modified version of binary search which is at best O(log(n))
# and at worst O(n). The algorithm is O(n) because of these lines:
# if L[lo] == L[mid] == L[hi]:
#    lo += 1
#    hi -= 1


print(search([2, 5, 6, 0, 0, 1, 2], 0))
print(search([2, 5, 6, 0, 0, 1, 2], 3))
print(search([2, 2, 2, 0, 2, 2], 0))
print(search([1, 3, 1, 1, 1], 3))

print(search_v2([2, 5, 6, 0, 0, 1, 2], 0))
print(search_v2([2, 5, 6, 0, 0, 1, 2], 3))
print(search_v2([2, 2, 2, 0, 2, 2], 0))
print(search_v2([1, 3, 1, 1, 1], 3))
