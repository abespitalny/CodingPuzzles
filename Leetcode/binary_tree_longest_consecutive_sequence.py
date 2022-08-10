'''
Given the root of a binary tree, return the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
The longest consecutive path needs to be from parent to child (cannot be the reverse).
'''
from leetcode import *

class Solution:
    # Recursive approach
    # Time: O(n) where n is the number of nodes in the tree.
    # Space: O(H) where H is the height of the tree because of the recursive stack. O(log(n)) for average case and O(n) for worst case.
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.longest = 0

        def recurse(root):
            if root is None:
                return 0

            leftPath = recurse(root.left)
            if root.left != None and (root.val + 1) == root.left.val:
                leftPath += 1
            else:
                leftPath = 1

            rightPath = recurse(root.right)
            if root.right != None and (root.val + 1) == root.right.val:
                rightPath += 1
            else:
                rightPath = 1

            maxPath = max(leftPath, rightPath)
            self.longest = max(self.longest, maxPath)
    
            return maxPath

        recurse(root)
        return self.longest

solution = Solution()

assert solution.longestConsecutive(construct_bin_tree_bfs_array([1,None,3,2,4,None,None,None,5])) == 3
assert solution.longestConsecutive(construct_bin_tree_bfs_array([2,None,3,2,None,1,None])) == 2
