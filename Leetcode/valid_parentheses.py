'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
'''
# This is an O(n) time algorithm.
def is_valid(s: str) -> bool:
    matching_parents = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for i in range(len(s)):
        p = s[i]
        # Is this parenthesis an opening one or a closing one? This can be determined in O(1).
        if p in matching_parents:
            stack.append(p)
        else:
            if (len(stack) == 0) or (p != matching_parents[stack[-1]]):
                return False
            stack.pop()

    return (len(stack) == 0)


print(is_valid('()'))
print(is_valid(r'()[]{}'))
print(is_valid('(]'))
print(is_valid('([)]'))
print(is_valid('{[]}'))
