'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''
from leetcode import *

class Solution:
    # Heap approach
    # Time: O(log(k)*n) where n is the length of the final merged linked list and k is the number of linked lists.
    # Space: O(k) for storing the heap.
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            ptr = lists[i]
            if ptr != None:
                heap.append((ptr.val, i))

        if len(heap) == 0:
            return None

        heapq.heapify(heap)
        _, idx = heapq.heappop(heap)
        mergedList = lists[idx]
        mergedPtr = mergedList
        if mergedPtr.next != None:
            heapq.heappush(heap, (mergedPtr.next.val, idx))
            lists[idx] = mergedPtr.next

        while len(heap) != 0:
            _, idx = heapq.heappop(heap)
            mergedPtr.next = lists[idx]
            mergedPtr = mergedPtr.next

            if mergedPtr.next != None:
                heapq.heappush(heap, (mergedPtr.next.val, idx))
                lists[idx] = mergedPtr.next

        return mergedList

    # Divide-and-conquer approach
    # Time: O(log(k)*n)
    # Space: O(k) for the recursion depth
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1, list2):
            if list1 is None:
                return list2
            elif list2 is None:
                return list1

            ptr1 = list1
            ptr2 = list2

            mergedHead = ptr1
            if ptr2.val < ptr1.val:
                mergedHead = ptr2
                ptr2 = ptr2.next
            else:
                ptr1 = ptr1.next

            mergedPtr = mergedHead
            while (ptr1 != None) or (ptr2 != None):
                if ptr1 is None:
                    mergedPtr.next = ptr2
                    break
                elif ptr2 is None:
                    mergedPtr.next = ptr1
                    break
                else:
                    if ptr1.val < ptr2.val:
                        mergedPtr.next = ptr1
                        ptr1 = ptr1.next
                    else:
                        mergedPtr.next = ptr2
                        ptr2 = ptr2.next

                mergedPtr = mergedPtr.next

            return mergedHead


        def helper(start, end):
            if end < start:
                return None
            elif start == end:
                return lists[start]

            mid = start + ((end - start) // 2)
            list1 = helper(start, mid)
            list2 = helper(mid + 1, end)

            return merge(list1, list2)

        return helper(0, len(lists) - 1)


solution = Solution()

# Expected: [1, 1, 2, 3, 4, 4, 5, 6]
print_linked_list(solution.mergeKLists([construct_linked_list_array([1,4,5]), construct_linked_list_array([1,3,4]), construct_linked_list_array([2,6])]))
print_linked_list(solution.mergeKLists2([construct_linked_list_array([1,4,5]), construct_linked_list_array([1,3,4]), construct_linked_list_array([2,6])]))

# Expected: []
print_linked_list(solution.mergeKLists([]))
print_linked_list(solution.mergeKLists2([]))

# Expected: []
print_linked_list(solution.mergeKLists([construct_linked_list_array([])]))
print_linked_list(solution.mergeKLists2([construct_linked_list_array([])]))
