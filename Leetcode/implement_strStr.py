'''
Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution:
    # KMP algorithm from Wikipedia
    # Time: O(m + n) where m is length of haystack and n is length of needle.
    # Space: O(n)
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        elif len(needle) > len(haystack):
            return -1
        
        def calculateKMPTable(pattern):
            i = 1
            j = 0
            table = [-1]*len(pattern)

            while i < len(pattern):
                if pattern[i] == pattern[j]:
                    table[i] = table[j]
                else:
                    table[i] = j
                    while j >= 0 and pattern[i] != pattern[j]:
                        j = table[j]
                
                i += 1
                j += 1
            return table


        kmpTable = calculateKMPTable(needle)

        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return (i - j)
            else:
                j = kmpTable[j]
                if j == -1:
                    i += 1
                    j += 1

        return -1

    # Still KMP algorithm, but is clearer about what's going on.
    def strStr2(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        elif len(needle) > len(haystack):
            return -1

        def compute_lps(pattern):
            # Longest Proper Prefix that is suffix array
            lps = [0] * len(pattern)

            prefi = 0
            for i in range(1, len(pattern)):
                # Phase 3: roll the prefix pointer back until match or
                # beginning of pattern is reached
                while prefi > 0 and pattern[i] != pattern[prefi]:
                    prefi = lps[prefi - 1]

                # Phase 2: if match, record the LSP for the current `i`
                # and move prefix pointer
                if pattern[prefi] == pattern[i]:
                    prefi += 1
                    lps[i] = prefi

                # Phase 1: is implicit here because of the for loop and
                # conditions considered above
            return lps


        pattern_lps = compute_lps(needle)

        patterni = 0
        for i in range(len(haystack)):
            # Phase 3: if a mismatch was found, roll back the pattern
            # index using the information in LPS
            while patterni > 0 and needle[patterni] != haystack[i]:
                patterni = pattern_lps[patterni - 1]

            # Phase 2: if match
            if needle[patterni] == haystack[i]:
                # If the end of a pattern is reached, record a result
                # and use infromation in LPS array to shift the index
                if patterni == len(needle) - 1:
                    return (i - patterni)
                else:
                    # Move the pattern index forward
                    patterni += 1

            # Phase 1: is implicit here because of the for loop and 
            # conditions considered above
        return -1

solution = Solution()

assert solution.strStr(haystack = "hello", needle = "ll") == 2
assert solution.strStr2(haystack = "hello", needle = "ll") == 2

assert solution.strStr(haystack = "aaaaa", needle = "bba") == -1
assert solution.strStr2(haystack = "aaaaa", needle = "bba") == -1
