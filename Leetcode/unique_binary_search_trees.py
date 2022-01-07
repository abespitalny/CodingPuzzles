'''
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
'''
from leetcode import *

# Time: O(n^2), Space: O(n).
def num_trees(n: int) -> int:
    num_trees_memo = {0: 1, 1: 1}
    for i in range(2, n + 1):
        trees = 0
        for root in range(1, i + 1):
            left_num_trees = root - 1
            right_num_trees = i - root
            trees += (num_trees_memo[left_num_trees] * num_trees_memo[right_num_trees])
        num_trees_memo[i] = trees

    return num_trees_memo[n]

# Expected: 1
print(num_trees(1))

# Expected: 2
print(num_trees(2))

# Expected: 5
print(num_trees(3))

# Expected: 14
print(num_trees(4))

# Expected: 42
print(num_trees(5))
