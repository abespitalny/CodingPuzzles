'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
'''
from leetcode import *

class Solution:
    # Recursive approach. There's an iterative version as well.
    # Time: O(H) where H is the height of the BST. O(log(N)) in average case and O(n) in worse.
    # Space: O(H)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        maxVal = max(p.val, q.val)
        minVal = min(p.val, q.val)
        
        def recurse(root):
            if root.val > maxVal:
                return recurse(root.left)
            elif root.val < minVal:
                return recurse(root.right)
            return root
        
        return recurse(root)
