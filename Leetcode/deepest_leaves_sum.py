'''
Given the root of a binary tree, return the sum of values of its deepest leaves.
'''
from leetcode import *

class Solution:
    # BFS approach
    # Time: O(n) where n is the number of nodes in the tree.
    # Space: O(n) because a level (i.e., the last one) could contain up to n/2 nodes for a balanced binary tree.
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        curLevel = [root]
        while len(curLevel) != 0:
            nextLevel = []
            levelSum = 0
            for i in range(len(curLevel)):
                node = curLevel[i]
                if node.left != None:
                    nextLevel.append(node.left)
                if node.right != None:
                    nextLevel.append(node.right)
                levelSum += node.val
            
            curLevel = nextLevel
        return levelSum
