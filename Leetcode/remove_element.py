'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.
'''
from leetcode import *

class Solution:
    # More complicated two-pointer approach
    # Time: O(n)
    # Space: O(1)
    def removeElement(self, nums: List[int], val: int) -> int:
        lastIdx = len(nums) - 1
        while lastIdx >= 0 and nums[lastIdx] == val:
            lastIdx -= 1
        
        if lastIdx < 0:
            return 0

        i = 0
        while i <= lastIdx:
            if nums[i] == val:
                nums[i], nums[lastIdx] = nums[lastIdx], nums[i]
                lastIdx -= 1
                while lastIdx >= 0 and nums[lastIdx] == val:
                    lastIdx -= 1
            i += 1

        return i

    # Simpler two pointer approach
    # Time: O(n)
    # Space: O(1)
    def removeElement2(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

solution = Solution()

# Expected: [2,2,_,_]
nums = [3,2,2,3]
assert solution.removeElement(nums, 3) == 2
print(nums)

# Expected: [0,1,4,0,3,_,_,_]
nums = [0,1,2,2,3,0,4,2]
assert solution.removeElement(nums, 2) == 5
print(nums)
