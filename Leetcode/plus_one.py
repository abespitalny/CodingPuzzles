'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''
from leetcode import *

class Solution:
    # Time: O(n)
    # Space: O(1)
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            if carry == 0:
                break

            add = digits[i] + carry
            carry = add // 10
            digits[i] = add % 10
        
        if carry != 0:
            digits.insert(0, carry)
        return digits

solution = Solution()

assert solution.plusOne([1,2,3]) == [1,2,4]

assert solution.plusOne([4,3,2,1]) == [4,3,2,2]

assert solution.plusOne([9]) == [1,0]
