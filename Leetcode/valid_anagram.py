'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
from leetcode import *

class Solution:
    # Hashtable approach
    # Time: O(n) where n is the length of s and t
    # Space: O(1) because we use a constant size hashtable since there are only 26 letters.
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = Counter(s)
        for i in t:
            count = counter.get(i, 0)
            if count == 0:
                return False
            counter[i] = count - 1
        return True

solution = Solution()

assert solution.isAnagram(s = "anagram", t = "nagaram") == True
assert solution.isAnagram(s = "rat", t = "car") == False
