'''
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths.
If it is impossible to form any triangle of a non-zero area, return 0.
'''
from leetcode import *

class Solution:
    # Sort / Greedy approach
    # Time: O(n*log(n))
    # Space: O(1)
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            # Do these 3 numbers obey the triangle theorem?
            if nums[i] < (nums[i + 1] + nums[i + 2]):
                return (nums[i] + nums[i + 1] + nums[i + 2])
        return 0

solution = Solution()

# Expected: 5
print(solution.largestPerimeter([2,1,2]))

# Expected: 0
print(solution.largestPerimeter([1,2,1]))
