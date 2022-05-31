from leetcode import *

class Solution:
    # Stack approach
    # Time: O(n)
    # Space: O(n)
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+': (lambda x, y: x+y), '-': (lambda x, y: x-y), '*': (lambda x, y: x*y), '/': (lambda x, y: int(x/y))}
        stack = []
        for i in tokens:
            if i in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                result = operators[i](op1, op2)
                stack.append(result)
            else:
                stack.append(int(i))
        return stack[-1]

solution = Solution()

# Expected: 9
print(solution.evalRPN(["2","1","+","3","*"]))

# Expected: 6
print(solution.evalRPN(["4","13","5","/","+"]))

# Expected: 22
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
