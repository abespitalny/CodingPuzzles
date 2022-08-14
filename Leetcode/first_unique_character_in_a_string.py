'''
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.
'''
from leetcode import *

class Solution:
    # Hash table approach
    # Time: O(n)
    # Space: O(1) since there are only 26 characters possible.
    def firstUniqChar(self, s: str) -> int:
        charCount = Counter(s)
        for i in range(len(s)):
            if charCount[s[i]] == 1:
                return i
        return -1

solution = Solution()

assert solution.firstUniqChar("leetcode") == 0
assert solution.firstUniqChar("loveleetcode") == 2
assert solution.firstUniqChar("aabb") == -1
