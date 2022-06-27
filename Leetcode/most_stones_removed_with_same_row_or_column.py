'''
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone,
return the largest possible number of stones that can be removed.
'''
from leetcode import *

class Solution:
    # DFS graph traversal approach.
    # Time: O(V + E) = O(n^2) in order to build the grapha and perform DFS. There could be O(V^2) edges in the worst case.
    # Space: O(V + E) = O(n^2).
    def removeStones(self, stones: List[List[int]]) -> int:
        numStones = len(stones)

        # Build graph where each vertex is a stone and an edge represents the two stones having the same row or column.
        stonesMap = {}
        rowToStones = {}
        colsToStones = {}
        for i in range(numStones):
            x, y = stones[i]
            neighbors = []

            row = rowToStones.get(x, [])
            for j in row:
                stonesMap[j].append(i)
                neighbors.append(j)
            row.append(i)
            rowToStones[x] = row

            col = colsToStones.get(y, [])
            for j in col:
                stonesMap[j].append(i)
                neighbors.append(j)
            col.append(i)
            colsToStones[y] = col

            stonesMap[i] = neighbors
    
        # Get the number of disjoint components
        visited = set()
        numComponents = 0
        for i in range(numStones):
            if i in visited:
                continue

            numComponents += 1
            stack = [i]
            while len(stack) != 0:
                stone = stack.pop()
                for j in stonesMap[stone]:
                    if j not in visited:
                        visited.add(j)
                        stack.append(j)

        return numStones - numComponents

    # There's also a union-find approach in order to get the number of disjoint connected components.

solution = Solution()

assert solution.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]) == 5
assert solution.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]) == 3
assert solution.removeStones([[0,0]]) == 0
