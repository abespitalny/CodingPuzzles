from leetcode import *

class Solution:
    # Recursive approach
    # From Leetcode, this could be simplified a little:
    # if head is None or head.next is None:
    #   return head
    #
    #   p = self.reverseList(head.next)
    #   head.next.next = head
    #   head.next = None
    #   return p
    #
    # Time: O(n)
    # Space: O(n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(head, prev):
            if head is None:
                return head

            nextNode = head.next
            head.next = prev
            if nextNode != None:
                reversedHead = helper(nextNode, head)
                return reversedHead
            return head

        return helper(head, None)

    # Iterative approach
    # Time: O(n)
    # Space: O(1)
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        prev = None
        while ptr != None:
            temp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = temp
        return prev

solution = Solution()

# Expected: [5,4,3,2,1]
print_linked_list(solution.reverseList(construct_linked_list_array([1,2,3,4,5])))
print_linked_list(solution.reverseList2(construct_linked_list_array([1,2,3,4,5])))

# Expected: [2,1]
print_linked_list(solution.reverseList(construct_linked_list_array([1,2])))
print_linked_list(solution.reverseList2(construct_linked_list_array([1,2])))

# Expected: []
print_linked_list(solution.reverseList(construct_linked_list_array([])))
print_linked_list(solution.reverseList2(construct_linked_list_array([])))
