'''
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees.
Since the answer may be too large, return it modulo 10**9 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.
'''
from leetcode import *

class Solution:
    # Time: O(n) where n is the number of nodes in the tree.
    # Space: O(H) where H is the height of the tree because of the recursion stack.
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def calcSum(root: TreeNode) -> int:
            if root is None:
                return 0
            root.val += calcSum(root.left) + calcSum(root.right)
            return root.val

        calcSum(root)

        self.totalSum = root.val
        self.maxProd = 0
        def splitTree(root: TreeNode) -> None:
            if root.left != None:
                product = root.left.val * (self.totalSum - root.left.val)
                if product > self.maxProd:
                    self.maxProd = product
                splitTree(root.left)

            if root.right != None:
                product = root.right.val * (self.totalSum - root.right.val)
                if product > self.maxProd:
                    self.maxProd = product
                splitTree(root.right)

        splitTree(root)
        return (self.maxProd) % (10**9 + 7)
    
    # If we wanted to do this without modifying the original tree, then we can store the subtree sums in an array and then perform the splitting
    # by checking the max product of the subtree sum and (total - subtree sum).

solution = Solution()

# Expected: 110
print(solution.maxProduct(construct_bin_tree_bfs_array([1,2,3,4,5,6,None])))

# Expected: 90
print(solution.maxProduct(construct_bin_tree_bfs_array([1,None,2,3,4,None,None,5,6])))
