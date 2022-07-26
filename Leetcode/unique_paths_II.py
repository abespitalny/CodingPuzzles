'''
You are given an m x n integer array grid.

There is a robot initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]).
The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid.
A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
'''
from leetcode import *

class Solution:
    # Bottom-up DP
    # Time: O(m*n)
    # Space: O(n)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [0]*n
        dp[0] = 1
        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                break
            dp[i] = 1

        next_dp = [0]*n
        for i in range(1, m):
            if dp[0] == 1 and obstacleGrid[i][0] == 0:
                next_dp[0] = 1
            else:
                next_dp[0] = 0

            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    next_dp[j] = 0
                else:
                    next_dp[j] = next_dp[j - 1] + dp[j]
            dp, next_dp = next_dp, dp

        return dp[-1]

solution = Solution()

assert solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2
assert solution.uniquePathsWithObstacles([[0,1],[0,0]]) == 1
