# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes in the copied list
such that the pointers in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y,
then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.
"""

# I'm not going to have example test cases because it's a waste of time to parse the input into the proper linked list structure.
# Therefore, this code isn't testable from here and must be submitted to Leetcode for testing.

# Time: O(n). We iterate through the original list twice.
# Space: O(n). We have a map of original nodes to indices.
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        ptr = head
        copyNodes = []
        oldNodeToIdx = {}
        while ptr != None:
            newNode = Node(ptr.val, None)
            oldNodeToIdx[ptr] = len(copyNodes)

            if len(copyNodes) > 0:
                copyNodes[-1].next = newNode
            copyNodes.append(newNode)
            
            ptr = ptr.next
        
        ptr = head
        i = 0
        while ptr != None:
            if ptr.random is None:
                copyNodes[i].random = None
            else:
                copyNodes[i].random = copyNodes[oldNodeToIdx[ptr.random]]

            i += 1
            ptr = ptr.next
        
        return copyNodes[0]
