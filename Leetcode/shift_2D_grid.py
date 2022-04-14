from leetcode import *

class Solution:
    # Time: O(n^2).
    # Space: O(n^2).
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])        
        rowShift = (k // cols) % rows
        colShift = k % cols
        if rowShift == 0 and colShift == 0:
            return grid
        
        shiftedGrid = [[0]*cols for i in range(rows)]
        for row in range(rows):
            for col in range(cols):
                shiftedCol = (col + colShift) % cols
                shiftedRow = (((col + colShift) // cols) + rowShift + row) % rows
                shiftedGrid[shiftedRow][shiftedCol] = grid[row][col]
        return shiftedGrid

solution = Solution()

# Expected: [[9,1,2],[3,4,5],[6,7,8]]
print(solution.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))

# Expected: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
print(solution.shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))

# Expected: [[1,2,3],[4,5,6],[7,8,9]]
print(solution.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9))
