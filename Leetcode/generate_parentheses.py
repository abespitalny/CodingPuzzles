'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
from leetcode import *

# Recursive approach
def generate_parenthesis(n: int) -> List[str]:
    def generate_parenthesis_helper(n: int, m: int, parenthesis: str, parenthesis_list: List[str]) -> None:
        if n == 0 and m == 0:
            parenthesis_list.append(parenthesis)

        # Add opening parenthesis
        if m < n:
            generate_parenthesis_helper(n, m + 1, parenthesis + "(", parenthesis_list)
        # Add closing parenthesis
        if m > 0:
            generate_parenthesis_helper(n - 1, m - 1, parenthesis + ")", parenthesis_list)

    parenthesis_list = []
    generate_parenthesis_helper(n, 1, "(", parenthesis_list)
    return parenthesis_list

# Turning recursive approach above into iteration.
# From Leetcode, the time and space complexity is O(4^n / sqrt(n)). It's rather complicated to derive and is related to Catalan numbers.
def generateParenthesis2(n: int) -> List[str]:
    stack = [('(', 1, n)]
    ans = []
    while len(stack) != 0:
        parentheses, unmatchedOpen, numPairsLeft = stack.pop()

        if unmatchedOpen == 0 and numPairsLeft == 0:
            ans.append(parentheses)
        else:
            if unmatchedOpen > 0:
                stack.append((parentheses + ')', unmatchedOpen - 1, numPairsLeft - 1))
            if unmatchedOpen < numPairsLeft:
                stack.append((parentheses + '(', unmatchedOpen + 1, numPairsLeft))
    return ans

# There's also a version of the recursive version that utilizes the backtracking template.


# Expected: ["((()))","(()())","(())()","()(())","()()()"]
print(generate_parenthesis(3))
print(generateParenthesis2(3))

# Expected: ["()"]
print(generate_parenthesis(1))
print(generateParenthesis2(1))
