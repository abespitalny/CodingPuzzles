'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''
from leetcode import *

class Solution:
    # Time: O(n)
    # Space: O(1)
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        ptr = dummy.next
        while ptr != None:
            if ptr.val == val:
                prev.next = ptr.next
            else:
                prev = ptr

            ptr = ptr.next

        return dummy.next
