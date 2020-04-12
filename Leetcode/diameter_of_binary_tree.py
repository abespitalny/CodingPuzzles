'''
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
Note: The length of path between two nodes is represented by the number of edges between them.
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# This is an O(V + E) algorithm, that is linear time in the number of nodes and edges.
def diameter_of_binary_tree(root: TreeNode) -> int:
    if root is None:
        return 0

    stack = [root]
    preorder_list = []
    while len(stack) != 0:
        # O(1) operation:
        visit_node = stack.pop()
        preorder_list.append(visit_node)

        left_node = visit_node.left
        if left_node is not None:
            # O(1) operation:
            stack.append(left_node)
        right_node = visit_node.right
        if right_node is not None:
            # O(1) operation:
            stack.append(right_node)

    diameter = 0
    # Iterate through the preorder list backwards in order to start from the children
    # and go up to the root (it's postorder in that case).
    for i in range(len(preorder_list) - 1, -1, -1):
        root = preorder_list[i]
        left_path = (-1 if root.left is None else root.left.val) + 1
        right_path = (-1 if root.right is None else root.right.val) + 1
        full_path = left_path + right_path
        if full_path > diameter:
            diameter = full_path
        root.val = max(left_path, right_path)
    return diameter

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(diameter_of_binary_tree(root))
