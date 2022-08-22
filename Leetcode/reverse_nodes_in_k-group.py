'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''
from leetcode import *

class Solution:
    # Iterative approach
    # Time: O(n)
    # Space: O(1)
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        ptr = head
        while ptr != None:
            length += 1
            ptr = ptr.next

        group = 0
        numGroups = length // k

        dummy = ListNode()
        dummy.next = head
        prevGroupTail = dummy
        prev = None
        ptr = head        

        while group < numGroups:
            groupTail = ptr
            i = 0
            while i < k:
                temp = ptr.next
                ptr.next = prev
                prev = ptr
                ptr = temp
                i += 1
            
            groupTail.next = ptr
            prevGroupTail.next = prev
            prevGroupTail = groupTail

            group += 1

        return dummy.next

solution = Solution()

# Expected: [2,1,4,3,5]
print_linked_list(solution.reverseKGroup(construct_linked_list_array([1,2,3,4,5]), 2))
# Expected: [3,2,1,4,5]
print_linked_list(solution.reverseKGroup(construct_linked_list_array([1,2,3,4,5]), 3))
