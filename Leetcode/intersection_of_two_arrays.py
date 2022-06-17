'''
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.
'''
from leetcode import *

class Solution:
    # Hashset approach.
    # Time: O(m + n)
    # Space: O(m + n)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Set = set(nums1)
        intersection = set()
        for i in nums2:
            if i in nums1Set:
                intersection.add(i)
        return list(intersection)
