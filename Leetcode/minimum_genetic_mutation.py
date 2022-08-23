'''
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end
where one mutation is defined as one single character changed in the gene string.
    - For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

There is also a gene bank bank that records all the valid gene mutations.
A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end.
If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.
'''
from leetcode import *

class Solution:
    # BFS approach
    # Time: O(n*(m*n)) where n is the number of strings in bank and m is the length of a gene which in this case is a constant of 8.
    # Space: O(n) where n is the number of strings in bank.
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        mutations = []
        endIdx = -1
        for i in range(len(bank)):
            numMutations = 0
            for ch1, ch2 in zip(bank[i], start):
                if ch1 != ch2:
                    numMutations += 1
            
            if numMutations == 1:
                mutations.append(i)

            if endIdx == -1 and end == bank[i]:
                endIdx = i

        if endIdx == -1:
            return -1
        elif start == end:
            return 0

        minMutations = 1
        visited = set(mutations)
        queue = mutations
        while len(queue) != 0:
            nextQueue = []
            for i in queue:
                if i == endIdx:
                    return minMutations
                
                for j in range(len(bank)):
                    if j in visited:
                        continue
                    
                    numMutations = 0
                    for ch1, ch2 in zip(bank[i], bank[j]):
                        if ch1 != ch2:
                            numMutations += 1
                    
                    if numMutations == 1:
                        nextQueue.append(j)
                        visited.add(j)

            queue = nextQueue
            minMutations += 1
        
        return -1

solution = Solution()

assert solution.minMutation(start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]) == 1
assert solution.minMutation(start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]) == 2
assert solution.minMutation(start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]) == 3
