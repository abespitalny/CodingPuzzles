'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
'''
from leetcode import *

class Solution:
    # Hashtable approach
    # Time: O(n*m) where n is the length of s and m is the length of p.
    # Space: O(m) to store the hashtable for p. We're excluding the output.
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagrams = []
        if len(p) > len(s):
            return anagrams

        anagram = Counter(p)
        counter = anagram.copy()
        right = 0
        for i in range(len(s) - len(p) + 1):
            isAnagram = True
            right = max(i, right)

            while right < (i + len(p)):
                count = counter.get(s[right], 0)

                if count == 0:
                    isAnagram = False
                    break

                counter[s[right]] -= 1
                right += 1

            if isAnagram:
                anagrams.append(i)
            if s[i] in counter:
                counter[s[i]] = min(anagram[s[i]], counter[s[i]] + 1)

        return anagrams

    # Simpler hashtable approach + sliding window
    # Time: O(n) because we're comparing hashtables which is of a limited size.
    # Space: O(1) since the hashtables will contain only 26 letters
    def findAnagrams2(self, s: str, p: str) -> List[int]:
        anagrams = []
        if len(p) > len(s):
            return anagrams

        pCounter = Counter(p)
        sCounter = Counter()
        for i in range(len(s)):
            if s[i] in sCounter:
                sCounter[s[i]] += 1
            else:
                sCounter[s[i]] = 1
            
            if i - len(p) >= 0:
                removeLetter = s[i - len(p)]
                count = sCounter[removeLetter] - 1
                if count == 0:
                    del sCounter[removeLetter]
                else:
                    sCounter[removeLetter] -= 1
            
            if sCounter == pCounter:
                anagrams.append(i - len(p) + 1)
        return anagrams


solution = Solution()

assert solution.findAnagrams(s = "cbaebabacd", p = "abc") == [0, 6]
assert solution.findAnagrams2(s = "cbaebabacd", p = "abc") == [0, 6]
assert solution.findAnagrams(s = "abab", p = "ab") == [0, 1, 2]
assert solution.findAnagrams2(s = "abab", p = "ab") == [0, 1, 2]
