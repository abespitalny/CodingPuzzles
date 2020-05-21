'''
Given a string s consisting of upper/lower-case alphabets and empty space characters ' ',
return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.
Note: A word is defined as a maximal substring consisting of non-space characters only.
'''
def length_of_last_word(s: str) -> int:
    len_last = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            if len_last == 0:
                continue
            return len_last
        len_last += 1
    return len_last


print(length_of_last_word("Hello World"))
