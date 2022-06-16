'''
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer.
This child pointer may or may not point to a separate doubly linked list, also containing these special nodes.
These child lists may have one or more children of their own, and so on, to produce a multilevel data structure.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list.
Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.
'''
from leetcode import *

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    # DFS preorder traversal recursive approach.
    # Time: O(n)
    # Space: O(n) because in the worst case where the whole list goes vertically down we have a recursive stack of n.
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def helper(head):
            prev = None
            ptr = head
            while ptr != None:
                if ptr.child != None:
                    childHead, childTail = helper(ptr.child)
                    
                    nextPtr = ptr.next
                    ptr.next = childHead
                    childHead.prev = ptr
                    childTail.next = nextPtr
                    if nextPtr != None:
                        nextPtr.prev = childTail
                    ptr.child = None

                    prev = childTail
                    ptr = nextPtr
                else:
                    prev = ptr
                    ptr = ptr.next

            return (head, prev)
        
        head, _ = helper(head)
        return head
