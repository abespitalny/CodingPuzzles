'''
You are given an (n x n) 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
'''
from leetcode import *

# Note: Do not return anything, modify matrix in-place instead.
# Time: O(n^2), Space: O(1).
def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    # The number of shells in an (n x n) matrix (e.g., if n = 4, then the number of shells is 2).
    num_shells = n // 2 if n % 2 == 0 else (n - 1) // 2
    for i in range(num_shells):
        shell_n_end = n - i - 1
        for j in range(shell_n_end - i):
            old_num = matrix[j + i][shell_n_end]
            matrix[j + i][shell_n_end] = matrix[i][j + i]
            old_num, matrix[shell_n_end][shell_n_end - j] = matrix[shell_n_end][shell_n_end - j], old_num
            old_num, matrix[shell_n_end - j][i] = matrix[shell_n_end - j][i], old_num
            matrix[i][j + i] = old_num

# Another clever solution is to swap the up and down values horizontally across the middle
# and then transpose the resulting matrix to get a 90deg clockwise rotation.
# See details of my solution and this one in the notes.

arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rotate(arr)
# Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
print(arr)

arr = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]
rotate(arr)
# Expected: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
print(arr)
