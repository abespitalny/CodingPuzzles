'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).
'''
from leetcode import *

class Solution:
    # BFS
    # Time: O(n)
    # Space: O(n)
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        levels = []
        level = [root]
        alternate = False
        while len(level) != 0:
            nextLevel = [] 

            vals = []
            for node in reversed(level):
                vals.append(node.val)

                if alternate:
                    if node.right != None:
                        nextLevel.append(node.right)
                    if node.left != None:
                        nextLevel.append(node.left)
                else:
                    if node.left != None:
                        nextLevel.append(node.left)
                    if node.right != None:
                        nextLevel.append(node.right)

            alternate = not(alternate)
            levels.append(vals)
            level = nextLevel

        return levels
