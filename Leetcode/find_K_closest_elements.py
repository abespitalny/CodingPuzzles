'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:
    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b
'''
from leetcode import *

class Solution:
    # Binary search approach. This is tricky because you have to make sure the indices are correct.
    # Time: O(log(n) + k).
    # Space: O(1) if we exclude the output.
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x < arr[0]:
            return arr[:k]
        elif x > arr[-1]:
            return arr[(len(arr) - k):]

        # Find x's position in array
        left = 0
        right = len(arr) - 1
        while (left + 1) < right:
            mid = (left + right) // 2
            if x >= arr[mid]:
                left = mid
            else:
                right = mid

        while (right - left - 1) < k:
            if left >= 0 and right < len(arr):
                leftDist = abs(arr[left] - x)
                rightDist = abs(arr[right] - x)

                if leftDist <= rightDist:
                    left -= 1
                else:
                    right += 1
            elif left >= 0:
                left -= 1
            else:
                right += 1

        return arr[(left + 1):right]

    # Beautiful solution from Leetcode. Basically, we're doing a binary search to find the left bound
    # Time: O(log(n - k) + k)
    # Space: O(1)
    def findClosestElements2(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        # This is the furthest left you can go.
        right = len(arr) - k
        while left < right:
            mid = (left + right) // 2

            # Leetcode simplifies these two if statements into one condition, but I separated them for clarity.
            # if x - arr[mid] > arr[mid + k] - x:
            #   left = mid + 1
            if abs(x - arr[mid]) > abs(x - arr[mid + k]):
                left = mid + 1
            elif abs(x - arr[mid]) == abs(x - arr[mid + k]):
                if x > arr[mid + k]:
                    left = mid + 1
                else:
                    right = mid
            else:
                right = mid

        return arr[left:(left + k)]


solution = Solution()

# Expected: [1,2,3,4]
print(solution.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))
print(solution.findClosestElements2(arr = [1,2,3,4,5], k = 4, x = 3))

# Expected: [1,2,3,4]
print(solution.findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1))
print(solution.findClosestElements2(arr = [1,2,3,4,5], k = 4, x = -1))
