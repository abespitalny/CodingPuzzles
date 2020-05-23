'''
Given a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''
from leetcode import *

# Both the recursive and iterative approaches are linear in time and space.
def is_symmetric_recurse_helper(root_left: TreeNode, root_right: TreeNode) -> bool:
    if (root_left is None) or (root_right is None):
        return root_left == root_right
    elif root_left.val != root_right.val:
        return False
    return (is_symmetric_recurse_helper(root_left.left, root_right.right)
        and is_symmetric_recurse_helper(root_left.right, root_right.left))

def is_symmetric_recurse(root: TreeNode) -> bool:
    if root is None:
        return True
    return is_symmetric_recurse_helper(root.left, root.right)

def is_symmetric_iterate(root: TreeNode) -> bool:
    if root is None:
        return True
    stack = [(root.left, root.right)]
    while len(stack) != 0:
        node1, node2 = stack.pop()
        if (node1 is None) or (node2 is None):
            if node1 != node2:
                return False
        elif node1.val != node2.val:
            return False
        else:
            stack.append((node1.right, node2.left))
            stack.append((node1.left, node2.right))
    return True


# Expected: True
print(is_symmetric_recurse(construct_bin_tree_bfs_array([1,2,2,3,4,4,3])))
# Expected: False
print(is_symmetric_recurse(construct_bin_tree_bfs_array([1,2,2,None,3,None,3])))

print(is_symmetric_iterate(construct_bin_tree_bfs_array([1,2,2,3,4,4,3])))
print(is_symmetric_iterate(construct_bin_tree_bfs_array([1,2,2,None,3,None,3])))
