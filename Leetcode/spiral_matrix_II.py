'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
'''
from leetcode import *

# Time: O(n^2).
# Space: O(1).
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize matrix
        matrix = [[0]*n for i in range(n)]
        count = 1
        layers = math.floor((n + 1) // 2)
        for i in range(layers):
            # Top row
            for j in range(i, n - i):
                matrix[i][j] = count
                count += 1
            
            # Right column
            for j in range(i + 1, n - i - 1):
                matrix[j][n - i - 1] = count
                count += 1
            
            # Bottom row
            for j in range(n - i - 1, i, -1):
                matrix[n - i - 1][j] = count
                count += 1
            
            # Left column
            for j in range(n - i - 1, i, -1):
                matrix[j][i] = count
                count += 1

        return matrix

solution = Solution()

# Expected: [[1,2,3],[8,9,4],[7,6,5]]
print(solution.generateMatrix(3))

# Expected: [[1]]
print(solution.generateMatrix(1))
