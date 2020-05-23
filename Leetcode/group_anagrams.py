from leetcode import *

# This algroithm runs in O(n * k * log(k)) where k is the longest string in the array.
def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_groups = {}
    for i in range(len(strs)):
        s = strs[i]
        s_sorted = ''.join(sorted(s))
        group = anagram_groups.get(s_sorted, None)
        if group is None:
            anagram_groups[s_sorted] = [s]
        else:
            anagram_groups[s_sorted].append(s)
    return [anagram_groups[k] for k in anagram_groups]

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))