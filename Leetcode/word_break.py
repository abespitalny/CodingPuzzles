'''
Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''
from leetcode import *

class Solution:
    # DP with top-down approach
    # Time: O(n^3) because for each position we iterate through the string and within each iteration we perform a substring action, so overall n*n*n.
    # Space: O(n + D) where n is the length of the string because of the memoization table which contains n possible prefixes
    # and where D is the number of words in the dictionary because we convert the list into a set.
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.words = set(wordDict)
        self.memo = {}
        
        def dfs(s):
            if s in self.memo:
                return self.memo[s]

            ret = False
            prefix = s[0]
            for i in range(1, len(s)):
                if prefix in self.words and dfs(s[i:]):
                    ret = True
                    break
                prefix += s[i]
            
            if prefix in self.words:
                ret = True

            self.memo[s] = ret
            return ret

        return dfs(s)

    # From Leetcode, the bottom-up approach is a little tricky here.
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        # Null string
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[len(s)]


solution = Solution()

# Expected: True
print(solution.wordBreak(s = "leetcode", wordDict = ["leet","code"]))

# Expected: True
print(solution.wordBreak(s = "applepenapple", wordDict = ["apple","pen"]))

# Expected: False
print(solution.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))
