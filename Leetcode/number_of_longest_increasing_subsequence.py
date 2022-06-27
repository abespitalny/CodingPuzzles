'''
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.
'''
from leetcode import *

class Solution:
    # Bottom-up DP approach
    # Time: O(n^2)
    # Space: O(n)
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [(1, 1)]*len(nums)
        for i in range(1, len(nums)):
            lenLIS, numLIS = dp[i]
            for j in range(i):
                if nums[i] > nums[j]:
                    lenIS = dp[j][0] + 1
                    if lenIS > lenLIS:
                        numLIS = dp[j][1]
                        lenLIS = lenIS
                    elif lenIS == lenLIS:
                        numLIS += dp[j][1]
            
            dp[i] = (lenLIS, numLIS)

        maxLength = 0
        maxLengthNum = 0
        for length, num in dp:
            if length > maxLength:
                maxLength = length
                maxLengthNum = num
            elif length == maxLength:
                maxLengthNum += num

        return maxLengthNum

solution = Solution()

assert solution.findNumberOfLIS([1,3,5,4,7]) == 2
assert solution.findNumberOfLIS([2,2,2,2,2]) == 5
