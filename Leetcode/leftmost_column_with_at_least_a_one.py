'''
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix,
this row is sorted in non-decreasing order.
Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it.
If such index doesn't exist, return -1.
You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:
- BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
- BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.

Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.
Also, any solutions that attempt to circumvent the judge will result in disqualification.
'''
from leetcode import *

# This is for testing purposes only!!
class BinaryMatrix:
    def __init__(self, mat):
        self.mat = mat
    def get(self, row: int, col: int) -> int:
        return self.mat[row][col]
    def dimensions(self) -> List[int]:
        return [len(self.mat), len(self.mat[0])]

# Time: O(rows * log(cols)), Space: O(1).
def leftmost_column_with_one(binaryMatrix: 'BinaryMatrix') -> int:
    rows, cols = binaryMatrix.dimensions()
    min_one_col_ind = cols
    for i in range(rows):
        # Perform binary search on the row to find the first 1:
        start = 0
        end = cols - 1
        one_col_ind = -1
        while start <= end:
            mid = (start + end) // 2
            # Go to the right to see if there is a 1 to the right:
            if binaryMatrix.get(i, mid) == 0:
                start = mid + 1
            # Go to the left to see if there is a 1 that's closer to the left:
            else:
                one_col_ind = mid
                end = mid - 1

        if one_col_ind != -1:
            if one_col_ind == 0:
                return 0
            elif one_col_ind < min_one_col_ind:
                min_one_col_ind = one_col_ind
    return -1 if (min_one_col_ind == cols) else min_one_col_ind

# This is a much smarter algorithm that runs in O(rows + cols) time and still has O(1) space complexity.
# This was from a Leetcode hint.
def leftmost_column_with_one_v2(binaryMatrix: 'BinaryMatrix') -> int:
    rows, cols = binaryMatrix.dimensions()
    ind = [0, cols - 1]
    min_one_col_ind = cols
    while (ind[0] < rows) and (ind[1] >= 0):
        if binaryMatrix.get(ind[0], ind[1]) == 1:
            min_one_col_ind = ind[1]
            ind[1] -= 1
        else:
            ind[0] += 1
    return -1 if (min_one_col_ind == cols) else min_one_col_ind

# Expected: 0
print(leftmost_column_with_one(BinaryMatrix([[0,0],[1,1]])))
# Expected: 1
print(leftmost_column_with_one(BinaryMatrix([[0,0],[0,1]])))
# Expected: -1
print(leftmost_column_with_one(BinaryMatrix([[0,0],[0,0]])))
# Expected: 1
print(leftmost_column_with_one(BinaryMatrix([[0,0,0,1],[0,0,1,1],[0,1,1,1]])))

print(leftmost_column_with_one_v2(BinaryMatrix([[0,0],[1,1]])))
print(leftmost_column_with_one_v2(BinaryMatrix([[0,0],[0,1]])))
print(leftmost_column_with_one_v2(BinaryMatrix([[0,0],[0,0]])))
print(leftmost_column_with_one_v2(BinaryMatrix([[0,0,0,1],[0,0,1,1],[0,1,1,1]])))
