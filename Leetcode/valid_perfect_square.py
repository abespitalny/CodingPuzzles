'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.
'''

class Solution:
    # Binary search approach. You can also use Newton's method which has the same runtime and space complexity.
    # Time: O(log(n))
    # Space: O(1)
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        left = 1
        right = num // 2
        while left <= right:
            mid = left + (right - left) // 2
            midSquared = mid*mid
            
            if midSquared == num:
                return True
            elif midSquared < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

solution = Solution()

# Expected: True
print(solution.isPerfectSquare(16))

# Expected: False
print(solution.isPerfectSquare(14))
