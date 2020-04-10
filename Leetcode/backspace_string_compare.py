'''
Given two strings S and T, return if they are equal when both are typed into empty text editors.
# means a backspace character.
'''
from typing import List

def final_str(s: str) -> List[str]:
    final_s = []
    end_s = -1
    for i in range(len(s)):
        c = s[i]
        if c == '#':
            if end_s >= 0:
                end_s -= 1
        else:
            # Append, set, and len for list is O(1) while insert is O(n).
            end_s += 1
            if end_s < len(final_s):
                final_s[end_s] = c
            else:
                final_s.append(c)
    return final_s[:(end_s + 1)]

# Algorithm runs in O(|S| + |T|).
def backspace_compare(S: str, T: str) -> bool:
    final_s = final_str(S)
    final_t = final_str(T)

    len_final_s = len(final_s)
    if len_final_s != len(final_t):
        return False
    for i in range(len_final_s):
        if final_s[i] != final_t[i]:
            return False
    return True


print(backspace_compare("ab#c", "ad#c"))
print(backspace_compare("ab##", "c#d#"))
print(backspace_compare("a##c", "#a#c"))
print(backspace_compare("a#c", "b"))
print(backspace_compare("bxj##tw", "bxo#j##tw"))
