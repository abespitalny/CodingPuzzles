'''
Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:
    - It is the empty string, contains only lowercase characters, or
    - It can be written as AB (A concatenated with B), where A and B are valid strings, or
    - It can be written as (A), where A is a valid string.
'''

# Time: O(n) where n is the length of string s.
# Space: O(n).
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != '(' and s[i] != ')':
                continue

            if s[i] == ')' and len(stack) > 0 and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)

        if len(stack) == 0:
            return s
        if len(stack) == len(s):
            return ""

        stackInd = 0
        validStr = s[:stack[stackInd]]
        for i in range(stack[stackInd], len(s)):
            if i != stack[stackInd]:
                validStr += s[i]
            else:
                stackInd += 1
                if stackInd == len(stack):
                    validStr += s[(i + 1):]
                    break

        return validStr

solution = Solution()

# Expected: "lee(t(c)o)de"
print(solution.minRemoveToMakeValid("lee(t(c)o)de)"))

# Expected: "ab(c)d"
print(solution.minRemoveToMakeValid("a)b(c)d"))

# Expected: ""
print(solution.minRemoveToMakeValid("))(("))
