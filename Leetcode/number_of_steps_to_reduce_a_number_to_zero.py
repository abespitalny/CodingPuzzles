'''
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
'''

class Solution:
    # Time: O(log(n))
    # Space: O(1)
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num != 0:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            steps += 1
        return steps

solution = Solution()

# Expected: 6
print(solution.numberOfSteps(14))

# Expected: 4
print(solution.numberOfSteps(8))

# Expected: 12
print(solution.numberOfSteps(123))
