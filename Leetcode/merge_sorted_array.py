'''
You are given two integer arrays nums1 and nums2,
sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''
from leetcode import *

class Solution:
    # Leetcode Tip: For problems that require modifying an array in-place, iterating backwards could be very helpful.
    # Time: O(m + n)
    # Space: O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        left = m - 1
        right = n - 1
        pos = len(nums1) - 1
        while left >= 0 and right >= 0:
            if nums1[left] >= nums2[right]:
                nums1[pos] = nums1[left]
                left -= 1
            else:
                nums1[pos] = nums2[right]
                right -= 1
            pos -= 1
        
        if left >= 0:
            while left >= 0:
                nums1[pos] = nums1[left]
                left -= 1
                pos -= 1
        elif right >= 0:
            while right >= 0:
                nums1[pos] = nums2[right]
                right -= 1
                pos -= 1
        return

solution = Solution()

nums1 = [1,2,3,0,0,0]
solution.merge(nums1, m = 3, nums2 = [2,5,6], n = 3)
# Expected: [1,2,2,3,5,6]
print(nums1)

nums1 = [1]
solution.merge(nums1, m = 1, nums2 = [], n = 0)
# Expected: [1]
print(nums1)

nums1 = [0]
solution.merge(nums1, m = 0, nums2 = [1], n = 1)
# Expected: [1]
print(nums1)
