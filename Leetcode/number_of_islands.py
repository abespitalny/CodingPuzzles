'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example:
Input:
11000
11000
00100
00011

Output: 3
'''
from leetcode import *

class Solution:
    # DFS approach.
    # This is an O(m*n) time,  where m is the number of rows and n is the number of columns in the grid, and an O(m*n) space solution.
    def num_islands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        if num_rows == 0:
            return 0
        num_cols = len(grid[0])
        row_len = num_cols - 1
        col_len = num_rows - 1

        num_isles = 0
        for i in range(num_rows):
            for j in range(num_cols):
                # Skip water:
                if grid[i][j] == '0':
                    continue
                # Discover island:
                else:
                    num_isles += 1
                    stack = [(i, j)]
                    while len(stack) != 0:
                        top = stack.pop()
                        grid[top[0]][top[1]] = '0'
                        # Check left:
                        if (top[0] > 0) and (grid[top[0] - 1][top[1]] == '1'):
                            stack.append((top[0] - 1, top[1]))
                        # Check top:
                        if (top[1] > 0) and (grid[top[0]][top[1] - 1] == '1'):
                            stack.append((top[0], top[1] - 1))
                        # Check right:
                        if (top[0] < col_len) and (grid[top[0] + 1][top[1]] == '1'):
                            stack.append((top[0] + 1, top[1]))
                        # Check down:
                        if (top[1] < row_len) and (grid[top[0]][top[1] + 1] == '1'):
                            stack.append((top[0], top[1] + 1))
        return num_isles

    # BFS approach
    # Time: O(m*n)
    # Space: O(min(m, n)). Look at the images folder for an explanation for why this is min(m, n).
    def num_islands2(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        numIslands = 0
        for i in range(rows):
            for j in range(cols):
                # Skip water:
                if grid[i][j] == '0':
                    continue
                # Discover island:
                else:
                    numIslands += 1

                    # Mark position as visited by turning it into water.
                    grid[i][j] = '0'
                    queue = deque([(i, j)])
                    while len(queue) != 0:
                        row, col = queue.popleft()

                        for x, y in directions:
                            x += row
                            y += col

                            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == '0':
                                continue

                            grid[x][y] = '0'
                            queue.append((x, y))
        return numIslands


solution = Solution()

print(solution.num_islands([['1','1','1','1','0'],
                   ['1','1','0','1','0'],
                   ['1','1','0','0','0'],
                   ['0','0','0','0','0']]))
print(solution.num_islands2([['1','1','1','1','0'],
                   ['1','1','0','1','0'],
                   ['1','1','0','0','0'],
                   ['0','0','0','0','0']]))

print(solution.num_islands([['1','1','0','0','0'],
                   ['1','1','0','0','0'],
                   ['0','0','1','0','0'],
                   ['0','0','0','1','1']]))
print(solution.num_islands2([['1','1','0','0','0'],
                   ['1','1','0','0','0'],
                   ['0','0','1','0','0'],
                   ['0','0','0','1','1']]))
