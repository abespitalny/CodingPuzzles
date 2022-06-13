'''
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.
'''
from leetcode import *

class Solution:
    # Backtracking approach
    # Time: O(n! / (k!(n - k)!)) = O(C(n, k)). It's truthfully a little slower because we need to copy the combo for each next number which is O(k).
    # Space: O(n*k + k) = O(n*k) because we make a copy of the combo for each next number to add + the depth of the recursion stack. Output is not included.
    # We could use less space (reduce to O(k)) by following the backtracking paradigm more closely (see Leetcode).
    def combine(self, n: int, k: int) -> List[List[int]]:
        combos = []
        def backtrack(k, num, combo):
            if k == 0:
                combos.append(combo)
                return
            
            for i in range(num, n + 1):
                comboCopy = combo.copy()
                comboCopy.append(i)
                backtrack(k - 1, i + 1, comboCopy)

        backtrack(k, 1, [])
        return combos

    # A more backtracky approach
    def combine2(self, n: int, k: int) -> List[List[int]]:
        combos = []
        def backtrack(num, combo):
            if len(combo) == k:
                combos.append(combo[:])
                return
            
            for i in range(num, n + 1):
                combo.append(i)
                backtrack(i + 1, combo)
                combo.pop()

        backtrack(1, [])
        return combos

solution = Solution()

# Expected: [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]
print(solution.combine(n = 4, k = 2))
print(solution.combine2(n = 4, k = 2))

# Expected: [[1]]
print(solution.combine(n = 1, k = 1))
print(solution.combine2(n = 1, k = 1))
