'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

# Time: O(n).
# Space: O(1).
# This is a classic problem introduced to teach recurrence relation.
# You can find a closed form solution to this because it's a simple fibonacci sequence.
# The closed form runs in O(log(n)) time because calculating exponentials takes O(log(n)) time.
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        prev = 2
        prevPrev = 1
        for i in range(3, n + 1):
            numWays = prev + prevPrev
            prevPrev = prev
            prev = numWays
        return numWays

solution = Solution()

# Expected: 2
print(solution.climbStairs(2))

# Expected: 3
print(solution.climbStairs(3))
