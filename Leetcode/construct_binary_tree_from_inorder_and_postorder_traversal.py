'''
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree
and postorder is the postorder traversal of the same tree, construct and return the binary tree.
'''
from leetcode import *

class Solution:
    # Iterative approach
    # Time: O(n^2). I think it's n^2 because we do a linear search for the root in an array. We could speed this up by using hashmap as demonstrated by the next function.
    # Space: O(n)
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        root = TreeNode(inorder)
        stack = [root]
        for r in reversed(postorder):
            node = stack.pop()
            if len(node.val) == 1:
                node.val = node.val[0]
                continue

            rootIdx = node.val.index(r)
            leftChildren = node.val[:rootIdx]
            if len(leftChildren) > 0:
                node.left = TreeNode(leftChildren)
                stack.append(node.left)
                
            rightChildren = node.val[rootIdx + 1:]
            if len(rightChildren) > 0:
                node.right = TreeNode(rightChildren)
                stack.append(node.right)
            
            node.val = node.val[rootIdx]
        return root

    # Time: O(n)
    # Space: O(n)
    def buildTree2(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        root = TreeNode()
        idxMap = {val: idx for idx, val in enumerate(inorder)}
        stack = [(root, 0, len(inorder) - 1)]

        for r in reversed(postorder):
            node, leftIdx, rightIdx = stack.pop()
            if leftIdx == rightIdx:
                node.val = inorder[leftIdx]
                continue

            rootIdx = idxMap[r]
            if rootIdx > leftIdx:
                node.left = TreeNode()
                stack.append((node.left, leftIdx, rootIdx - 1))

            if rightIdx > rootIdx:
                node.right = TreeNode()
                stack.append((node.right, rootIdx + 1, rightIdx))
            
            node.val = r
        return root

    # There's also a recursive solution which is really similar to the approach in buildTree2.

solution = Solution()

print_bin_tree_bfs(solution.buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]))
print_bin_tree_bfs(solution.buildTree2(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]))

print_bin_tree_bfs(solution.buildTree(inorder = [-1], postorder = [-1]))
print_bin_tree_bfs(solution.buildTree2(inorder = [-1], postorder = [-1]))
