'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
