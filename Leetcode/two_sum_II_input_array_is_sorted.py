'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
'''
from leetcode import *

class Solution:
    # Two pointers approach
    # Time: O(n)
    # Space: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            diff = target - numbers[left]
            if diff == numbers[right]:
                return [left + 1, right + 1]
            elif diff > numbers[right]:
                left += 1
            else:
                right -= 1
        return [-1, -1]

solution = Solution()

assert solution.twoSum(numbers = [2,7,11,15], target = 9) == [1, 2]

assert solution.twoSum(numbers = [2,3,4], target = 6) == [1, 3]

assert solution.twoSum(numbers = [-1,0], target = -1) == [1, 2]
