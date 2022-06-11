'''
You are given an n x n grid where we place some 1 x 1 x 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of the cell (i, j).

We view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3-dimensional figure to a 2-dimensional plane.
We are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.
'''
from leetcode import *

class Solution:
    # Time: O(n^2)
    # Space: O(1)
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)

        xzProjArea = sum(max(grid[i]) for i in range(n))
        
        yzProjArea = 0
        xyProjArea = 0
        for j in range(n):
            maxCol = 0
            for i in range(n):
                maxCol = max(grid[i][j], maxCol)
                if grid[i][j] != 0:
                    xyProjArea += 1
            yzProjArea += maxCol

        return xyProjArea + xzProjArea + yzProjArea

solution = Solution()

# Expected: 17
print(solution.projectionArea([[1,2],[3,4]]))

# Expected: 5
print(solution.projectionArea([[2]]))

# Expected: 8
print(solution.projectionArea([[1,0],[0,2]]))
