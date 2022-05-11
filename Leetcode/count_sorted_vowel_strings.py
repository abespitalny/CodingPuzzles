'''
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
'''

class Solution:
    # Dynamic programming bottom-up approach
    # Time: O(n)
    # Space: O(1) because there is a constant number of vowels.
    def countVowelStrings(self, n: int) -> int:
        dp = [5, 4, 3, 2, 1]
        for i in range(1, n):
            for j in reversed(range(len(dp) - 1)):
                dp[j] += dp[j + 1]
        return dp[0]
    
    # There is a mathematical solution to this because it's similar to getting the number of combinations where repetition is allowed.
    # The formula for that is C(n + k - 1, k) where n = 5 (the number of vowels in the set) and k is the number of selections from the set,
    # i.e. n from the input of the function (don't confuse this with n = 5 or the size of the set!).
    # So, this can be solved in O(1) time and space.

solution = Solution()

# Expected: 5
print(solution.countVowelStrings(1))

# Expected: 15
print(solution.countVowelStrings(2))

# Expected: 66045
print(solution.countVowelStrings(33))
