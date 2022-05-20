'''
You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

You have an array arr of length length with all zeros, and you have some operation to apply on arr.
In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

Return arr after applying all the updates.
'''
from leetcode import *

class Solution:
    # Time: O(n + k) where n is length and k is the number of updates.
    # Space: O(1) excluding the output array.
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0]*length
        for start, end, inc in updates:
            ans[start] += inc
            if end < (length - 1):
                ans[end + 1] -= inc

        for i in range(1, length):
            ans[i] += ans[i - 1]

        return ans

solution = Solution()

# Expected: [-2,0,3,5,3]
print(solution.getModifiedArray(length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]))

# Expected: [0,-4,2,2,2,4,4,-4,-4,-4]
print(solution.getModifiedArray(length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]))
