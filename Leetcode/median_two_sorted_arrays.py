'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''
from leetcode import *

class Solution:
    # Binary search approach. Very tricky to actually implement. Relied heavily on geeksforgeeks.com solution :(
    # Time: O(min(log(m), log(n)))
    # Space: O(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums1 should be smaller than nums2 because of how we calculate the index for nums2.
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
    
        m = len(nums1)
        n = len(nums2)

        halfLength = (m + n + 1) // 2
        left = 0
        right = m

        # Basically, we're determining what the left half of the final merged array looks like.
        while left <= right:
            mid = (left + right) // 2
        
            # Rightmost element from left part from nums1, [left, mid).
            left1 = -math.inf if mid <= 0 else nums1[mid - 1]
            # Leftmost element from right part from nums1, [mid, right].
            right1 = math.inf if mid == m else nums1[mid]

            index2 = halfLength - mid - 1
            # Rightmost element from left part from nums2, [0, halfLength - mid).
            left2 = -math.inf if index2 < 0 else nums2[index2]
            # Leftmost element from right part from nums2, [halfLength - mid, len(nums2)).
            right2 = math.inf if index2 == (n - 1) else nums2[index2 + 1]

            if left1 > right2:
                right = mid - 1
            elif right1 < left2:
                left = mid + 1
            else:
                # Merged array is even.
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
        return -1

solution = Solution()

assert solution.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]) == 2.0

assert solution.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]) == 2.5
