from typing import List, Tuple, Set, Any, Optional, Dict
from collections import deque, Counter
import threading
import math
import random
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for singly-linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)

def print_bin_tree_bfs(root: TreeNode) -> None:
    queue = deque([root])
    while len(queue) != 0:
        # Popleft is O(1) for deques.
        node = queue.popleft()
        if node is not None:
            print(node.val, end=' ')
            left_node = node.left
            right_node = node.right
            if (left_node is not None) or (right_node is not None):
                queue.append(node.left)
                queue.append(node.right)
        else:
            print('null', end=' ')
    print()

def construct_bin_tree_bfs_array(arr: List[Any]) -> TreeNode:
    if len(arr) == 0:
        return None

    root = TreeNode(arr[0])
    pos = 1
    queue = deque([root])
    while len(queue) != 0:
        node = queue.popleft()
        if node is None or pos >= len(arr):
            continue
        else:
            if arr[pos] is None:
                node.left = None
            else:
                node.left = TreeNode(arr[pos])
            queue.append(node.left)
            pos += 1
            if arr[pos] is None:
                node.right = None
            else:
                node.right = TreeNode(arr[pos])
            queue.append(node.right)
            pos += 1
    return root

# To create a cycle, pos is used to denote the index of the node that tail's next pointer is connected to.
def construct_linked_list_array(arr: List[Any], pos = -1) -> ListNode:
    if len(arr) == 0:
        return None

    head = ListNode(arr[0])
    ptr = head
    cyclePtr = head if (pos == 0) else None
    for i in range(1, len(arr)):
        ptr.next = ListNode(arr[i])
        ptr = ptr.next

        if pos == i:
            cyclePtr = ptr

    ptr.next = cyclePtr
    return head

def print_linked_list(head: ListNode) -> None:
    ptr = head
    while ptr != None:
        print(ptr.val, end=' ')
        ptr = ptr.next
    print()
