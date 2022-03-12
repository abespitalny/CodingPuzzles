'''
Given the head of a linked list, rotate the list to the right by k places.
'''
from leetcode import *

# Time: O(n) where n is the length of the linked list.
# Space: O(1).
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        listLen = 0
        ptr = head
        while ptr != None:
            ptr = ptr.next
            listLen += 1
        
        if listLen <= 1:
            return head

        k = (k % listLen)
        if k <= 0:
            return head
        
        ptr = head
        index = 0
        while ptr != None:
            if index == (listLen - k - 1):
                newHead = ptr.next
                ptr.next = None
                
                ptr = newHead
                while ptr.next != None:
                    ptr = ptr.next
                
                ptr.next = head
                head = newHead
                break

            ptr = ptr.next
            index += 1
        return head

solution = Solution()

# Expected: [4,5,1,2,3]
print_linked_list(solution.rotateRight(construct_linked_list_array([1,2,3,4,5], 2)))

# Expected: [2,0,1]
print_linked_list(solution.rotateRight(construct_linked_list_array([0,1,2], 4)))
