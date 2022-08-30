'''
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
'''
from leetcode import *

class Solution:
    # Time: O(m*n)
    # Space: O(max(m, n)) for storing the temporary diagonal "rows". We're excluding the output which is m*n in size.
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        if m == 1:
            return mat[0]

        order = []
        alternate = False
        for i in range(m):
            row = []
            for j in range(min(i + 1, n)):
                row.append(mat[i - j][j])

            order.extend(reversed(row) if alternate else row)
            alternate = not(alternate)

        for i in range(1, n):
            row = []
            for j in range(min(n - i, m)):
                row.append(mat[m - 1 - j][i + j])

            order.extend(reversed(row) if alternate else row)
            alternate = not(alternate)

        return order


solution = Solution()

assert solution.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,4,7,5,3,6,8,9]
assert solution.findDiagonalOrder([[1,2],[3,4]]) == [1,2,3,4]
