'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Return the linked list sorted as well.
'''
from leetcode import *

# Time: O(n).
# Space: O(1).
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        foundDup = False
        prevPtr = None
        ptr = head
        while ptr != None and ptr.next != None:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
                foundDup = True
            else:
                if foundDup:
                    if ptr == head:
                        head = None
                    elif prevPtr != None:
                        prevPtr.next = ptr.next
                    foundDup = False
                else:
                    prevPtr = ptr
                    if head is None:
                        head = ptr
                ptr = ptr.next
        
        if foundDup:
            if ptr == head:
                head = None
            elif prevPtr != None:
                prevPtr.next = ptr.next
        elif head is None:
            head = ptr

        return head

solution = Solution()

# Expected: [1,2,5]
print_linked_list(solution.deleteDuplicates(construct_linked_list_array([1,2,3,3,4,4,5])))

# Expected: [2,3]
print_linked_list(solution.deleteDuplicates(construct_linked_list_array([1,1,1,2,3])))
