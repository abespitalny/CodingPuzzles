'''
Given the root of a binary tree, return the maximum average value of a subtree of that tree.

A subtree of a tree is any node of that tree plus all its descendants.

The average value of a tree is the sum of its values, divided by the number of nodes.
'''
from leetcode import *

class Solution:
    # Time: O(n)
    # Space: O(H) where H is the height of the tree.
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        if root is None:
            return 0
        
        def postorder(root):
            numNodes = 1
            nodeSum = root.val
            maxAvgLeft = 0
            maxAvgRight = 0
            
            if root.left != None:
                numNodesLeft, nodeSumLeft, maxAvgLeft = postorder(root.left)
                
                numNodes += numNodesLeft
                nodeSum += nodeSumLeft
            
            if root.right != None:
                numNodesRight, nodeSumRight, maxAvgRight = postorder(root.right)

                numNodes += numNodesRight
                nodeSum += nodeSumRight
            
            return (numNodes, nodeSum, max(maxAvgLeft, maxAvgRight, nodeSum / numNodes))
        
        _, _, maxAvg = postorder(root)
        return maxAvg
