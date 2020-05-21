'''
Given two binary strings, return their sum (also a binary string).
'''

# I'm assuming both input strings are both non-empty and contains only the characters 1 or 0.
# Time: O(|max(a, b)|), i.e., it's a linear time solution.
def add_binary(a: str, b: str) -> str:
    if len(a) > len(b):
        max_str = a
        min_str = b
    else:
        max_str = b
        min_str = a
    diff_len = len(max_str) - len(min_str)

    bin_sum = ""
    carry = "0"
    for i in range(len(max_str) - 1, -1, -1):
        c1 = max_str[i]
        # Index of the min_str:
        min_ind = i - diff_len
        c2 = "0" if min_ind < 0 else min_str[min_ind]

        num_ones = (1 if c1 == "1" else 0) + (1 if c2 == "1" else 0) + (1 if carry == "1" else 0)
        if num_ones == 0:
            bin_sum = "0" + bin_sum
            carry = "0"
        elif num_ones == 1:
            bin_sum = "1" + bin_sum
            carry = "0"
        elif num_ones == 2:
            bin_sum = "0" + bin_sum
            carry = "1"
        else:
            bin_sum = "1" + bin_sum
            carry = "1"

    if carry == "1":
        bin_sum = "1" + bin_sum
    return bin_sum


print(add_binary("11", "1"))
print(add_binary("1010", "1011"))
