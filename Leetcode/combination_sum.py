'''
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
'''
from leetcode import *

class Solution:
    # Backtracking approach
    # Time: O(n^(T/M + 1)) where n is the number of candidates, T is tha target sum, and M is the minimal number in candidates.
    # Space: O(T/M)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort so that we can break out of the recrusive for loop early.
        candidates.sort()
        self.combos = []

        def recurse(candidates: List[int], target: int, combo: List[int]) -> None:
            if target == 0:
                self.combos.append(combo[:])
                return
            elif target < 0:
                return

            for i in range(len(candidates)):
                newTarget = target - candidates[i]
                if newTarget < 0:
                    break

                combo.append(candidates[i])
                recurse(candidates[i:], newTarget, combo)
                combo.pop()

        recurse(candidates, target, [])
        return self.combos

solution = Solution()

# Expected: [[2,2,3],[7]]
print(solution.combinationSum(candidates = [2,3,6,7], target = 7))

# Expected: [[2,2,2,2],[2,3,3],[3,5]]
print(solution.combinationSum(candidates = [2,3,5], target = 8))

# Expected: []
print(solution.combinationSum(candidates = [2], target = 1))
