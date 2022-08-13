'''
You are a hiker preparing for an upcoming hike.
You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col).
You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed).
You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
'''
from leetcode import *

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        efforts = [[math.inf]*n for _ in range(m)]
        efforts[0][0] = 0
        queue = deque([(0, 0)])
        while len(queue) != 0:
            posX, posY = queue.popleft()

            for x, y in directions:
                x += posX
                y += posY

                if x < 0 or x >= m or y < 0 or y >= n:
                    continue

                effort = max(efforts[posX][posY], abs(heights[posX][posY] - heights[x][y]))

                if effort >= efforts[x][y]:
                    continue

                efforts[x][y] = effort
                queue.append((x, y))

        return efforts[-1][-1]

    # This is actually a variation on Dijkstra's algorithm.
    # Time: O(m*n*log(m*n)) because we visit each cell (m*n) and insertion and popping from the priority queue
    # takes O(log(m*n)) since the queue can contain m*n elements.
    # Space: O(m*n)
    def minimumEffortPath2(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        efforts = [[math.inf]*n for _ in range(m)]
        efforts[0][0] = 0
        heap = [(0, 0, 0)]
        while len(heap) != 0:
            _, posX, posY = heapq.heappop(heap)

            if posX == (m - 1) and posY == (n - 1):
                break

            for x, y in directions:
                x += posX
                y += posY

                if x < 0 or x >= m or y < 0 or y >= n:
                    continue

                effort = max(efforts[posX][posY], abs(heights[posX][posY] - heights[x][y]))

                if effort >= efforts[x][y]:
                    continue

                efforts[x][y] = effort
                heapq.heappush(heap, (effort, x, y))

        return efforts[-1][-1]


solution = Solution()

assert solution.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]) == 2
assert solution.minimumEffortPath2([[1,2,2],[3,8,2],[5,3,5]]) == 2

assert solution.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]) == 1
assert solution.minimumEffortPath2([[1,2,3],[3,8,4],[5,3,5]]) == 1

assert solution.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]) == 0
assert solution.minimumEffortPath2([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]) == 0
