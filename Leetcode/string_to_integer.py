'''
Note:
- If no valid conversion could be performed, a zero value is returned.
- Only the space character ' ' is considered as whitespace character.
- Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values,
INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.
'''
def my_atoi(s: str) -> int:
    s_len = len(s)
    if s_len == 0:
        return 0

    start = 0
    # Discard any initial whitespace:
    while s[start] == ' ':
        start += 1
        if start == s_len:
            return 0
    # Check for optional sign: True is negative.
    sign = s[start]
    if sign == '-' or sign == '+':
        start += 1
        if start == s_len:
            return 0
        sign = (sign == '-')
    else:
        sign = False

    ans = 0
    base = ord('0')
    # Simulate a do...while loop:
    while True:
        val = ord(s[start]) - base
        if val < 0 or val > 9:
            break
        ans = (ans * 10) + val
        start += 1
        if start == s_len:
            break

    if sign:
        ans = -ans

    INT_MIN = -(1 << 31)
    INT_MAX = -(INT_MIN + 1)
    if ans > INT_MAX:
        ans = INT_MAX
    elif ans < INT_MIN:
        ans = INT_MIN
    return ans

print(my_atoi("42"))
print(my_atoi("   -42"))
print(my_atoi("4193 with words"))
print(my_atoi("words and 987"))
print(my_atoi("-91283472332"))
