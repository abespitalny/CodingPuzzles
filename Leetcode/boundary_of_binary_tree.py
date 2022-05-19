'''
The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right,
and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:
    - The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
    - If a node in the left boundary and has a left child, then the left child is in the left boundary.
    - If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
    - The leftmost leaf is not in the left boundary.

The right boundary is similar to the left boundary, except it is the right side of the root's right subtree.
Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.
'''
from leetcode import *

class Solution:
    # This was the simplest solution, but we could've also made use of preorder traversal with the help of a flag to determine
    # if node is root, left boundary, right boundary, or leaf.
    # Time: O(n) where n is the number of nodes in the tree.
    # Space: O(H) where H is the height of the tree
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        boundary = [root.val]
        # If there's a left boundary, add it!
        if root.left != None:
            def leftBoundaryOfBinaryTree(root, boundary):
                if root.left != None:
                    boundary.append(root.val)
                    leftBoundaryOfBinaryTree(root.left, boundary)
                elif root.right != None:
                    boundary.append(root.val)
                    leftBoundaryOfBinaryTree(root.right, boundary)
            
            leftBoundaryOfBinaryTree(root.left, boundary)
        
        # Add the leaves from left to right
        stack = [root]
        while len(stack) != 0:
            node = stack.pop()
            # It's a leaf!
            if (node.left is None) and (node.right is None) and node != root:
                boundary.append(node.val)

            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)

        # If there's a right boundary, add it (reverse order)!
        if root.right != None:
            def rightBoundaryOfBinaryTree(root, boundary):
                if root.right != None:
                    rightBoundaryOfBinaryTree(root.right, boundary)
                    boundary.append(root.val)
                elif root.left != None:
                    rightBoundaryOfBinaryTree(root.left, boundary)
                    boundary.append(root.val)
            
            rightBoundaryOfBinaryTree(root.right, boundary)

        return boundary
