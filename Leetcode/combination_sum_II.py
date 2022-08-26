'''
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''
from leetcode import *

class Solution:
    # Backtracking with index
    # Time: O(2^n) where n is the number of candidates.
    # Space: O(n)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # Duplicate entries means we could get duplicate combinations.
        self.combos = []

        def recurse(idx: int, target: int, combo: List[int]) -> None:
            if target == 0:
                self.combos.append(combo[:])
                return
            elif target < 0:
                return

            while idx < len(candidates):
                newTarget = target - candidates[idx]
                if newTarget < 0:
                    break

                combo.append(candidates[idx])
                recurse(idx + 1, newTarget, combo)
                combo.pop()

                idx += 1
                while idx < len(candidates) and candidates[idx] == candidates[idx - 1]:
                    idx += 1

        recurse(0, target, [])
        return self.combos

solution = Solution()

# Expected: [[1,1,6],[1,2,5],[1,7],[2,6]]
print(solution.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))

# Expected: [[1,2,2],[5]]
print(solution.combinationSum2(candidates = [2,5,2,1,2], target = 5))
