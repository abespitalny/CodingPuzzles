'''
You are given an n x n integer matrix. You can do the following operation any number of times:
- Choose any two adjacent elements of matrix and multiply each of them by -1.

Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.
'''
from leetcode import *

class Solution:
    # Greedy approach
    # Time: O(n^2)
    # Space: O(1)
    # Basic idea is that if there's an even number of negatives then we can do the operation specified in the problem statement to make them all positive.
    # Otherwise, we'll have at most one number in the matrix that's negative, and we should choose the minimum number for that negative number.
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        numNegatives = 0
        minNum = math.inf
        matrixSum = 0
        for i in range(n):
            for j in range(n):
                elem = matrix[i][j]
                absElem = abs(elem)
                matrixSum += absElem

                if elem < 0:
                    numNegatives += 1
                if absElem < minNum:
                    minNum = absElem

        if numNegatives % 2 == 0:
            return matrixSum
        return (matrixSum - 2*minNum)

solution = Solution()

# Expected: 4
print(solution.maxMatrixSum([[1,-1],[-1,1]]))

# Expected: 16
print(solution.maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]))
