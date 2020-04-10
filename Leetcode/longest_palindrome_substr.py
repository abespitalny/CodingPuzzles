# Assume s has at least 1 character. This algorithms runs in O(n^3) time.
def longest_palindrome(s: str) -> str:
    longest_palin = ''
    s_len = len(s)
    for i in range(s_len):
        k = s_len
        while i < k:
            sub = s[i:k]
            if sub == sub[::-1]:
                break
            k -= 1

        if (k - i) > len(longest_palin):
            longest_palin = s[i:k]
    return longest_palin

# This algorithm is O(n^2).
def longest_palindrome_v2(s: str) -> str:
    s_len = len(s)
    if s_len < 2:
        return s

    longest_palin = (0, 0)
    prev_palins = {}
    if s[0] == s[1]:
        prev_palins[1] = {0}
        longest_palin = (0, 1)

    for i in range(2, len(s)):
        prev_ind = i - 1
        prev_palin_inds = prev_palins.get(prev_ind, None)
        longest_palin_len = longest_palin[1] - longest_palin[0]

        palin_inds = set()
        prev_prev_ind = prev_ind - 1
        if s[i] == s[prev_prev_ind]:
            palin_inds.add(prev_prev_ind)
            if 2 > longest_palin_len:
                longest_palin = (prev_prev_ind, i)
        if s[i] == s[prev_ind]:
            palin_inds.add(prev_ind)
            if 1 > longest_palin_len:
                longest_palin = (prev_ind, i)

        if prev_palin_inds is not None:
            for j in prev_palin_inds:
                j -= 1
                if (j >= 0) and (s[i] == s[j]):
                    palin_inds.add(j)
                    if (i - j) > longest_palin_len:
                        longest_palin = (j, i)
        if len(palin_inds) > 0:
            prev_palins[i] = palin_inds

    return s[longest_palin[0]:longest_palin[1] + 1]

# Think more on how to decrease the runtime. The best known one is O(n).

print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
print(longest_palindrome(""))
print(longest_palindrome("aaabaaaa"))
print(longest_palindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))

print(longest_palindrome_v2("babad"))
print(longest_palindrome_v2("cbbd"))
print(longest_palindrome_v2(""))
print(longest_palindrome_v2("aaabaaaa"))
print(longest_palindrome_v2("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
