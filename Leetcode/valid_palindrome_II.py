'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
'''

# Time: O(n).
# Space: O(1).
# My solution can be improved by modularizing the code.
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while (left < right) and (s[left] == s[right]):
            left += 1
            right -= 1

        if left >= right:
            return True
        
        # Delete left mismatched char
        delCharLeft = left + 1
        delCharRight = right
        while (delCharLeft < delCharRight) and (s[delCharLeft] == s[delCharRight]):
            delCharLeft += 1
            delCharRight -= 1

        if delCharLeft >= delCharRight:
            return True
        
        # Delete right mismatched char
        delCharLeft = left
        delCharRight = right - 1
        while (delCharLeft < delCharRight) and (s[delCharLeft] == s[delCharRight]):
            delCharLeft += 1
            delCharRight -= 1

        if delCharLeft >= delCharRight:
            return True
        return False

solution = Solution()

# Expected: True
print(solution.validPalindrome("aba"))

# Expected: True
print(solution.validPalindrome("abca"))

# Expected: False
print(solution.validPalindrome("abc"))
