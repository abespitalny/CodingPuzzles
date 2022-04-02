'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''
from leetcode import *

# TIme: O(n). Gauss's formula.
# Space: O(1).
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        targetSum = (n * (n + 1)) // 2
        actualSum = sum(nums)
        
        return (targetSum - actualSum)

solution = Solution()

# Expected: 2
print(solution.missingNumber([3,0,1]))

# Expected: 2
print(solution.missingNumber([0,1]))

# Expected: 8
print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))
