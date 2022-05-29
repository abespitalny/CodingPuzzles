from leetcode import *

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    # Recursive approach
    # Time: O(n)
    # Space: O(n). It's O(1) if we discount the recursion stack.
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def helper(root, rightNode):
            if root is None:
                return
            
            root.next = rightNode
            if rightNode != None:
                helper(root.right, rightNode.left)
            else:
                helper(root.right, None)
            
            helper(root.left, root.right)
        
        helper(root, None)
        return root
    
    # Iterative approach. We treat each level as a linked list.
    # Time: O(n)
    # Space: O(1)
    def connect2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root

        leftmost = root
        while leftmost.left != None:
            ptr = leftmost
            while ptr != None:
                ptr.left.next = ptr.right

                if ptr.next != None:
                    ptr.right.next = ptr.next.left

                ptr = ptr.next

            leftmost = leftmost.left
        return root
