from typing import List, Tuple, Set, Any, Optional
from collections import deque
import threading
import math
import random

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

def construct_linked_list_array(arr: List[Any]) -> ListNode:
    if len(arr) == 0:
        return None

    head = ListNode(arr[0])
    ptr = head
    for i in range(1, len(arr)):
        ptr.next = ListNode(arr[i])
        ptr = ptr.next
    return head

def print_linked_list(head: ListNode) -> None:
    ptr = head
    while ptr != None:
        print(ptr.val, end=' ')
        ptr = ptr.next
    print()
