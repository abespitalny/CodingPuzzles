'''
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
    - Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
    - Each vowel 'a' may only be followed by an 'e'.
    - Each vowel 'e' may only be followed by an 'a' or an 'i'.
    - Each vowel 'i' may not be followed by another 'i'.
    - Each vowel 'o' may only be followed by an 'i' or a 'u'.
    - Each vowel 'u' may only be followed by an 'a'.

Since the answer may be too large, return it modulo 10^9 + 7.
'''

class Solution:
    # Bottom-up DP approach
    # Time: O(n). Can be solved in O(log(n)) time by using matrix exponentiation.
    # Space: O(1) since we're using arrays of fixed size.
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [1, 1, 1, 1, 1]
        nextRow = [0, 0, 0, 0, 0]

        for i in range(2, n + 1):
            nextRow[0] = dp[1]
            nextRow[1] = (dp[0] + dp[2]) % MOD
            nextRow[2] = (dp[0] + dp[1] + dp[3] + dp[4]) % MOD
            nextRow[3] = (dp[2] + dp[4]) % MOD
            nextRow[4] = dp[0]

            dp, nextRow = nextRow, dp

        return sum(dp) % MOD

solution = Solution()

assert solution.countVowelPermutation(1) == 5
assert solution.countVowelPermutation(2) == 10
assert solution.countVowelPermutation(5) == 68
