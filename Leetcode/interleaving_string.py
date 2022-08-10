'''
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
'''

class Solution:
    # Top-down DP approach
    # Time: O(L1*L2) where L1, L2, and L3 are the length of the strings s1, s2, and s3, respectively.
    # Space: O(L1*L2 + L3) = O(L1*L2)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1) + len(s2)) != len(s3):
            return False

        memo = {}

        def dp(i, j, k):
            if k == len(s3):
                return True
            elif (i, j, k) in memo:
                return memo[(i, j, k)]
            
            canInterleave = False
            if i < len(s1) and s1[i] == s3[k]:
                canInterleave |= dp(i + 1, j, k + 1)

            if not(canInterleave) and j < len(s2) and s2[j] == s3[k]:
                canInterleave |= dp(i, j + 1, k + 1)

            memo[(i, j, k)] = canInterleave
            return canInterleave
        
        return dp(0, 0, 0)

    # Bottom-up DP approach
    # Time: O(L1*L2)
    # Space: O(L1*L2)
    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1) + len(s2)) != len(s3):
            return False
        elif len(s3) == 0:
            return True

        dp = [[False]*(len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[-1][-1] = True
        for i in range(len(s1) - 1, -1, -1):
            dp[i][-1] = (dp[i + 1][-1] and s1[i] == s3[i + len(s2)])
        for i in range(len(s2) - 1, -1, -1):
            dp[-1][i] = (dp[-1][i + 1] and s2[i] == s3[i + len(s1)])

        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                k = i + j
                dp[i][j] = (dp[i + 1][j] and s1[i] == s3[k]) or (dp[i][j + 1] and s2[j] == s3[k])

        return dp[0][0]

    # Bottom-up DP approach with space optimization
    # Time: O(L1*L2)
    # Space: O(L2)
    def isInterleave3(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1) + len(s2)) != len(s3):
            return False
        elif len(s3) == 0:
            return True

        dp = [False]*(len(s2) + 1)
        dp[-1] = True
        for i in range(len(s2) - 1, -1, -1):
            dp[i] = (dp[i + 1] and s2[i] == s3[i + len(s1)])

        for i in range(len(s1) - 1, -1, -1):
            dp[-1] = (dp[-1] and s1[i] == s3[i + len(s2)])

            for j in range(len(s2) - 1, -1, -1):
                k = i + j
                dp[j] = (dp[j] and s1[i] == s3[k]) or (dp[j + 1] and s2[j] == s3[k])

        return dp[0]


solution = Solution()

assert solution.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac") == True
assert solution.isInterleave2(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac") == True
assert solution.isInterleave3(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac") == True

assert solution.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc") == False
assert solution.isInterleave2(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc") == False
assert solution.isInterleave3(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc") == False

assert solution.isInterleave(s1 = "", s2 = "", s3 = "") == True
assert solution.isInterleave2(s1 = "", s2 = "", s3 = "") == True
assert solution.isInterleave3(s1 = "", s2 = "", s3 = "") == True
