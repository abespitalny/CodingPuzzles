'''
Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
'''
from leetcode import *

class Solution:
    # Recursive approach
    # Time: O(n)
    # Space: O(n)
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        
        sum -= root.val
        if root.left is None and root.right is None:
            return (sum == 0)
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        
        stack = [(root, sum)]
        while len(stack) != 0:
            node, sum = stack.pop()
            sum -= node.val
            if node.left is None and node.right is None:
                if sum == 0:
                    return True
                continue
                
            if node.right != None:
                stack.append((node.right, sum))
            if node.left != None:
                stack.append((node.left, sum))
        return False
