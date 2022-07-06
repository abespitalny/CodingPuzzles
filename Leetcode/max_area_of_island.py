'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical).
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''
from leetcode import *

class Solution:
    # Iterative BFS approach
    # Time: O(m*n) because we'll visit each cell at most twice.
    # Space: O(m*n) because of the queue, but it'll be in reality much less because of how BFS explores the grid.
    # Based on other problems of this kind, the space complexity should be O(min(m, n)).
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        
        maxIslandArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    islandArea = 1
                    queue = deque([(i, j)])
                    grid[i][j] = 0

                    while len(queue) != 0:
                        pos = queue.popleft()
                        for x, y in directions:
                            x += pos[0]
                            y += pos[1]
                            
                            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                                continue
                            
                            grid[x][y] = 0
                            islandArea += 1
                            queue.append((x, y))
                    
                    maxIslandArea = max(maxIslandArea, islandArea)

        return maxIslandArea

solution = Solution()

assert solution.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]) == 6
assert solution.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]) == 0
