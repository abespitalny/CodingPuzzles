'''
Given two integer arrays pushed and popped each with distinct values,
return true if this could have been the result of a sequence of push and pop operations
on an initially empty stack, or false otherwise.
'''
from leetcode import *

# Time: O(n).
# Space: O(n).
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pushedIdx = poppedIdx = 0
        while poppedIdx < len(popped):
            if len(stack) > 0 and stack[-1] == popped[poppedIdx]:
                stack.pop()
                poppedIdx += 1
            elif pushedIdx < len(pushed):
                stack.append(pushed[pushedIdx])
                pushedIdx += 1
            else:
                return False
        return True

solution = Solution()

# Expected: True
print(solution.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1]))

# Expected: False
print(solution.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2]))
