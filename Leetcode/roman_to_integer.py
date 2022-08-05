'''
Given a roman numeral, convert it to an integer.
'''

class Solution:
    # Time: O(n)
    # Space: O(1)
    def romanToInt(self, s: str) -> int:
        integer = 0
        numerals = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
                    'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
                    'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

        index = 0
        while index < len(s):
            if index < (len(s) - 1) and s[index:(index + 2)] in numerals:
                integer += numerals[s[index:(index + 2)]]
                index += 2
            else:
                integer += numerals[s[index]]
                index += 1

        return integer

solution = Solution()

assert solution.romanToInt("III") == 3
assert solution.romanToInt("LVIII") == 58
assert solution.romanToInt("MCMXCIV") == 1994
