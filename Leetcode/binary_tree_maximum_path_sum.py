'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
A node can only appear in the sequence at most once.
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
'''
from leetcode import *

class Solution:
    # Recursive approach
    # Time: O(n)
    # Space: O(H) where H is the height of the binary tree.
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = -math.inf

        def helper(root):
            leftMaxPath = -math.inf
            if root.left != None:
                leftMaxPath = helper(root.left)

            rightMaxPath = -math.inf
            if root.right != None:
                rightMaxPath = helper(root.right)

            # This continues the length of a path
            maxPathWithRoot = max(leftMaxPath + root.val, rightMaxPath + root.val, root.val)
            # Max path if we decided to end path here
            self.maxPath = max(self.maxPath, leftMaxPath, rightMaxPath, leftMaxPath + rightMaxPath + root.val)

            return maxPathWithRoot

        maxLeftOrRightPath = helper(root)
        self.maxPath = max(self.maxPath, maxLeftOrRightPath)
        return self.maxPath

    # Leetcode's solution is the same, but it is a little cleaner.
    def maxPathSum2(self, root: Optional[TreeNode]) -> int:
        max_path = -math.inf

        def get_max_gain(node):
            nonlocal max_path
            if node is None:
                return 0

            # max sum on the left and right sub-trees of node
            gain_on_left = max(get_max_gain(node.left), 0)
            gain_on_right = max(get_max_gain(node.right), 0)
            
            # the price to start a new path where `node` is a highest node
            current_max_path = node.val + gain_on_left + gain_on_right
            
            # update max_sum if it's better to start a new path
            max_path = max(max_path, current_max_path)
        
            # for recursion:
            # return the max gain if continue the same path
            return node.val + max(gain_on_left, gain_on_right)

        get_max_gain(root)
        return max_path


solution = Solution()

assert solution.maxPathSum(construct_bin_tree_bfs_array([1,2,3])) == 6
assert solution.maxPathSum(construct_bin_tree_bfs_array([-10,9,20,None,None,15,7])) == 42
