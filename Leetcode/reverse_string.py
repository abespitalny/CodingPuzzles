'''
Write a function that reverses a string. The input string is given as an array of characters s.
'''
from leetcode import *

# Time: O(n).
# Space: O(1).
class Solution:
    # Time: O(n)
    # Space: O(1)
    def reverseString(self, s: List[str]) -> None:
        halfLen = len(s) // 2
        i = 0
        while i < halfLen:
            temp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = temp
            i += 1

    # Recursion approach
    # Time: O(n)
    # Space: O(n)
    def reverseString2(self, s: List[str]) -> None:
        def helper(s, start, end):
            if (end - start) < 1:
                return
            s[start], s[end] = s[end], s[start]
            helper(s, start + 1, end - 1)

        helper(s, 0, len(s) - 1)


solution = Solution()

s = ["h","e","l","l","o"]
solution.reverseString(s)
print(s)

s = ["H","a","n","n","a","h"]
solution.reverseString(s)
print(s)
