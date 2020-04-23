'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''
from typing import List

# This is an O(m*n) time and O(1) space solution which I think is the best one could do.
def min_path_sum(grid: List[List[int]]) -> int:
    num_rows = len(grid)
    if num_rows == 0:
        return 0
    num_cols = len(grid[0])

    # Get the shortest path for the leftmost column:
    for i in range(1, num_rows):
        grid[i][0] += grid[i - 1][0]
    # Get the shortest path for the topmost row:
    for i in range(1, num_cols):
        grid[0][i] += grid[0][i - 1]

    for i in range(1, num_rows):
        for j in range(1, num_cols):
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
    return grid[-1][-1]


print(min_path_sum([[1,3,1],
                    [1,5,1],
                    [4,2,1]]))
