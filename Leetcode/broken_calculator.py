'''
There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:
    - multiply the number on display by 2, or
    - subtract 1 from the number on display.

Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.
'''
from leetcode import *

# Time: O(log(target)).
# Space: O(1).
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue == target:
            return 0
        elif target < startValue:
            return (startValue - target)
        else:
            numOps = 0
            while target > startValue:
                if target % 2 == 0:
                    target = target // 2
                else:
                    target = target + 1
                numOps += 1

            return numOps + (startValue - target)

solution = Solution()

# Expeceted: 2
print(solution.brokenCalc(startValue = 2, target = 3))

# Expeceted: 2
print(solution.brokenCalc(startValue = 5, target = 8))

# Expeceted: 3
print(solution.brokenCalc(startValue = 3, target = 10))
