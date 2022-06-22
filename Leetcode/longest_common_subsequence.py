'''
Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.
'''

class Solution:
    # Top-down DP approach.
    # Time: O(m*n)
    # Space: O(m*n)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        
        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            elif (i, j) in memo:
                return memo[(i, j)]
            
            if text1[i] == text2[j]:
                lcs = 1 + dp(i + 1, j + 1)
            else:
                lcs = max(dp(i + 1, j), dp(i, j + 1))
            
            memo[(i, j)] = lcs
            return lcs
        
        return dp(0, 0)

    # Bottom-up DP approach. Optimized space.
    # Time: O(m*n)
    # Space: O(n)
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)
        for i in range(len(text1) - 1, -1, -1):
            nextDp = [0] * (len(text2) + 1)
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    nextDp[j] = 1 + dp[j + 1]
                else:
                    nextDp[j] = max(dp[j], nextDp[j + 1])

            dp = nextDp

        return dp[0]


solution = Solution()

assert solution.longestCommonSubsequence(text1 = "abcde", text2 = "ace") == 3
assert solution.longestCommonSubsequence2(text1 = "abcde", text2 = "ace") == 3

assert solution.longestCommonSubsequence(text1 = "abc", text2 = "abc") == 3
assert solution.longestCommonSubsequence2(text1 = "abc", text2 = "abc") == 3

assert solution.longestCommonSubsequence(text1 = "abc", text2 = "def") == 0
assert solution.longestCommonSubsequence2(text1 = "abc", text2 = "def") == 0
