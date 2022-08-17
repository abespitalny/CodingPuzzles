'''
Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
'''
from leetcode import *

class Solution:
    # Sliding window approach
    # Time: O(m + n)
    # Space: O(1) since the counter for t will only consist of upper and lower case letters which is a constant number.
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        tCount = Counter(t)
        numMatched = 0
        minLength = math.inf
        minWindow = (0, -1)

        left = 0
        right = -1
        while right < len(s):
            if numMatched != len(tCount):
                right += 1

                if right < len(s) and s[right] in tCount:
                    count = tCount[s[right]] - 1

                    if count == 0:
                        numMatched += 1
                    tCount[s[right]] = count

            else:
                if s[left] in tCount:
                    count = tCount[s[left]] + 1
                    
                    if count == 1:
                        numMatched -= 1
                    tCount[s[left]] = count
                left += 1

            if numMatched == len(tCount):
                length = right - left
                if length < minLength:
                    minLength = length
                    minWindow = (left, right)

        return s[minWindow[0]:(minWindow[1] + 1)]

    # There's an optimization here where we can create a new string s that has only the characters that show up in t,
    # and then perform the same sliding window approach on the new filtered string. See Leetcode for details.

solution = Solution()

assert solution.minWindow(s = "ADOBECODEBANC", t = "ABC") == "BANC"
assert solution.minWindow(s = "a", t = "a") == "a"
assert solution.minWindow(s = "a", t = "aa") == ""
