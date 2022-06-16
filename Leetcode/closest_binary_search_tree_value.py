'''
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
'''
from leetcode import *

class Solution:
    # Time: O(log(n))
    # Space: O(1)
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        node = root
        closest = math.inf
        while node != None:
            if abs(target - node.val) < abs(target - closest):
                closest = node.val
            
            if target == node.val:
                return node.val
            elif target < node.val:
                node = node.left
            else:
                node = node.right
        return closest
