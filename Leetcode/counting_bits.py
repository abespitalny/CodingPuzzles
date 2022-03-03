'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
'''
from leetcode import *

# Time: O(n), Space: O(n).
# Use dynamic programming in a bottom-up approach to calculate the number of 1s.
# Also, some clever bit manipulation to determine if the current number is a power of 2.
class Solution:
    def countBits(self, n: int) -> List[int]:
        oneCount = [0]*(n + 1)
        for i in range(1, n + 1):
            # Only powers of 2 will be 0.
            if (i & (i - 1)) == 0:
                oneCount[i] = 1
                lastTwoPower = i
            else:
                oneCount[i] = oneCount[i - lastTwoPower] + 1
        return oneCount

solution = Solution()

# Expected: [0,1,1]
print(solution.countBits(2))

# Expected: [0,1,1,2,1,2]
print(solution.countBits(5))
