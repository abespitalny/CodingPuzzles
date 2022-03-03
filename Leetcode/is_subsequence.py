'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''
from leetcode import *

# Time: O(t), Space: O(1).
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        sIndex = 0
        for i in t:
            if i == s[sIndex]:
                sIndex += 1
            if sIndex == len(s):
                return True
        return False

solution = Solution()

# Expected: True
print(solution.isSubsequence("abc", "ahbgdc"))

# Expected: False
print(solution.isSubsequence("axc", "ahbgdc"))
