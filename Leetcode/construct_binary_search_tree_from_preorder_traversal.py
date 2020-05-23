'''
Return the root node of a binary search tree that matches the given preorder traversal.

Note: 
- The values of preorder are distinct.
'''
from leetcode import *

# Time: O(n), Space: O(n).
# I thought it might be O(n^2) in the worst case, but you do not visit a node more than twice so it's linear.
def bst_from_preorder(preorder: List[int]) -> TreeNode:
    # Assume that there is at least one element in the preorder list.
    root = TreeNode(preorder[0])
    stack = [root]
    for i in range(1, len(preorder)):
        val = preorder[i]
        new_node = TreeNode(val)
        # This node's value is less than the previous one (i.e. it's parent node) meaning it's to the left of it.
        if preorder[i - 1] > val:
            stack[-1].left = new_node
        else:
            parent_node = stack.pop()
            while len(stack) != 0:
                if val < stack[-1].val:
                    break
                parent_node = stack.pop()
            parent_node.right = new_node
        stack.append(new_node)
    return root

# There is also a nice recursive algorithm, but Python's recursion stack limit makes me hesitate to implement
# recursion when there is a way to avoid it.

print_bin_tree_bfs(bst_from_preorder([8, 5, 1, 7, 10, 12]))
