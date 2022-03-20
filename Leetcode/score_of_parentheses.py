'''
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:
    - "()" has score 1.
    - AB has score A + B, where A and B are balanced parentheses strings.
    - (A) has score 2 * A, where A is a balanced parentheses string.
'''

# Time: O(n).
# Space: O(n).
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in s:
            if i == ')':
                top = stack.pop()
                if top == '(':
                    score = 1
                else:
                    score = 0
                    while top != '(':
                        score += top
                        top = stack.pop()
                    score = 2*score

                stack.append(score)
            else:
                stack.append(i)

        return sum(stack)

solution = Solution()

# Expected: 1
print(solution.scoreOfParentheses("()"))

# Expected: 2
print(solution.scoreOfParentheses("(())"))

# Expected: 2
print(solution.scoreOfParentheses("()()"))

# From Leetcode, my solution can be expressed in a much simpler way:
#   stack = [0]
#   for x in s:
#       if x == '(':
#           stack.append(0)
#       else:
#           top = stack.pop()
#           stack[-1] += max(2 * top, 1)
#   return stack.pop()

# Also, there is an O(1) space solution which is based on the fact that (2^x)*(A+B) = (2^x)*A + (2^x)*B where x is the number of parentheses around A and B.
#   score = balance = 0
#   for i in range(len(s)):
#       if s[i] == '(':
#           balance += 1
#       else:
#           balance -= 1
#           if s[i-1] == '(':
#               score += (1 << balance)
#   return score
