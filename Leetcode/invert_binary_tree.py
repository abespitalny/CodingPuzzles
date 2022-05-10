'''
Given the root of a binary tree, invert the tree, and return its root.
'''
from leetcode import *

class Solution:
    # Recursive approach
    # Time: O(n) where n are the number of nodes in the tree.
    # Space: O(H) where H is the height of the tree.
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

solution = Solution()

# Expected: [4,7,2,9,6,3,1]
print_bin_tree_bfs(solution.invertTree(construct_bin_tree_bfs_array([4,2,7,1,3,6,9])))

# Expected: [2,3,1]
print_bin_tree_bfs(solution.invertTree(construct_bin_tree_bfs_array([2,1,3])))

# Expected: []
print_bin_tree_bfs(solution.invertTree(construct_bin_tree_bfs_array([])))
