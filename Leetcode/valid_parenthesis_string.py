'''
Given a string containing only three types of characters: '(', ')' and '*',
write a function to check whether this string is valid. We define the validity of a string by these rules:
- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
- An empty string is also valid.
'''

# Original solution which is O(n^2) time and O(n) space.
def check_valid_string(s: str) -> bool:
    stack = []
    for i in range(len(s)):
        p = s[i]
        # Push all left parentheses and stars on stack.
        if p == '(' or p == '*':
            stack.append(p)
        # The only other char. it can be is the right parenthesis.
        else:
            stack_size = len(stack)
            if stack_size == 0:
                return False
            end = stack_size - 1
            while end >= 0:
                if stack[end] == '(':
                    stack.pop(end)
                    break
                end -= 1

            if end == -1:
                if stack[stack_size - 1] == '*':
                    stack.pop()
                else:
                    return False

    sec_stack = []
    for i in range(len(stack)):
        p = stack[i]
        if p == '*':
            if len(sec_stack) == 0:
                continue
            else:
                sec_stack.pop()
        else:
            sec_stack.append(p)
    return (len(sec_stack) == 0)

# Using two stacks simultaneously solves the problem now in O(n) time and O(n) space.
# Very similar to my original solution and was inspired by a solution on LeetCode.
def check_valid_string_v2(s: str) -> bool:
    left_par_stack = []
    star_stack = []
    for i in range(len(s)):
        c = s[i]
        if c == '(':
            left_par_stack.append(i)
        elif c == '*':
            star_stack.append(i)
        # The char. must be a right parenthesis then:
        elif len(left_par_stack) > 0:
            left_par_stack.pop()
        elif len(star_stack) > 0:
            star_stack.pop()
        else:
            return False

    if len(left_par_stack) > 0:
        while (len(left_par_stack) > 0) and (len(star_stack) > 0) and (left_par_stack[-1] < star_stack[-1]):
            left_par_stack.pop()
            star_stack.pop()
    return (len(left_par_stack) == 0)

# Another solution (on LeetCode) was able to do even better with O(n) time and O(1) space:
# WARNING! This is a very clever solution.
def check_valid_string_v3(s: str) -> bool:
    # Treat all '*' as '(', so the maximum number of left parentheses:
    max_left = 0
    # Treat all '*' as ')', so the minimum number of left parentheses:
    min_left = 0
    for i in range(len(s)):
        c = s[i]
        # If c is '*' or '(' add 1 else subtract 1:
        max_left += (-1 if c == ')' else 1)
        # If c is '(' add 1 else (i.e. c is '*' or ')') subtract 1:
        min_left += (1 if c == '(' else -1)
        # Ignore any of the extra stars that subtracted min_left
        min_left = max(0, min_left)
        # There are no left parentheses or stars to match with a right parenthesis:
        if max_left < 0:
            return False
    # If min_left is 0 that means there are no leftover left parentheses that
    # could not be matched with a star or a right parenthesis.
    return (min_left == 0)

# Another similar approach to the one above that is a little simpler to understand. It's a two-pointer approach.
def check_valid_string_v4(s: str) -> bool:
    s_len = len(s) - 1
    open_count = 0
    closed_count = 0
    for i in range(s_len + 1):
        if (s[i] == '*') or (s[i] == '('):
            open_count += 1
        else:
            open_count -= 1

        if (s[s_len - i] == '*') or (s[s_len - i] == ')'):
            closed_count += 1
        else:
            closed_count -= 1
        
        if (open_count < 0) or (closed_count < 0):
            return False
    return True

print(check_valid_string('*'))
print(check_valid_string('*)'))
print(check_valid_string('(*)'))
print(check_valid_string('(*))'))
print(check_valid_string('()'))
print(check_valid_string('(*(**))))'))
print(check_valid_string('(*()'))
print(check_valid_string('()*()(()(*()(((())()()())*))()*()(*)(((*))(())(())((*()*(()(())()*(((*(**))((())*)(((()()))(())()))'))

print(check_valid_string_v2('*'))
print(check_valid_string_v2('*)'))
print(check_valid_string_v2('(*)'))
print(check_valid_string_v2('(*))'))
print(check_valid_string_v2('()'))
print(check_valid_string_v2('(*(**))))'))
print(check_valid_string_v2('(*()'))
print(check_valid_string_v2('()*()(()(*()(((())()()())*))()*()(*)(((*))(())(())((*()*(()(())()*(((*(**))((())*)(((()()))(())()))'))

print(check_valid_string_v3('*'))
print(check_valid_string_v3('*)'))
print(check_valid_string_v3('(*)'))
print(check_valid_string_v3('(*))'))
print(check_valid_string_v3('()'))
print(check_valid_string_v3('(*(**))))'))
print(check_valid_string_v3('(*()'))
print(check_valid_string_v3('()*()(()(*()(((())()()())*))()*()(*)(((*))(())(())((*()*(()(())()*(((*(**))((())*)(((()()))(())()))'))

print(check_valid_string_v4('*'))
print(check_valid_string_v4('*)'))
print(check_valid_string_v4('(*)'))
print(check_valid_string_v4('(*))'))
print(check_valid_string_v4('()'))
print(check_valid_string_v4('(*(**))))'))
print(check_valid_string_v4('(*()'))
print(check_valid_string_v4('()*()(()(*()(((())()()())*))()*()(*)(((*))(())(())((*()*(()(())()*(((*(**))((())*)(((()()))(())()))'))
