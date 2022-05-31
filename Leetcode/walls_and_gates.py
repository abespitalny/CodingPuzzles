'''
You are given an m x n grid rooms initialized with these three possible values.
    1) -1 A wall or an obstacle.
    2) 0 A gate.
    3) INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
'''
from leetcode import *

# BFS approach. Start the queue with all the gates and then start visiting neighboring empty rooms.
# Time: O(m*n)
# Space: O(m*n) for the queue.
class Solution:
    INF = (1 << 31) - 1

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        gates = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    gates.append((i, j, 0))

        queue = deque(gates)
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        while len(queue) != 0:
            row, col, dist = queue.popleft()
            
            if rooms[row][col] != Solution.INF and rooms[row][col] != 0:
                continue
            
            rooms[row][col] = dist
            
            for x, y in directions:
                x += row
                y += col
                
                if x < 0 or x >= len(rooms) or y < 0 or y >= len(rooms[0]) or rooms[x][y] != Solution.INF:
                    continue
                queue.append((x, y, dist + 1))
        return

solution = Solution()

rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
solution.wallsAndGates(rooms)
print(rooms)

rooms = [[-1]]
solution.wallsAndGates(rooms)
print(rooms)
