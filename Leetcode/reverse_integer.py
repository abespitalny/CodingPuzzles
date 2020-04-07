def reverse(x: int) -> int:
    is_negative = False    
    if x < 0:
        is_negative = True
        x = -x

    ans = 0
    while x > 0:
        last_digit = x % 10
        x //= 10
        ans = (ans * 10) + last_digit
    if is_negative:
        ans = -ans
    # Checks if the answer overflowed the bounds of a 32-bit integer:
    if (ans >= (1 << 31)) or (ans < (-1 << 31)):
        return 0
    return ans

print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(1534236469))
