'''
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
'''
from leetcode import *

# Time: O(n). Detect if there is a cycle in list. If there is, then starting from intersection of tortoise and hare algorithm find the start of cycle.
# Space: O(1).
# This explanation is courtesy of Leetcode:
# Let's say there are F nodes then a cycle of length C.
# If the tortoise goes F steps, then the hare goes 2F where F steps are in cycle C.
# Therefore, F + 2x = x (mod C) where x = C - F. x is tortoise's position and F + 2x is hare's position.
# Both of these coincide when x = C - F. Obviously, starting from the list's head and from the intersection of tortoise and hare,
# we will collide with each other after F steps which is exactly where the cycle begins!
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        slowPtr = head
        fastPtr = head
        hasCycle = False
        while fastPtr != None and fastPtr.next != None:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                hasCycle = True
                break
        
        if not(hasCycle):
            return None
        
        ptrInCycle = fastPtr
        ptrFromStart = head
        while ptrFromStart != ptrInCycle:
            ptrFromStart = ptrFromStart.next
            ptrInCycle = ptrInCycle.next
        return ptrInCycle

solution = Solution()

# Expected: 2
print(solution.detectCycle(construct_linked_list_array([3,2,0,-4], 1)))

# Expected: 1
print(solution.detectCycle(construct_linked_list_array([1,2], 0)))

# Expected: None
print(solution.detectCycle(construct_linked_list_array([1], -1)))
