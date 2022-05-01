'''
You are given an array of variable pairs equations and an array of real numbers values,
where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].
Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
'''
from leetcode import *

class Solution:
    # Time: O((V + E) * n) = O(m*n) where m is the number of equations and n is the number of queries.
    # Space: O(V + E + n) = O(m + n).
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for i in range(len(equations)):
            a, b = equations[i]
            edges = graph.setdefault(a, [])
            edges.append((b, values[i]))
            
            edges = graph.setdefault(b, [])
            edges.append((a, 1/values[i]))

        answers = [-1]*len(queries)
        for i in range(len(queries)):
            a, b = queries[i]
            if (a not in graph) or (b not in graph):
                continue

            stack = [(a, 1)]
            visited = set()
            while len(stack) != 0:
                var, val = stack.pop()
                if var == b:
                    answers[i] = val
                    break
                visited.add(var)
                
                for child in graph[var]:
                    if child[0] in visited:
                        continue
                    stack.append((child[0], val * child[1]))
        return answers

solution = Solution()

# Expected: [6.0,0.5,-1,1,-1]
print(solution.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))

# Expected: [3.75,0.4,5.0,0.2]
print(solution.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))

# Expected: [0.5,2.0,-1,-1]
print(solution.calcEquation(equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]))
