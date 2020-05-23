'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
'''
from leetcode import *

# O(n) algorithm:
def middle_node(head: ListNode) -> ListNode:
    if head is None:
        return head

    list_len = 1
    ptr = head.next
    while ptr is not None:
        list_len += 1
        ptr = ptr.next

    middle_ind = list_len // 2
    ptr = head
    while middle_ind > 0:
        middle_ind -= 1
        ptr = ptr.next
    return ptr

# A much smarter solution that only requires one pass through the linked list:
# def middle_node(head: ListNode) -> ListNode:
#     slow_ptr = head
#     fast_ptr = head
#     while fast_ptr and fast_ptr.next:
#         slow_ptr = slow_ptr.next
#         fast_ptr = fastPtr.next.next
#     return slow_ptr


middle = middle_node(construct_linked_list_array([1, 2, 3, 4, 5]))
print(f"val: {middle.val}, next: {middle.next}")

middle = middle_node(construct_linked_list_array([1, 2, 3, 4, 5, 6]))
print(f"val: {middle.val}, next: {middle.next}")
