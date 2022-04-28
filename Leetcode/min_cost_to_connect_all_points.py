'''
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
'''
from leetcode import *

# NOTE: I went rogue here. I should use the standard Kruskal's or Prim's algorithm to get the MST. Prim's can run in O(n^2) time and O(n) space.
# Time: O(n^2 * log(n)). I didn't use the union-find data structure, but I believe that determining components and joining them up is a
# nearly constant operation like in union-find, so the bulk of the time is taken up by sorting the n^2 edges, O(n^2 * log(n^2)) = O(n^2 * log(n)).
# Space: O(n^2 + n) = O(n^2).
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distancesToLines = {}
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                lines = distancesToLines.get(dist, [])
                if len(lines) == 0:
                    distancesToLines[dist] = lines
                lines.append((i, j))

        components = []
        numLines = 0
        cost = 0
        for d in sorted(distancesToLines.keys()):
            lines = distancesToLines[d]
            for i, j in lines:
                if numLines == len(points) - 1:
                    return cost

                componenti = -1
                for k in range(len(components)):
                    if i in components[k]:
                        componenti = k
                        break

                if componenti != -1 and j in components[componenti]:
                    continue
                
                componentj = -1
                for k in range(len(components)):
                    if j in components[k]:
                        componentj = k
                        break

                numLines += 1
                cost += d
                if componenti == -1 and componentj == -1:
                    components.append(set([i, j]))
                elif componenti != -1 and componentj == -1:
                    components[componenti].add(j)
                elif componenti == -1 and componentj != -1:
                    components[componentj].add(i)
                else:
                    components[componenti].update(components[componentj])
                    components.pop(componentj)
        return cost

solution = Solution()

# Expected: 20
print(solution.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))

# Expected: 18
print(solution.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
