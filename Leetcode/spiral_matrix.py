'''
Given an m x n matrix, return all elements of the matrix in spiral order.
'''
from leetcode import *

class Solution:
    # Setting the boundaries approach
    # Time: O(m*n)
    # Space: O(1) if we exclude the output which is m*n
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        numElems = m*n

        order = []
        start = (0, 0)
        end = (m - 1, n - 1)
        while len(order) < numElems:
            # Top row
            for i in range(start[1], end[1] + 1):
                order.append(matrix[start[0]][i])
            # Right column
            for i in range(start[0] + 1, end[0] + 1):
                order.append(matrix[i][end[1]])

            # Is this a rectangle?
            if (end[0] > start[0]) and (end[1] > start[1]):
                # Bottom row
                for i in range(end[1] - 1, start[1] - 1, -1):
                    order.append(matrix[end[0]][i])
                # Left column
                for i in range(end[0] - 1, start[0], -1):
                    order.append(matrix[i][start[1]])

            start = (start[0] + 1, start[1] + 1)
            end = (end[0] - 1, end[1] - 1)
        return order

solution = Solution()

assert solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
assert solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
