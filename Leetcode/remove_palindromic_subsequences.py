'''
You are given a string s consisting only of letters 'a' and 'b'.
In a single step you can remove one palindromic subsequence from s.

Return the minimum number of steps to make the given string empty.

A string is a subsequence of a given string if it is generated by deleting some characters of a given string without changing its order.
Note that a subsequence does not necessarily need to be contiguous.
'''

class Solution:
    # Trick question!
    # Time: O(n)
    # Space: O(n)
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1
        return 2

solution = Solution()

assert solution.removePalindromeSub("ababa") == 1
assert solution.removePalindromeSub("abb") == 2
assert solution.removePalindromeSub("baabb") == 2
