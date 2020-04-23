'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).
'''
from typing import List

# Time: O(log(n)), Space: O(1).
def search(nums: List[int], target: int) -> int:
    nums_size = len(nums)
    start = 0
    end = nums_size - 1
    # Find pivot in O(log(n)):
    while start < end:
        mid = (start + end) // 2
        if nums[start] <= nums[mid]:
            if nums[mid] < nums[end]:
                break
            start = mid + 1
        else:
            end = mid
    # start is the pivot
    pivot = start
    # The number of times the array was left-rotated
    num_rotated = nums_size - pivot

    start = 0
    end = nums_size - 1
    # Find the target using binary search in O(log(n))
    while start <= end:
        mid = (start + end) // 2
        # Convert the mid index to rotated array index:
        # Regular indices   : 0 1 2 3 4 5 6
        # Array values      : 0 1 2 4 5 6 7
        # Rot. Array indices: 4 5 6 0 1 2 3
        if mid >= num_rotated:
            mid_rot = mid - num_rotated
        else:
            mid_rot = mid + pivot

        mid_val = nums[mid_rot]
        if mid_val == target:
            return mid_rot
        elif mid_val > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([4, 5, 6, 7, 0, 1, 2], 3))
print(search([1, 2, 4, 5, 6, 7, 0], 0))
print(search([0, 1, 2, 4, 5, 6, 7], 0))
print(search([6, 7, 0, 1, 2, 4, 5], 0))
print(search([3, 1], 2))
print(search([1], 1))
print(search([], 1))
