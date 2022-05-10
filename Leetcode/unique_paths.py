'''
There is a robot on an m x n grid.
The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
'''

class Solution:
    # Dynamic programming approach
    # Time: O(m*n)
    # Space: O(n)
    # A smart way to improve this is by taking the min of m and n, and doing what we did here with the row for either the column or the row
    # depending on which is smaller, so space will be O(min(m, n)).
    def uniquePaths(self, m: int, n: int) -> int:
        # Keep only one row at a time
        curRow_dp = [1]*n
        
        for i in range(1, m):
            nextRow_dp = [0]*n
            nextRow_dp[0] = 1
            for j in range(1, n):
                nextRow_dp[j] = curRow_dp[j] + nextRow_dp[j - 1]
            curRow_dp = nextRow_dp

        return curRow_dp[-1]

    # This can also be solved mathematically in a very straightforward way:
    # C((m - 1) + (n - 1), m - 1) = C((m - 1) + (n - 1), n - 1) = (m + n - 2)! / (m - 1)!(n - 1)!

solution = Solution()

# Expected: 28
print(solution.uniquePaths(m = 3, n = 7))

# Expected: 3
print(solution.uniquePaths(m = 3, n = 2))
