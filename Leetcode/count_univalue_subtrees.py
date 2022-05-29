'''
Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.
'''
from leetcode import *

class Solution:
    # Time: O(n)
    # Space: O(n)
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.numUnivalTrees = 0
        if root is None:
            return self.numUnivalTrees

        def treeVal(root):
            leftValMatch = True
            if root.left != None:
                leftValMatch = (treeVal(root.left) == root.val)
            
            rightValMatch = True
            if root.right != None:
                rightValMatch = (treeVal(root.right) == root.val)
            
            if leftValMatch and rightValMatch:
                self.numUnivalTrees += 1
                return root.val
            return None
        
        treeVal(root)
        return self.numUnivalTrees
