'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''
from leetcode import *

# Time: O(numCourses + len(prerequisites)) = O(V + E). This is basically finding the topological order of a directed acyclic graph (DAG) which has a runtime of O(V + E).
# Space: O(numCourses * len(prerequisites)) or O(V*E) because of the storage for the graph.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Form of graph, {node: ({incoming edges}, {outgoing edges})}.
        graph = {i:(set(), set()) for i in range(numCourses)}
        # Build graph
        for i in prerequisites:
            courseA = graph[i[0]]
            courseB = graph[i[1]]
            courseA[0].add(i[1])
            courseB[1].add(i[0])
        
        coursesToTake = deque()
        for i in graph:
            # No prereqs, so you can take the course.
            if len(graph[i][0]) == 0:
                coursesToTake.append(i)
        
        while len(coursesToTake) != 0:
            numCourses = len(coursesToTake)
            for i in range(numCourses):
                courseNum = coursesToTake.popleft()
                courseNode = graph.pop(courseNum)
                for j in courseNode[1]:
                    prereqs = graph[j][0]
                    prereqs.remove(courseNum)
                    if len(prereqs) == 0:
                        coursesToTake.append(j)                
        
        return (len(graph) == 0)

solution = Solution()

# Expected: True
print(solution.canFinish(2, [[1,0]]))

# Expected: False
print(solution.canFinish(2, [[1,0],[0,1]]))
