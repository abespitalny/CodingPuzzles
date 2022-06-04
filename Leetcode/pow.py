'''
Implement pow(x, n), which calculates x raised to the power n.
'''

class Solution:
    # Recursive approach
    # Time: O(log(n))
    # Space: O(log(n))
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1

            result = helper(x, n // 2)
            result *= result

            if n % 2 != 0:
                result *= x
            return result
        
        ans = helper(x, abs(n))
        if n < 0:
            return 1/ans
        return ans
    
    # Iterative approach
    # Time: O(log(n))
    # Space: O(1)
    def myPow2(self, x: float, n: int) -> float:
        i = abs(n)
        result = 1
        product = x
        while i > 0:
            if i & 1 != 0:
                result *= product
            product *= product
            i >>= 1
        
        if n < 0:
            return 1/result
        return result

solution = Solution()

# Expected: 1024
print(solution.myPow(x = 2.00000, n = 10))
print(solution.myPow2(x = 2.00000, n = 10))

# Expected: 9.261
print(solution.myPow(x = 2.10000, n = 3))
print(solution.myPow2(x = 2.10000, n = 3))

# Expected: 0.25
print(solution.myPow(x = 2.00000, n = -2))
print(solution.myPow2(x = 2.00000, n = -2))
