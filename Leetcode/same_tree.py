'''
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
'''
from leetcode import *

# Time: O(min((V_p + E_p), (V_q + E_q))), Space: min((V_p + E_p), (V_q + E_q)).
# It's linear in time and space with respect to the smaller of the two trees.
def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if (p is None) or (q is None):
        return p == q

    stack_p = [p]
    stack_q = [q]
    while len(stack_p) > 0 and len(stack_q) > 0:
        node_p = stack_p.pop()
        node_q = stack_q.pop()
        if node_p.val != node_q.val:
            return False

        if (node_p.left is not None) and (node_q.left is not None):
            stack_p.append(node_p.left)
            stack_q.append(node_q.left)
        elif node_p.left != node_q.left:
            return False
        
        if (node_p.right is not None) and (node_q.right is not None):
            stack_p.append(node_p.right)
            stack_q.append(node_q.right)
        elif node_p.right != node_q.right:
            return False

    return len(stack_p) == len(stack_q)
