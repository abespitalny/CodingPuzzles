from leetcode import *

class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.average = 0
        self.size = size

    def next(self, val: int) -> float:
        n = len(self.queue)
        sumVals = self.average * n
        
        if n == self.size:
            front = self.queue.popleft()
            sumVals -= front
        
        self.queue.append(val)
        sumVals += val
        self.average = sumVals / len(self.queue)
        return self.average

movingAverage = MovingAverage(3)
print(movingAverage.next(1))
print(movingAverage.next(10))
print(movingAverage.next(3))
print(movingAverage.next(5))
