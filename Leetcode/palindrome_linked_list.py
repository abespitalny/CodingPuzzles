'''
Given the head of a singly linked list, return true if it is a palindrome.
'''
from leetcode import *

class Solution:
    # Time: O(n)
    # Space: O(n)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        ptr = head
        while ptr != None:
            arr.append(ptr.val)
            ptr = ptr.next
        return (arr == list(reversed(arr)))

    # Very messy. The Leetcode version of this is based on the same idea, but is much cleaner.
    # Also, it's good practice to restore the linked list after modifying it in-place.
    # Time: O(n)
    # Space: O(1) by modifying the linked list in-place.
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        length = 0
        ptr = head
        while ptr != None:
            length += 1
            ptr = ptr.next

        mid = length // 2
        i = 0
        prev = None
        ptr = head
        while ptr != None:
            if i < mid:
                nextPtr = ptr.next
                ptr.next = prev
                prev = ptr
                ptr = nextPtr
            else:
                if i == mid and length % 2 != 0:
                    ptr = ptr.next
                else:
                    if ptr.val != prev.val:
                        return False
                    ptr = ptr.next
                    prev = prev.next
            i += 1

        return True

solution = Solution()

# Expected: True
print(solution.isPalindrome(construct_linked_list_array([1,2,2,1])))

# Expected: False
print(solution.isPalindrome(construct_linked_list_array([1,2])))

# Expected: True
print(solution.isPalindrome2(construct_linked_list_array([1,2,2,1])))

# Expected: False
print(solution.isPalindrome2(construct_linked_list_array([1,2])))
