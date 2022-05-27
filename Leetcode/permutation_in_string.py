'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
'''

class Solution:
    # Hashmap / Sliding window approach
    # Time: O(len(s2))
    # Space: O(1) since the diffCounter has at most only 26 entries.
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        # Keep count of the difference between substring of s2 and s1.
        diffCounter = {}
        for i in range(len(s1)):
            if s2[i] == s1[i]:
                continue

            count = diffCounter.get(s2[i], 0) + 1
            if count == 0:
                del diffCounter[s2[i]]
            else:
                diffCounter[s2[i]] = count
            
            count = diffCounter.get(s1[i], 0) - 1
            if count == 0:
                del diffCounter[s1[i]]
            else:
                diffCounter[s1[i]] = count

        if len(diffCounter) == 0:
            return True

        for i in range(len(s1), len(s2)):
            # Remove this character
            char = s2[i - len(s1)]
            count = diffCounter.get(char, 0) - 1
            if count == 0:
                del diffCounter[char]
            else:
                diffCounter[char] = count
            
            # Add this character
            char = s2[i]
            count = diffCounter.get(char, 0) + 1
            if count == 0:
                del diffCounter[char]
            else:
                diffCounter[char] = count
            
            if len(diffCounter) == 0:
                return True

        return False

solution = Solution()

# Expected: True
print(solution.checkInclusion(s1 = "ab", s2 = "eidbaooo"))

# Expected: False
print(solution.checkInclusion(s1 = "ab", s2 = "eidboaoo"))
