'''
Given a characters array letters that is sorted in non-decreasing order and a character target,
return the smallest character in the array that is larger than target.

Note that the letters wrap around. For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
'''
from leetcode import *

class Solution:
    # Binary search approach.
    # Time: O(log(n))
    # Space: O(1)
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)
        while left < right:
            mid = (left + right) // 2
            
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid

        if left == len(letters):
            return letters[0]
        return letters[left]

solution = Solution()

# Expected: "c"
print(solution.nextGreatestLetter(letters = ["c","f","j"], target = "a"))

# Expected: "f"
print(solution.nextGreatestLetter(letters = ["c","f","j"], target = "c"))

# Expected: "f"
print(solution.nextGreatestLetter(letters = ["c","f","j"], target = "d"))

# Expected: "a"
print(solution.nextGreatestLetter(letters = ["a", "b"], target = "z"))
