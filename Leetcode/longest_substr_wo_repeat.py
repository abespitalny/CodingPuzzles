'''
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
'''
def lengthOfLongestSubstring(s: str) -> int:
    hash_table = {}
    start = 0
    run = 0
    max_run = 0
    for i, c in enumerate(s):
        prev_i = hash_table.get(c, None)
        if prev_i is None:
            run += 1
        else:
            # another duplicate has occurred so ignore this duplicate
            if prev_i < start:
                run += 1
            else:
                # see if the current run exceeds the known max
                if run > max_run:
                    max_run = run
                # run cannot include the previous occurence of the char and also must not include a previous duplicate
                start = prev_i + 1
                # reset the run to exclude the duplicate occurence
                run = i - start + 1
        # either save the char or update the location of the last char
        hash_table[c] = i
    # this case handles if the substring occurs at the very end
    if run > max_run:
        max_run = run
    return max_run

if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("bbbbb"))
    print(lengthOfLongestSubstring("pwwkew"))
    print(lengthOfLongestSubstring(" "))
    print(lengthOfLongestSubstring("abba"))