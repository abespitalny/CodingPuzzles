'''
Given the head of a linked list, return the list after sorting it in ascending order.
'''
from leetcode import *

# Time: O(n*log(n)), Space: O(log(n)) because of recursive call stack. We did this using mergesort. Heapsort wouldn't work, and quicksort has a worst case of O(n^2).
# There's a mergesort version (bottom-up approach, we used top-down approach here) that requires only O(1) space because it avoids recursion and uses iteration instead.
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        length = 0
        ptr = head
        while ptr != None:
            length += 1
            ptr = ptr.next
        
        return self.mergeSortList(head, length)
    
    def mergeSortList(self, head: ListNode, length: int) -> ListNode:
        # Base cases
        if length == 0:
            return None
        elif length == 1:
            return head
        elif length == 2:
            if head.val > head.next.val:
                newHead = head.next
                head.next = None
                newHead.next = head
                head = newHead
            
            return head
        
        # Split list in half
        nodeCount = 0
        middle = length // 2
        ptr = head
        secondHead = None
        while ptr != None:
            nodeCount += 1
            if nodeCount == middle:
                secondHead = ptr.next
                ptr.next = None
                break
            
            ptr = ptr.next
        
        # Perform mergesort on each half
        firstPtr = self.mergeSortList(head, middle)
        secondPtr = self.mergeSortList(secondHead, length - middle)
        
        # Merge back the two lists
        if firstPtr.val < secondPtr.val:
            head = firstPtr
            firstPtr = firstPtr.next
        else:
            head = secondPtr
            secondPtr = secondPtr.next
        
        ptr = head
        while firstPtr != None and secondPtr != None:
            if firstPtr.val < secondPtr.val:
                ptr.next = firstPtr
                ptr = firstPtr
                firstPtr = firstPtr.next
            else:
                ptr.next = secondPtr
                ptr = secondPtr
                secondPtr = secondPtr.next
        
        if firstPtr != None:
            ptr.next = firstPtr
        else:
            ptr.next = secondPtr
        return head

solution = Solution()

head = construct_linked_list_array([4,2,1,3])
# Expected: [1,2,3,4]
print_linked_list(solution.sortList(head))

head = construct_linked_list_array([-1,5,3,4,0])
# Expected: [-1,0,3,4,5]
print_linked_list(solution.sortList(head))

head = construct_linked_list_array([])
# Expected: []
print_linked_list(solution.sortList(head))
