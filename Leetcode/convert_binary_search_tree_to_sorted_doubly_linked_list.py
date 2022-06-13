'''
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list.
For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place.
After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor.
You should return the pointer to the smallest element of the linked list.
'''
from leetcode import *

class Solution:
    # Time: O(n)
    # Space: O(n)
    def treeToDoublyList(self, root: 'Optional[TreeNode]') -> 'Optional[TreeNode]':
        self.head = None
        self.prev = None

        def inorder(root):
            if root.left != None:
                inorder(root.left)
            
            if self.head is None:
                self.head = root
            
            root.left = self.prev
            if self.prev != None:
                self.prev.right = root
            self.prev = root
            
            if root.right != None:
                inorder(root.right)            

        if root is None:
            return self.head
        inorder(root)
        
        self.head.left = self.prev
        self.prev.right = self.head

        return self.head
