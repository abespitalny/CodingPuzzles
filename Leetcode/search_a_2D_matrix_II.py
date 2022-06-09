from leetcode import *

class Solution:
    # Divide and conquer approach. There's a slightly more efficient D&C approach that uses only 2 recursive calls instead of 3.
    # This other approach takes the middle column and finds the point in it where target should be using binary search.
    # If target is found then just return True; otherwise, recurse on the top-right and bottom-left sections.
    # Time: O((sqrt(n))^(log(3)) by applying the Master theorem for a = 3, b = 4, f(n) = O(1) where n = area of matrix.
    # Space: log(n) which is the max depth of recursion.
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def helper(topLeft, bottomRight):
            m = bottomRight[0] - topLeft[0]
            n = bottomRight[1] - topLeft[1]

            if m < 1 or n < 1:
                return False
            if m == 1 and n == 1:
                return (matrix[topLeft[0]][topLeft[1]] == target)

            centerRow = topLeft[0] + (m // 2)
            centerCol = topLeft[1] + (n // 2)

            if matrix[centerRow][centerCol] < target:
                return any([helper((centerRow + 1, topLeft[1]), (bottomRight[0], centerCol + 1)),
                            helper((topLeft[0], centerCol + 1), (centerRow + 1, bottomRight[1])),
                            helper((centerRow + 1, centerCol + 1), bottomRight)])
            elif matrix[centerRow][centerCol] > target:
                return any([helper(topLeft, (centerRow, centerCol)),
                            helper((centerRow, topLeft[1]), (bottomRight[0], centerCol)),
                            helper((topLeft[0], centerCol), (centerRow, bottomRight[1]))])
            else:
                return True

        return helper((0, 0), (len(matrix), len(matrix[0])))

    # Brilliant solution from Leetcode.
    # Time: O(m + n)
    # Space: O(1)
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) - 1
        col = 0
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        return False


solution = Solution()

# Expected: True
print(solution.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5))
print(solution.searchMatrix2(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5))

# Expected: False
print(solution.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))
print(solution.searchMatrix2(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))
