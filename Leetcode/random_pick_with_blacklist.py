'''
You are given an integer n and an array of unique integers blacklist.
Design an algorithm to pick a random integer in the range [0, n - 1] that is not in blacklist.
Any integer that is in the mentioned range and not in blacklist should be equally likely to be returned.

Optimize your algorithm such that it minimizes the number of calls to the built-in random function of your language.
'''
from leetcode import *

class Solution:
    # Time: O(n) where n is the length of the blacklist.
    # Space: O(n)
    def __init__(self, n: int, blacklist: List[int]):
        blackset = set(blacklist)
        remapList = []
        endRange = n - len(blacklist)
        for i in blacklist:
            if i < endRange:
                remapList.append(i)

        pos = 0
        blackmap = {}
        for i in range(endRange, n):
            if i not in blackset:
                blackmap[remapList[pos]] = i
                pos += 1

        self.n = endRange - 1
        self.blackmap = blackmap

    # Time: O(1)
    # Space: O(n) where n is the length of the blacklist.
    def pick(self) -> int:
        randnum = random.randint(0, self.n)
        if randnum in self.blackmap:
            return self.blackmap[randnum]
        return randnum

solution = Solution(7, [2, 3, 5])
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
