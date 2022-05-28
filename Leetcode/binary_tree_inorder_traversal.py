from leetcode import *

class Solution:
    # Iterative approach
    # Time: O(n)
    # Space: O(n)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root is None:
            return output
        
        stack = [root]
        node = root.left
        while node != None:
            stack.append(node)
            node = node.left
        
        while len(stack) > 0:
            node = stack.pop()
            output.append(node.val)

            node = node.right
            if node != None:
                stack.append(node)
                node = node.left
                while node != None:
                    stack.append(node)
                    node = node.left

        return output
    
    # From Leetcode, this is a better iterative answer.
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = []
        node = root
        while node != None or len(stack) > 0:
            while node != None:
                stack.append(node)
                node = node.left

            node = stack.pop()
            output.append(node.val)
            node = node.right

        return output
