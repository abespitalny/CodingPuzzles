'''
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return null.
'''
from leetcode import *

class Solution:
    # Time: O(n) in worst case and O(log(n)) in the average case.
    # Space: Same complexity as time.
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        elif root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)

    # Nice iterative approach
    # Time: O(n) in worst case and O(log(n)) in the average case.
    # Space: O(1).
    def searchBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None and root.val != val:
            if root.val < val:
                root = root.right
            else:
                root = root.left
        return root
