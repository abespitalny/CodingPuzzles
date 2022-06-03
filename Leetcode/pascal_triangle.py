'''
Given an integer numRows, return the first numRows of Pascal's triangle.
'''
from leetcode import *

class Solution:
    # Time: O(n^2) where n is the number of rows
    # Space: O(1) if we exclude the output.
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
            triangle.append(row)
        return triangle

solution = Solution()

# Expected: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print(solution.generate(5))

# Expected: [[1]]
print(solution.generate(1))
