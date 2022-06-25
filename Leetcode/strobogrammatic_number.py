'''
Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
'''

class Solution:
    # Time: O(n)
    # Space: O(1)
    def isStrobogrammatic(self, num: str) -> bool:
        goodDigits = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        left = 0
        right = len(num) - 1
        while left <= right:
            if num[left] not in goodDigits or goodDigits[num[left]] != num[right]:
                return False
            
            left += 1
            right -= 1

        return True

solution = Solution()

assert solution.isStrobogrammatic("69") == True

assert solution.isStrobogrammatic("88") == True

assert solution.isStrobogrammatic("962") == False
