'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''
from leetcode import *

class Solution:
    # Time: O(m) where m is the length of magazine.
    # Space: O(1) since the counters will have at most 26 entries.
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        counterMag = Counter(magazine)
        counterNote = Counter(ransomNote)

        for i in counterNote:
            if i not in counterMag or counterMag[i] < counterNote[i]:
                return False
        return True

solution = Solution()

# Expected: False
print(solution.canConstruct(ransomNote = "a", magazine = "b"))

# Expected: False
print(solution.canConstruct(ransomNote = "aa", magazine = "ab"))

# Expected: True
print(solution.canConstruct(ransomNote = "aa", magazine = "aab"))
