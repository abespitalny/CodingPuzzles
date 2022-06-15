'''
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version.
'''

bad = 4
def isBadVersion(version):
    return (version == bad)

class Solution:
    # Binary search approach
    # Time: O(log(n))
    # Space: O(1)
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n + 1
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
