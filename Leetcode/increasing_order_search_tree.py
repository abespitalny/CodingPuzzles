'''
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree,
and every node has no left child and only one right child.
'''
from leetcode import *

class Solution:
    # Space: O(n).
    # Time: O(n).
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def inOrderTraversal(root: TreeNode) -> None:
            if root.left != None:
                inOrderTraversal(root.left)
            arr.append(root)
            if root.right != None:
                inOrderTraversal(root.right)
        inOrderTraversal(root)
        
        for i in range(len(arr) - 1):
            node = arr[i]
            node.left = None
            node.right = arr[i + 1]
        
        lastNode = arr[-1]
        lastNode.left = lastNode.right = None
        return arr[0]
    
    # From Leetcode, this solution relinks the tree in one pass by using a pointer.
    # Time: O(n).
    # Space: O(H), so the height of the tree.
    def increasingBST2(self, root: TreeNode) -> TreeNode:
        dummyNode = TreeNode(None)
        self.currentNode = dummyNode
        def inOrderTraversal(root: TreeNode) -> None:
            if root.left != None:
                inOrderTraversal(root.left)
            
            root.left = None
            self.currentNode.right = root
            self.currentNode = root
            
            if root.right != None:
                inOrderTraversal(root.right)
            return

        inOrderTraversal(root)
        return dummyNode.right
