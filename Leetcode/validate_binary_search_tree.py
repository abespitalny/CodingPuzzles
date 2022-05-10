'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
'''
from leetcode import *

class Solution:
    # Time: O(n) where n is the number of nodes in the BST.
    # Space: O(n) because we store the entire tree in an array after inorder traversal.
    # This is not the smartest implementation of the inorder traversal version because we don't need to store the entire array.
    # Instead, we can just store the previous value and check it against the current node while performing the inorder traversal.
    # Also, we can do this iteratively.
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.bstArray = []
        
        def inorder(root):
            if root is None:
                return
            
            if root.left != None:
                inorder(root.left)
            self.bstArray.append(root)
            if root.right != None:
                inorder(root.right)

        inorder(root)
        prev = self.bstArray[0]
        for i in range(1, len(self.bstArray)):
            if self.bstArray[i].val <= prev.val:
                return False
            prev = self.bstArray[i]
        return True

    # Recursive solution
    # Time: O(n)
    # Space: O(H) where H is the height of the BST.
    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        def recurse(root: TreeNode, minVal: int, maxVal: int):
            if root is None:
                return True
            elif root.val <= minVal or root.val >= maxVal:
                return False
            else:
                return recurse(root.left, minVal, root.val) and recurse(root.right, root.val, maxVal)
        
        return recurse(root, -math.inf, math.inf)

solution = Solution()

# Expected: True
print(solution.isValidBST(construct_bin_tree_bfs_array([2,1,3])))
print(solution.isValidBST2(construct_bin_tree_bfs_array([2,1,3])))

# Expected: False
print(solution.isValidBST(construct_bin_tree_bfs_array([5,1,4,None,None,3,6])))
print(solution.isValidBST2(construct_bin_tree_bfs_array([5,1,4,None,None,3,6])))
