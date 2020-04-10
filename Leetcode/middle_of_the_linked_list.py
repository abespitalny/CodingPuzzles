'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
'''

# Definition for singly-linked list:
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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

arr = [1, 2, 3, 4, 5]
head = ListNode(1)
ptr = head
for i in range(1, len(arr)):
    ptr.next = ListNode(arr[i])
    ptr = ptr.next

middle = middle_node(head)
print(f"val: {middle.val}, next: {middle.next}")

arr = [1, 2, 3, 4, 5, 6]
head = ListNode(1)
ptr = head
for i in range(1, len(arr)):
    ptr.next = ListNode(arr[i])
    ptr = ptr.next

middle = middle_node(head)
print(f"val: {middle.val}, next: {middle.next}")
