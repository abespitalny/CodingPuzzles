'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''
from leetcode import *

class Solution:
    # Two pointer approach
    # Time: O(n)
    # Space: O(1)
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        leftIdx = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if leftIdx == -1:
                    leftIdx = i
            else:
                if leftIdx != -1:
                    maxOnes = max(maxOnes, i - leftIdx)
                    leftIdx = -1

        if leftIdx != -1:
            maxOnes = max(maxOnes, len(nums) - leftIdx)
    
        return maxOnes

    # Simplified two pointer approach
    # Time: O(n)
    # Space: O(1)
    def findMaxConsecutiveOnes2(self, nums: List[int]) -> int:
        maxOnes = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                maxOnes = max(maxOnes, count)
                count = 0

        return max(maxOnes, count) 

solution = Solution()

assert solution.findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3
assert solution.findMaxConsecutiveOnes([1,0,1,1,0,1]) == 2
