class Solution:
    # Time: O(n)
    # Space: O(n)
    def fib(self, n: int) -> int:
        memo = {}
        def helper(n):
            if n < 2:
                return n
            if n in memo:
                return memo[n]
            
            result = helper(n - 1) + helper(n - 2)
            memo[n] = result
            return result
        
        return helper(n)

solution = Solution()

# Expected: 1
print(solution.fib(2))

# Expected: 2
print(solution.fib(3))

# Expected: 3
print(solution.fib(4))
