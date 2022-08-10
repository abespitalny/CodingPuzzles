'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
'''
from fileinput import close
from leetcode import *

class Solution:
    # Sort + Two pointers approach
    # Time: O(n^2)
    # Space: O(n) because of the sort operation.
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        # Edge cases
        minSum = sum(nums[0:3])
        maxSum = sum(nums[-3:])
        if target < minSum:
            return minSum
        elif target > maxSum:
            return maxSum
        
        def twoSumClosest(i, t):
            left = i
            right = len(nums) - 1
            closest = nums[left] + nums[right]

            while (left + 1) < right:
                leftSum = nums[left + 1] + nums[right]
                rightSum = nums[left] + nums[right - 1]
                if abs(t - leftSum) < abs(t - rightSum):
                    left += 1
                else:
                    right -= 1
                
                newSum = nums[left] + nums[right]
                if abs(t - newSum) < abs(t - closest):
                    closest = newSum

            return closest


        closest = math.inf
        for i in range(len(nums) - 2):
            newSum = nums[i] + twoSumClosest(i + 1, target - nums[i])
            if abs(target - newSum) < abs(target - closest):
                closest = newSum

        return closest

solution = Solution()

assert solution.threeSumClosest(nums = [-1,2,1,-4], target = 1) == 2
assert solution.threeSumClosest(nums = [0,0,0], target = 1) == 0
