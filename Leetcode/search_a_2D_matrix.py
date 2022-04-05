'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
    - Integers in each row are sorted from left to right.
    - The first integer of each row is greater than the last integer of the previous row.
'''
from leetcode import *

# Time: O(log(m) + log(n)) = O(log(m*n)). Binary search on rows and then columns. Alternatively (from leetcode), we could treat the 2D matrix
# as one long array and get the row = (index // n) and column = (index % n) and then do a regular binary search. This'll be O(log(m*n)) which is the length
# of this one long 1D array.
# Space: O(1).
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Search row
        start = 0
        end = len(matrix)
        while start < (end - 1):
            mid = (start + end) // 2
            midCell = matrix[mid][0]
            
            if target < midCell:
                end = mid
            elif target > midCell:
                start = mid
            else:
                return True

        # Search column
        row = start
        start = 0
        end = len(matrix[0])
        while start < end:
            mid = (start + end) // 2
            midCell = matrix[row][mid]
            
            if target < midCell:
                end = mid
            elif target > midCell:
                start = mid + 1
            else:
                return True
        return False

solution = Solution()

# Expected: True
print(solution.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))

# Expected: False
print(solution.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
