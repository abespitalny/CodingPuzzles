'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
'''
from leetcode import *

# Time: O(n), Space: O(1). There was a much simpler solution that's still O(n) time and O(1) space though it doesn't do a single pass through the array.
#   1) Count the number of 0s, 1s, and 2s in array in one pass.
#   2) Pass through the array again setting the number of 0s equivalent to the count of 0s. Do the same for 1s and 2s.
def sort_colors(nums: List[int]) -> None:
    blue_index = len(nums) - 1
    i = red_index = 0
    while i <= blue_index:
        if nums[i] == 0:
            swap(nums, i, red_index)
            red_index += 1
            i += 1
        elif nums[i] == 1:
            i += 1
        else:
            swap(nums, i , blue_index)
            blue_index -= 1
    return

def swap(arr: List[int], i: int, j: int) -> None:
    if i == j:
        return

    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return

nums = [2,0,2,1,1,0]
sort_colors(nums)
# Expected: [0,0,1,1,2,2]
print(nums)

nums = [2,0,1]
sort_colors(nums)
# Expected: [0,1,2]
print(nums)

nums = [1,2,0]
sort_colors(nums)
# Expected: [0,1,2]
print(nums)
