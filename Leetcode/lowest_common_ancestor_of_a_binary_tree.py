'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”
'''
from leetcode import *

class Solution:
    # Recursive approach
    # Time: O(n)
    # Space: O(n)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        
        def helper(root):
            if root is None:
                return False, False

            leftFound = helper(root.left)
            rightFound = helper(root.right)
            
            foundP = leftFound[0] or rightFound[0] or (root == p)
            foundQ = leftFound[1] or rightFound[1] or (root == q)
            if foundP and foundQ and self.lca is None:
                self.lca = root
            return foundP, foundQ

        helper(root)
        return self.lca

    # A simpler recursive approach from Leetcode
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor2(root.left, p, q)
        right = self.lowestCommonAncestor2(root.right, p, q)
        
        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root

    # There's an iterative approach to this problem as well on Leetcode.
