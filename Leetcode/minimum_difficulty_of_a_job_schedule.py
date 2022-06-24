from leetcode import *

class Solution:
    # Top-down DP approach.
    # Recurrence relation:
    # OPT(i, d) = min(max(jobs[i:(i+k)]) + OPT(i + k, d - 1)) for 1 <= k <= numJobs - i - (d - 1)
    # Time: O(d * (n - d)^2) because for each state we need to iterate from 1 to n-d.
    # Space: O((n - d) * d) where n is the number of jobs because of memoization map.
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        numJobs = len(jobDifficulty)

        maxJobDiff = [0]*numJobs
        maxJobDiff[-1] = jobDifficulty[-1]
        for i in reversed(range(numJobs - 1)):
            maxJobDiff[i] = max(maxJobDiff[i + 1], jobDifficulty[i])

        memo = {}

        def dp(i, d):            
            if i == numJobs and d > 0:
                return -1
            elif (i, d) in memo:
                return memo[(i, d)]

            minJobSchedDiff = math.inf
            if d == 1:
                minJobSchedDiff = maxJobDiff[i]
            else:
                maxDiff = 0
                for k in range(1, numJobs - i - d + 2):
                    jobSchedDiff = dp(i + k, d - 1)
                    maxDiff = max(maxDiff, jobDifficulty[i + k - 1])
                    if jobSchedDiff == -1:
                        continue
                    minJobSchedDiff = min(minJobSchedDiff, jobSchedDiff + maxDiff)

            if minJobSchedDiff == math.inf:
                minJobSchedDiff = -1

            memo[(i, d)] = minJobSchedDiff
            return minJobSchedDiff
        
        return dp(0, d)

    # Bottom-up DP approach
    # Time: O(n*d*(n - d))
    # Space: O(n*d)
    def minDifficulty2(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        dp = [[0]*(n + 1) for i in range(d)]

        dp[0][-2] = jobDifficulty[-1]
        for i in reversed(range(n - 1)):
            dp[0][i] = max(dp[0][i + 1], jobDifficulty[i])

        for i in range(d):
            dp[i][-1] = -1
        
        for i in range(1, d):
            for j in range(n):
                minJobSchedDiff = math.inf
                maxDiff = 0

                for k in range(1, n - j - i + 1):
                    jobSchedDiff = dp[i - 1][j + k]
                    maxDiff = max(maxDiff, jobDifficulty[j + k - 1])

                    if jobSchedDiff == -1:
                        continue
                    minJobSchedDiff = min(minJobSchedDiff, jobSchedDiff + maxDiff)

                if minJobSchedDiff == math.inf:
                    minJobSchedDiff = -1
                dp[i][j] = minJobSchedDiff

        return dp[d - 1][0]


solution = Solution()

assert solution.minDifficulty(jobDifficulty = [6,5,4,3,2,1], d = 2) == 7
assert solution.minDifficulty2(jobDifficulty = [6,5,4,3,2,1], d = 2) == 7

assert solution.minDifficulty(jobDifficulty = [9,9,9], d = 4) == -1
assert solution.minDifficulty2(jobDifficulty = [9,9,9], d = 4) == -1

assert solution.minDifficulty(jobDifficulty = [1,1,1], d = 3) == 3
assert solution.minDifficulty2(jobDifficulty = [1,1,1], d = 3) == 3
