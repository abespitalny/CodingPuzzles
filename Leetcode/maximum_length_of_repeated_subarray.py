'''
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
'''
from leetcode import *

class Solution:
    # Bottom-up DP approach with space optimization
    # Time: O(m*n)
    # Space: O(min(m, n))
    def findLength(self, A: List[int], B: List[int]) -> int:
        if len(A) > len(B):
            A, B = B, A

        maxLength = 0
        prev = [0]*(len(A) + 1)
        cur = [0]*(len(A) + 1)
        for i in range(len(B)):
            for j in range(len(A)):
                length = 0
                if A[j] == B[i]:
                    length = prev[j] + 1
                    maxLength = max(maxLength, length)

                cur[j + 1] = length

            prev, cur = cur, prev

        return maxLength

solution = Solution()

assert solution.findLength([1,2,3,2,1], [3,2,1,4,7]) == 3
assert solution.findLength([0,0,0,0,0], [0,0,0,0,0]) == 5
