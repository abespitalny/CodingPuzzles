'''
Given the root of a binary tree, the value of a target node target, and an integer k,
return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
'''
from leetcode import *

class Solution:
    # Time: O(n)
    # Space: O(n) to store the recursion stack and the path from root to target node.
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def findPath(root, target):
            if root is None:
                return None
            elif root == target:
                return {target}

            path = findPath(root.left, target)
            if path != None:
                path.add(root)
                return path
            path = findPath(root.right, target)
            if path != None:
                path.add(root)
                return path
            return None
        
        path = findPath(root, target)
        def distFromNode(root, dist, path, k, kDistNodes):
            if dist == k:
                kDistNodes.append(root.val)
            
            if root.left != None:
                if root.left in path:
                    distFromNode(root.left, dist - 1, path, k, kDistNodes)
                else:
                    distFromNode(root.left, dist + 1, path, k, kDistNodes)

            if root.right != None:
                if root.right in path:
                    distFromNode(root.right, dist - 1, path, k, kDistNodes)
                else:
                    distFromNode(root.right, dist + 1, path, k, kDistNodes)
        
        kDistNodes = []
        distFromNode(root, len(path) - 1, path, k, kDistNodes)
        return kDistNodes
