'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.
'''
from leetcode import *

# Time: O(4^n * n) where n is the length of digits. For each of the 4^n combinations, it costs up to n to build the combination.
# Space: O(4^n + n) where 4^n is to store the output and n is the max depth of the stack.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combos = []
        if len(digits) == 0:
            return combos

        letters = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        stack = [("", 0)]
        seen = set()
        while len(stack) != 0:
            top = stack[-1]

            if top in seen:
                stack.pop()
            elif top[1] == len(digits):
                combos.append(top[0])
                stack.pop()
            else:
                seen.add(top)
                nextNum = top[1] + 1
                for i in letters[int(digits[top[1]]) - 2]:
                    stack.append((top[0] + i, nextNum))
        return combos

solution = Solution()

# Expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(solution.letterCombinations("23"))

# Expected: []
print(solution.letterCombinations(""))

# Expected: ["a","b","c"]
print(solution.letterCombinations("2"))
