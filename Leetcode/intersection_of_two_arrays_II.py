'''
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''
from leetcode import *

class Solution:
    # Hashmap approach
    # Time: O(m + n)
    # Space: O(m) for the dictionary of nums1. We're excluding the output. To reduce memory, we could
    # convert the smaller of the two arrays to a hashmap. Also, we could overwrite one of the passed in arrays instead of allocating additional
    # space for the output.
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Counter = Counter(nums1)
        intersection = []
        for i in nums2:
            if i in nums1Counter:
                count = nums1Counter[i]
                count -= 1
                if count == 0:
                    del nums1Counter[i]
                else:
                    nums1Counter[i] = count

                intersection.append(i)
        return intersection
