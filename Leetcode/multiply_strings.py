'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

# Time: O(m*n) where m is the length of num1 and n is the length of num2.
# Space: O(1)
# I misunderstood the question a little, so my algorithm uses an int and not a string to store the answer.
# The solutions on Leetcode show algorithms that use an array of characters of size (m + n) to store the answer.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = 0
        i = 0
        while i < len(num1):
            digit1 = (ord(num1[len(num1) - i - 1]) - ord('0')) * (10**i)
            j = 0
            while j < len(num2):
                digit2 = (ord(num2[len(num2) - j - 1]) - ord('0')) * (10**j)
                product += (digit1 * digit2)
                j += 1
            i += 1
        return str(product)

solution = Solution()

# Expected: "6"
print(solution.multiply("2", "3"))

# Expected: "56088"
print(solution.multiply("123", "456"))
