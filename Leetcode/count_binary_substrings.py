'''
Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's,
and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.
'''
class Solution:
    # Time: O(n)
    # Space: O(1)
    def countBinarySubstrings(self, s: str) -> int:
        zeros = 0
        ones = 0

        ans = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                zeros += 1
            else:
                ones += 1

            if s[i] != s[i + 1]:
                ans += min(zeros, ones)
                if s[i] == "0":
                    ones = 0
                else:
                    zeros = 0

        if s[-1] == "0":
            zeros += 1
        else:
            ones += 1
        ans += min(zeros, ones)

        return ans

solution = Solution()

# Expected: 6
print(solution.countBinarySubstrings("00110011"))

# Expected: 4
print(solution.countBinarySubstrings("10101"))
