'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''
from leetcode import *

class Solution:
    # BFS approach.
    # Time: O(n)
    # Space: O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        output = []
        curLevel = [root]
        while len(curLevel) != 0:
            nextLevel = []
            curLevelVals = []
            for node in curLevel:
                curLevelVals.append(node.val)
                
                if node.left != None:
                    nextLevel.append(node.left)
                if node.right != None:
                    nextLevel.append(node.right)
            
            output.append(curLevelVals)
            curLevel = nextLevel
        return output
