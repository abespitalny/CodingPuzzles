'''
Given an integer, convert it to a roman numeral.
'''

class Solution:
    # Greedy approach
    # Time: O(1) since the loop will run only 13 times.
    # Space: O(1)
    def intToRoman(self, num: int) -> str:
        numerals = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
                    (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
                    (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

        roman = []
        for val, sym in numerals:
            times = num // val
            roman.append(times*sym)
            num %= val

        return ''.join(roman)

solution = Solution()

assert solution.intToRoman(3) == "III"
assert solution.intToRoman(58) == "LVIII"
assert solution.intToRoman(1994) == "MCMXCIV"
