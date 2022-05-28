'''
Implement the MedianFinder class:
- MedianFinder()
    - initializes the MedianFinder object.
- void addNum(int num)
    - adds the integer num from the data stream to the data structure.
- double findMedian()
    - returns the median of all elements so far.
'''
from leetcode import *

# I went with the two heaps approach. This idea was given to me by Cracking the Coding Interview book.
# There's also an AVL tree approach with the same runtime and space complexity.
class MedianFinder:
    def __init__(self):
        # Max heap
        self.lowerHeap = []
        # Min heap
        self.upperHeap = []

    # Time: O(log(n)) for the heap insertions / deletions.
    # Space: O(n) for storing the two heaps.
    def addNum(self, num: int) -> None:
        if len(self.lowerHeap) == 0:
            heapq.heappush(self.lowerHeap, -num)
            return

        if num < -self.lowerHeap[0]:
            heapq.heappush(self.lowerHeap, -num)
        else:
            heapq.heappush(self.upperHeap, num)
        
        if len(self.lowerHeap) - len(self.upperHeap) > 1:
            lowerMax = -heapq.heappop(self.lowerHeap)
            heapq.heappush(self.upperHeap, lowerMax)
        elif len(self.upperHeap) - len(self.lowerHeap) > 0:
            upperMin = heapq.heappop(self.upperHeap)
            heapq.heappush(self.lowerHeap, -upperMin)

    # Time: O(1)
    # Space: O(n)
    def findMedian(self) -> float:
        if len(self.lowerHeap) == 0:
            return 0

        if len(self.lowerHeap) - len(self.upperHeap) == 0:
            return (-self.lowerHeap[0] + self.upperHeap[0]) / 2
        else:
            return -self.lowerHeap[0]

medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
# Expected: 1.5
print(medianFinder.findMedian())
medianFinder.addNum(3)
# Expected: 2
print(medianFinder.findMedian())
