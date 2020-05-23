'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''
from leetcode import *

# Time: O(n * |s_min|) where |s_min| is the length of the shortest string in the array, Space: O(n * |s_min|) because
# you could keep taking the substring of the prefix.
def longest_common_prefix(strs: List[str]) -> str:
    num_strs = len(strs)
    if num_strs == 0:
        return ""
    # Set the longest prefix to the shortest string:
    longest_prefix = strs[0]
    for i in range(1, num_strs):
        if len(strs[i]) < len(longest_prefix):
            longest_prefix = strs[i]
    if len(longest_prefix) == 0:
        return ""

    for i in range(num_strs):
        s = strs[i]
        min_len = min(len(s), len(longest_prefix))
        for j in range(min_len):
            if s[j] != longest_prefix[j]:
                longest_prefix = longest_prefix[:j]
                break
        if min_len < len(longest_prefix):
            longest_prefix = longest_prefix[:min_len]
    return longest_prefix


print(longest_common_prefix(["flower","flow","flight"]))
print(longest_common_prefix(["dog","racecar","car"]))
print(longest_common_prefix(["aa","a"]))
