'''
You are given an m x n integer matrix points (0-indexed).
Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row.
Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row.
For every two adjacent rows r and r + 1 (where 0 <= r < m - 1),
picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.
'''
from leetcode import *

class Solution:
    # Bottom-up DP approach.
    # Original recurrence relation: dp[i][j] = max(dp[i - 1][k] - abs(k - j)) + points[i][j] for k = 0..n
    # This gives an O(n^3) runtime which is too slow.
    # For a certain index i, the maximum value for i is a index that could either come from its left, or its right.
    # Thus, we can build two arrays (I used just one by being clever) and focus on the maximum value only coming from its left or right.
    # Finding the best fit for a single index i could just cost O(1) time from then on.
    #
    # Time: O(m*n)
    # Space: O(n)
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])

        dp = points[0][:]
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = max(dp[j - 1] - 1, dp[j])
            
            for j in reversed(range(n - 1)):
                dp[j] = max(dp[j + 1] - 1, dp[j])
            
            for j in range(n):
                dp[j] += points[i][j]

        return max(dp)

solution = Solution()

assert solution.maxPoints([[1,2,3],[1,5,1],[3,1,1]]) == 9
assert solution.maxPoints([[1,5],[2,3],[4,2]]) == 11
