'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.s
'''
from leetcode import *

# Time: O(n).
# Space: O(n) in worst case for a tree with just left nodes for example. In a balanced tree, it would be O(log(n)).
# We can come up with a tail recursion and iterative solution to this problem as well.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

solution = Solution()

# Expected: 3
print(solution.maxDepth(construct_bin_tree_bfs_array([3,9,20,None,None,15,7])))

# Expected: 2
print(solution.maxDepth(construct_bin_tree_bfs_array([1,None,2])))
