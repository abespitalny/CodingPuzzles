'''
Convert a non-negative integer num to its English words representation.
'''

class Solution:
    # Time: O(1)
    # Space: O(1)
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        numsToWords = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
            7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven",
            12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
            16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
            20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty",
            70: "Seventy", 80: "Eighty", 90: "Ninety", 100: "Hundred",
            1000: "Thousand", 1_000_000: "Million", 1_000_000_000: "Billion"
        }

        words = []

        def helper(n):
            hundreds = n // 100
            n %= 100
            if hundreds > 0:
                words.append(numsToWords[hundreds])
                words.append(numsToWords[100])

            tens = n // 10
            if tens > 1:
                words.append(numsToWords[tens * 10])
                n %= 10

                if n > 0:
                    words.append(numsToWords[n])
            elif n > 0:
                words.append(numsToWords[n])


        billions = num // 1_000_000_000
        num %= 1_000_000_000
        if billions > 0:
            helper(billions)
            words.append(numsToWords[1_000_000_000])

        millions = num // 1_000_000
        num %= 1_000_000
        if millions > 0:
            helper(millions)
            words.append(numsToWords[1_000_000])

        thousands = num // 1000
        num %= 1000
        if thousands > 0:
            helper(thousands)
            words.append(numsToWords[1000])

        helper(num)

        return ' '.join(words)

solution = Solution()

assert solution.numberToWords(123) == "One Hundred Twenty Three"
assert solution.numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five"
assert solution.numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
