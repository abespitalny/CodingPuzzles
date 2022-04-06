'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
'''
from leetcode import *

# Time: O(n). From Leetcode, this can be done in a single pass by maintaining a node k nodes behind the current node.
# Space: O(1).
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        ptr = head
        while ptr != None:
            length += 1
            ptr = ptr.next

        ptr = head
        index = 1
        kStart = kEnd = None
        while ptr != None:
            if index == k:
                kStart = ptr
            if index == (length - k + 1):
                kEnd = ptr

            ptr = ptr.next
            index += 1

        if kStart != None and kEnd != None:
            temp = kStart.val
            kStart.val = kEnd.val
            kEnd.val = temp
        return head
