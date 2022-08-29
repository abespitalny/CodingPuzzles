'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
Return the solution in any order.
'''
from leetcode import *

class Solution:
    # Backtracking approach
    # Time: O(n*(2^n)) where n is the number of elements in nums.
    # Space: O(n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.powerset = []

        def backtrack(i, subset):            
            self.powerset.append(subset[:])

            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()
            return

        backtrack(0, [])
        return self.powerset

solution = Solution()

# Expected: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(solution.subsets([1,2,3]))

# Expected: [[],[0]]
print(solution.subsets([0]))
