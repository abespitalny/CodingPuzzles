'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
of which the sum is greater than or equal to target.
If there is no such subarray, return 0 instead.
'''
from leetcode import *

# Time: O(n), Space: O(1). This algorithm wouldn't work if we allowed negative numbers in the array.
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = math.inf
        
        start = end = 0
        currentSum = nums[0]
        while start <= end:
            if currentSum >= target:
                subarrayLen = end - start + 1
                
                if subarrayLen < minLen:
                    minLen = subarrayLen
                    # A length of 1 is as small as you're going to get!
                    if minLen == 1:
                        break
                
                currentSum -= nums[start]
                start += 1
            else:
                if (end + 1) < len(nums):
                    end += 1
                    currentSum += nums[end]
                else:
                    break

        if minLen == math.inf:
            return 0
        else:
            return minLen

solution = Solution()

# Expected: 2
print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))

# Expected: 1
print(solution.minSubArrayLen(4, [1,4,4]))

# Expected: 0
print(solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
