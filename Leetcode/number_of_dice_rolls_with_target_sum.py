'''
You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the k^n total ways) to roll the dice
so the sum of the face-up numbers equals target.

Since the answer may be too large, return it modulo 10^9 + 7.
'''

class Solution:
    # Bottom-up DP with space optimization.
    # Time: O(n*k*target)
    # Space: O(target)
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        prevRoll = [0]*target
        for i in range(k):
            if i >= target:
                break
            prevRoll[i] = 1

        curRoll = [0]*target
        for i in range(1, n):
            for j in range(target):
                numWays = 0
                for die in range(k):
                    remainder = j - die - 1
                    if remainder < 0:
                        break

                    numWays += prevRoll[remainder]

                curRoll[j] = numWays

            prevRoll, curRoll = curRoll, prevRoll

        return prevRoll[-1] % (10**9 + 7)

solution = Solution()

assert solution.numRollsToTarget(n = 1, k = 6, target = 3) == 1
assert solution.numRollsToTarget(n = 2, k = 6, target = 7) == 6
assert solution.numRollsToTarget(n = 30, k = 30, target = 500) == 222616187
