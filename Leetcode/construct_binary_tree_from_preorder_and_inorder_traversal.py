from leetcode import *

class Solution:
    # Recursive approach. Very similar to the problem for constructing a tree with inorder and postorder.
    # Time: O(n)
    # Space: O(n)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preIdx = 0
        idxMap = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(leftInIdx, rightInIdx):
            if leftInIdx > rightInIdx:
                return None

            root = TreeNode(preorder[self.preIdx])
            self.preIdx += 1
            rootIdx = idxMap[root.val]
            root.left = helper(leftInIdx, rootIdx - 1)
            root.right = helper(rootIdx + 1, rightInIdx)
            
            return root

        return helper(0, len(inorder) - 1)
