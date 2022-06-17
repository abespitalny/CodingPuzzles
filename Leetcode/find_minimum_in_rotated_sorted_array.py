'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''
from leetcode import *

def find_min(nums: List[int]) -> int:
    start = 0
    end = len(nums) - 1
    mid = -1
    while start <= end:
        mid = (start + end) // 2
        mid_val = nums[mid]

        if ((mid - 1) < 0 or mid_val < nums[mid - 1]) and ((mid + 1) >= len(nums) or mid_val < nums[mid + 1]):
            return mid_val
        elif mid_val > nums[end]:
            start = mid + 1
        else:
            end = mid - 1

    return nums[mid]

print(find_min([4,5,6,7,0,1,2]))
print(find_min([0,1,2,4,5,6,7]))
print(find_min([3,4,5,1,2]))
print(find_min([4,5,6,7,0,1,2]))
print(find_min([11,13,15,17]))
print(find_min([1]))
print(find_min([2,1]))
