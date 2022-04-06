'''
Write a function that reverses a string. The input string is given as an array of characters s.
'''
from leetcode import *

# Time: O(n).
# Space: O(1).
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        halfLen = len(s) // 2
        i = 0
        while i < halfLen:
            temp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = temp
            i += 1

solution = Solution()

s = ["h","e","l","l","o"]
solution.reverseString(s)
print(s)

s = ["H","a","n","n","a","h"]
solution.reverseString(s)
print(s)
