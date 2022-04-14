from leetcode import *

class Solution:
    # Time: O(n).
    # Space: O(n).
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for i in ops:
            if i == '+':
                record.append(record[-1] + record[-2])
            elif i == 'D':
                record.append(2*record[-1])
            elif i == 'C':
                record.pop()
            else:
                record.append(int(i))
        return sum(record)

solution = Solution()

# Expected: 30
print(solution.calPoints(["5","2","C","D","+"]))

# Expected: 27
print(solution.calPoints(["5","-2","4","C","D","9","+","+"]))

# Expected: 1
print(solution.calPoints(["1"]))
