from leetcode import *

class Solution:
    # Time: O(n + k) where n is the number of rooms and k is the number of total keys.
    # Space: O(n).
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        stack = [0]

        while len(stack) != 0:
            room = stack.pop()
            keys = rooms[room]
            
            for k in keys:
                if k not in visited:
                    visited.add(k)
                    stack.append(k)
        
        return (len(visited) == len(rooms))

solution = Solution()

# Expected: True
print(solution.canVisitAllRooms([[1],[2],[3],[]]))

# Expected: False
print(solution.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
