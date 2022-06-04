'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
'''
from leetcode import *

# Iterative approach
# Time: O(|l1| + |l2|), and Space: O(1) since we are reusing the nodes.
def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    elif l2 is None:
        return l1

    if l1.val < l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next

    ptr = head
    while (l1 is not None) and (l2 is not None):
        if l1.val < l2.val:
            ptr.next = l1
            l1 = l1.next
        else:
            ptr.next = l2
            l2 = l2.next
        ptr = ptr.next

    if l1 is not None:
        ptr.next = l1
    elif l2 is not None:
        ptr.next = l2
    return head

# Recursion approach
# Time: O(m + n) where m is the length of l1 and n is the length of l2.
# Space: O(m + n)
def merge_two_lists2(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    
    def helper(head, l1, l2):
        if l1 is None:
            head.next = l2
            return
        if l2 is None:
            head.next = l1
            return

        if l1.val <= l2.val:
            head.next = l1
            helper(l1, l1.next, l2)
        else:
            head.next = l2
            helper(l2, l1, l2.next)

    helper(dummy, l1, l2)
    return dummy.next

# Expected: [1,1,2,3,4,4]
print_linked_list(merge_two_lists(construct_linked_list_array([1,2,4]), construct_linked_list_array([1,3,4])))
print_linked_list(merge_two_lists2(construct_linked_list_array([1,2,4]), construct_linked_list_array([1,3,4])))

# Expected: []
print_linked_list(merge_two_lists(construct_linked_list_array([]), construct_linked_list_array([])))
print_linked_list(merge_two_lists2(construct_linked_list_array([]), construct_linked_list_array([])))

# Expected: [0]
print_linked_list(merge_two_lists(construct_linked_list_array([]), construct_linked_list_array([0])))
print_linked_list(merge_two_lists2(construct_linked_list_array([]), construct_linked_list_array([0])))
