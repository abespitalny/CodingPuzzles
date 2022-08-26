'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
    - Only numbers 1 through 9 are used.
    - Each number is used at most once.

Return a list of all possible valid combinations.
The list must not contain the same combination twice, and the combinations may be returned in any order.
'''
from leetcode import *

class Solution:
    # Backtracking
    # Time: O(k * P(9, k)) where k <= 9.
    # Space: O(k)
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.combos = []

        def recurse(num: int, target: int, combo: List[int]) -> None:
            if target == 0 and len(combo) == k:
                self.combos.append(combo[:])
                return
            elif target < 0 or len(combo) >= k:
                return

            for i in range(num, 10):
                newTarget = target - i
                if newTarget < 0:
                    break

                combo.append(i)
                recurse(i + 1, newTarget, combo)
                combo.pop()

        recurse(1, n, [])
        return self.combos


solution = Solution()

# Expected: [[1,2,4]]
print(solution.combinationSum3(k = 3, n = 7))

# Expected: [[1,2,6],[1,3,5],[2,3,4]]
print(solution.combinationSum3(k = 3, n = 9))

# Expected: []
print(solution.combinationSum3(k = 4, n = 1))
