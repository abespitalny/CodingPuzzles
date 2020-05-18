'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your *maximum* jump length at that position.
Determine if you are able to reach the last index.
'''
from typing import List

# Time: O(n), Space: O(1).
def can_jump(nums: List[int]) -> bool:
    possible = True
    last = len(nums) - 1
    for i in range(last - 1, -1, -1):
        if (i + nums[i]) >= last:
            last = i
            possible = True
        else:
            possible = False
    return possible


# Expected: True
print(can_jump([2,3,1,1,4]))
# Expected: False
print(can_jump([3,2,1,0,4]))
# Expected: True
print(can_jump([3,4,0,1,0,1,1]))
# Expected: False
print(can_jump([2,4,1,2,1,1,0,1]))
