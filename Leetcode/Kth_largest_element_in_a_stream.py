'''
Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
    - KthLargest(int k, int[] nums):
        Initializes the object with the integer k and the stream of integers nums.
    - int add(int val):
        Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
'''
from leetcode import *

# Time: Initialization takes O(n*log(n)), and add operation takes O(n + log(n)) = O(n).
# Space: O(1). No additional space needed.
# We could use a heap to make the add operation be O(log(k)). Basically, we maintain a min-heap of k elements.
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse=True)
        self.nums = nums

    def binarySearch(self, val: int) -> int:
        start = 0
        end = len(self.nums)
        while start < end:
            mid = (start + end) // 2
            midVal = self.nums[mid]
            
            if midVal > val:
                start = mid + 1
            elif midVal < val:
                end = mid
            else:
                return mid
        return start

    def add(self, val: int) -> int:
        idx = self.binarySearch(val)
        self.nums.insert(idx, val)
        return self.nums[self.k - 1]

kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))   # return 4
print(kthLargest.add(5))   # return 5
print(kthLargest.add(10))  # return 5
print(kthLargest.add(9))   # return 8
print(kthLargest.add(4))   # return 8
