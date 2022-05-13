'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
'''
from leetcode import *

class Solution:
    # Approach: breadth-first search starting from the 0s
    # Time: O(m*n)
    # Space: O(m*n) because the queue could contain m*n cells if the matrix is full of 0s and has only one 1.
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[None]*n for i in range(m)]
        
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    
                    if i > 0:
                        queue.append((i - 1, j))
                    if i < (m - 1):
                        queue.append((i + 1, j))
                    if j > 0:
                        queue.append((i, j - 1))
                    if j < (n - 1):
                        queue.append((i, j + 1))
        
        while len(queue) != 0:
            i, j = queue.popleft()
            if ans[i][j] != None:
                continue
            
            neighbors = []
            if i > 0:
                neighbors.append((i - 1, j))
            if i < (m - 1):
                neighbors.append((i + 1, j))
            if j > 0:
                neighbors.append((i, j - 1))
            if j < (n - 1):
                neighbors.append((i, j + 1))
            
            minNeighbor = math.inf
            for a, b in neighbors:
                if ans[a][b] is None:
                    queue.append((a, b))
                else:
                    minNeighbor = min(minNeighbor, ans[a][b])
            ans[i][j] = minNeighbor + 1
        return ans

    # There's a clever DP approach that requires 2 loops over the matrix.
    # The first goes from top left to bottom right considering only the top and left directions.
    # The second pass goes from bottom right to top left considering the bottom and right directions.
    # In each loop, we compare the current value of the cell to (min(neighbors) + 1).
    # This approach runs in O(m*n) time with O(1) space [ignoring the space needed for the output].

solution = Solution()

# Expected: [[0,0,0],[0,1,0],[0,0,0]]
print(solution.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))

# Expected: [[0,0,0],[0,1,0],[1,2,1]]
print(solution.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
