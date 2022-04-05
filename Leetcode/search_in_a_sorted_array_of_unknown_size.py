"""
This is ArrayReader's API interface.
You should not implement it, or speculate about its implementation
"""
class ArrayReader:
    def __init__(self, array):
        self.array = array
    def get(self, index: int) -> int:
        if index >= len(self.array):
            return ((1 << 31) - 1)
        return self.array[index]

"""
You have a sorted array of unique elements and an unknown size.
You do not have an access to the array but you can use the ArrayReader interface to access it.
You can call ArrayReader.get(i) that:
    - returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]), or
    - returns 2**31 - 1 if the i is out of the boundary of the array.

You are also given an integer target.

Return the index k of the hidden array where secret[k] == target or return -1 otherwise.

You must write an algorithm with O(log n) runtime complexity.
"""

# Time: O(log(n)). It must be said that this is a dumb solution. There are two much better ideas from leetcode:
# 1. Find the end by checking if target > right end. If it is, left = right and right = 2 * right. Stop when target <= right end.
# Once the boundaries are determined in logarithmic time, we can do a simple binary search.
# 2. We can determine the boundaries in O(1) time because we're given the fact that the array is a sorted list of *unique* elements.
# Therefore, right end is target - reader.get(0) because we can have at most n = (target - reader.get(0)) elements between 0th index and the target.
# Space: O(1).
class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        start = 0
        end = 10**4 # This is the max length of the secret array.
        while start < end:
            mid = (start + end) // 2
            midVal = reader.get(mid)
            
            if target < midVal:
                end = mid
            elif target > midVal:
                start = mid + 1
            else:
                return mid
        return -1

secret = ArrayReader([-1,0,3,5,9,12])

solution = Solution()

# Expected: 4
print(solution.search(secret, 9))

# Expected: -1
print(solution.search(secret, 2))
