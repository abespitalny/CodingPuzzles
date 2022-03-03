'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them.
If it is impossible to finish all courses, return an empty array.
'''
from leetcode import *

# Time: O(numCourses + len(prerequisites)) = O(V + E). This is basically finding the topological order of a directed acyclic graph (DAG) which has a runtime of O(V + E).
# Space: O(V + E) because storage for the adjacency list representation of the graph is O(E) and the queue of courses to take next is O(V).
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        
        courseOrder = []
        while len(coursesToTake) != 0:
            numCoursesToTake = len(coursesToTake)
            for i in range(numCoursesToTake):
                courseNum = coursesToTake.popleft()
                courseOrder.append(courseNum)
                courseNode = graph.pop(courseNum)
                
                for j in courseNode[1]:
                    prereqs = graph[j][0]
                    prereqs.remove(courseNum)
                    if len(prereqs) == 0:
                        coursesToTake.append(j)
        
        if len(courseOrder) != numCourses:
            return []
        else:
            return courseOrder

solution = Solution()

# Expected: [0,1]
print(solution.findOrder(numCourses = 2, prerequisites = [[1,0]]))

# Expected: [0,1,2,3]
print(solution.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))

# Expected: [0]
print(solution.findOrder(numCourses = 1, prerequisites = []))
