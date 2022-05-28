from leetcode import *

class Solution:
    # Recursive approach
    # Time: O(n)
    # Space: O(n)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root is None:
            return output
        
        def postorder(root):
            if root.left != None:
                postorder(root.left)
            if root.right != None:
                postorder(root.right)
            output.append(root.val)
        
        postorder(root)
        return output

    # Iterative solution from Wikipedia
    # Time: O(n), Space: O(n)
    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        lastNode = None
        stack = []
        node = root
        while node != None or len(stack) != 0:
            while node != None:
                stack.append(node)
                node = node.left

            peek = stack[-1]
            if peek.right != None and peek.right != lastNode:
                node = peek.right
            else:
                lastNode = stack.pop()
                output.append(lastNode.val)

        return output
