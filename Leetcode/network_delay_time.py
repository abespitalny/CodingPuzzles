'''
You are given a network of n nodes, labeled from 1 to n.
You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),
where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k.
Return the time it takes for all the n nodes to receive the signal.
If it is impossible for all the n nodes to receive the signal, return -1.
'''
from leetcode import *

class Solution:
    # Dijkstra's algorithm. This isn't the best implementation. There's a better one using a priority queue.
    # Time: O(V^2) where V is the number of nodes in the graph because we have to search through the unvisited nodes to find the one with smallest distance.
    # Space: O(V + E)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create graph
        graph = {}
        for u, v, w in times:
            edges = graph.setdefault(u - 1, [])
            edges.append((v - 1, w))

        # Dijkstra's algorithm
        distances = [math.inf]*n
        distances[k - 1] = 0
        visited = set()
        unvisited = set([k - 1])

        while len(unvisited) != 0:
            # To get the next visited node, we need to find the unvisited need with the smallest distance.
            minDist = math.inf
            for i in unvisited:
                if distances[i] < minDist:
                    minDist = distances[i]
                    node = i

            unvisited.remove(node)
            visited.add(node)
            if node not in graph:
                continue

            for v, w in graph[node]:
                if v not in visited:
                    distances[v] = min(distances[v], w + distances[node])
                    unvisited.add(v)

        maxDistance = max(distances)
        if maxDistance == math.inf:
            return -1
        return maxDistance

solution = Solution()

# Expected: 2
print(solution.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))

# Expected: 1
print(solution.networkDelayTime(times = [[1,2,1]], n = 2, k = 1))

# Expected: -1
print(solution.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))
