'''
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that
every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
'''
from leetcode import *

# From leetcode, there's an O(n) time and O(1) space solution using Morris in-order traversal.
class Solution:
    # Recursion
    # Time: O(n)
    # Space: O(H)
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        self.runningTotal = 0
        def inOrder(root: TreeNode) -> None:
            if root.right != None:
                inOrder(root.right)
            
            self.runningTotal += root.val
            root.val = self.runningTotal
            
            if root.left != None:
                inOrder(root.left)

        inOrder(root)
        return root
    
    # Iterative
    # Time: O(n)
    # Space: O(H)
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack = []
        node = root
        while node != None:
            stack.append(node)
            node = node.right
        
        runningTotal = 0
        while len(stack) != 0:
            node = stack.pop()
            runningTotal += node.val
            node.val = runningTotal
            if node.left != None:
                node = node.left
                while node != None:
                    stack.append(node)
                    node = node.right
        return root
