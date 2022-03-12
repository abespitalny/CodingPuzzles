'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Return true if there is a cycle in the linked list. Otherwise, return false.
'''
from leetcode import *

# Time: O(n).
# Space: O(1).
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slowPtr = head
        fastPtr = head
        while fastPtr != None and fastPtr.next != None:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                return True
        return False

solution = Solution()

# Expected: True
print(solution.hasCycle(construct_linked_list_array([3,2,0,-4], 1)))

# Expected: True
print(solution.hasCycle(construct_linked_list_array([1,2], 0)))

# Expected: False
print(solution.hasCycle(construct_linked_list_array([1], -1)))
