from leetcode import *

class Solution:
    # Recursive solution
    # Time: O(n)
    # Space: O(n)
    def swapPairs(self, head: ListNode) -> ListNode:
        def helper(head):
            if head is None:
                return None
            if head.next is None:
                return head
            
            ptr = head.next.next
            head.next.next = head
            newHead = head.next
            head.next = helper(ptr)
            return newHead
        
        return helper(head)

    # Iterative solution.
    # Time: O(n)
    # Space: O(1)
    def swapPairs2(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head

        ptr = head
        prev = None
        head = head.next
        while ptr != None and ptr.next != None:
            temp = ptr.next.next
            ptr.next.next = ptr
            if prev != None:
                prev.next = ptr.next

            prev = ptr
            ptr = temp
        prev.next = ptr

        return head

solution = Solution()

# Expected: [2,1,4,3]
print_linked_list(solution.swapPairs(construct_linked_list_array([1,2,3,4])))
print_linked_list(solution.swapPairs2(construct_linked_list_array([1,2,3,4])))

# Expected: []
print_linked_list(solution.swapPairs(construct_linked_list_array([])))
print_linked_list(solution.swapPairs2(construct_linked_list_array([])))

# Expected: [1]
print_linked_list(solution.swapPairs(construct_linked_list_array([1])))
print_linked_list(solution.swapPairs2(construct_linked_list_array([1])))
