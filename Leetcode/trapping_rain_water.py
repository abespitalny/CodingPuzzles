'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''
from leetcode import *

class Solution:
    # Kinda similar to 2 pointer approach, but it's less efficient than Leetcode solution since it's not a single pass.
    # Time: O(n)
    # Space: O(1)
    def trap(self, height: List[int]) -> int:
        water = 0

        leftWall = 0
        for i in range(1, len(height)):
            if height[i] >= height[leftWall]:
                leftWallHeight = height[leftWall]
                
                for j in range(leftWall + 1, i):
                    water += leftWallHeight - height[j]

                leftWall = i
        
        rightWall = len(height) - 1
        for i in reversed(range(len(height) - 1)):
            if height[i] > height[rightWall]:
                rightWallHeight = height[rightWall]

                for j in reversed(range(i + 1, rightWall)):
                    water += rightWallHeight - height[j]

                rightWall = i
        
        return water

solution = Solution()

assert solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert solution.trap([4,2,0,3,2,5]) == 9
