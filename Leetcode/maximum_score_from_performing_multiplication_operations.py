'''
You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:
    - Choose one integer x from either the start or the end of the array nums.
    - Add multipliers[i] * x to your score.
    - Remove x from the array nums.

Return the maximum score after performing m operations.
'''
from leetcode import *

class Solution:
    # Top-down DP approach. Time limit exceeded.
    # Time: O(m^2) where m is the length of the multipliers array.
    # Space: O(m^2)
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        memo = {}

        def dp(i, left):
            if i == len(multipliers):
                return 0
            elif (i, left) in memo:
                return memo[(i, left)]
            
            right = len(nums) - 1 - (i - left)

            useLeft = dp(i + 1, left + 1) + multipliers[i] * nums[left]
            useRight = dp(i + 1, left) + multipliers[i] * nums[right]
            maxScore = max(useLeft, useRight)
            memo[(i, left)] = maxScore

            return maxScore

        return dp(0, 0)
    
    # Bottom-up DP approach
    # Time: O(m^2)
    # Space: O(m)
    def maximumScore2(self, nums: List[int], multipliers: List[int]) -> int:
        scores = [0] * (len(multipliers) + 1)
        for i in range(len(multipliers)):
            mult = multipliers[i]

            right = len(nums) - 1 - i
            prev = scores[0]
            scores[0] += (nums[right] * mult)

            for j in range(1, i + 1):
                right += 1
                temp = scores[j]
                scores[j] = max(prev + (nums[j - 1] * mult), scores[j] + (nums[right] * mult))                
                prev = temp

            scores[i + 1] = prev + (nums[i] * mult)

        return max(scores)

    # My solution is great and optimized for space complexity, but I think Leetcode's solution is clearer:
    # n, m = len(nums), len(multipliers)
    # dp = [[0] * (m + 1) for i in range(m + 1)]

    # for i in range(m - 1, -1, -1):
    # for left in range(i, -1, -1):
    #     mult = multipliers[i]
    #     right = n - 1 - (i - left)
        
    #     dp[i][left] = max(mult * nums[left] + dp[i + 1][left + 1], mult * nums[right] + dp[i + 1][left])
    # return dp[0][0]


solution = Solution()

assert solution.maximumScore2(nums = [1,2,3], multipliers = [3,2,1]) == 14

assert solution.maximumScore2(nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]) == 102
