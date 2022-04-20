from leetcode import *

class Solution:
    # Recursion
    # Time: O(H), so O(n) in worst-case and O(log(n)) in average-case.
    # Space: O(H)
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        return root
    
    # Using iteration instead of recursion brings down the space complexity to O(1).
