from leetcode import *

# Time: O(k) where k is the smallest integer such that 26^k > column_number, Space: O(1).
def convert_to_title(column_number: int) -> str:
    column_title = ""

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while column_number > 0:
        # 1 -> A, ..., 25 -> Y, 26 -> Z
        letter_ind = (column_number % 26) - 1
        column_title = alphabet[letter_ind] + column_title
        column_number //= 26
        if letter_ind < 0:
            column_number -= 1
    return column_title

# Base conversion with a shift!

# Expected: A
print(convert_to_title(1))
# Expected: AB
print(convert_to_title(28))
# Expected: ZY
print(convert_to_title(701))
# Expected: FXSHRXW
print(convert_to_title(2147483647))
