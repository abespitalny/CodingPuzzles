'''
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it.
The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%),
and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
'''
from leetcode import *

class Solution:
    # Time: O(n) where n is the length of w.
    # Space: O(n) for storing the prefix sum array of weights.
    def __init__(self, w: List[int]):
        weightSum = [w[0]]
        for i in range(1, len(w)):
            weightSum.append(w[i] + weightSum[i - 1])
        self.weightSum = weightSum

    # Time: O(log(n)) for finding the position in prefix sum array.
    # Space: O(1).
    def pickIndex(self) -> int:
        randnum = random.randint(0, self.weightSum[-1] - 1)

        start = 0
        end = len(self.weightSum)
        while start < end:
            mid = (start + end) // 2
            if randnum < self.weightSum[mid]:
                end = mid
            elif randnum > self.weightSum[mid]:
                start = mid + 1
            else:
                end = mid + 1
                break
        return end

solution = Solution([1])
print(solution.pickIndex())

print()

solution = Solution([1, 3])
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
