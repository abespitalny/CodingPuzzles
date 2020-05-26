'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''
from leetcode import *

# Linear in time and space.
def is_balanced(root: TreeNode) -> bool:
    if root is None:
        return True
    if not(is_balanced(root.left) and is_balanced(root.right)):
        return False

    height_left = 0 if root.left is None else root.left.val
    height_right = 0 if root.right is None else root.right.val
    if abs(height_left - height_right) > 1:
        return False
    root.val = 1 + max(height_left, height_right)
    return True


print(is_balanced(construct_bin_tree_bfs_array([3,9,20,None,None,15,7])))
print(is_balanced(construct_bin_tree_bfs_array([1,2,2,3,3,None,None,4,4])))
print(is_balanced(construct_bin_tree_bfs_array([1,2,2,3,None,None,3,4,None,None,4])))
