class Solution:
    # Time: O(n*k). We're finding the minimum of a dictionary with at most k elements.
    # Space: O(k). Again, the dictionary can grow to at most k.
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k < 1:
            return 0

        start = 0
        chars = {s[0]: 0}
        longestSubstr = 1
        for i in range(1, len(s)):
            if s[i] in chars:
                chars[s[i]] = i
            else:
                if len(chars) == k:
                    # Get char with minimum index
                    index, char = min([(val, key) for key, val in chars.items()])
                    del chars[char]
                    start = index + 1
                    chars[s[i]] = i
                else:
                    chars[s[i]] = i

            substringLen = i - start + 1
            if substringLen > longestSubstr:
                longestSubstr = substringLen
        return longestSubstr
    
    # We can reduce the time complexity by using an ordered dictionary. An ordered dictionary uses a hashmap and a doubly linked list to provide a kind of LRU cache.
    # See the LRU cache problem.

solution = Solution()

# Expected: 3
print(solution.lengthOfLongestSubstringKDistinct(s = "eceba", k = 2))

# Expected: 2
print(solution.lengthOfLongestSubstringKDistinct(s = "aa", k = 1))
