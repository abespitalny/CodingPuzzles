class Solution:
    # Binary search approach.
    # Time: O(log(x))
    # Space: O(1)
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        while start <= end:
            mid = (start + end) // 2
            midSquared = mid*mid
            
            if midSquared < x:
                start = mid + 1
            elif midSquared > x:
                end = mid - 1
            else:
                return mid
        return start - 1

solution = Solution()

# Expected: 2
print(solution.mySqrt(4))

# Expected: 2
print(solution.mySqrt(8))
