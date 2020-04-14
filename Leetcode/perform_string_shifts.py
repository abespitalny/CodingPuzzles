'''
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:
- direction can be 0 (for left shift) or 1 (for right shift). 
- amount is the amount by which string s is to be shifted.
- A left shift by 1 means remove the first character of s and append it to the end.
- Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.

Return the final string after all operations.
'''
from typing import List

# Time: O(|s| + |shift|) (i.e., it's linear)
def string_shift(s: str, shift: List[List[int]]) -> str:
    # Combine all shifts into one shift value by adding them up:
    total_shift = 0
    for i in range(len(shift)):
        sh = shift[i]
        if sh[0] == 0:
            total_shift -= sh[1]
        else:
            total_shift += sh[1]

    s_len = len(s)
    # No shifting is necessary:
    if (total_shift == 0) or ((total_shift % s_len) == 0):
        return s
    # Shift to the right:
    elif total_shift > 0:
        total_shift %= s_len
        offset = s_len - total_shift
        return s[offset:] + s[:offset]
    # Shift to the left:
    else:
        total_shift = (-total_shift) % s_len
        return s[total_shift:] + s[:total_shift]


print(string_shift("abc", [[0, 1], [1, 2]]))
print(string_shift("abcdefg", [[1, 1], [1, 1], [0, 2], [1, 3]]))
