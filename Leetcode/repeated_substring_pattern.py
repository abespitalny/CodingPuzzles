'''
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
'''
from leetcode import *

# Time: O(n^2) because we're comparing n-length strings in a for loop.
# Space: O(n) to store the substring which can at most be n/2.
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub = ""
        halfLength = len(s) // 2
        for i in range(halfLength):
            sub += s[i]
            if len(s) % len(sub) == 0:
                timesRepeated = len(s) // len(sub)
                if s == (sub*timesRepeated):
                    return True
        return False

solution = Solution()

# Expectedd: True
print(solution.repeatedSubstringPattern("abab"))

# Expectedd: False
print(solution.repeatedSubstringPattern("aba"))

# Expectedd: True
print(solution.repeatedSubstringPattern("abcabcabcabc"))
