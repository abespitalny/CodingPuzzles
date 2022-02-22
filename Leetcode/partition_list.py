from leetcode import *

# Time: O(n), Space: O(1).
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        prevNode = None
        currentNode = head
        rightPartitionHead = rightPartitionCurrent = None
        
        while currentNode != None:
            if currentNode.val >= x:
                if rightPartitionHead is None:
                    rightPartitionHead = rightPartitionCurrent = currentNode
                else:
                    rightPartitionCurrent.next = currentNode
                    rightPartitionCurrent = currentNode
                
                if prevNode is not None:
                    prevNode.next = currentNode.next
                
                nextNode = currentNode.next
                currentNode.next = None
                currentNode = nextNode

                if head == rightPartitionCurrent:
                    head = currentNode
            else:
                prevNode = currentNode
                currentNode = currentNode.next
        
        # Add right partition onto left partition.
        if rightPartitionHead is not None:
            if prevNode is not None:
                prevNode.next = rightPartitionHead
            else:
                head = rightPartitionHead
        
        return head

solution = Solution()

# Expected: [1,2,2,4,3,5]
print_linked_list(solution.partition(construct_linked_list_array([1,4,3,2,5,2]), 3))

# Expected: [1,2]
print_linked_list(solution.partition(construct_linked_list_array([2,1]), 2))
