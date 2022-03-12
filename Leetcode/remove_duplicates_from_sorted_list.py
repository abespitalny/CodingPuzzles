'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''
from leetcode import *

# Time: O(n).
# Space: O(1).
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        while ptr != None and ptr.next != None:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return head

solution = Solution()

# Expected: [1,2]
print_linked_list(solution.deleteDuplicates(construct_linked_list_array([1,1,2])))

# Expected: [1,2,3]
print_linked_list(solution.deleteDuplicates(construct_linked_list_array([1,1,2,3,3])))
