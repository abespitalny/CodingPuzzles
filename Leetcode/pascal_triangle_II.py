'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
'''
from leetcode import *

class Solution:
    # DP approach
    # Time: O(n^2) where n is the rowIndex.
    # Space: O(n)
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            nextRow = [1]
            for j in range(1, i):
                nextRow.append(row[j - 1] + row[j])
            nextRow.append(1)
            row = nextRow
        return row
    
    # A more memory-efficient DP approach would be to reuse the array for the next row instead of creating a new one.
    def getRow2(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
            row.append(1)
        return row

    # There's also a nice mathematical solution on Leetcode that uses Pascal's rule for combinatorics.

solution = Solution()

# Expected: [1,3,3,1]
print(solution.getRow(3))
print(solution.getRow2(3))

# Expected: [1]
print(solution.getRow(0))
print(solution.getRow2(0))

# Expected: [1,1]
print(solution.getRow(1))
print(solution.getRow2(1))
