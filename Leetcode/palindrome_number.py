def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    elif x < 10:
        return True

    reverse_int = 0
    tmp = x
    while tmp != 0:
        reverse_int = (10 * reverse_int) + (tmp % 10)
        tmp //= 10
    return (reverse_int == x)

print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(10))
