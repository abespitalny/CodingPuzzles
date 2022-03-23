'''
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.
'''
from leetcode import *

# Time: O(n)*C where C is 26, number of letters in the alphabet, and n = len(s).
# Space: O(n). The partitions map is O(1) because it contains only a constant number of elements (i.e., the alphabet). However, the paritions take up an additional O(n).
# My solution isn't optimal. The Leetcode solution which is similar to the Remove Duplicate Letters solution:
#
#   lettersToLastPosition = {c: i for i, c in enumerate(s)}
#   j = anchor = 0
#   answer = []
#
#   for i in range(len(s)):
#       j = max(j, lettersToLastPosition[s[i]])
#       if i == j:
#           answer.append(i - anchor + 1)
#           anchor = i + 1
#
#   return answer
#
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partitions = {}
        stack = []
        for i in s:
            if i in partitions:
                partitionIdx = partitions[i]
                coalescePartitions = i
                while (partitionIdx + 1) < len(stack):
                    partition = stack.pop()
                    for j in partition:
                        partitions[j] = partitionIdx

                    coalescePartitions = partition + coalescePartitions

                stack[-1] = stack[-1] + coalescePartitions
            else:
                partitions[i] = len(stack)
                stack.append(i)

        return [len(p) for p in stack]

solution = Solution()

# Expected: [9,7,8]
print(solution.partitionLabels("ababcbacadefegdehijhklij"))

# Expected: [10]
print(solution.partitionLabels("eccbbbbdec"))
