from leetcode import *

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    # Iterative approach
    # Time: O(n)
    # Space: O(1)
    def connect(self, root: 'Node') -> 'Node':
        leftmost = root
        while leftmost != None:
            ptr = leftmost
            nextLeftmost = None
            prev = None
            while ptr != None:
                if ptr.left != None and ptr.right != None:
                    if prev != None:
                        prev.next = ptr.left
                    else:
                        nextLeftmost = ptr.left
                    ptr.left.next = ptr.right
                    prev = ptr.right

                elif ptr.left != None and ptr.right is None:
                    if prev != None:
                        prev.next = ptr.left    
                    else:
                        nextLeftmost = ptr.left
                    prev = ptr.left

                elif ptr.left is None and ptr.right != None:
                    if prev != None:
                        prev.next = ptr.right
                    else:
                        nextLeftmost = ptr.right
                    prev = ptr.right
                
                ptr = ptr.next
            
            leftmost = nextLeftmost

        return root
